import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('screening', Path(__file__).resolve().parents[1] / 'scripts/check_screening.py')
screening = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screening)


class ScreeningTests(unittest.TestCase):
    def setUp(self):
        self.record = dict(id='2609.22987', title='Example experience memory',
                           decision='include', direct=True, policy_version='2026-09-30',
                           track='procedural_memory', target='LLM agent',
                           memory_content='Verified execution experiences',
                           memory_operation='Retrieve and revise persistent records',
                           centrality='Tests cross-task reuse of those records',
                           evidence='Reported reuse ablation; limited task domain',
                           reason='Memory lifecycle is the central contribution',
                           source_url='https://arxiv.org/abs/2609.22987',
                           source_sha256='a' * 64, reading_scope='abstract',
                           experience_lifecycle='Executions form stored procedures, validated and reused across tasks')
        self.selected = [{'id': self.record['id']}]

    def check(self, record=None, history=()):
        return screening.validate(self.selected, [record or self.record], history)

    def test_direct_evidence_accepted(self):
        self.assertEqual(self.check(), [])

    def test_excluded_held_or_adjacent_never_approved(self):
        for change in ({'decision': 'exclude'}, {'decision': 'hold'}, {'direct': False}):
            self.assertTrue(self.check(self.record | change))

    def test_missing_mechanism_and_experience_rejected(self):
        for field in ('target', 'memory_content', 'memory_operation', 'centrality', 'evidence', 'experience_lifecycle'):
            r = copy.deepcopy(self.record)
            del r[field]
            self.assertTrue(self.check(r), field)

    def test_version_alias_deduplication(self):
        self.assertEqual(screening.normalize_id('https://arxiv.org/pdf/2609.22987v2.pdf'), '2609.22987')
        self.selected.append({'id': 'arXiv:2609.22987v2'})
        self.assertTrue(self.check())

    def test_reintroduction_requires_new_evidence(self):
        old = self.record | {'decision': 'exclude'}
        self.assertTrue(self.check(history=[old]))
        r = self.record | {'reassessment': dict(previous_source_sha256='a' * 64,
             new_source_url='https://arxiv.org/html/2609.22987v2',
             new_source_sha256='a' * 64, reason='New section addresses the prior objection')}
        self.assertTrue(self.check(r, [old]))
        r['reassessment']['new_source_sha256'] = 'b' * 64
        self.assertEqual(self.check(r, [old]), [])

    def test_reading_scope_and_official_source(self):
        self.assertTrue(self.check(self.record | {'reading_scope': 'abstract_and_selected_sections'}))
        self.assertTrue(self.check(self.record | {'source_url': 'https://example.org/paper'}))

    def test_missing_or_duplicate_review(self):
        self.assertTrue(screening.validate(self.selected, [], []))
        self.assertTrue(screening.validate(self.selected, [self.record, self.record], []))

    def test_comment_links_not_additions(self):
        self.assertEqual(screening.paper_ids('<!-- https://arxiv.org/abs/2609.10000 --> https://arxiv.org/pdf/2609.22987v2'), {'2609.22987'})


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Validate human screening evidence before publishing arXiv additions (stdlib only)."""
import argparse
import json
from pathlib import Path
import re
import subprocess

POLICY_VERSION = '2026-10-09'
MEMORY_SIGNAL = re.compile(r'\b(?:memory|memories)\b', re.I)
TRACKS = {'agent_memory', 'llm_memory', 'procedural_memory', 'memory_evaluation',
          'memory_security', 'memory_survey'}
ID = r'(?:\d{4}\.\d{4,5}|[a-z][a-z.\-]+/\d{7})'
HASH = re.compile(r'[0-9a-f]{64}')


def normalize_id(value):
    value = str(value).strip()
    value = re.sub(r'^https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/', '', value)
    value = re.sub(r'^arXiv:', '', value, flags=re.I)
    value = re.sub(r'\.pdf$', '', value)
    value = re.sub(r'v\d+$', '', value)
    if not re.fullmatch(ID, value):
        raise ValueError(f'Invalid arXiv ID: {value!r}')
    return value


def paper_ids(source):
    source = re.sub(r'<!--.*?-->', '', source, flags=re.S)
    return {normalize_id(m) for m in re.findall(
        rf'https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/({ID}(?:v\d+)?)', source)}


def nonempty(record, field):
    return isinstance(record.get(field), str) and bool(record[field].strip())


def validate(selected, reviews, history):
    """Return all errors. Content truth and relevance require human review."""
    errors, records = [], {}
    for record in reviews:
        ident = normalize_id(record['id'])
        if ident in records:
            errors.append(f'{ident}: duplicate review')
        records[ident] = record
    selected = [normalize_id(p['id']) for p in selected]
    if len(selected) != len(set(selected)):
        errors.append('Duplicate selected arXiv ID (including version aliases)')
    for ident in selected:
        r = records.get(ident)
        if r is None:
            errors.append(f'{ident}: missing review')
            continue
        if r.get('decision') != 'include' or r.get('direct') is not True:
            errors.append(f'{ident}: requires a direct include decision')
        if r.get('policy_version') != POLICY_VERSION or r.get('track') not in TRACKS:
            errors.append(f'{ident}: unsupported policy version or memory track')
        for field in ('title', 'abstract', 'memory_focus_quote', 'memory_focus_reason',
                      'target', 'memory_content', 'memory_operation', 'centrality',
                      'evidence', 'reason', 'source_url', 'source_sha256', 'reading_scope'):
            if not nonempty(r, field):
                errors.append(f'{ident}: missing {field}')
        # Only official title/abstract text supplies the entry signal. Human review
        # must still distinguish central memory research from incidental mentions.
        sources = [' '.join(r[field].split()) for field in ('title', 'abstract')
                   if isinstance(r.get(field), str)]
        if not any(MEMORY_SIGNAL.search(s) for s in sources):
            errors.append(f'{ident}: no memory/memories in official title or abstract')
        quote = r.get('memory_focus_quote', '')
        quote = ' '.join(quote.split()) if isinstance(quote, str) else ''
        if not quote or not MEMORY_SIGNAL.search(quote) or not any(quote in s for s in sources):
            errors.append(f'{ident}: memory_focus_quote must quote title/abstract memory evidence')
        if not HASH.fullmatch(str(r.get('source_sha256', ''))):
            errors.append(f'{ident}: invalid source SHA-256')
        if r.get('source_url') != 'https://arxiv.org/abs/' + ident:
            errors.append(f'{ident}: requires canonical official abstract URL')
        if r.get('reading_scope') not in {'abstract', 'abstract_and_selected_sections', 'full_text'}:
            errors.append(f'{ident}: invalid reading scope')
        if r.get('reading_scope') == 'abstract_and_selected_sections' and not nonempty(r, 'sections_read'):
            errors.append(f'{ident}: missing sections_read')
        if r.get('track') == 'procedural_memory' and not nonempty(r, 'experience_lifecycle'):
            errors.append(f'{ident}: missing experience_lifecycle')
        blocked = [h for h in history if normalize_id(h['id']) == ident
                   and h.get('decision') in {'exclude', 'hold'}]
        for old in blocked:
            a = r.get('reassessment', {})
            if not isinstance(a, dict):
                a = {}
            if (a.get('previous_source_sha256') != old.get('source_sha256')
                    or not all(nonempty(a, k) for k in ('new_source_url', 'new_source_sha256', 'reason'))
                    or not HASH.fullmatch(str(a.get('new_source_sha256', '')))
                    or a.get('new_source_sha256') == old.get('source_sha256')
                    or not str(a.get('new_source_url', '')).startswith('https://arxiv.org/')):
                errors.append(f'{ident}: previously {old["decision"]}; new-evidence reassessment required')
                break
    return errors


def load(path):
    records = json.loads(path.read_text())
    if not isinstance(records, list) or not all(isinstance(r, dict) for r in records):
        raise ValueError(f'{path}: expected an array of records')
    return records


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--papers', type=Path)
    selection.add_argument('--base', help='Git revision to compare both README files against')
    parser.add_argument('--review', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    history = [r for p in sorted((root / 'screening').glob('*-review.json')) for r in load(p)]
    if args.papers:
        selected = load(args.papers)
    else:
        # Include committed history as well, so deleting an exclusion file cannot hide it.
        names = git(root, 'ls-tree', '-r', '--name-only', args.base, '--', 'screening').splitlines()
        for name in names:
            if name.endswith('-review.json'):
                old_text = git(root, 'show', f'{args.base}:{name}')
                history.extend(json.loads(old_text))
                if not (root / name).exists() or (root / name).read_text() != old_text:
                    raise ValueError(f'Keep historical screening records unchanged: {name}')
        additions = []
        for name in ('README.md', 'README_en.md'):
            before = paper_ids(git(root, 'show', f'{args.base}:{name}'))
            after = paper_ids((root / name).read_text())
            additions.append(after - before)
        if additions[0] != additions[1]:
            raise ValueError('New arXiv IDs differ between Chinese and English README files')
        selected = [{'id': ident} for ident in sorted(additions[0])]
    errors = validate(selected, load(args.review), history)
    if errors:
        raise ValueError('\n'.join(errors))
    print(f'Screening gate passed: {len(selected)} selected additions; policy {POLICY_VERSION}.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f'Screening gate failed: {exc}')

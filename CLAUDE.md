# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a curated research paper collection (Awesome-AI-Memory) covering AI memory and memory systems for large language models. It is not a typical software project — the primary content is research paper metadata stored in HTML tables within README.md and README_cn.md.

## Repository Structure

- `README.md` — Main paper list (English)
- `README_cn.md` — Main paper list (Chinese)
- `CONTRIBUTING.md` — Detailed workflow for adding papers
- `scripts/update_paper_count.py` — Updates paper count badges in both READMEs
- `assets/` — Images and resources

## Paper Format

Papers are stored as HTML `<tr>` rows in the READMEs. Each paper consists of two rows:
1. First row: date, title, tags (shield.io badges), arXiv link
2. Second row: three bullet-point summaries

**Key pattern**: Each paper entry uses `rowspan="2"` on the date cell.

When adding a paper, you must update BOTH `README.md` (English) and `README_cn.md` (Chinese).

## Scripts

```bash
# Update paper count badges in both READMEs
python scripts/update_paper_count.py
```

## Git Workflow

1. Fork and create a branch from `upstream/main`
2. Add paper entries to both READMEs (follow existing HTML table format, sorted by date descending)
3. Run `python scripts/update_paper_count.py` to update badges
4. Commit and push, then create PR via `gh pr create`

See `CONTRIBUTING.md` for detailed step-by-step instructions including the exact HTML format and PR body template.

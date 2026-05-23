# Contributing Guide

## 添加论文流程

### 1. 准备工作

从上游仓库 fork 并创建新分支：
```bash
git remote add upstream https://github.com/IAAR-Shanghai/Awesome-AI-Memory.git
git fetch upstream
git checkout -b add-paper-{论文简称} upstream/main
```

### 2. 确定插入位置

论文按**日期倒序**排列（最新在前）。找到目标日期附近的位置插入。

### 3. 论文格式

**HTML 表格行格式**：

```html
<tr>
    <td rowspan="2" style="width: 15%;">[日期如 2026-01-30]</td>
    <td style="width: 55%;"><strong>[论文标题]</strong></td>
    <td style="width: 15%;">
        <img src="https://img.shields.io/badge/[标签1]-blue" alt="...">
        <img src="https://img.shields.io/badge/[标签2]-brightgreen" alt="...">
    </td>
    <td style="width: 15%;"><a href="[arXiv PDF链接]">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
    </a></td>
</tr>
<tr>
    <td colspan="3">
        • [创新点1]<br>
        • [任务/方法]<br>
        • [重要结果]
    </td>
</tr>
```

**标签参考**：Behavior Tree, Policy Verifiability, Safety, Memory System, Agent Memory, Long-Term Memory 等（见现有条目）

### 4. 语言要求

- **README.md**：英文描述
- **README_cn.md**：中文描述

### 5. 提交并创建 PR

```bash
git add README.md README_cn.md
git commit -m "Add [论文简称] paper on [主题] for LLM Agents"
git push -u origin add-paper-{论文简称}
```

使用 `gh pr create` 或 GitHub 网页创建 PR：

```bash
gh pr create --repo IAAR-Shanghai/Awesome-AI-Memory \
  --title "Add [论文标题]" \
  --body "## Summary
- Add paper: [论文标题]
- [简短描述]

## Paper Details
- **Title**: [完整标题]
- **Authors**: [作者]
- **arXiv**: [编号](https://arxiv.org/abs/xxx)

## Test plan
- [x] Added entry to README.md
- [x] Added entry to README_cn.md"
```

### 6. Issue 模板（可选）

如果不提交 PR，可以先提交 Issue：
```
Title: [论文标题]
Head: [作者名字1] (, [作者名字2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```

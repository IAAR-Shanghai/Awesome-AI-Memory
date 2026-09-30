# 论文收录规则 / Paper screening policy

Policy version: **2026-09-30**

## 核心范围

只收录以以下对象为**核心研究问题**的论文；关键词命中只用于召回候选，不能作为收录理由。

1. **Agent Memory**：语言模型或多模态语言模型智能体的语义、情节、长期、共享或流程记忆。论文必须具体研究记忆的形成、写入、组织、召回、更新、压缩、遗忘或治理，不能只是系统中附带一个 memory 模块。
2. **语言模型内部记忆机制**：参数、隐状态、循环状态或注意力中的信息存储、保持、寻址、召回、干扰或遗忘。须有明确的语言模型研究对象、实验或直接针对语言模型的理论分析；不设置任意参数规模门槛。
3. **上述记忆的专门评测、安全研究或综述**：其研究问题必须直接针对记忆能力或记忆生命周期。负结果、理论和概念性工作可以收录，但摘要必须准确标明证据类型与局限。

## 流程技能的额外门槛

技能复用仅在它是**经验形成的持久流程记忆**时收录：交代经验来自哪里、保存什么、如何跨任务或会话取用，以及如何验证、维护或更新。贡献必须落在这一记忆过程上。

- 可收录：从执行结果提炼可复用经验，研究适用范围、检索、冲突、更新、退役或经验污染。
- 不收录：静态技能包、提示词搜索/优化、工具路由、训练课程、策略蒸馏或一般自演化系统，仅因用了 skill bank、memory、experience 等名称就归为记忆。
- 例如：OptiSkill 的求解器验证经验与 SkillBank 生命周期属于范围；GraphSkillEvo 的图结构提示词优化不属于范围。

## 明确排除

- 纯视觉骨干、视觉世界模型、低层机器人控制、SLAM 几何建图，以及没有语言模型记忆证据的通用循环网络。
- 仅优化吞吐、显存、硬件缓存或 KV 传输的工作；若研究语言模型的内容保持和召回机制，则按核心范围单独判断。
- 通用 RAG、搜索、规划、长上下文、个性化、安全或智能体基准，未把记忆作为核心研究问题。
- 单纯奖励/可靠性分数、路由统计或优化器状态；名称含 memory 不等同于语义、情节或流程记忆。
- 仅声称“未来可迁移到 LLM”的相邻领域工作。

多模态与具身不是自动排除条件：高层语言模型智能体持续积累并召回情节/语义记忆可以收录；纯视觉的 VisionHOPE 不可以。

## 证据与人工判断

每篇候选须核验官方标题、摘要、arXiv ID、v1 时间、链接，并回答：**谁使用记忆？保存什么？如何存取/维护？记忆为什么是核心贡献？用什么实验、分析或论证支持？**

- `include`：直接相关，以上问题有具体来源支持。
- `exclude`：明确不符合，记录逐篇原因。
- `hold`：对象、机制或证据不清楚；暂不进入 README。必要时读正文相关部分，再决定，不能靠猜测补齐。
- 如只阅读摘要，写 `reading_scope: abstract`；阅读部分正文写 `abstract_and_selected_sections` 并列出章节。只有实际全文阅读才能写 `full_text`。不得把 PDF 下载或摘要核验称为全文核验。
- 三条中英文介绍分别说明创新、方法、结果与限制。不要把作者的设想写成已验证结果。

## 发布检查

新增条目必须在 `screening/YYYY-MM-DD-review.json` 中附上人工筛选记录。字段示例见 [本次复核记录](screening/2026-09-30-review.json)，逐篇结论见 [复核报告](screening/2026-09-30-review.md)。

```sh
# 在仓库根目录运行；先 fetch 最新 main。
python3 scripts/check_screening.py --base origin/main --review screening/YYYY-MM-DD-review.json
# 编辑 README 前也可对已选论文数组（每项含 id）运行：
python3 scripts/check_screening.py --papers /absolute/path/papers.json --review screening/YYYY-MM-DD-review.json
python3 -m unittest discover -s tests -p 'test_screening.py'
python3 scripts/update_paper_count.py
git diff --check
```

检查器验证新增 arXiv ID、两种语言一致性、直接相关结论、必填证据、流程记忆额外说明与历史排除记录。它**不代替人工语义判断**，也不自动把关键词匹配变成通过。此前 `exclude`/`hold` 的条目不能直接重新加入：必须附 `reassessment`，指向原记录的 `source_sha256`，提供新的来源/正文证据哈希及重新判断理由。保留原筛选记录，不能删除旧结论来绕过检查。

日期覆盖、分页、下载、去重、表格渲染与发布核验仍须完成；筛选规则收紧不代表可以缩短检索窗口。历史条目按批次复核，本次不声称已重审全库。

## English summary

Include papers whose central research question concerns (1) memory of language-model or multimodal-language-model agents, (2) storage, retention, addressing, recall, interference or forgetting inside language models, or (3) evaluations, security or surveys specifically about those mechanisms. Keywords are candidate-retrieval signals only.

Procedural skills qualify only as persistent memory formed from execution experience, with documented content, later reuse and a validation/maintenance lifecycle. Generic prompt optimization, static skill packages, routing statistics, policy training, pure vision/low-level robotics and hardware-only cache efficiency do not qualify. Embodied or multimodal work can qualify when high-level language-agent memory is central. Adjacent work is not admitted on speculative transfer value.

Record concrete evidence for the model/agent, stored content, memory operations, central contribution and evaluation or argument. Use `include`, `exclude`, or `hold`; unresolved candidates stay outside the README. Report the actual reading depth. Run the publication gate above, preserve prior exclusion records, and require new evidence for reassessment. The gate checks evidence records and prevents silent reintroduction; it does not automate scientific judgment.

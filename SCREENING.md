# 论文收录规则 / Paper screening policy

Policy version: **2026-10-09**

## 标题与摘要入口门槛

先检查 arXiv 官方标题和摘要，再判断核心贡献。新增收录必须同时通过以下两道门槛：

1. **明确的记忆主题信号**：标题或摘要至少一处出现独立单词 `memory` 或 `memories`（忽略大小写，允许 `long-term memory`、`memory-based` 等写法）。两者都没有时，默认 `exclude`，不进入本轮收录；仅有正文提及、方法名称中的拼接字符或我们自行撰写的介绍不能补足这一条件。
2. **记忆是核心研究问题**：标题或摘要须明确说明研究的是语言/多模态语言模型或其智能体的记忆机制、记忆能力或专门的记忆评测。出现单词本身不代表相关：背景介绍、相关工作、附带模块、显存/硬件缓存，以及泛泛的“提升记忆”，均不构成收录依据。

`experience`、`skill`、`history`、`retrieval`、`retention`、`memorization`、`forgetting`、`continual learning` 等相邻词可用于召回，**不能替代上述入口条件**。不得把一般持续学习、微调、经验复用或长上下文工作自行解释成 Memory 论文。流程技能、模型内部机制、安全、理论、负结果与综述同样适用，不设自动例外。

标题/摘要缺失或无法核验时标 `hold`；已核验但没有记忆主题信号时标 `exclude`。若发现特殊候选，只能留在排除/待核验记录中，由维护者明确重新决定范围，自动更新不得自行豁免。阅读正文用于核实已具备主题信号的候选，不用于从相邻论文中寻找收录理由。

## 核心范围

通过标题/摘要入口门槛后，只收录以以下对象为**核心研究问题**的论文；关键词命中不能作为充分的收录理由。

1. **Agent Memory**：语言模型或多模态语言模型智能体的语义、情节、长期、共享或流程记忆。论文必须具体研究记忆的形成、写入、组织、召回、更新、压缩、遗忘或治理，不能只是系统中附带一个 memory 模块。
2. **语言模型内部记忆机制**：参数、隐状态、循环状态或注意力中的信息存储、保持、寻址、召回、干扰或遗忘。须有明确的语言模型研究对象、实验或直接针对语言模型的理论分析；不设置任意参数规模门槛。
3. **上述记忆的专门评测、安全研究或综述**：其研究问题必须直接针对记忆能力或记忆生命周期。负结果、理论和概念性工作可以收录，但摘要必须准确标明证据类型与局限。

## 流程技能的额外门槛

技能复用仅在它是**经验形成的持久流程记忆**时收录：交代经验来自哪里、保存什么、如何跨任务或会话取用，以及如何验证、维护或更新。贡献必须落在这一记忆过程上。

- 可收录：从执行结果提炼可复用经验，研究适用范围、检索、冲突、更新、退役或经验污染。
- 不收录：静态技能包、提示词搜索/优化、工具路由、训练课程、策略蒸馏或一般自演化系统，仅因用了 skill bank、memory、experience 等名称就归为记忆。
- 上述条件仍须通过标题/摘要入口门槛；不能因为存在经验库或技能生命周期就自动收录。

## 明确排除

- 纯视觉骨干、视觉世界模型、低层机器人控制、SLAM 几何建图，以及没有语言模型记忆证据的通用循环网络。
- 仅优化吞吐、显存、硬件缓存或 KV 传输的工作；若研究语言模型的内容保持和召回机制，则按核心范围单独判断。
- 通用 RAG、搜索、规划、长上下文、个性化、安全或智能体基准，未把记忆作为核心研究问题。
- 单纯奖励/可靠性分数、路由统计或优化器状态；名称含 memory 不等同于语义、情节或流程记忆。
- 仅声称“未来可迁移到 LLM”的相邻领域工作。

多模态与具身不是自动排除条件：高层语言模型智能体持续积累并召回情节/语义记忆可以收录；纯视觉的 VisionHOPE 不可以。

## 证据与人工判断

每篇候选须核验官方标题、摘要、arXiv ID、v1 时间、链接，并回答：**谁使用记忆？保存什么？如何存取/维护？记忆为什么是核心贡献？用什么实验、分析或论证支持？**

- `include`：通过标题/摘要入口门槛，直接相关，以上问题有具体来源支持。记录官方原始 `abstract`、来自标题或摘要且含 `memory`/`memories` 的原文片段 `memory_focus_quote`，以及说明该片段为何体现核心研究问题的 `memory_focus_reason`。不能引用自己生成的摘要作为主题证据。
- `exclude`：明确不符合，记录逐篇原因。
- `hold`：对象、机制或证据不清楚；暂不进入 README。必要时读正文相关部分，再决定，不能靠猜测补齐。
- 如只阅读摘要，写 `reading_scope: abstract`；阅读部分正文写 `abstract_and_selected_sections` 并列出章节。只有实际全文阅读才能写 `full_text`。不得把 PDF 下载或摘要核验称为全文核验。
- 三条中英文介绍分别说明创新、方法、结果与限制。不要把作者的设想写成已验证结果。

## 发布检查

新增条目必须在 `screening/YYYY-MM-DD-review.json` 中附上人工筛选记录。历史记录结构可参考 [早期复核记录](screening/2026-09-30-review.json)，但新增记录必须使用 `policy_version: 2026-10-09` 并补齐本页要求的 `abstract`、`memory_focus_quote`、`memory_focus_reason`。保留历史记录原样，不应仅改版本号使旧结论通过新规则。

```sh
# 在仓库根目录运行；先 fetch 最新 main。
python3 scripts/check_screening.py --base origin/main --review screening/YYYY-MM-DD-review.json
# 编辑 README 前必须对已选论文数组（每项含 id）运行：
python3 scripts/check_screening.py --papers /absolute/path/papers.json --review screening/YYYY-MM-DD-review.json
python3 -m unittest discover -s tests -p 'test_screening.py'
python3 scripts/update_paper_count.py
git diff --check
```

检查器验证标题/摘要中的记忆词、原文片段归属、必填主题依据、新增 arXiv ID、两种语言一致性、直接相关结论、流程记忆额外说明与历史排除记录。它**不代替人工语义判断**，也不自动把关键词匹配变成通过。此前 `exclude`/`hold` 的条目不能直接重新加入：必须附 `reassessment`，指向原记录的 `source_sha256`，提供新的来源/正文证据哈希及重新判断理由。保留原筛选记录，不能删除旧结论来绕过检查。

日期覆盖、分页、下载、去重、表格渲染与发布核验仍须完成；筛选规则收紧不代表可以缩短检索窗口。历史条目按批次复核，本次不声称已重审全库。

## English summary

New inclusions must first contain the standalone word `memory` or `memories` in the official arXiv title or abstract (case-insensitive). If neither contains it, exclude by default; adjacent terms, body-only mentions and generated descriptions cannot substitute. Missing or unverifiable metadata stays on hold. There are no automatic exceptions for skills, continual learning, forgetting, safety, theory or surveys.

Passing this lexical gate is necessary but insufficient: the title or abstract must make language-model/agent memory the central research question. Background mentions, incidental components and hardware memory do not qualify. Record the official `abstract`, a verbatim `memory_focus_quote` from the title or abstract containing the signal, and a concrete `memory_focus_reason`. Body reading verifies a candidate's claims; it must not manufacture relevance for a candidate outside this entry scope.

Within this entry scope, include papers whose central research question concerns (1) memory of language-model or multimodal-language-model agents, (2) storage, retention, addressing, recall, interference or forgetting inside language models, or (3) evaluations, security or surveys specifically about those mechanisms. Keywords never suffice as an inclusion reason.

Procedural skills qualify only as persistent memory formed from execution experience, with documented content, later reuse and a validation/maintenance lifecycle. Generic prompt optimization, static skill packages, routing statistics, policy training, pure vision/low-level robotics and hardware-only cache efficiency do not qualify. Embodied or multimodal work can qualify when high-level language-agent memory is central. Adjacent work is not admitted on speculative transfer value.

Record concrete evidence for the model/agent, stored content, memory operations, central contribution and evaluation or argument. Use `include`, `exclude`, or `hold`; unresolved candidates stay outside the README. Report the actual reading depth. Run the publication gate above, preserve prior exclusion records, and require new evidence for reassessment. The gate checks evidence records and prevents silent reintroduction; it does not automate scientific judgment.

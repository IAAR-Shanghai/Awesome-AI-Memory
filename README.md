# Awesome-AI-Memory

<p align="center">
    【中文 | <a href="README_en.md">English</a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)
[![Papers](https://img.shields.io/badge/Papers-794-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-111-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)


## 👋 简介
大语言模型（LLM）已迅速发展为强大的通用推理与生成引擎。然而，尽管其能力不断提升，LLM 仍然受到一个根本性限制的约束：上下文窗口（Context Window）长度有限。这一限制决定了模型在单次推理过程中能够直接访问的信息范围，使其在本质上仅具备短期记忆能力，难以支持长期对话、个性化交互、持续学习以及复杂的多阶段任务。

为突破上下文窗口的固有限制，面向大模型的记忆与记忆系统（AI Memory & Memory Systems for LLMs）逐渐成为一个重要且活跃的研究与工程方向。通过为模型引入参数之外的外部、可持久化且可控的记忆结构，记忆系统使大模型能够在生成过程中存储、检索、压缩和管理历史信息，从而在有限上下文中持续利用长期经验，实现跨会话的一致性与连续推理能力。

Awesome-AI-Memory 是一个围绕 AI 大模型记忆与记忆系统构建的资源汇编仓库，系统性地收集相关的研究论文、框架工具与实践经验。该仓库致力于梳理并呈现大模型记忆领域快速发展的研究脉络，连接自然语言处理、信息检索、智能体系统与认知科学等多个研究方向。

---

## 🎯 仓库目标
本仓库的目标是构建一个集中、持续演进的知识库，为研究者与工程实践者提供参考，助力构建能够长期记忆、持续推理并随时间不断适应的智能系统。

---

## 📏 项目范围
本仓库关注的是用于扩展或补充大模型上下文窗口能力的记忆机制与系统设计，而非单纯的模型预训练或通用知识学习。内容同时涵盖理论研究与工程实践。

🌀 包含内容（In Scope）
- 面向大语言模型的记忆与记忆系统设计
- 模型参数之外的外部显式记忆
- 短期记忆、长期记忆、情节记忆与语义记忆
- 作为记忆访问机制的检索增强生成（RAG）
- 记忆管理策略（写入、更新、遗忘、压缩）
- 智能体（Agent）中的记忆系统
- 多智能体的共享记忆与协作记忆
- 受认知科学与生物记忆启发的记忆模型
- 与大模型记忆相关的评测方法、基准与数据集
- 记忆增强型 LLM 的开源框架与工具

🌀 不包含内容（Out of Scope）
- 与记忆无直接关联的一般模型预训练或规模化研究
- 不涉及记忆交互的纯参数化知识学习
- 与 LLM 无关的传统数据库或信息检索系统
- 非大模型场景下的通用记忆系统（除非具有直接迁移价值）

---

<!-- ## 🗂️ AI-Memory Taxonomy

To systematically organize the diverse research and practical resources in the field of AI large model memory, this repository categorizes memory systems across multiple orthogonal dimensions, reflecting variations in storage methods, temporal scales, content forms, operational processes, and system architectures.
1. Memory by Storage Location
- Parametric Memory
  - Knowledge implicitly encoded within model weights
  - Static and not directly editable during inference
- External / Explicit Memory
  - Memory stored outside model parameters
  - Readable, writable, and dynamically updatable
2. Memory by Temporal Scope
- Short-Term Memory
  - Entirely dependent on context window
  - Session-level, temporary information
- Long-Term Memory
  - Persistent memory across sessions and time scales
  - Supports long-term consistency and personalization
3. Memory by Content Type
- Episodic Memory
  - Event-based historical interaction memory
  - Preserves temporal sequence and contextual relationships
- Semantic Memory
  - Facts, rules, and preferences abstracted from multiple experiences
  - Typically derived from compression or induction of episodic memory
- Procedural Memory
  - Memory related to action patterns, skills, and task execution strategies
4. Memory Operations
- Writing: Determining which information should be stored
- Retrieval: Selecting relevant memories for current tasks
- Updating: Correcting or merging existing memories
- Forgetting: Removing or weakening low-value information
- Compression: Summarizing historical information to fit context windows
5. Memory Mechanisms & Architectures
- Retrieval-Augmented Generation (RAG)
- Summary-based memory mechanisms
- Vectorized semantic retrieval
- Symbolic-neural hybrid memory systems
- Event-driven and trigger-based memory mechanisms
- Reinforcement learning-based memory strategy optimization
6. Memory in Agent Systems
- Single-agent memory
- Multi-agent shared memory
- Tool-augmented memory
- Planning-aware memory
- Personality and emotion-related memory
7. Evaluation & Benchmarks
- Long-term consistency evaluation
- Continuous interaction and long-term task benchmarks
- Memory recall and utilization efficiency metrics
- Personalization and user preference retention evaluation

--- -->

## 🔔 近期热点研究与新闻
+ 2026-09-15 - 🎉 更新 250 篇论文，其中综述 3 篇，方法类与框架类论文 180 篇，数据集和评估基准类论文 32 篇，模型和系统类论文 35 篇
+ 2026-09-15 - 🎉 更新 1 篇论文，其中方法类与框架类论文 1 篇
+ 2026-07-06 - 🎉 更新25篇论文，数据集和评估基准类5篇，方法类与框架类23篇
+ 2026-06-21 - 🎉 更新27篇论文，模型和系统类9篇，数据集和评估基准类5篇，方法类与框架类13篇
+ 2026-06-14 - 🎉 更新24篇论文，综述类2篇，模型和系统类4篇，数据集和评估基准类2篇，方法类与框架类16篇
+ 2026-06-06 - 🎉 更新45篇论文，综述类1篇，模型和系统类6篇，数据集和评估基准类12篇，方法类与框架类26篇
+ 2026-05-10 - 🎉 更新16篇论文，系统&模型类3篇，Benchmark类1篇，方法类12篇；并新增1个开源系统项目
+ 2026-05-06 - 🎉 更新16篇论文，系统&模型类2篇，Benchmark类2篇，方法类12篇
+ 2026-04-27 - 🎉 更新15篇论文，综述类2篇，系统与模型类3篇，方法类10篇
+ 2026-04-17 - 🎉 更新46篇论文，综述类1篇，系统与模型类5篇，Benchmark类3篇，方法类37篇
+ 2026-04-07 - 🎉 更新16篇论文，方法类15篇，Benchmark类1篇
+ 2026-03-15 - 🎉 更新14篇论文，方法类14篇
+ 2026-03-08 - 🎉 更新15篇论文，综述类3篇, 系统&模型类2篇，Benchmark类5篇，方法类5篇。
+ 2026-03-02 - 🎉 新增一个代码agent到仓库中
+ 2026-02-27 - 🎉 更新20篇论文，综述类1篇, 系统&模型类2篇，Benchmark类2篇，方法类15篇。
+ 2026-02-26 - 🎉 更新14篇论文，方法类14篇
+ 2026-02-14 - 🎉 更新15篇论文，综述类1篇，方法类12篇，benchmark类1篇，系统与模型类1篇
+ 2026-02-09 - 🎉 更新15篇论文
+ 2026-02-01 - 🎉 更新16篇论文，方法类9篇，benchmark类4篇，系统与模型类3篇
+ 2025-12-24 – 🎉 发布仓库-V(1.0)
+ 2025-12-10 – 🎉 仓库初始化

---

🗺️ 目录表
- [Awesome-AI-Memory](#awesome-ai-memory)
  - [👋 简介](#-简介)
  - [🎯 仓库目标](#-仓库目标)
  - [📏 项目范围](#-项目范围)
  - [🔔 近期热点研究与新闻](#-近期热点研究与新闻)
  - [🧠 核心概念](#-核心概念)
  - [📚 论文列表](#-论文列表)
  - [🧰 仓库资源](#-仓库资源)
    - [📊 测试基准](#-测试基准)
    - [💻 开源系统](#-开源系统)
    - [🎥 多媒体资源](#-多媒体资源)
    - [🧠 Adam 框架](#-adam-框架)
  - [🤝  如何贡献](#--如何贡献)
  - [💬 社区和支持](#-社区和支持)
  - [🌟 仓库关注量](#-仓库关注量)

---

## 🧠 核心概念

- 大模型记忆: LLM的记忆机制融合了隐性知识（通过训练过程内化于模型参数中）与显式存储（运行时可检索的外部存储），这种双重架构使模型突破token处理的局限，具备类似人类"记忆过往、认知当下、预见未来"的认知能力。

- **记忆系统**：为大语言模型实现记忆功能的完整技术架构，包含四大核心组件：
  - **记忆存储层**：向量数据库（如 Chroma、Weaviate）、图数据库或混合存储方案
  - **记忆处理层**：嵌入模型、摘要生成器与记忆分割器
  - **记忆检索层**：多阶段检索器、重排序模块与上下文注入器
  - **记忆控制层**：记忆优先级管理器、遗忘控制器与一致性协调器

- **记忆操作**：通过记忆系统工具调用执行的原子级记忆操作：
  - **写入**：将对话内容转换为向量进行存储，通常结合摘要生成以减少噪声信息
  - **检索**：根据当前上下文生成查询语句以获取Top-K相关记忆
  - **更新**：通过向量相似度找到相关记忆并进行替换或增强
  - **删除**：基于用户指令或自动策略（如隐私数据过期）删除特定记忆
  - **压缩**：将多个相关记忆合并为摘要以释放存储空间

- **记忆管理**：在记忆系统内实施记忆管控的方法论，包含以下机制：
  - **记忆生命周期**：从创建、活跃使用、冷启动访问到归档/删除的全周期管理
  - **冲突解决**：矛盾信息仲裁机制（如时间戳优先级、来源可信度加权）
  - **资源预算**：为不同用户/任务分配内存配额以防止资源滥用
  - **安全治理**：自动检测和去标识化个人身份信息（PII）

- **记忆分类**：记忆系统特有的多维度分类体系：
  - **按访问频率**：工作记忆（当前任务）、常用记忆（个人偏好）、归档记忆（历史记录）
  - **按结构化程度**：结构化记忆（数据库记录）、半结构化记忆（对话摘要）、非结构化记忆（原始对话文本）
  - **按共享范围**：个人记忆（单用户）、团队记忆（协作空间）、公共记忆（共享知识库）
  - **按时效属性**：永久记忆（核心事实）、临时记忆（对话上下文）、时效性记忆（如"用户今天心情不好"）

- **记忆机制**：驱动记忆系统功能的核心技术组件：
  - **检索增强生成（RAG）**：通过从知识库中检索相关信息来增强生成能力
  - **记忆反思循环**：模型定期"回顾"对话历史以生成高层次摘要
  - **记忆路由**：根据查询类型（个人记忆/公共知识库）自动选择检索源

- **显式记忆**：以原始文本形式存储在模型外部的记忆，通过融合混合索引策略的向量数据库实现：
  - **稠密向量索引**：处理语义相似性查询
  - **稀疏关键词索引**：处理精确匹配查询
  - **多向量索引**：将长文档切分为多个部分，每个部分独立索引

- **参数化记忆**：存储于语言模型固定权重中的知识与能力，具有以下特征：
  - 作为模型的核心长期语义记忆载体
  - 无需外部检索或显式上下文支持即可激活
  - 提供零样本推理、通用响应与语言生成的基础能力

- **长期记忆**：设计用于持久存储的关键信息，通常通过外部知识库实现，包含以下功能：
  - **自动摘要生成**：将多轮对话提炼为结构化记忆
  - **上下文绑定**：记录记忆上下文以防止错误泛化
  - **多模态存储**：同时保存文本、图像、音频等多种模态记忆

- **短期记忆**：受限于注意力机制的大语言模型上下文窗口中的活跃信息，包含以下关键技术：
  - **KV缓存管理**：复用键值缓存以减少冗余计算
  - **上下文压缩**：使用摘要替代详细历史（如："前5轮对话讨论了项目预算"）
  - **滑动窗口注意力机制**：仅关注最近N个token，同时保留特殊标记
  - **记忆摘要注入**：将长期记忆摘要动态插入短期上下文

- **情景记忆**：记录特定用户交互历史的记忆类型，是个性化AI的基础：
  - **用户身份识别**：跨会话识别同一用户
  - **交互轨迹记录**：保存用户决策路径与反馈
  - **情绪状态追踪**：记录用户情绪变化规律
  - **偏好演化建模**：捕捉用户兴趣长期变化

- **记忆遗忘**：大模型中刻意设计的遗忘机制，包含以下技术实现：
  - **选择性遗忘（机器遗忘）**：移除训练数据中特定信息的影响，例如通过遗忘层覆盖特定知识
  - **隐私保护遗忘**：自动识别并删除个人身份信息（PII），或设置自动过期策略
  - **记忆衰减**：根据使用频率自动降低低频访问记忆的优先级
  - **冲突驱动遗忘**：当新证据与旧记忆冲突时，策略性更新或淘汰旧记忆

- **记忆检索**：从海量记忆库中精确定位相关信息的复杂过程：
  - **语义预过滤**：通过向量相似度匹配获取Top-100候选结果
  - **上下文重排序**：根据当前查询上下文重新排序结果
  - **时间过滤**：优先选择最新相关数据

- **记忆压缩**：在资源受限条件下最大化记忆效用的技术体系：
  - **内容级压缩**：提取核心信息并舍弃冗余细节
  - **表征级压缩**：向量量化（如乘积量化编码）、维度约简
  - **组织级压缩**：聚类相似记忆、构建分层记忆结构
  - **知识蒸馏**：将外部记忆中的关键模式迁移至参数化记忆

---

## 📚 论文列表
以下论文按发表日期排列：

<details>
  <summary><strong>综述</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08599"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 综述长期个性化智能体的图记忆。<br>
        • 围绕表示、演化、检索和评测组织研究。<br>
        • 比较设计选择，并梳理可靠性与可控性挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-28</td>
      <td style="width: 55%;"><strong>Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture">
        <img src="https://img.shields.io/badge/Survey-blue" alt="Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.25380"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从模型架构视角综述大语言模型记忆。<br>
        • 按表示形式、更新动态及持久性组织记忆机制。<br>
        • 综合分析写入、路由、固化、效率权衡及评测方向。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-20</td>
      <td style="width: 55%;"><strong>The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.19433"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分类梳理有状态智能体中的时间持久攻击。<br>
        • 分析记忆注入、延迟欺骗及工作流级威胁模型。<br>
        • 综合轨迹监控、形式验证及可信记忆等防御方向。
      </td>
    </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-25</td>
        <td style="width: 55%;"><strong>Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/综述-4A90E2" alt="Survey">
          <img src="https://img.shields.io/badge/Agent%20隐私-F5A623" alt="Agent Privacy">
          <img src="https://img.shields.io/badge/数据治理-7ED321" alt="Data Governance">
          <img src="https://img.shields.io/badge/记忆风险-D0021B" alt="Memory Risk">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.26627v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从数据中心视角综述 LLM Agent 的隐私问题，关注智能体查询、存储、记忆、交换并据此行动的数据，而不只是按攻击类型分类。<br>
          • 论文围绕数据库、文档集合、API、跨会话记忆、中间工作流状态和多智能体通信组织风险，指出敏感信息可能在最终回答生成前就通过多种路径泄露。<br>
          • 该综述强调 Agent 隐私需要覆盖记忆写入、检索、委托、日志和工具调用的全生命周期控制，因此持久状态与数据治理是安全部署的核心问题。
        </td>
      </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>Are We Ready For An Agent-Native Memory System?</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20System-green" alt="Memory System">
          <img src="https://img.shields.io/badge/Evaluation-orange" alt="Evaluation">
          <img src="https://img.shields.io/badge/Data%20Management-purple" alt="Data Management">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24775v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从数据管理视角研究 Agent Memory，指出面向 LLM Agent 的记忆不应只被视作检索增强组件，而应作为支持持久化存储、检索、更新、整合与生命周期治理的系统来评估。<br>
          • 论文将 Agent 原生记忆系统拆解为四个模块：表示与存储、提取、检索与路由、维护，并在这一框架下评估了 12 个代表性记忆系统和 2 个基线，覆盖 5 类基准工作负载与 11 个数据集。<br>
          • 实验表明不存在一种在所有场景下都占优的记忆架构，效果高度依赖记忆结构与工作负载瓶颈的匹配；细粒度消融进一步量化了表示保真度、检索精度、更新正确性和长程稳定性等因素，成本分析也显示局部维护通常比全局重组更高效。
        </td>
      </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agents-F5A623" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Environment%20Modeling-7ED321" alt="Environment Modeling">
          <img src="https://img.shields.io/badge/Synthesis-D0021B" alt="Synthesis">
          <img src="https://img.shields.io/badge/Evaluation-9013FE" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文系统梳理了LLM代理环境的全生命周期框架，覆盖建模、合成、评估与应用四个核心环节。<br>
          • 提出了符号与神经两类环境合成范式，并从结构属性与能力维度分析了环境设计的演化路径。<br>
          • 强调代理与环境的协同演化机制（记忆、工作流、轨迹与探索），并指出未来将走向环境即服务与多代理生态。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Security-%2350E3C2" alt="LLM Security">
          <img src="https://img.shields.io/badge/Attacks-%23F8E71C" alt="Attacks">
          <img src="https://img.shields.io/badge/Defenses-%23FF6FB5" alt="Defenses">
          <img src="https://img.shields.io/badge/Evaluation-%239B9B9B" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10749">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从生命周期视角系统刻画LLM代理的安全风险，并统一建模信息流、授权委托与持久状态三类关键交互。<br>
          • 通过综述247篇研究，归纳攻击面、防御机制与评估体系，揭示当前安全方法整体仍偏脆弱且不完整。<br>
          • 强调需要构建可信边界清晰、权限控制原则化、且贴近真实环境的长期状态安全评估框架。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
          <img src="https://img.shields.io/badge/Memory%20Systems-green" alt="Memory Systems">
          <img src="https://img.shields.io/badge/Long--Horizon%20Tasks-red" alt="Long-Horizon Tasks">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06448">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 将 Agent Memory 定位为长程有状态工作负载，而不只是检索增强模块。<br>
          • 提出系统导向分类法和阶段感知 profiling 工具，用于拆解构建、检索和生成成本。<br>
          • 分析十个代表性系统，并总结面向规模化部署、新鲜度与延迟权衡的系统建议。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-23</td>
        <td style="width: 55%;"><strong>MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/多模态记忆-blue" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/视觉Benchmark-red" alt="Visual Benchmark">
          <img src="https://img.shields.io/badge/评估框架-green" alt="Evaluation Framework">
          <img src="https://img.shields.io/badge/长期记忆-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.15128">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MemEye，一个以视觉为中心的基准测试，用于评估多模态 Agent 的长期记忆能力，避免文本主导的"捷径"问题。<br>
          • 设计了二维评估矩阵（X轴：场景/区域/实例/像素粒度；Y轴：原子检索/关系关联/演化合成推理深度）。<br>
          • 引入三阶段验证闸门，确保问题无法通过文本上下文、简短字幕或超出 VLM 能力的方式被解决。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20OS-orange" alt="Memory OS">
          <img src="https://img.shields.io/badge/自组织-green" alt="Self-Organizing">
          <img src="https://img.shields.io/badge/语义整合-red" alt="Semantic Consolidation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.02163">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 EverMemOS，一个三阶段记忆生命周期（情景记忆形成 → 语义整合 → 重构式回忆），将碎片化对话组织为结构化、可演化的记忆单元（MemCell/MemScene）。<br>
          • 引入 MemCell 作为原子记忆单元，包含 Episode + Atomic Facts + Foresight + Metadata；MemScene 用于场景级整合，支持长期用户画像演化。<br>
          • 设计重构式检索范式，包含 MemScene 引导检索、前瞻有效性过滤和充分性验证，实现长期推理中"必要且充分"的上下文获取。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-19</td>
        <td style="width: 55%;"><strong>An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Experience--RAG-yellow" alt="Experience-RAG">
          <img src="https://img.shields.io/badge/Retrieval%20Strategy-orange" alt="Retrieval Strategy">
          <img src="https://img.shields.io/badge/Skill%20Orchestration-green" alt="Skill Orchestration">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03989">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 识别了流水线式检索的三个工程问题：策略逻辑不可复用、路由决策不可观测、工作流耦合导致不可演进。<br>
          • 提出 Experience-RAG Skill，包含六个模块（统一接口、场景分析、经验记忆、策略路由、检索器池、结果打包），将检索策略选择封装为可插拔的 Agent skill。<br>
          • 规则路由（0.8924）优于学习路由（0.8778/0.8627），经验记忆记录 (scene_features, score_vector, best_margin) 为未来升级到学习路由奠定基础。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Human Cognition in Machines: A Unified Perspective of World Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/World%20Models-brightgreen" alt="World Models">
          <img src="https://img.shields.io/badge/Cognitive%20Architecture-yellow" alt="Cognitive Architecture">
          <img src="https://img.shields.io/badge/Meta--cognition-teal" alt="Meta-cognition">
          <img src="https://img.shields.io/badge/Structured%20Knowledge-orange" alt="Structured Knowledge">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16592">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 从认知架构视角统一梳理世界模型中的记忆、感知、语言、推理、想象、动机与元认知等能力。<br>
          • 提出面向科学发现的 Epistemic World Models 类别，并给出跨视频、具身与认知世界模型的分类和未来方向。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Agentic Frameworks for Reasoning Tasks: An Empirical Study</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Context%20Management-brightgreen" alt="Context Management">
          <img src="https://img.shields.io/badge/Agentic%20Framework-yellow" alt="Agentic Framework">
          <img src="https://img.shields.io/badge/Orchestration-teal" alt="Orchestration">
          <img src="https://img.shields.io/badge/Memory%20Control-orange" alt="Memory Control">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16646">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 对 22 种常用 Agentic 框架在 BBH、GSM8K 与 ARC 上进行统一评测，比较准确率、耗时、成本与跨基准一致性。<br>
          • 结果表明性能差异主要来自编排质量，尤其是记忆控制、上下文增长和失败重试机制会显著影响效率与成本。
        </td>
      </tr>
<tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Survey-red" alt="Survey">
            <img src="https://img.shields.io/badge/Externalization-teal" alt="Externalization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08224">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 从“外化”视角综述 LLM Agent 的记忆、技能、协议与 harness 工程。<br>
            • 指出记忆外化跨时间状态，技能外化程序能力，协议外化交互结构，harness 负责统一协调这些模块。<br>
            • 梳理了从模型参数到上下文再到外部基础设施的演进路径，并讨论其中的关键权衡与开放问题。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-05</td>
        <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
            <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 解决业界关于长上下文模型与外部记忆系统在构建持久化代理时的效能与成本优劣之争。<br>
            • 在三大主流记忆基准上，从准确率与累计 API 推理成本双重维度，系统交叉评测长上下文与事实型外部记忆方案。<br>
            • 长上下文在事实召回上具有优势，但成本随轮次递增；在 100k 上下文长度下，记忆系统在约 10 轮交互后即可实现成本反超，为实际工程选型提供了量化依据。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Modular Memory is the Key to Continual Learning Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Continual%20Learning-blue" alt="Continual Learning">
            <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01761">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 传统基础模型在持续学习时依赖权重更新，极易导致灾难性遗忘，难以实现大规模经验积累。<br>
            • 提出一种结合上下文学习与权重内学习的模块化记忆架构路线图。<br>
            • 该架构利用上下文学习实现快速适应，通过权重更新实现能力固化，为构建真正意义上的终身学习智能体提供了理论指引。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Cognitive%20Alignment-blue" alt="Cognitive Alignment">
            <img src="https://img.shields.io/badge/Interpretability-brightgreen" alt="Interpretability">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01822">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 旨在探究大语言模型内部在处理海量语义记忆时，是否具备类似人类的高效策略性访问机制。<br>
            • 借助机械可解释性技术分析语义流畅性任务，严密剖析模型内部收敛性与发散性的记忆搜索模式。<br>
            • 证实 LLM 不同层级中存在类人的策略性记忆搜寻行为，为认知对齐研究及强化人机协作奠定了可解释性基础。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized%20Agents-blue" alt="Personalized Agents">
            <img src="https://img.shields.io/badge/User%20Adaptation-brightgreen" alt="User Adaptation">
            <img src="https://img.shields.io/badge/Evaluation-yellow" alt="Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22680.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 本论文探讨了个性化LLM驱动代理的基础、评估和未来方向，对个性化 LLM 驱动代理的基础、评估及未来方向进行了能力导向的系统性综述。<br>
            • 论文围绕用户画像建模、记忆、规划和行动执行这四个相互依赖的核心组件构建了分类法。<br>
            • 本文综合分析了用户信号的表示、传播与利用方式，并探讨了从通用辅助到专业领域的应用场景及设计权衡。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2602.06052">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 从存储介质、认知机制和服务主体三个维度构建了统一的分类框架，系统化地定义了基础智能体记忆的分类学。<br>
          • 深入剖析了记忆在单智能体与多智能体系统中的动态操作机制，并归纳了提示词学习、参数微调和强化学习三种主流的学习策略。<br>
          • 全面梳理了现有的评价指标与基准测试体系，并结合多领域应用现状，提出了提升记忆效率、安全性及多模态能力的未来研究方向。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-15</td>
      <td style="width: 55%;">
      <strong>Memory in the Age of AI Agents: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
        <img src="https://img.shields.io/badge/Forms--Functions--Dynamics-purple" alt="Forms-Functions-Dynamics">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2512.13564">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提供了一个全面且最新的智能体记忆全景图，明确将其与 LLM 记忆、RAG 和上下文工程等相关概念区分开来。<br>
          • 引入了一个统一的分类体系，通过三个视角审视记忆：<strong>形式</strong>（Token 级、参数化、潜在）、<strong>功能</strong>（事实性、经验性、工作）和<strong>动态</strong>（形成、演变、检索）。<br>
          • 探讨了新兴的研究前沿，如面向自动化的记忆设计、强化学习集成和可信度，同时汇编了具有代表性的基准和框架。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-18</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/full/10.1145/3749987">
        <img src="https://img.shields.io/badge/ACM-paper-black?labelColor=blue" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 深入探讨了机器遗忘的概念和背景，强调了其在现代机器学习中的重要性。<br>
          • 机器遗忘旨在使学习算法能够有效地消除特定数据的影响，而无需进行完整的模型重新训练。<br>
          • 论文分析了机器遗忘的必要性、挑战和设计要求，回顾了当前的研究进展，并强调了该领域在算法有效性、公平性和隐私保护方面的复杂性和多样性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-02</td>
      <td style="width: 55%;">
      <strong>A Survey on the Memory Mechanism of Large Language Model based Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules Badge">
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/pdf/10.1145/3748302">
        <img src="https://img.shields.io/badge/ACM-paper-black?labelColor=blue" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了基于 LLM 的智能体的记忆机制，强调了记忆在智能体自我进化和复杂交互中的关键作用。<br>
          • 系统总结和分类了现有的记忆模块设计和评估方法，并分析了它们在不同应用场景中的作用和局限性。<br>
          • 此类智能体能够改善决策制定和任务执行。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-31</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2503.01854v2">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文调查了大语言模型（LLM）中的机器遗忘，旨在有效消除不良数据（如敏感或非法信息）的影响，无需完全重新训练，同时保留整体模型效用。<br>
          • 它定义了 LLM 遗忘的目标和范式，并建立了一个全面的分类体系。<br>
          • 论文回顾了现有方法，评估了它们的优势和局限性，并讨论了未来的研究机会。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-27</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory in AI Taxonomy, Operations, Topics, and Future Directions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.00675">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探索了人工智能（AI）中关于记忆的多维研究，特别关注大语言模型（LLM）中的记忆操作和管理。<br>
          • 对各种类型的记忆表示和操作（包括整合、更新、索引、遗忘、检索和压缩）进行了分类，并系统分析了记忆在 AI 中的重要性及其实现方式。<br>
          • 通过广泛的文献回顾，论文确定了四个关键研究主题：长期记忆、参数化记忆、长上下文记忆和多源记忆整合。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-24</td>
      <td style="width: 55%;">
      <strong>Cognitive Memory in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.02441">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 对大语言模型（LLM）中的记忆机制进行了全面考察，特别关注不同类型的记忆及其在模型中的作用。<br>
          • 虽然 LLM 在信息检索和交互总结方面表现出色，但其长期记忆仍然不稳定。<br>
          • 将记忆集成到 AI 系统中对于提供上下文丰富的响应、减少幻觉、提高数据处理效率以及实现 AI 系统的自我进化至关重要。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-23</td>
      <td style="width: 55%;"><strong>From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.15965">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了人类记忆与基于 LLM 的人工智能（AI）系统的记忆机制之间的关系。<br>
          • 主要贡献包括系统定义了 LLM 驱动的 AI 系统中的记忆，及其与人类记忆的概念联系。<br>
          • 论文提出了一个基于对象、形式和时间的三维记忆分类体系，并总结了当前个人记忆和系统记忆研究中的关键开放问题。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-02</td>
      <td style="width: 55%;"><strong>Digital Forgetting in Large Language Models: A Survey of Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.02062">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文探讨了大语言模型（LLM）中的数字遗忘及相应的遗忘方法，重点是解决与隐私、版权和社会伦理相关的问题。<br>
          • 它分析了不同类型的模型架构和训练过程，以及数字遗忘的实际方法，包括数据重新训练、机器遗忘和提示工程。<br>
          • 通过引入“遗忘保证”的概念，论文强调了精确遗忘和近似遗忘的有效机制。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-12</td>
      <td style="width: 55%;"><strong>Human-inspired Perspectives: A Survey on AI Long-term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Non--Parametric%20Memory-green" alt="Non-Parametric Memory">
      <img src="https://img.shields.io/badge/Sensory%20Memory-brown" alt="Sensory Memory">
      <img src="https://img.shields.io/badge/Working%20Memory-blueviolet" alt="Working Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2411.00489">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 本文系统地考察了人类长期记忆机制与 AI 长期记忆之间的相互作用，并提出了一种自适应长期记忆认知架构（SALM）。<br>
          • 它介绍了人类记忆的结构，包括感官记忆、工作记忆以及不同类型的长期记忆（情景记忆、语义记忆和程序记忆）。<br>
          • 论文分析了 AI 长期记忆的分类——参数化记忆和非参数化记忆——及其存储和检索机制。
        </td>
    </tr>
  </table>
</details>



<details>
  <summary><strong>方法类与框架类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.15009"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合多智能体的个体经验与集体记忆。<br>
        • 通过私人经验沉淀及双路检索共享经过筛选的知识并保持多样性。<br>
        • ALFWorld 和 PDDL 实验报告性能提升及记忆污染减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.15457"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用非对称视觉记忆支持 GUI 纠错及跨次学习。<br>
        • 预测误差决定选择性保留截图，并聚焦流程贡献分配。<br>
        • 四个基准报告成功率提高及次线性上下文增长。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>MessyMem: Learning-from-Doing Memory for Mobile Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.15976"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为重复移动操作任务保留交互中获取的知识。<br>
        • 具有空间依据的三维场景图连接对象属性、结果及视觉观察。<br>
        • 仿真和机器人实验展示长任务序列中的经验复用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>EvoOntology: A Self-Evolving Ontology Layer for Data Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.15779"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 EvoOntology，为异构数据智能体构建可自演化的本体层，属于邻近的智能体知识组织方向。<br>
        • 通过 MCP 提供模式、内容与工具层，由构建智能体生成本体，并通过归因指导的编辑和成对评估持续修订。<br>
        • 摘要报告三个数据智能体基准、四个模型上的基线提升；其主要贡献是本体与数据交互，而非跨会话记忆评测。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-13</td>
      <td style="width: 55%;"><strong>Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.14773"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 按需且可逆地展开对话工作记忆。<br>
        • 确定性目录让模型仅展开相关历史轮次。<br>
        • LoCoEval 报告查询上下文 token 减少超过 70%，未测得质量损失。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-12</td>
      <td style="width: 55%;"><strong>When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.13889"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究通过智能体记忆写入而持久存在的外部指令。<br>
        • 跨会话评估改变运行框架、模型、模态及触发设置。<br>
        • 提示防御减少部分注入，但对已持久化投毒保护有限。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-12</td>
      <td style="width: 55%;"><strong>GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.14066"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用图记忆协调多智能体多模态推理。<br>
        • 跟踪动作与观察依赖，并训练拓扑感知的贡献分配策略。<br>
        • 多模态基准报告复杂多步推理表现提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-12</td>
      <td style="width: 55%;"><strong>LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.14138"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合分配终身智能体的记忆回放与推理预算。<br>
        • 在线策略无需修改智能体权重即可调整资源选择。<br>
        • LifelongAgentBench 在三个基座上报告更好的成本与准确率权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.12354"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将存储记忆记录视为重建原始上下文的线索。<br>
        • 轮次图扩展恢复检索锚点周围的时间和语义证据。<br>
        • LoCoMo 和 LongMemEval 优于记忆基线，成本低于完整历史输入。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.12436"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 区分临时信息与需要长期保留的知识。<br>
        • 通过生命周期标注训练及阶段感知读取管理专用记忆组件。<br>
        • 受控测试减少覆盖，两项公开基准保持总体竞争力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>LifeMem: Enabling Lifelong Experience Reuse for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.12655"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 支持智能体跨环境终身复用经验。<br>
        • 按工作流聚类交互轨迹，并为新任务检索可复用技能。<br>
        • 十个环境的实验报告遗忘减少与任务迁移改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>BadEngram: Backdoor Attack on Gated Memory Components in LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.13478"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究仅植入门控参数记忆组件的后门。<br>
        • 保持基座权重不变，并通过受控干预定位记忆传播路径。<br>
        • 实验在受控及生产规模模型中展示触发器依赖的攻击行为。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-10</td>
      <td style="width: 55%;"><strong>Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.11060"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用最新环境观察校验任务后的记忆整理。<br>
        • 以只读工具核验、限定和刷新候选记忆，无需重新训练。<br>
        • CLBench 和改编 APEX 实验改善奖励并降低任务智能体成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-10</td>
      <td style="width: 55%;"><strong>2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.11308"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将操作任务记忆保留在动作策略之外的智能体中。<br>
        • 通过子任务语言及可选二维提示引导无状态 RGB 动作模型。<br>
        • LIBERO-Mem 实验改善完成度，但严格成功率仍明显较低。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-10</td>
      <td style="width: 55%;"><strong>MAPLE: Memory-Augmented Planning with Language and Evolution</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.11636"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在连续自然语言修改中维护优化问题状态。<br>
        • 保留可执行程序、已接受计划、历史更新及候选解。<br>
        • NLDO 实验展示有效更新及对既有搜索结果的复用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-09</td>
      <td style="width: 55%;"><strong>ROAM: Robust Organization of Atomic Memories for Agents through Semantic Relations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.09778"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过显式语义关系组织原子记忆。<br>
        • 主记忆与证据角色将活动视图和冗余或冲突观察分离。<br>
        • 实验报告回答改善、关键证据召回提高及干扰 token 减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-09</td>
      <td style="width: 55%;"><strong>What Should an Agent Forget? Separating What Is Stored from What Is Used</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.10263"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离保留的历史与每次回答实际使用的证据。<br>
        • 查询条件视图抑制过时事实，同时保留历史访问和关系。<br>
        • 多场景消融支持相关性筛选及显式控制被替代信息。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-09</td>
      <td style="width: 55%;"><strong>Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent Coherence in LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.10413"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用本体指导个人事实的记忆生命周期管理。<br>
        • 通过分类衰减、替代、有效期及路由区分变化信息。<br>
        • 消融将正确率收益主要归于生命周期元数据，将校准收益归于类型划分。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08228"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据历史执行证据演化技能检索图。<br>
        • 更新拓扑、边权和描述，无需修改技能内容或模型权重。<br>
        • SkillsBench 实验报告更高奖励及对留出任务的迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08273"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过事件中心树结构压缩智能体记忆。<br>
        • 利用渐进节点合并及锚点引导时间检索保留有用证据。<br>
        • 单模态和多模态实验在压缩一半记忆时保留大部分性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Safe Task Planning with Long-Term Graph Memory for Embodied Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08444"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用长期语义图记忆改善具身规划安全性。<br>
        • 风险预测器根据累积观察评估动作并触发保守重规划。<br>
        • IS-Bench 和真实机器人实验报告安全成功率提高。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>CreaMem: A Scene-Aware Memory Architecture for Personalized Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08550"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 按生活场景划分个性化记忆。<br>
        • 情节和特征双重编码在平衡检索中融合互补视角。<br>
        • 两个记忆基准报告问答提升，多跳问题收益尤为明显。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>MemSentry: A Framework for Detecting Persistent Memory Poisoning in Agentic AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08747"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用可配置安全状态标准筛查持久记忆写入。<br>
        • 信任、语义风险、依赖影响范围及访问控制产生确定性决策。<br>
        • 合成场景测试展示所建模环境中的检测能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08832"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将不稳定执行步骤转化为可复用情节指导。<br>
        • 一致性分析器诊断失败并存储针对性指南供后续运行使用。<br>
        • AppWorld 实验改善重复及相似任务的五次运行一致成功率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08919"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 交替进行快速文本状态适应及较慢策略固化。<br>
        • 通过转移感知蒸馏内化跨状态修订仍有效的行为。<br>
        • 智能体基准报告优于仅状态或仅策略演化的方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.09115"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 抑制对当前查询具有负面下游效用的记忆。<br>
        • 合作归因识别单项删除筛查遗漏的交互有害证据。<br>
        • 十个记忆池报告恢复改善，无需永久修改存储。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Procedural Graphs: Self-Evolving Execution Structures for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.09153"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将可复用流程表示为自演化执行图。<br>
        • 局部子图指导动作，并用验证结果筛选从成败轨迹学到的编辑。<br>
        • 多任务及多模型评估报告优于记忆基线的表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-07</td>
      <td style="width: 55%;"><strong>Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.07093"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离记忆检索、证据定位及答案生成。<br>
        • 多粒度图与训练后的定位器提供紧凑且位置明确的证据。<br>
        • 四个基准的实验报告较强检索准确率及回答质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-07</td>
      <td style="width: 55%;"><strong>MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.07471"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在文本与视觉记忆通道间分配检索证据。<br>
        • 训练后的提取及呈现策略选择有来源的证据单元和布局。<br>
        • 四个基准报告受限记忆 token 预算下的任务表现改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-04</td>
      <td style="width: 55%;"><strong>Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.04802"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将长期对象运动历史编码为可用语言查询的轨迹。<br>
        • 文本描述及稀疏空间、视觉锚点保留动态状态变化。<br>
        • 空间记忆基准改善长期检索，并大幅压缩轨迹。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-04</td>
      <td style="width: 55%;"><strong>From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.04869"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从交互轨迹构建持久且版本化的 GUI 技能。<br>
        • 利用冻结技能库快照及评估反馈支持可审计的在线修订。<br>
        • 四个 OSWorld 领域出现条件性收益，反复编辑并不保证任务恢复。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-04</td>
      <td style="width: 55%;"><strong>Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.04875"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将遗忘扩展至派生执行状态，而非仅删除存储记录。<br>
        • 根据来源恢复检查点，并通过净化回放重建受影响的后续过程。<br>
        • 行为审计以更少重算 token 达到完整重置的遗忘效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-04</td>
      <td style="width: 55%;"><strong>Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.04915"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在紧张提示词预算下优化紧凑智能体记忆。<br>
        • 最大成员在线聚类及原子感知打包控制合并与证据组装。<br>
        • AMA-Bench 实验以 32% token 成本达到完整上下文质量的 83%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-03</td>
      <td style="width: 55%;"><strong>EdgeMem: LLM-Free Agent Memory Construction and Retrieval via Evidence-Preserving Multi-Anchor Hypergraph</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.05553"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以多锚点超图保留原始对话证据。<br>
        • 利用本地内容、时间及情节处理，避免生成式记忆构建。<br>
        • LoCoMo 和 LongMemEval-S 实验在无需模型管理调用时保持较强检索表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-03</td>
      <td style="width: 55%;"><strong>RuleMem: Active Rule Memory for Long-Term Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.03915"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 归纳可复用逻辑规则用于对话记忆推理。<br>
        • 自然语言 Horn 子句及困惑度一致性验证指导证据检索。<br>
        • LoCoMo 和 LongMemEval 评估报告相较记忆基线的较强表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.05533"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将采样且带时间戳的视频历史直接输入 VLA 基座。<br>
        • 子任务隐藏状态指导动作，共享前缀预填充控制延迟。<br>
        • 四个记忆基准优于匹配的检索和压缩机制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.02074"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过归因分离规划记忆与执行记忆。<br>
        • 先判断结果归属，再写入相应经验库。<br>
        • 四个基准报告规划提升、记忆精简及跨基座迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>MASkills: Continual Skills Optimization for Multi-Agent LLM Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.02094"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 持续优化多智能体系统的流程技能。<br>
        • 利用分层贡献及动量更新指导精炼、固化、归纳和裁剪。<br>
        • HotpotQA、LoCoMo 和 GAIA 实验报告有效的持续提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.02217"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将任务特定技能固化为可复用流程族。<br>
        • 通过执行验证接纳全局先验，并在本地重新生成实例细节。<br>
        • 四个基准报告迁移改善，且技能库小于逐任务存储。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.02253"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合轨迹记忆与流程技能支持深度研究。<br>
        • 交替强化学习训练执行、蒸馏与规划，并支持测试时适应。<br>
        • 七个基准的实验报告优于所比较最强记忆基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.02265"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 区分真实偏好漂移、投毒及临时变化。<br>
        • 信念跟踪、多时间尺度记录、澄清及反事实审计指导更新。<br>
        • 留出测试改善个性化，但自适应攻击暴露稳健性权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-02</td>
      <td style="width: 55%;"><strong>MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.03201"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过稀疏局部关系建模文本记忆生命周期。<br>
        • 利用合并、替代及矛盾链接重建包含来源的证据单元。<br>
        • BEAM 和 StructMemEval 实验报告推理改善及运行时间降低。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-01</td>
      <td style="width: 55%;"><strong>Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00523"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究贯穿完整记忆流程的间接投毒。<br>
        • 阶段反馈建模写入、检索及后续利用之间的相互影响。<br>
        • 跨框架评估揭示可迁移漏洞，多种受测防御仍有不足。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-01</td>
      <td style="width: 55%;"><strong>EM^2Mem: Event-Centric Multimodal Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00551"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在检索前将多模态证据绑定至共同事件锚点。<br>
        • 事件记忆单元对齐来源、时间、关系及出处。<br>
        • 三个长视频问答基准改善准确率与证据召回并降低推理成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-01</td>
      <td style="width: 55%;"><strong>MemoryWalker: Stop Training Agents on Contexts They Never Saw</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00865"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 修正智能体历史压缩后的训练条件上下文。<br>
        • 精确树式评分与自蒸馏恢复条件一致性。<br>
        • 七个网络搜索基准报告训练与运行差距缩小及奖励提高。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-01</td>
      <td style="width: 55%;"><strong>HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00950"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为变化的具身环境维护时间化三维记忆。<br>
        • 语义空间图、衰减及位移感知检索定位移动对象。<br>
        • Dyna-THOR 实验提高重新定位准确率并减少探索成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-01</td>
      <td style="width: 55%;"><strong>Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.01272"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将前瞻记忆结构化为带类型的意图存储。<br>
        • 代码管理意图生命周期，小模型负责限定范围的语言决策。<br>
        • PM-Bench 实验无需微调即可明显改善延迟意图执行。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.30177"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 区分记忆生命周期不同阶段的效用与风险权衡。<br>
        • 匹配正常和投毒测试改变准入、管理及检索暴露程度。<br>
        • 十一个模型发现不同风险模式，支持阶段感知控制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.30198"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 追踪错误在多轮记忆系统中的传播。<br>
        • 利用反事实干预区分记忆更新与问题反馈路径。<br>
        • 实验发现潜伏错误持续存在，修复记忆可带来更强纠错效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.30760"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 训练技能学习器维护持久具身智能体技能。<br>
        • 结构化批量编辑及对比轨迹为冻结执行器改进技能库。<br>
        • EB-ALFRED 和 EB-Habitat 在连续更新轮次中报告提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00237"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用可学习的紧凑执行记忆路由多智能体协作。<br>
        • 写入及检索门控过滤历史，自适应停止控制任务结束。<br>
        • 五个基准报告平均准确率提高及代码生成推理成本降低。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-30</td>
      <td style="width: 55%;"><strong>AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.29537"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 仅在物理目标经过验证达成后推进机器人进度记忆。<br>
        • 交互线索和视觉验证为冻结 VLA 建立闭环。<br>
        • 计数任务及机器人实验报告提升，摘要中部分数值缺失。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-29</td>
      <td style="width: 55%;"><strong>Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.28978"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 对比图记忆、选择性裁剪与扁平检索。<br>
        • 根据新近性、频率、中心性及年龄裁剪带类型的对话图。<br>
        • 该图检索弱于匹配基线，裁剪则以有限测得损失节省存储。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-29</td>
      <td style="width: 55%;"><strong>When to Adapt: Conditional Memory Adapters for Retention-Preserving Domain Specialization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.29327"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用条件记忆适配器实现兼顾能力保留的领域适应。<br>
        • 通过局部 n-gram 匹配及可学习门控选择性注入领域知识。<br>
        • Qwen3 实验保留域外平均表现的 99.4–100.1%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-28</td>
      <td style="width: 55%;"><strong>What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.27924"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究记忆对识别不可回答问题的支持。<br>
        • 在不同数据集、模型及迁移设置下比较四种记忆方法。<br>
        • 流程指导比更多经验存储更易迁移，但收益仍依赖数据集。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-28</td>
      <td style="width: 55%;"><strong>ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.28476"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习长程智能体的主动上下文编辑策略。<br>
        • 加入规划、长期记忆和卸载工具，并通过强化学习分配动作级贡献。<br>
        • 问答和深度搜索实验报告以更小上下文获得更好表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-27</td>
      <td style="width: 55%;"><strong>GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.26983"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为多模态记忆构造查询特定证据森林。<br>
        • 预算化图优化平衡直接支持、关系验证及激活成本。<br>
        • 四个基准在多个基座上报告准确率与生命周期成本权衡改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-26</td>
      <td style="width: 55%;"><strong>Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.25329"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 共同演化共享与用户专属记忆管理策略。<br>
        • 通过角色差异及跨层规则升降调整个体保留策略。<br>
        • 实验报告相较记忆增强个性化基线的持续收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-26</td>
      <td style="width: 55%;"><strong>EVOMAL: Self-Poisoning in Self-Evolving Coding Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.25776"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究通过智能体自编技能库传播的投毒。<br>
        • 受控代码任务追踪恶意模板如何进入新生成的持久技能。<br>
        • 实验发现移除源头后仍会传播，反制提示可减少观察到的复制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-26</td>
      <td style="width: 55%;"><strong>VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.26005"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为流式语音交互分离信息记忆与情感记忆。<br>
        • 并行路径支持情感归因、角色建模及流式检索。<br>
        • 实验报告个性化改善，检索延迟为 134 毫秒。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-25</td>
      <td style="width: 55%;"><strong>Memory Is Not Always Needed: Characterizing Conditional Memory in Scientific Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.23982"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析条件记忆何时帮助或干扰科学推理。<br>
        • 知识边界路由器在生成前控制记忆激活位置与强度。<br>
        • 生物和化学实验支持选择性路由优于静态记忆注入。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-25</td>
      <td style="width: 55%;"><strong>Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.24876"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合工作状态跟踪与递归演化的经验记忆。<br>
        • 固定元智能体根据执行证据进行局部且经验证的技能更新。<br>
        • 四个长程基准在大多数模型与基准组合中报告提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-24</td>
      <td style="width: 55%;"><strong>The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22767"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 记住历史相关性判断以摊薄记忆重排序成本。<br>
        • 通过因果矩阵补全融合稀疏实测评分与候选相关性估计。<br>
        • 对话实验仅直接评分少数候选即可改善准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-24</td>
      <td style="width: 55%;"><strong>UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22869"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在单一 VLA 基座中统一多模态记忆与动作控制。<br>
        • 事件触发更新、关键帧编码及缓存保留有用视觉历史。<br>
        • 仿真及硬件测试优于固定采样和分层基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-24</td>
      <td style="width: 55%;"><strong>Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.23268"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为冻结多模态模型结合示例记忆及抽象流程模式。<br>
        • 在线分类与 Shapley 归因估计规则效用以指导检索。<br>
        • MathVista、MMMU 和 MMMU-Pro 在四种基座上报告提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-24</td>
      <td style="width: 55%;"><strong>InjecMEM: Memory Injection Attack on LLM Agent Memory Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.23471"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试无需直接访问存储的单次交互记忆注入。<br>
        • 评估多个系统中后续主题相关检索及回答操纵。<br>
        • 结果显示记忆漂移下仍可持续影响，提示需要加强记忆治理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-23</td>
      <td style="width: 55%;"><strong>Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22215"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合选择性外部写入与较慢的参数固化。<br>
        • 通过模型级联路由新信息，再将高价值记忆微调进入参数。<br>
        • 作者报告冗余最多减少 68%，同时保留基线问答准确率的 98% 以上。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-23</td>
      <td style="width: 55%;"><strong>HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22310"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在用户画像引导的异构记忆图中保留原始对话。<br>
        • 查询锚点及用户画像指导迭代证据遍历。<br>
        • 两个基准报告事实推理及个性化推理改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-23</td>
      <td style="width: 55%;"><strong>When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22339"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为成功经验提炼的技能记忆加入适用边界。<br>
        • 利用条件、风险信号、规避规则及恢复说明指导选择性使用。<br>
        • AppWorld、BFCL 和 AgentDojo 实验报告可靠性与效率改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-23</td>
      <td style="width: 55%;"><strong>CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22533"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从多模型执行差异中蒸馏流程记忆。<br>
        • 通过局部整理维护可复用应用功能卡及任务技能卡。<br>
        • 留出电脑操作任务报告明显收益及跨模型迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-22</td>
      <td style="width: 55%;"><strong>MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.21867"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在智能体记忆全生命周期保留验证器信号。<br>
        • 奖励、置信度、标签及不确定性指导准入、检索、冲突处理和归档。<br>
        • 四个基准在匹配运行预算下报告成功率提高及步骤减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-22</td>
      <td style="width: 55%;"><strong>MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.22061"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究通过记住外部内容间接操纵立场。<br>
        • 社交信息流和邮件场景追踪摄入、整理及下游影响。<br>
        • BiasBench 报告持久效应，边界防御仅部分缓解。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-21</td>
      <td style="width: 55%;"><strong>Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.20631"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 动态加权任务、子任务及动作的分层记忆。<br>
        • 通过事件更新和衰减折叠已完成工作，同时保留可恢复证据。<br>
        • GAIA-Text 实验报告准确率提高与提示词 token 减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-21</td>
      <td style="width: 55%;"><strong>Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.21230"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试超出显式提示注入内容的虚假事实记忆。<br>
        • 受控投毒比较写入筛查及来源加权检索。<br>
        • 结果揭示效用损失，以及仅内容过滤和加性来源惩罚的局限。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-21</td>
      <td style="width: 55%;"><strong>ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
        <img src="https://img.shields.io/badge/自我进化-brightgreen" alt="自我进化">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.20920">
        <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 ForeDreamer，一种面向开放网络未来事件预测的自进化双智能体记忆框架，将问题级事实记忆与跨预测任务持久化的经验记忆分离。<br>
        • 主智能体负责检索与预测，记忆处理子智能体通过 MemGuide 和可执行 MemTool 将嘈杂、受时间截点约束的网页证据转化为结构化事实记忆；文本与程序性记忆通过验证门控更新共同演化。<br>
        • 在 Qwen3.5-Flash 和 GPT-5.4-Nano 上，ForeDreamer 在 Prophet Arena 上分别取得 0.1471 和 0.1839 的 Brier 分数，在 FutureX 上分别取得 0.4108 和 0.3883 的准确率，均优于对应基准和骨干模型下最强的已有对比方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-20</td>
      <td style="width: 55%;"><strong>Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.19701"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 防止相关联的多智能体记忆形成虚假多数。<br>
        • 利用依赖推断及来源信息估计独立来源并指导证据补充。<br>
        • 基准实验报告相较所比较基线更可靠的仲裁。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-19</td>
      <td style="width: 55%;"><strong>MemFuse: Multi-Source Memory Fusion from Fragmented Observations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.18704"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将碎片观察融合为可追溯来源的情节记忆。<br>
        • 利用原子事件及融合簇在因果图中组织证据。<br>
        • MemFuseBench 在三种模型设置下报告跨来源推理改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-18</td>
      <td style="width: 55%;"><strong>Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.18177"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出对过时企业记忆进行可逆抑制。<br>
        • 活动、休眠及退役状态结合滞回阈值与影子测试再激活。<br>
        • 主要给出概念控制器和示例，尚非广泛实验验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-18</td>
      <td style="width: 55%;"><strong>ArborMem: Navigating Interaction States with Memory Forests</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.17534"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将中断及恢复的对话表示为交互状态森林。<br>
        • 先定位活动分支，再恢复上下文并检索跨分支证据。<br>
        • 既有基准及 BranchMemEval 报告在有界读取预算下连续性改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-18</td>
      <td style="width: 55%;"><strong>CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.17911"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 添加超出检索器语义邻域的稀疏关联。<br>
        • 经过验证的前因链接将检索种子扩展至原先遗漏的支持证据。<br>
        • 多个记忆系统在跨会话及偏好问题上报告收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-18</td>
      <td style="width: 55%;"><strong>On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.18066"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 重新评估基于记忆的自改进智能体可靠性。<br>
        • 重复运行及打乱任务流揭示方差和任务顺序影响。<br>
        • 更明确的任务说明仅部分缓解问题，仍存在明显脆弱性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16114"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将流程记忆组织为子任务与技能超图。<br>
        • 双路检索及结构感知维护复用轨迹层关系。<br>
        • 三个智能体基准报告优于十种记忆基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16168"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从演化的个人记忆推断查询所需用户状态。<br>
        • 类型化情节记录及顺序检索智能体判断时间和情境相关性。<br>
        • PersonaMem 和 KnowU-Bench 实验报告较强个性化表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16303"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 围绕事实、时间及情感组织低信息密度对话记忆。<br>
        • 保持边界的分段构建连贯情境级记忆单元。<br>
        • ES-MemEval 和 LoCoMo 实验通过合适构建粒度改善记忆问答。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16357"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 协调分布式智能体记忆，同时显式保留矛盾。<br>
        • 通过可审计补丁及复制声明状态支持合并和分区恢复。<br>
        • HotpotQA 及部署实验报告召回、存储和收敛方面的收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16551"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离净化后的对话记忆与精确隐私值。<br>
        • 隔离存储及同意感知检索管理敏感信息全生命周期。<br>
        • 隐私感知基准报告个性化收益及不必要暴露减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>Cross-Model Memory Transfer via Target-Side Reader Adaptation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.17050"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在不同基座间迁移冻结的可寻址记忆。<br>
        • 保留已学习记忆表，仅适配轻量目标端读取器。<br>
        • 受控问答实验显示读取器对齐对有效复用至关重要。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-15</td>
      <td style="width: 55%;"><strong>Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.15071"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将嘈杂的单次执行上下文编译为可复用技能框架。<br>
        • 冻结智能体在连续任务间更新结构化流程指导。<br>
        • 五个真实任务基准评估在线跨任务适应及其影响因素。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-13</td>
      <td style="width: 55%;"><strong>ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12720"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 共同演化可执行检索技能及查询路由器。<br>
        • 经验前缀树及分离的探索、部署前沿支持稳定更新。<br>
        • 多个记忆基准报告优于静态和自演化基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-13</td>
      <td style="width: 55%;"><strong>Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12743"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将经过验证的空间经验转化为可迁移流程记忆。<br>
        • 通过反思及结果校准的可靠性评分指导冻结视觉语言模型。<br>
        • 五个空间基准在四种基座上报告改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-13</td>
      <td style="width: 55%;"><strong>When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12888"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试智能体直接搜索未改写的对话档案。<br>
        • 利用词法索引、会话控制、时间过滤及迭代搜索收集证据。<br>
        • MemoryAgentBench 和 LongMemEval 结果表明复杂语义索引并非总是必要。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-13</td>
      <td style="width: 55%;"><strong>LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12990"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在语义片段边界固化对话，避免逐轮处理。<br>
        • 类型化记录及轻量索引支持有计划的证据检索。<br>
        • LoCoMo 和 LongMemEval-S 实验减少构建 token 且不增加查询成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-13</td>
      <td style="width: 55%;"><strong>RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.13334"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以自适应联想回忆替代孤立检索。<br>
        • 线索丰富的情节锚点沿事件图关联扩展并补齐证据。<br>
        • LoCoMo 和 LongMemEval-S 实验改善准确率并降低建图成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-12</td>
      <td style="width: 55%;"><strong>Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.11654"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过容量约束下的知识覆盖形式化智能体记忆。<br>
        • 顺序决策模型将写入视为动作，将查询效用视为延迟奖励。<br>
        • 《奥德赛》案例展示效用容量前沿及覆盖率与精度的差异。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-12</td>
      <td style="width: 55%;"><strong>ε-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12522"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在程序演化任务间迁移任务无关的策略记忆。<br>
        • 自适应门控决定是否注入检索策略及其强度。<br>
        • 八项留出任务测试报告更快改进及更少有害迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-11</td>
      <td style="width: 55%;"><strong>From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.10502"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在诊断记忆故障后修复回答及持久状态。<br>
        • 依赖图使无依据的后继失效，并选择性回放受影响计算。<br>
        • 受控及轨迹派生测试改善恢复，同时保留正常记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-11</td>
      <td style="width: 55%;"><strong>Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.10676"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在搜索证据变化时修复下游推理。<br>
        • 来源关联证据树支持局部修订及受影响分支裁剪。<br>
        • 四个问答及搜索基准报告在有界单步上下文下提高准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-10</td>
      <td style="width: 55%;"><strong>Muscle Memory for Agents: Compile not Merely Retrieve</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.08995"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将重复用户意图编译为专门的可执行智能体。<br>
        • 质量门控流程挖掘历史，并通过分阶段触发匹配专家。<br>
        • 90 个场景的研究报告个性化收益及轻微准确率权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-10</td>
      <td style="width: 55%;"><strong>Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.09410"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离学习得到的运动技能与可执行记忆管理代码。<br>
        • 代码智能体启发式及多模态完成检查引导马尔可夫式 VLA。<br>
        • RoboMemArena 报告累积和任务成功率高于所比较策略。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-10</td>
      <td style="width: 55%;"><strong>MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.10108"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 按任务选择互补记忆结构的组合。<br>
        • 先验引导搜索学习冻结读取器应使用五类证据视图中的哪些。<br>
        • AMA-Bench 报告相较全结构输入以更少 token 改善回答。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-09</td>
      <td style="width: 55%;"><strong>OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.08749"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据在线轨迹结果学习机器人记忆保留。<br>
        • 离线先验及价值引导更新保留显著转移与高价值经验。<br>
        • 长程操作实验通过持续记忆演化改善预训练策略。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-08</td>
      <td style="width: 55%;"><strong>SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.08055"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在图记忆中跟踪证据来源及时间有效性。<br>
        • 类型化事实事件与规划读取检索区分更新和矛盾。<br>
        • LongMemEval-S 报告较高准确率，但使用自评且跨系统成本为估计值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-08</td>
      <td style="width: 55%;"><strong>LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.08236"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在记忆写入阶段处理多智能体矛盾声明。<br>
        • 通过显式状态及符号检查，仅在必要时调用模型协调。<br>
        • ConflictBank 明显改善，但相较讨论式方法的规划结果不一致。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-08</td>
      <td style="width: 55%;"><strong>Mitigating Over-Personalization in LLMs via Structured Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.08300"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究持久用户记忆导致的过度个性化。<br>
        • 推理时按领域划分记忆，而不修改存储内容。<br>
        • PersistBench 在七个模型上减少跨领域泄漏并保持效用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.06745"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在持久经验之上构造任务条件工作视图。<br>
        • 轻量策略选择关系、证据范围、结果条件及粒度。<br>
        • 具身及网络智能体实验改善性能并减少记忆 token。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.06811"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将分层规划与情节记忆结合用于软件修复。<br>
        • 规划阶段指导检索，记忆统计触发重规划及执行证据验证。<br>
        • SWE-bench Verified 报告解决问题增多、重复失败减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>Controlled Memory Interference in Continual LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.07622"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 诊断累积智能体记忆之间的干扰。<br>
        • 通过受控关系及更新权威信号生成针对性学习样本。<br>
        • 实验表明特定关系干扰对更新的损伤超出单纯记忆增长。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.07068"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使教师监督与学生轨迹实际使用的记忆状态对齐。<br>
        • 重建每次调用的位置和因果可见性，再进行打包式在策略蒸馏。<br>
        • 匹配对照报告相较持续历史教师评分获得 7.0% 的 F1 提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>MemWM: Memory-Augmented Text-Based World Model</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.07107"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用显式转移规则及事实记忆增强文本世界模型。<br>
        • 世界记忆约束预测，检索技能指导冻结的规划策略。<br>
        • 三个环境报告状态保真度及下游任务成功率提高。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.07169"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将教师经验转化为小模型智能体的分层记忆。<br>
        • 工作流、子任务及函数记忆提供主动和错误触发指导。<br>
        • 三个工具使用基准报告 4B–8B 学生无需参数训练即可提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-07</td>
      <td style="width: 55%;"><strong>TEPA: Revoking Stale Memories for Conflict-Robust Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.07429"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过可撤销证据记录显式表示演化记忆的有效性。<br>
        • 同键矛盾使过时先例失效，同时保留审计历史。<br>
        • 漂移测试改善当前证据利用，多跳设置暴露额外检索瓶颈。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-06</td>
      <td style="width: 55%;"><strong>Causal Episodic Memory for Feedback-Driven Agent Repair</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.05906"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 跨 SQL 修复轮次复用已验证纠正及失败方向。<br>
        • 在预言机反馈下按失败类型仅检索较早结束的经验。<br>
        • Spider 收益明确，BIRD 证据较弱，部分检索对照表现相近。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-06</td>
      <td style="width: 55%;"><strong>SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.05970"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将潜在原子技能存为可检索情节记忆。<br>
        • 专家引导分段及门控将相关技能基元融入动作预测。<br>
        • 仿真及真实任务改善扩散策略和 VLA 的组合泛化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-05</td>
      <td style="width: 55%;"><strong>FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.04530"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在潜在 GUI 记忆中分离内容保留、读取及信任。<br>
        • 角色感知表示和状态条件门控支持冻结动作策略。<br>
        • 五个 GUI 基准改善性能并减少无关记忆的负面影响。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-05</td>
      <td style="width: 55%;"><strong>MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.04843"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 训练记忆构建及查询时摘要以优化成本效率。<br>
        • 蒸馏与成本感知强化学习生成紧凑检索上下文。<br>
        • LoCoMo 和 LongMemEval 实验改善单位推理成本的质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-05</td>
      <td style="width: 55%;"><strong>Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.04933"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离具身世界记忆与任务进度记忆。<br>
        • 动态关联将活动目标绑定至回忆的对象、位置及证据。<br>
        • EB-ALFRED 和 EB-Habitat 在所评估基座上改善成功率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-05</td>
      <td style="width: 55%;"><strong>Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.05095"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过局部证据路径更新分层图记忆。<br>
        • 查询及更新条件子图协调记忆单元与依赖关系改写。<br>
        • 对话和冲突感知测试报告回答质量及 token 效率改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03130"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用差分隐私保护重复记忆条件回答中的属性。<br>
        • 私有视图选择及逐属性预算限制回答模型接收的信息。<br>
        • 受控及迁移测试在明确接口契约下保留有用个性化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03137"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 统一管理长期记忆、活动上下文与情节历史。<br>
        • 利用局部和全局验证器及分层奖励训练七种记忆操作。<br>
        • 五个基准的实验报告准确率及 token 预算效率优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03420"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究顺序博弈决策中的经验记忆。<br>
        • 通过赛后反思提炼可复用规则，无需修改模型参数。<br>
        • 井字棋实验显示可测收益，但整体顺序决策能力仍存在不足。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>LeanMem: Simple and Efficient Long-Term Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03463"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据信息属性分离画像、事件及原始记录记忆。<br>
        • 选择性事件更新及查询相关预算避免统一处理的额外开销。<br>
        • LoCoMo 和 LongMemEval-S 实验报告低构建成本下的准确率收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03699"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将记忆更新细分为五种可执行动作，超越写入或保留二选一。<br>
        • 时间范围和来源可靠性决定声明进入接受、待定或拒绝记录。<br>
        • TARL-Mem 评估报告状态恢复改善及累积污染减少。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01619"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从存储状态反向审计回答草稿中的过时行为依赖。<br>
        • 经过核验的引文及时间顺序决定候选状态转移能否触发修复。<br>
        • STALE 表现改善，外部测试则限制其普遍适用性结论。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01637"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究单独看似无害的记忆片段协同投毒。<br>
        • 受控社交平台设置追踪存储及独立会话中的行为影响。<br>
        • OpenClaw 评估揭示稀释和记忆防御下仍存在的组合风险。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01708"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将演化的用户画像直接连接至支持事件记忆。<br>
        • 通过类型化证据边及有效性排序指导个性化检索。<br>
        • 三个小模型基准优于多类记忆表示基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>CoEvo-Mem: Co-Evolving Retrieval Policy and Memory Bank for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01739"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过任务反馈共同演化检索策略与记忆库。<br>
        • 交替更新路由器及记忆以控制反馈环中的非平稳性。<br>
        • 七个基准报告联合检索与记忆适应的收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01742"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合结构化交互、稳定事实及查询中形成的事实记忆。<br>
        • 主题片段与事件轨迹保留跨时间连续性。<br>
        • LoCoMo 和 LongMemEval-S 在五个基座上报告提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Benign Alone, Harmful Together: Exploiting Experience Composition in Self-Evolving LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01759"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究单独无害的持久经验组合后产生的安全风险。<br>
        • 通过顺序经验获取测试互补记忆如何共同改变后续行为。<br>
        • 跨框架评估揭示经验组合作为独立持久攻击面的风险。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>MemArbiter: Decision-Time Memory Arbitration for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02113"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在决策时仲裁长程智能体记忆的显著性。<br>
        • 功能记忆库及时间呈现门控将存储条目转化为可用行动上下文。<br>
        • 预算匹配的 ALFWorld 实验改善成功率及失败后恢复。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>EvoGraph-Mem: Failure-Aware Editable Graph Memory for Long-Term Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.11248"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过失败感知图编辑维护可复用见解。<br>
        • 正负证据指导检索、修订、归档及新增写入。<br>
        • 多基座实验支持可编辑维护优于仅追加记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02508"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 限制记忆效用状态规模以集中稀疏学习反馈。<br>
        • 以结果和动态因子替代不断扩张的轨迹级奖励坐标。<br>
        • ALFWorld 和 LifelongAgentBench 报告更小记忆、更少调用及更好表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-02</td>
      <td style="width: 55%;"><strong>PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.00962"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在固化阶段编译面向未来的多模态记忆程序。<br>
        • 问题预测、规划及验证构建可复用证据路由库。<br>
        • 多模态基准改善答案质量和视觉召回，并降低查询成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-02</td>
      <td style="width: 55%;"><strong>TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.00967"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将记忆存储为具有来源的演化轨迹。<br>
        • 不可变快照、声明编辑及互联百科页面支持分层检索。<br>
        • LoCoMo 和 MedMT 报告对话表现及诊断可追溯性改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-02</td>
      <td style="width: 55%;"><strong>Learning What to Remember and What to Internalize in LLM Self-Evolution via Adaptive Memory-Parameter Coordination</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01234"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 协调智能体自演化中的外部记忆与参数学习。<br>
        • 根据任务路由并调度两种适应通道的知识更新。<br>
        • 实验报告相较单一通道获得更稳健的能力提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-02</td>
      <td style="width: 55%;"><strong>Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01285"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 当检索证据足够时提前终止记忆处理。<br>
        • 训练后的路由器仅将未解决查询升级至深入分析。<br>
        • AMA-Bench 和 BEAM 相较完整执行降低平均推理时间。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-02</td>
      <td style="width: 55%;"><strong>V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01543"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据查询及证据模态路由多模态记忆检索。<br>
        • 轮次对齐及生成搜索锚点缓解模态和相关性差距。<br>
        • Mem-Gallery 和 LoCoMo 报告收益，含图查询改善尤为明显。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>Tokenizer-Agnostic Engram Module</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29065"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使 Engram 查表摆脱特定分词边界的依赖。<br>
        • 使用字节序列多项式哈希，让不同 n-gram 长度共享嵌入空间。<br>
        • 测试保持接近的性能，并使相同字节序列获得相同哈希。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>Reproducing LightMem: Naive RAG Is Just as Good for Memory Management</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29104"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 复现 LightMem，并比较构造记忆与原始轮次检索。<br>
        • 受控改变检索器和预算以定位性能变化来源。<br>
        • 原始检索常相当或更好，构造记忆主要在紧预算下有优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>Zero-Mem: Zero-Token Memory Operations for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29377"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在记忆操作阶段避免生成模型调用。<br>
        • 利用实体上下文图及时间层级组织原始轨迹，支持查询特定检索。<br>
        • 匹配读取器测试保持问答竞争力并减少记忆操作时间。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>Know It, Act on It: Investigating Memory Utilization in LLM Personalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29433"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 区分知道用户偏好与实际按偏好行动。<br>
        • 配对回忆及行为测试覆盖十六个系统和五种记忆架构。<br>
        • 结果显示即使回忆出相关偏好，实际利用仍存在明显差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>Beyond Retrieval: Analytic Memory for Multimodal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29440"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为重复多模态观察加入分析运算。<br>
        • 具有来源的属性支持过滤、聚合、排序及时间比较。<br>
        • MemEye 和 MemGallery 报告优于侧重检索的记忆系统。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>CrystalMem: Elastic Memory for Self-Evolving LLM Agents via Knowledge Crystallization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.00303"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究记忆预算缩减再恢复后仍残留的能力损失。<br>
        • 使用四级保真度及受资源约束的验证式记忆重建。<br>
        • 七个环境的实验报告优于所比较基线的能力恢复效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.27773"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为智能体记忆加入语义版本控制及回滚。<br>
        • 通过完整记忆快照和混合检索将自然语言撤销请求映射至版本。<br>
        • 接触后续信息后的测试改善回滚一致问答及历史摘要。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>SKILL-KD: Contrastive Skill Distillation for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.28048"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从师生行为差异蒸馏显式技能补丁。<br>
        • 重新运行学生验证编辑，并通过轨迹关联固化限制技能漂移。<br>
        • 五个智能体基准报告冻结学生优于所比较适应方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.28103"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过紧凑意图行为表示检测记忆注入。<br>
        • 信息瓶颈过滤重复上下文，再进行轻量威胁分类。<br>
        • 实验降低攻击成功率并保持任务准确率及推理效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.28156"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将可复用检索策略与当前视频事实分离存储。<br>
        • 对历史轨迹的反思指导查询，生命周期策略控制经验噪声。<br>
        • 三个长视频基准报告多模态推理改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>MemHarness: Memory Is Reconstructed, Not Replayed</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.28272"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据当前智能体状态重构检索经验。<br>
        • 统一策略批判记忆，并通过 GRPO 学习情境化指导。<br>
        • ALFWorld 和 WebShop 实验改善性能及分布外稳健性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-29</td>
      <td style="width: 55%;"><strong>MemRetriever: Learning to Search, Reflect, and Retrieve from Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.11951"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习面向长期记忆的多步搜索和反思。<br>
        • 监督热启动及 GRPO 奖励覆盖、去噪、证据充分性和停止决策。<br>
        • 五个问答基准报告优于静态及仅监督检索。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-29</td>
      <td style="width: 55%;"><strong>Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.26637"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 系统研究文件系统中的声明性和流程记忆。<br>
        • 改变组织、工具及智能体能力以测试质量、成本和存储健康度。<br>
        • 组织结构节省搜索成本，但测得智能体未稳定将其转化为更好回答。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-29</td>
      <td style="width: 55%;"><strong>Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.27415"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过动作图连接情节经验与推理时搜索。<br>
        • 双路时序差分价值编码有用动作及高风险选项。<br>
        • 多个基准报告相较基础智能体的成功率和进展率提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-28</td>
      <td style="width: 55%;"><strong>MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.25992"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过交互式管理面板展示记忆价值。<br>
        • Shapley 式评估指导存储并可视化分层记忆记录。<br>
        • 学习助手应用支持比较质量、延迟及 token 用量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-27</td>
      <td style="width: 55%;"><strong>MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.24097"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习可解释的检索后记忆轨迹以支持回答。<br>
        • 通过证据依据奖励优化证据计划及显式记忆动作。<br>
        • LoCoMo 和 LongMemEval-S 实验改善准确率并缩短回答上下文。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-26</td>
      <td style="width: 55%;"><strong>Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.23444"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究通过恶意工具接口提取记忆。<br>
        • 跨会话评估测试用户记忆隔离下仍发生的数据暴露。<br>
        • 结果显示仅隔离存储不足以保护传入工具调用的数据。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-26</td>
      <td style="width: 55%;"><strong>MemVLN: Episodic and Procedural Memory for Vision-and-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.23504"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合情节视觉历史及紧凑流程动作用于导航。<br>
        • 金字塔记忆分辨率保留远期上下文，并降低解码开销。<br>
        • VLN-CE 实验提高成功率，推理速度快于匹配基座。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-25</td>
      <td style="width: 55%;"><strong>ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.22962"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过自一致支持评分筛查候选记忆写入。<br>
        • 重复判断或对数概率变体无需微调即可拦截依据不足的事实。<br>
        • 四个基座减少记忆污染，但对隐含事实存在代价。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-23</td>
      <td style="width: 55%;"><strong>AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21106"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为记忆构建分配细粒度过程奖励。<br>
        • 强化学习中以 token 级答案归因补充全局任务奖励。<br>
        • 长对话问答实验报告泛化改善及优化更稳定。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-22</td>
      <td style="width: 55%;"><strong>PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.20064"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以程序化方式访问完整结构化交互日志。<br>
        • 代码智能体搜索保留历史，而非依赖有损固定摘要。<br>
        • ARC-AGI-3 实验报告更高成功率及更少 token 消耗。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-20</td>
      <td style="width: 55%;"><strong>Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.17545"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据记忆预算压力选择保留或固化。<br>
        • 校准效用模型选择合并、抽象、改写或原始保留。<br>
        • LongMemEval 和 LoCoMo 显示紧预算利于固化，宽松预算利于保留。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-20</td>
      <td style="width: 55%;"><strong>Mechanistic Attention Guidance for Agent Memory Refinement</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.17621"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用内部注意力信号改进智能体记忆。<br>
        • 片段利用模式指导编辑，并通过重新执行验证。<br>
        • 交互基准在任务结果和记忆效率上优于仅文本改进方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-20</td>
      <td style="width: 55%;"><strong>Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.17879"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合探索式检索及经验回放重排序优化。<br>
        • 迭代搜索收集反馈以更新共享全局检索策略。<br>
        • 两个对话基准报告检索改善及对噪声反馈的稳健性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-17</td>
      <td style="width: 55%;"><strong>Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.15657"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究仅通过图像影响持久多模态记忆的攻击。<br>
        • 黑盒测试区分历史回忆污染与无文本依据的视觉注入。<br>
        • 五种记忆架构在攻击者无法访问文本或模型内部时仍存在漏洞。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-17</td>
      <td style="width: 55%;"><strong>LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.22690"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将记忆构建推迟至查询明确之后。<br>
        • 训练后的小模型在并行窗口中选择性压缩广泛检索的证据。<br>
        • LongMemEval 报告紧凑上下文下的较强准确率，并可迁移至 LoCoMo。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-16</td>
      <td style="width: 55%;"><strong>MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.14651"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测直接、组合及休眠式记忆污染。<br>
        • 人工核验案例覆盖注入渠道、记忆介质及模型系列。<br>
        • 写入检查对直接攻击的抑制强于组合或触发式攻击。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-15</td>
      <td style="width: 55%;"><strong>Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.13591"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习检索、计划复用、固化及遗忘的自适应控制。<br>
        • 轻量在线上下文老虎机策略封装既有记忆后端。<br>
        • 六个基准报告更高成功率及更少 token 消耗。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-15</td>
      <td style="width: 55%;"><strong>CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.20553"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用内在奖励与任务奖励联合训练轻量记忆管理器。<br>
        • 条件互信息不依赖采样查询，为非冗余记忆更新提供监督。<br>
        • 实验报告迁移能力及训练、推理效率改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-15</td>
      <td style="width: 55%;"><strong>Experience Memory Graph: One-Shot Error Correction for Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.13884"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将智能体失败恢复表述为经验图匹配。<br>
        • 成功子图及纠正编辑路径提供可复用动作指导。<br>
        • ALFWorld 和 ScienceWorld 无需测试时反复试错即可改善恢复。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-15</td>
      <td style="width: 55%;"><strong>MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.14252"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从累积第一视角视频形成具身动作记忆。<br>
        • 多个存储及在线、离线固化提炼可复用惯例与偏好。<br>
        • 45 小时基准和机器人演示支持超出已观察事件的记忆规划。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-14</td>
      <td style="width: 55%;"><strong>Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.12267"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为多跳推理显式表示调查工作状态。<br>
        • 来源明确的事实、排序假设及开放问题指导搜索和作答决策。<br>
        • 五个基准显示推理链越困难，收益通常越大。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-14</td>
      <td style="width: 55%;"><strong>AutoMem: A Text-Gradient Recursive Self-Improvement Framework for Automated Memory Architectures Search</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.14621"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 搜索适配任务的智能体记忆架构。<br>
        • 通过经验引导搜索和失败诊断优化编码、存储、检索及管理模块。<br>
        • 作者报告在六组实验设置中平均准确率提升 2.8 个百分点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-13</td>
      <td style="width: 55%;"><strong>ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.11126"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将可复用工具知识放入提供方的图记忆。<br>
        • 通过执行验证探测记录能力、失败边界及工具组合。<br>
        • MCP 基准报告收益及跨智能体、环境实例迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-13</td>
      <td style="width: 55%;"><strong>LightMem-Ego: Your AI Memory for Everyday Life</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.11487"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为日常生活助手维护流式多模态记忆。<br>
        • 对齐第一视角音视频并写入当前、短期及长期存储。<br>
        • 手机和眼镜演示支持回忆、寻物及个性化辅助。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-12</td>
      <td style="width: 55%;"><strong>The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.10608"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 诊断冲突记忆如何改变智能体动作轨迹。<br>
        • 通过进入、传播及恢复分析区分记忆诱发失败阶段。<br>
        • WebArena 和受控测试发现早期盲从及偏离后恢复不足。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-09</td>
      <td style="width: 55%;"><strong>What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.08032"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过率失真视角统一记忆压缩。<br>
        • 共享分类连接 KV 缓存、提示词、循环状态及智能体记忆。<br>
        • 指出不可逆早期删除和重复压缩评估不足等开放问题。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-09</td>
      <td style="width: 55%;"><strong>Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.08716"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用独立记忆智能体选择性主动提醒。<br>
        • 通过结构化状态更新判断何时干预未修改的行动智能体。<br>
        • Terminal-Bench 和 tau-squared-bench 实验优于被动或始终开启的记忆输入。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-08</td>
      <td style="width: 55%;"><strong>MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.06974"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 构建具有可学习选择机制的模块化步骤指令记忆。<br>
        • 粗到细检索扩展记忆，并训练面向正确率的轻量选择头。<br>
        • 实验报告推理准确率、效率及迁移方面的优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-08</td>
      <td style="width: 55%;"><strong>Parametric Multimodal User Memory: Storing What Captions Cannot Carry</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.28609"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 保留文本描述难以承载的感知用户身份。<br>
        • 情境定位和专用身份编码器与独立事实文本存储结合。<br>
        • PerceptMem 实验展示感知记忆与事实记忆的互补作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-07</td>
      <td style="width: 55%;"><strong>From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.05794"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 训练智能体主动导航多粒度用户记忆金字塔。<br>
        • 记忆工具为强化学习开放相连的对话、记录、主题及画像。<br>
        • 三个记忆基准保持竞争力，并基本保留通用能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-07</td>
      <td style="width: 55%;"><strong>MemDefrag: Latent Memory Defragmentation for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.05969"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 无需额外训练即可整理潜在记忆碎片。<br>
        • 利用中间层注意力引导片段排序、过滤及信息感知遗忘。<br>
        • 作者报告在多轮记忆更新后获得明显更好的知识保留率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-07</td>
      <td style="width: 55%;"><strong>NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.06678"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用 VLA 原生视觉编码器压缩历史相机帧。<br>
        • 先对齐单 token 帧记忆，再进行任务特定策略微调。<br>
        • 仿真及机器人实验报告较强成功率和较低额外延迟。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-06</td>
      <td style="width: 55%;"><strong>Your Agent&#39;s Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.05029"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究伪造推理历史形成的持久记忆攻击。<br>
        • 分层结构检测器筛查候选推理条目中的操纵。<br>
        • 小规模评估报告攻击减少，受测正常轨迹中未观察到误报。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-06</td>
      <td style="width: 55%;"><strong>When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.05189"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试通过普通外部邮件处理发生的隐蔽记忆注入。<br>
        • WhisperBench 追踪持久智能体中的静默采纳及后续影响。<br>
        • 留出评估揭示多层防御下仍存在跨系统持久风险。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-06</td>
      <td style="width: 55%;"><strong>When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.06595"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究工具使用型个人智能体的记忆投毒。<br>
        • 两阶段评估追踪投毒记录的初始存储及后续激活。<br>
        • 记忆保存策略和检索筛查降低攻击成功率并保持效用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆漂移-blue" alt="记忆漂移">
          <img src="https://img.shields.io/badge/个性化-brightgreen" alt="个性化">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.02374v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • DRIFTLENS 是一个无需真值标签的框架，将每个表达出的推理步骤映射到一个价值本体符号，并测量问题在"无记忆"轨迹与"注入用户属性记忆"轨迹之间的偏离，揭示出个性化记忆会悄然重塑模型的推理方式（"符号漂移"），而不仅仅是其答案。<br>
          • 使用价值本体和两个漂移指标（DTW 和 SRI），在一个不可验证、与人设无关的问题基准上测量个性化 LLM 在记忆扰动下的逐实例推理稳定性，并评估基于 GRPO 和 DPO 的后训练作为缓解手段。<br>
          • 在四个 LLM 和 10 个用户属性类别上，无关的人设记忆引起中到大的推理漂移（Cohen's d ≈ 0.35–0.98）；GRPO 和 DPO 都能减少漂移但均不占绝对优势（例如在 Gemma2-2B 上 GRPO 将 DTW 降至 0.186 vs. 0.309；DPO 在 Qwen3-4B 上达到 0.204）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/KV记忆-blue" alt="KV记忆">
          <img src="https://img.shields.io/badge/持续学习-brightgreen" alt="持续学习">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.02010v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将持续的多模态 LLM 适应重构为预算受限的在线诱导集选择：任务增量被存储为与注意力兼容的外部 KV 记忆（一个冻结的检索键加上紧凑的逐层 KV 载荷），注入自注意力，在严格固定的记忆预算下保持骨干冻结。<br>
          • 固定占用的 MLLM 持续适应（任务增量微调、持续 VQA、领域增量、终身微调）；提取可直接用于注意力的记忆条目，并通过双层优化（内层检索校准；外层权重选择）构建紧凑的诱导集。<br>
          • 在预算相当的条件下持续超越 PEFT、MoE、回放和提示检索基线；在 UCIT 上相较 HiDe-LLaVA 提升 0.88 Avg/1.12 Last，在 COIN 上提升 1.35/1.43，并将持续 VQA 的 AP 从 51.34 提升至 52.64（优于 CL-MoE），在 VQACL 上超越 QUAD。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-blue" alt="长期记忆">
          <img src="https://img.shields.io/badge/状态感知-brightgreen" alt="状态感知">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01935v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 识别出"幽灵记忆"——一种状态协调失败，其中旧的、当前的和过渡态的事实共存并误导答案——并提出 A-TMA（自适应真值维护审计），一个状态感知的叠加层，将记忆解耦为三个可诊断的层级（记忆库维护、检索、回答时消解）。<br>
          • 用户事实变化下的长期智能体记忆；A-TMA 用带类型的链接保留被取代/过渡记录（一个轻量的 Sentry 门控加上一个 Qwen2.5-3B 评判器），构建状态对齐的证据包，并将问答以显式标签为条件，同时提出一个冲突密集的新基准 LTP（LoCoMo Temporal Plus）。<br>
          • 在 LTP 上，Graphiti/Zep +A-TMA 将冲突准确率绝对提升 0.240（0.480→0.720），InsideOut+A-TMA 将准确率从 0.117 提升至 0.662；在 LoCoMo 上，Graphiti/Zep +A-TMA 将时间 F1 从 0.0295 提升至 0.1705。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>Learning User-Aware Recall: Personalized Retrieval in Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-blue" alt="长期记忆">
          <img src="https://img.shields.io/badge/个性化检索-brightgreen" alt="个性化检索">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00017v2">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 画像引导的个性化检索优化（PPRO）通过将派生的用户画像嵌入作为显式的个性化先验注入检索排序分数，使长期对话记忆检索既具用户感知又可优化。<br>
          • 个性化长期对话问答；PPRO 离线构建情景与语义记忆库以及用户画像，执行画像引导的双路检索，并用 GRPO 以证据检索与答案质量为奖励训练一个查询改写器，同时保持记忆库和回答模型冻结。<br>
          • 在 LoCoMo 上，PPRO 在三个骨干模型上均取得最佳总体 F1，以 7–19 个百分点胜过此前最佳的 SimpleMem（例如 GPT-4o 总体 F1 48.16 vs. 40.87）；在 LongMemEval-S 上达到 81.5 的总体准确率，而最佳基线为 75.9。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>ISM: Self-Improving Strategy Memory for Continual Mathematical Reasoning</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/策略记忆-blue" alt="策略记忆">
          <img src="https://img.shields.io/badge/持续学习-brightgreen" alt="持续学习">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.31191v3">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 智能图式记忆（ISM）是一种自演化的外部记忆，通过维护一个紧凑、有界的策略图式库（双重表示：稳定内容 + 在线自适应特征钩子），让冻结的 LLM 在硬性回合重置下提升数学推理能力，其中每次更新都由符号验证把关。<br>
          • 在参数冻结的流式回合协议下进行持续数学推理；ISM 采用两阶段检索（算子过滤 + 软打分）、对称的成功/失败学习，以及七种自我改进机制加上条件化的图式合成。<br>
          • 在 300 回合的流上，MATH-Hard 达 80.67%、OlympiadBench 达 61.67%，各以 +2.00 个百分点胜过最强基线，同时存储的图式分别减少 64% 和 86%（条目最多减少 23×），并在 OlympiadBench 上取得正向后向迁移（+0.03）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>Multi-Head Recurrent Memory Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/循环记忆-blue" alt="循环记忆">
          <img src="https://img.shields.io/badge/长上下文-brightgreen" alt="长上下文">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01523v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将循环记忆性能分解为"捕获"与"保持"，诊断出保持是主导瓶颈（由单块整体记忆造成），并提出多头循环记忆（MHM）——一个免训练框架，将记忆划分为独立的头，采用分阶段的"先选择再更新"策略，从结构上保护未选中的头不被覆写。<br>
          • 在 100K–1M token 上进行可靠的长上下文推理；MHM-LRU 是一个轻量实例，每步选择最近最少更新的头，保证各头利用均匀，零额外 token 开销且无需重训。<br>
          • 在 896K token 的 RULER-HQA 上，MHM-LRU 将保持率从小于30% 提升至 73.96%、准确率提升至 49.74%（vs. MemAgent 21.62%、原生 LLM 0.00%）；在 1M token 的 BABILong 上达到 41.41% vs. MemAgent 的 25.26%，在基线崩溃之处仍保持稳定。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>AUTOMEM: Automated Learning of Memory as a Cognitive Skill</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/元记忆-brightgreen" alt="元记忆">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01224v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 通过将文件系统操作（读/写/搜索/追加/创建）提升为与任务动作并列的一等记忆动作，将记忆管理重构为一项可独立训练的"元记忆"技能，然后经由元-LLM 驱动的外层循环，沿脚手架结构与模型熟练度两个维度自动化地改进它。<br>
          • 长程程序化生成游戏（Crafter、MiniHack、NetHack）；循环 1（元-LLM 修订智能体脚手架/文件模式）和循环 2（元-LLM 甄选优质记忆决策，对一个专门的"记忆专家"进行 LoRA 微调，同时游戏模型保持冻结）。<br>
          • 仅优化记忆就在 Qwen2.5-32B 基座上带来约 2×–4× 的提升——Crafter 25.0→51.36%、MiniHack 7.5→30.0%、NetHack 0.42→1.85%——使该 32B 模型达到 Claude Opus 4.5 和 Gemini 3.1 Pro Thinking 等前沿系统的水平。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-01</td>
      <td style="width: 55%;"><strong>Imprint: Online Memory Compression for Long-Horizon Egocentric QA</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆压缩-blue" alt="记忆压缩">
          <img src="https://img.shields.io/badge/第一人称问答-brightgreen" alt="第一人称问答">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00696v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Imprint 将长程第一人称记忆重构为一个在线记忆压缩问题（而非分层文本摘要），将观测表示为结构化的交互记录，并用受认知启发的重现性、近因性和独特性信号对其进行整合。<br>
          • 长程第一人称问答；通过 Qwen2.5-7B-Instruct 将字幕解析为（人物、动作、物体、时间戳）记录，将其归组为事件原型，为重要性打分，并在线整合为紧凑的面向检索的记忆。<br>
          • 在 EgoLifeQA 7 天基准上，将问答准确率从 31.0% 提升至 35.8%，将有据可依的准确率从 10.8% 提升至 64.8%（比 EgoRAG 多 6× 的证据支撑答案），同时将记忆占用降低 2.3×（109 MB vs. 254 MB）、检索延迟降低 11.8×（1.7 秒 vs. 20.1 秒/查询）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-30</td>
      <td style="width: 55%;"><strong>From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆架构-blue" alt="记忆架构">
          <img src="https://img.shields.io/badge/语言涌现-brightgreen" alt="语言涌现">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.00233v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 证明在使用冻结 LLM 智能体的 Lewis 信号博弈中，对语言涌现而言记忆架构比信道容量更重要——一个持久的私有笔记本让智能体能够外化习得的约定，从而避免无状态智能体中出现的高容量崩溃。<br>
          • 一个双智能体指称信号博弈（发送方/接收方从零协调一套编码），用 gpt-5.4-mini 运行；在从 4 到 125 的信道容量下比较五种记忆架构（仅记忆、环境板、便签本、码本、码本元）。<br>
          • 便签本笔记实现了最可靠的协调（容量=25 时为 0.867 ± 0.023），而无状态的"仅记忆"在 cap=25 达到峰值后崩溃（cap=64 时冲突为 1.0）；信息瓶颈点（cap=8）是一个双峰脆弱点，而非组合性最优点。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-30</td>
      <td style="width: 55%;"><strong>The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/记忆更新-brightgreen" alt="记忆更新">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.31121v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Janus 是一个与方法无关的插件式记忆控制器，把每次候选记忆更新都视为"接受/拒绝"的部署决策，将"记忆动量触发器"（何时比较新旧记忆）与由覆盖、边界和新鲜任务构成的紧凑混合评估集（在什么上比较）结合起来。<br>
          • 面向任务求解智能体的顺序演化 LLM 记忆；Janus 包裹现有的记忆更新器（如 DC-RS、ExpeL）而不改变其更新规则，利用记忆更新轨迹的方向性偏离来触发成本有界的新旧对比验证。<br>
          • 在六个数据集、两个 LLM（Qwen3-8B、DeepSeek-V4-Flash）和两个更新器上，Janus 将平均准确率提升 +2.7 至 +4.6 个百分点（例如在 Qwen3-8B 上 DC-RS 79.5→83.2、ExpeL 78.3→81.5）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Forensic Trajectory Signatures for Agent Memory Poisoning Detection</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆投毒-blue" alt="记忆投毒">
          <img src="https://img.shields.io/badge/智能体安全-brightgreen" alt="智能体安全">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.30566v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 发现一个由机制强制产生的行为不变量（"发送邮件前先回忆事实"），持久性记忆投毒攻击会将其印刻在 LLM 智能体的工具调用轨迹上，从而无需访问记忆内容、模型权重或激活值，仅凭操作级工具日志即可检测。<br>
          • 通过从触发会话工具日志中提取 19 个轨迹特征并训练 LR/RF/GBM 分类器来检测记忆通道（延迟触发）投毒，在跨 9 个模型（7B–120B）的 2,520 次运行上，经 5 折交叉验证、BCa 自助法和留一模型验证进行评估。<br>
          • 单条不变量规则本身即达到 AUC=0.9563；完整的随机森林达到 AUC=0.9904（Recall 0.984），在 6/9 的跨模型留出上 AUC=1.000，并可零重训迁移到 GPT-4.1/GPT-4o；仅用前缀的变体达到 AUC=0.934，可用于在线拦截。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/程序性记忆-blue" alt="程序性记忆">
          <img src="https://img.shields.io/badge/激活引导-brightgreen" alt="激活引导">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29824v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • NPM 是一个免训练框架，将智能体的程序性记忆表示为残差流中的隐式激活引导向量，而非显式文本指令，这些向量从双粒度对比经验中蒸馏而来，以克服 RAG 注入指南的"文本-动作脱节"问题。<br>
          • 面向 LLM 智能体的程序性记忆；从对比的成功/失败轨迹预先计算引导向量，然后检索并动态合成一个任务特定向量，在推理时注入以调制推理与动作选择，无需参数更新或上下文扩展。<br>
          • 在四个基准（ALFWorld、WebShop、ScienceWorld、BabyAI）上，NPM 匹敌/超越显式文本基线（例如 MiniCPM3-4B 均值 22.60→28.87；Qwen3-8B 30.63→36.32），而混合的 NPM+Workflows 设置总体最佳（Qwen3-8B 均值 41.89，ALFWorld 66.42%）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-29</td>
      <td style="width: 55%;"><strong>Mandol: An Agglomerative Agent Memory System for Long-Term Conversations</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/长期对话-brightgreen" alt="长期对话">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29778v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • Mandol 将碎片化的向量/图记忆整合为统一的记忆原生架构，结合了分层记忆模型、原生融合键值/向量/图存储的凝聚式 SemanticMap/SemanticGraph 结构，以及一种无需调用 LLM 即可运行的定量检索机制。<br>
          • 长期跨会话对话记忆；用查询自适应路由、基于 MAD 的去噪/冲突消解，以及在内存统一存储（配合 DuckDB 持久化）上的 MMR token 受限上下文生成，取代 RAG 式的"先召回再排序"。<br>
          • 在 LoCoMo（92.21%）和 LongMemEval（88.40%）上取得最佳总体准确率，在 10 QPS 负载下平均检索加速约 5.4×、平均插入加速约 4.8×，相较 EverMemOS 削减 token 17.4–20.0%。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-28</td>
      <td style="width: 55%;"><strong>Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆整合-blue" alt="记忆整合">
          <img src="https://img.shields.io/badge/记忆投毒-brightgreen" alt="记忆投毒">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29279v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 诊断出"人为制造的自信"——记忆整合产品（mem0、LangMem）会把含糊、随口的言论改写成自信、带日期的独立"事实"，智能体随后照单全收；表明智能体依据措辞的自信程度而非来源，且无需攻击者。<br>
          • 使用无需评判的访问控制与预算审批智能体，跨五个模型/四个供应商隔离该失败，对 mem0、LangMem 及逐字存储对照运行相同的投毒协议，并测试措辞方式、来源归属、不确定性标签以及一个保留含糊语气的抽取提示。<br>
          • mem0 和 LangMem 以 100% 的比例将含糊注入"洗白"为自信事实（逐字对照为 0%）；自信措辞授予未授权访问约 0.81，而含糊语气则坍缩至约 0.00；冗余目录可将错误授予恢复为 0.00，保留含糊语气的抽取将错误授予从 0.45 降至 0.10。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-28</td>
      <td style="width: 55%;"><strong>Selective Memory Retention for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆保留-blue" alt="记忆保留">
          <img src="https://img.shields.io/badge/长程智能体-brightgreen" alt="长程智能体">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29178v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • TraceRetain 是面向冻结 LLM 智能体的轻量级容量受限记忆保留框架，通过可解释特征（成功度、年龄、访问频率、冗余度、特异性、相似度、下游效用）为记忆条目打分，并驱逐得分最低者。<br>
          • 将外部记忆管理表述为 ALFWorld 上的容量受限保留问题（gpt-5-mini，ReAct 风格），在 75% 干扰项的噪声写入压力下，将 TraceRetain-Linear/CEM 与缓存启发式（FIFO/LRU/LFU/Random/Ebbinghaus）及无界记忆进行比较。<br>
          • 在干净的 ALFWorld 上各方法趋于饱和（47–49/50 vs. 无记忆 39/50）；在噪声写入下，无界与 FIFO 的 Precision@5 崩溃，而 TraceRetain-CEM 保持稳定（16.9%→16.6%）并保住 97/100 的任务成功率，且有界 K=50 可媲美无界 K=100。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-27</td>
      <td style="width: 55%;"><strong>Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆攻击-blue" alt="记忆攻击">
          <img src="https://img.shields.io/badge/智能体安全-brightgreen" alt="智能体安全">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.29030v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将 LLM 智能体的外部记忆视为攻击面，表明通过普通自然语言交互插入的误导性或被污染的记忆，即使在当前查询是干净的情况下，也能悄然改变智能体的答案。<br>
          • 构建一个由规划器引导、带外部记忆的 LLM 问答智能体用于四选一多选题，然后施加两种攻击——虚假信息记忆注入和基于交互的答案选项引导——覆盖机器学习、网络安全和网络领域，在 GPT-5.4/GPT-4o mini、Gemma2-9B 和 Phi3-14B 上进行。<br>
          • 干净基线平均为 91.85%（闭卷）vs. 77.10%（开卷）；虚假记忆注入导致 82/1064 个答案改变（7.80% 攻击成功率），Phi3-14B 最脆弱（网络安全领域偏移 34.48%）；反馈强化对答案的偏置作用大于示例暴露。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-25</td>
      <td style="width: 55%;"><strong>Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/记忆更新-blue" alt="记忆更新">
          <img src="https://img.shields.io/badge/强化学习环境-brightgreen" alt="强化学习环境">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.27472v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将"取代"（保持已变更事实的当前值）确立为一种独立、可训练的失败模式，并发布 Supersede——首个奖励直接针对事实时效性而非代理指标的强化学习环境，将 FAMA 指标重构为稠密训练信号。<br>
          • 在有界、自维护的记忆下处理长多会话对话中的被取代事实；在 LongMemEval 知识更新子集上诊断该差距，并通过对 Qwen2.5-3B 进行 GRPO 微调、配以程序化的取代感知奖励来将其训练缩小。<br>
          • 有界记忆使前沿 gpt-5.4 的知识更新准确率从 92% 降至 77%（p=0.0033）；随对话增长 24×，准确率进一步从 68% 降至 28%；GRPO 训练在真实未见对话上将留出的取代准确率几乎翻倍（9.0%→16.7%）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-25</td>
      <td style="width: 55%;"><strong>Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/时效性-blue" alt="时效性">
          <img src="https://img.shields.io/badge/检索记忆-brightgreen" alt="检索记忆">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.26511v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • MemStrata 通过在双时态账本中的确定性（主语、关系、宾语）取代规则来维护时效性——无需相似度阈值、读取路径上无需调用 LLM 即可淘汰陈旧事实——并有一个证明支撑：余弦相似度无法区分矛盾与重复（AUROC 0.59）。<br>
          • 在演化知识（代码重命名、配置/依赖/API 变更）下保持智能体记忆最新；像 RAG 一样存储事实以实现完整的静态召回，但对被矛盾的值进行取代，在本地 7B 模型上跨 6 个基准完全确定性地评估。<br>
          • 在静态知识上与 RAG 打平，但在演化知识上达到 0.95–1.00 准确率，而 RAG 仅为 0.20–0.47（2–5× 提升），将陈旧事实错误率从 15–40% 降至约 0%，并比 LLM 重排基线快约 8×（约 2.1 秒 vs. 约 16–18 秒）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-24</td>
      <td style="width: 55%;"><strong>Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/会话记忆-blue" alt="会话记忆">
          <img src="https://img.shields.io/badge/记忆分类法-brightgreen" alt="记忆分类法">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.25361v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 提出首个按功能角色划分的细粒度会话记忆分类法（回答型、澄清型、丰富型、干扰型、无关型），并配以以用户为中心、上下文感知的"LLM 作为评判者"评估框架，涵盖准确性、相关性与信息量。<br>
          • 在两个长期多会话数据集（LongMemEval-m、Long-MT-Bench+）上对会话式 RAG 进行受控对比实验，使用三种前沿 LLM 和三种检索器，改变上下文规模与记忆类型组成。<br>
          • 澄清型记忆可靠地提升事实准确性；干扰型记忆显著损害准确性/相关性；无关型记忆降低主题相关性；随上下文增长性能先升后降（信息过载），且回答型记忆始终不可或缺。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/联想记忆-blue" alt="联想记忆">
          <img src="https://img.shields.io/badge/测试时计算-brightgreen" alt="测试时计算">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24543v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将 LLM 推理重新表述为从稠密联想记忆中的检索——正确推理链为平坦极小值的吸引子盆地，幻觉为尖锐极小值——并引入"Gibbs 加权盆地选择"算子，按谱熵的平方反比（W ∝ E⁻²）对采样路径重新加权。<br>
          • 数学推理（GSM8K）；采样 K 条高温轨迹，将每条路径的轨迹能量计算为长度归一化的 NLL，然后通过事后 Gibbs 测度重新加权，以"弛豫"进入主导吸引子盆地。<br>
          • 在 GSM8K 上用 Phi-3.5-mini（3.8B），Gibbs 加权检索（K=12）达到 90.07%，而标准采样/多数投票为 84.69%、贪心解码为 78.4%——相较自洽性提升 +5.38%。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/推理记忆-blue" alt="推理记忆">
          <img src="https://img.shields.io/badge/混合智能体-brightgreen" alt="混合智能体">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24437v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 一个记忆增强的混合智能体框架，构建于"排序推理记忆"之上，通过一个比较式的评审智能体持久地存储/排序跨层推理轨迹，并搭配"精选多样化记忆路由"以同时保持推理质量与探索多样性。<br>
          • 可扩展的多智能体 LLM 推理；每一层由评审智能体带理由地比较打分轨迹，后续智能体接收不同的高/低/对比轨迹子集，并可选地用前沿模型（GPT-5.5）LoRA 蒸馏流水线来升级评审智能体。<br>
          • 在五个推理基准（MATH、MMLU-redux、Formal Logic、CRUX、HellaSwag）上持续超越以往 MoA 变体，且差距随深度加大——例如 MATH 在 L=9 时：ReM-MoA* 84.0% vs. AttentionMoA 76.9% vs. 标准 MoA 61.0%。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-19</td>
      <td style="width: 55%;"><strong>When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/轨迹检索-brightgreen" alt="轨迹检索">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.28376v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • OSU-Mem 将智能体轨迹记忆组织为重叠的语义单元，并进行预算受限的由粗到细检索；通过单元格条件分析表明，仅当证据步骤共享工具调用或实体（T+E+）时重叠才有帮助，而当二者都不共享（T−E−）时重叠反而有害。<br>
          • 在严格 token 预算下从长程 LLM 智能体轨迹中进行预算受限检索；从实体/工具/子目标/相似度视图构建 OSU，再进行查询自适应的质心打分扩展，在合成基准、τ-bench 和 ToolBench 上以 2×2（工具/实体）交叉列联表进行评估。<br>
          • 在合成基准上，B=256 时相较最强基线 Recall +39.9%、Hit@2 +61.5%；在 τ-bench 上于 T+E+ 取胜但在 T−E− 落败；在 ToolBench 上重叠构建以单调的剂量-响应关系胜过不相交构建。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-05-30</td>
      <td style="width: 55%;"><strong>Memory Shot for Long-Term Dialogue</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/对话记忆-blue" alt="对话记忆">
          <img src="https://img.shields.io/badge/视觉记忆-brightgreen" alt="视觉记忆">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.28338v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • MemShot 将原始对话片段直接渲染为结构化的视觉"记忆快照"（保留说话者轮次、时间戳和轮次边界的图像），并利用 MLLM 的内部视觉推理能力，避免了脆弱、笨重的基于文本的记忆构建。<br>
          • 长期对话记忆增强问答；将对话切分为连续片段，把每个片段渲染为分层的"标题+聊天"视觉单元，检索 top-k 单元（Qwen3-VL-Embedding-8B），并用 Qwen3-VL-Instruct MLLM（2B/8B/32B）生成答案。<br>
          • 在 LoCoMo（32B 时总体准确率 79.61）和 LongMemEval（32B 时总体准确率 74.80）上表现从有竞争力到更优，同时记忆构建速度快约 70×（≈9.56 秒），并以超过 10% 的优势击败视觉记忆基线 MemOCR。
      </td>
  </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-25</td>
        <td style="width: 55%;"><strong>MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agentic%20RAG-4A90E2" alt="Agentic RAG">
          <img src="https://img.shields.io/badge/红队测试-F5A623" alt="Red Teaming">
          <img src="https://img.shields.io/badge/记忆引导搜索-7ED321" alt="Memory Guided Search">
          <img src="https://img.shields.io/badge/安全-D0021B" alt="Security">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.26793v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文研究多模态 agentic RAG 系统的红队测试问题，其攻击面同时包含检索文本、图像注入、直接用户查询以及编排器层面的工具操纵。<br>
          • MIRROR 将成功攻击轨迹组成的情景记忆库与蒙特卡洛树搜索结合：检索到的记忆提供搜索先验，而确定性的 novelty gate 阻止复用已知或已检索攻击模板。<br>
          • 在四类攻击面上，该框架通过确定性 replay 或结构化工具调用解析来验证候选攻击，使记忆引导的对抗搜索更有效，同时减少对重复模板的依赖。
        </td>
      </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Experience%20Learning-4A90E2" alt="Experience Learning">
        <img src="https://img.shields.io/badge/Agent%20Memory-F5A623" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Verification-7ED321" alt="Verification">
        <img src="https://img.shields.io/badge/Self--Evolution-D0021B" alt="Self-Evolution">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.24428v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文研究 LLM Agent 的经验驱动自我演化，并指出一种“自我确认陷阱”：单代理循环可能把错误但自洽的轨迹误判为成功经验，导致错误记忆在后续检索和复用中持续累积。<br>
        • 论文提出 EDV（Execute-Distill-Verify）框架：多个异构代理先并行探索同一任务空间，第三方蒸馏代理再比较候选轨迹并生成经验候选，最后由执行组通过共识机制验证，只有通过验证的经验才会写入共享或私有记忆。<br>
        • 通过解耦执行、经验蒸馏与验证，EDV 将孤立自反思转化为协作式经验构建，并在记忆写入前过滤噪声和错误内容；在 tau2-bench、Mind2Web 与 MMTB 上的实验显示其稳定优于强基线，强调可靠记忆构建对于 Agent 自我演化的重要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-18</td>
      <td style="width: 55%;"><strong>Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Self--Attention-4A90E2" alt="Self-Attention">
        <img src="https://img.shields.io/badge/Mixture--of--Experts-F5A623" alt="Mixture-of-Experts">
        <img src="https://img.shields.io/badge/Grouped--Query%20Attention-7ED321" alt="Grouped-Query Attention">
        <img src="https://img.shields.io/badge/Long%20Context-D0021B" alt="Long Context">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.20945v2">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文提出 Grouped Query Experts（GQE），在 grouped-query attention 之上引入 mixture-of-experts 层，用于降低长上下文场景中密集 self-attention 的高昂计算成本。<br>
        • 在每个 GQA group 内，路由器为每个 token 选择 k 个 query-head experts，而所有 key-value heads 保持密集且不变；该设计保留 GQA 的 KV cache 优势，同时根据 token 难度或信息量减少活跃 query head 计算。<br>
        • 在 250M 参数规模、固定 30B token 训练预算下，GQE 在下游准确率上匹配全激活 GQA 基线，同时每个 token 仅激活一半 query heads，为更高效的长上下文处理提供了一条路径。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-18</td>
      <td style="width: 55%;"><strong>Multi-Agent Transactive Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multi%20Agent%20Systems-4A90E2" alt="Multi-Agent Systems">
        <img src="https://img.shields.io/badge/Transactive%20Memory-F5A623" alt="Transactive Memory">
        <img src="https://img.shields.io/badge/Trajectory%20Retrieval-7ED321" alt="Trajectory Retrieval">
        <img src="https://img.shields.io/badge/Knowledge%20Sharing-D0021B" alt="Knowledge Sharing">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.19911v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文提出多智能体交互记忆MATM，将异构代理生成的行动—观测轨迹组织为群体级共享记忆：生产者代理贡献执行经验，消费者代理检索既有轨迹，从而复用通常会在单次任务后被丢弃的过程性知识。<br>
        • MATM采用状态条件的键值索引，将当前任务及近期交互历史作为检索键、后续轨迹片段作为值，并进一步使用学习排序模型综合生产者可靠性、消费者特征、检索得分与轨迹属性进行个性化重排序。<br>
        • 在ALFWorld和WebArena中，检索共享轨迹能够在无需代理间直接协调或联合训练的情况下提升任务效果并减少交互步骤，且收益可覆盖不同能力水平的代理；该工作由此将个体经验记忆扩展为支持开放代理生态的集体知识基础设施。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-17</td>
      <td style="width: 55%;"><strong>What Must Generalist Agents Remember?</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Theoretical%20Analysis-4A90E2" alt="Theoretical Analysis">
        <img src="https://img.shields.io/badge/Memory%20Necessity-F5A623" alt="Memory Necessity">
        <img src="https://img.shields.io/badge/Domain%20Disambiguation-7ED321" alt="Domain Disambiguation">
        <img src="https://img.shields.io/badge/Model%20Reconstruction-D0021B" alt="Model Reconstruction">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.18746">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文从形式化角度研究通用智能体为在多个环境和目标上保持近最优行为所必须保存的信息，并将观测相同但最优动作冲突的状态定义为揭示记忆必要性的观测瓶颈。<br>
        • 分离定理表明，当不同领域在该瓶颈处要求互不兼容的最优动作时，任何统一近最优策略都必须形成不同的记忆分布；因此，仅依赖当前观测的无记忆策略无法同时维持高成功率和跨领域鲁棒性。<br>
        • 论文进一步证明，若记忆足以估计一组相关目标的价值函数，则可由其近似恢复局部转移动力学，使记忆同时承担领域消歧、环境模型重构与规划基质的功能；这些结论属于理论必要性结果，并不直接指定具体的工程记忆架构。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-17</td>
      <td style="width: 55%;"><strong>User as Engram: Internalizing Per-User Memory as Local Parametric Edits</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Personalized%20Memory-4A90E2" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Local%20Parametric%20Edits-F5A623" alt="Local Parametric Edits">
        <img src="https://img.shields.io/badge/Content%20Skill%20Separation-7ED321" alt="Content-Skill Separation">
        <img src="https://img.shields.io/badge/Engram%20Architecture-D0021B" alt="Engram Architecture">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.19172">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文将个性化记忆拆分为用户特定内容与跨用户共享推理技能，并提出在Engram模型的哈希键记忆表中以局部行编辑保存用户事实，同时由单一共享适配器承担事实解释和间接推理能力。<br>
        • 与对全局权重产生稠密影响的每用户LoRA不同，局部Engram编辑仅在精确触发位置生效，不改变其他位置；不同用户的事实写入互不重叠的哈希槽，因此能够在共享表中实现可加、无损的多用户组合。<br>
        • 论文报告该设计在直接召回上匹配每用户LoRA，间接推理准确率平均提高5.6倍，记忆占用约缩小33000倍，并在约100条事实后超过使用更大模型的检索流水线；其适用性则依赖底层模型具备可编辑的Engram记忆结构。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-16</td>
      <td style="width: 55%;"><strong>Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Verbal%20Reinforcement%20Learning-4A90E2" alt="Verbal Reinforcement Learning">
        <img src="https://img.shields.io/badge/Insight%20Governance-F5A623" alt="Insight Governance">
        <img src="https://img.shields.io/badge/Structured%20Evidence-7ED321" alt="Structured Evidence">
        <img src="https://img.shields.io/badge/Nonstationary%20Environments-D0021B" alt="Non-stationary Environments">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.17591">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文指出，无参数更新的言语强化学习在非平稳环境中面临“保留—遗忘”两难：长期保留失效规则会产生负迁移，而永久删除旧知识又会在相似条件重现时造成灾难性遗忘。<br>
        • 作者提出由规则、证据和技能组成的三层记忆架构，并以反馈驱动的策展循环连接三层：规则蒸馏经验，证据记录规则跨回合的可靠性，技能负责规则选择、冲突消解与必要时的拒绝决策。<br>
        • 金融预测案例显示，相同的累积经验在缺少治理时可能使表现低于零样本基线，而加入策展循环后能够改善预测准确率与风险调整后收益，说明智能体持续学习的关键瓶颈不仅是经验提取，更是知识生命周期与应用权限的治理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-16</td>
      <td style="width: 55%;"><strong>Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Embodied%20Memory-4A90E2" alt="Embodied Memory">
        <img src="https://img.shields.io/badge/Flash%20Endurance-F5A623" alt="Flash Endurance">
        <img src="https://img.shields.io/badge/Storage%20Hierarchy-7ED321" alt="Storage Hierarchy">
        <img src="https://img.shields.io/badge/Resource%20Pricing-D0021B" alt="Resource Pricing">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.18144">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文将机器人闪存的有限擦写寿命建模为不可再生的折旧资本，引入耐久性影子价格η，并据此构造磨损增强的每字节索引，以优化记忆在RAM、板载非易失存储与云端之间的层级放置。<br>
        • 理论分析表明，阈值式放置策略在不同价值—写入相关性χ下均可实现成本最优；只有当χ为正时，最优策略才可能呈现非单调性，即将写入频繁的高价值记忆移出本地闪存。真实日志显示χ在循环性长程操作、短程任务和非循环遥操作中分别表现为正、近零和负。<br>
        • 耐久性约束在高端约3000次P/E的TLC器件上通常不活跃，却可能约束约1000次P/E的QLC或eMMC设备；论文同时明确指出，磨损感知主要改善设备寿命和成本，尚未证明能够提升任务价值或任务成功率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-15</td>
      <td style="width: 55%;"><strong>Posterior Twins: Distributional Behavioral Simulation for Enterprise Decisions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Digital%20Twins-4A90E2" alt="Digital Twins">
        <img src="https://img.shields.io/badge/Behavioral%20Simulation-F5A623" alt="Behavioral Simulation">
        <img src="https://img.shields.io/badge/Distributional%20Fidelity-7ED321" alt="Distributional Fidelity">
        <img src="https://img.shields.io/badge/Memory%20Grounded-D0021B" alt="Memory Grounded">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.16415">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文提出Posterior Twins，将企业数字孪生的输出从单一最可能行为扩展为特定决策情境下的后验行为分布，以刻画不同群体的接受、流失、犹豫和风险迁移状态。<br>
        • 该系统以受治理的历史记忆为证据基础，并结合行为模型路由、场景编排、分布聚合及审计机制；评估同时使用模态准确率与Wasserstein-1距离，以区分点预测正确性和总体分布保真度。<br>
        • 在226个留出样本上，TL-Twin Alpha取得论文结果集中最低的Wasserstein-1距离1.16，而Gamma与Delta表现出较均衡的运行点；研究说明企业模拟需要分布性评估，但其结论仍受单一基准规模与特定系统配置限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-15</td>
      <td style="width: 55%;"><strong>Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multi%20Agent%20Systems-4A90E2" alt="Multi-Agent Systems">
        <img src="https://img.shields.io/badge/Knowledge%20Graph-F5A623" alt="Knowledge Graph">
        <img src="https://img.shields.io/badge/Confidence%20Calibration-7ED321" alt="Confidence Calibration">
        <img src="https://img.shields.io/badge/Traceability%20Governance-D0021B" alt="Traceability Governance">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.17203">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文面向多智能体软件工程流水线中的错误级联问题，以共享知识图谱同时充当集中式语义记忆和协调界面，使下游智能体能够依据经校准的置信度评估并继承上游产物。<br>
        • 方法包含嵌入检索与大模型多准则分析组成的两阶段可追溯链接预测、用于比较生成时与验证时置信度的追踪种子机制，以及阈值门控、置信度分歧检测和冲突解决协议。<br>
        • 汽车软件工程案例及消融实验表明，置信度校准是协调协议有效运行的关键；不过其证据主要来自特定领域案例，因此更适合作为高可信多智能体工件治理的架构验证，而非对所有协作场景的普遍性结论。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-15</td>
      <td style="width: 55%;"><strong>HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Optimization-4A90E2" alt="Memory Optimization">
        <img src="https://img.shields.io/badge/Credit%20Assignment-F5A623" alt="Credit Assignment">
        <img src="https://img.shields.io/badge/Hindsight%20Relevance-7ED321" alt="Hindsight Relevance">
        <img src="https://img.shields.io/badge/Policy%20Learning-D0021B" alt="Policy Learning">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.16285">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文聚焦长程智能体记忆写入中的因果信用纠缠：最终失败可能源于工具调用、噪声观测或后续推理，但轨迹级奖励却容易错误惩罚此前正确的记忆更新。<br>
        • HiMPO首先在相同写入前状态下比较新旧记忆可恢复的任务相关信息，以估计记忆更新的局部效用；随后利用有界的事后相关性滤波器校准该效用，并仅将记忆特定优势施加于记忆token。<br>
        • 在开放域评测与压缩记忆问答任务中，该方法优于多种记忆及强化学习基线；受控干预进一步表明，HiMPO能够减少由工具错误引起的责任泄漏，提高记忆写入归因的准确性与可解释性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-15</td>
      <td style="width: 55%;"><strong>User as Code: Executable Memory for Personalized Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Executable%20Memory-4A90E2" alt="Executable Memory">
        <img src="https://img.shields.io/badge/User%20Modeling-F5A623" alt="User Modeling">
        <img src="https://img.shields.io/badge/Typed%20State-7ED321" alt="Typed State">
        <img src="https://img.shields.io/badge/Proactive%20Service-D0021B" alt="Proactive Service">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.16707">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文提出“用户即代码”范式，将个性化智能体的用户模型实现为持续演化的软件项目：类型化Python对象保存用户状态，普通函数编码约束、聚合逻辑与响应规则，使记忆表示与记忆推理共享同一可执行介质。<br>
        • 系统采用只增事实日志与周期性代码检查点构成的两阶段流水线，既保留原始历史，又将其整理为可验证的结构化状态，从而支持矛盾处理、跨记录聚合以及由状态变化主动触发的安全规则。<br>
        • UaC在LOCOMO上的普通事实召回率达到78.8%，而在历史聚合问题上达到约99%，显著高于检索式记忆的6%—43%；其核心贡献不只是提高召回，而是将用户记忆从被动查询数据库扩展为可确定性执行的主动服务系统。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-15</td>
      <td style="width: 55%;"><strong>TokenPilot: Cache-Efficient Context Management for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Context%20Management-4A90E2" alt="Context Management">
        <img src="https://img.shields.io/badge/Prompt%20Cache-F5A623" alt="Prompt Cache">
        <img src="https://img.shields.io/badge/Token%20Efficiency-7ED321" alt="Token Efficiency">
        <img src="https://img.shields.io/badge/Long%20Horizon%20Agents-D0021B" alt="Long-Horizon Agents">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.17016">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文指出，传统上下文剪枝与动态记忆驱逐虽然减少了输入令牌，却会改变序列边界和提示布局，造成前缀不匹配与KV缓存失效，因此上下文稀疏性与缓存连续性之间存在系统性张力。<br>
        • TokenPilot采用双粒度管理策略：全局的Ingestion-Aware Compaction在信息进入上下文时压缩环境噪声并稳定提示前缀，局部的Lifecycle-Aware Eviction则根据上下文片段的剩余任务效用执行保守的批次化卸载。<br>
        • 在PinchBench和Claw-Eval的独立及连续运行模式中，论文报告成本降幅分别覆盖56%—61%和61%—87%，同时维持与既有系统相当的任务性能，说明缓存友好的稳定布局是长程智能体成本优化中的独立设计目标。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-14</td>
      <td style="width: 55%;"><strong>FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/LLM%20Agent%20Security-4A90E2" alt="LLM Agent Security">
        <img src="https://img.shields.io/badge/Memory%20Attack-F5A623" alt="Memory Attack">
        <img src="https://img.shields.io/badge/Access%20Control-7ED321" alt="Access Control">
        <img src="https://img.shields.io/badge/Temporal%20Channel-D0021B" alt="Temporal Channel">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.15609">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文揭示长期记忆为智能体访问控制引入了跨轮次时间通道：原本会触发拒绝的违规请求可被拆分为表面无害的片段，分别写入记忆，并在后续检索阶段重新融合。<br>
        • FragFuse包含拒绝敏感片段识别、基于标记载体的记忆注入以及融合式检索攻击三个阶段，并通过代理模型优化融合指令与标记设计，使攻击生成能够在黑盒威胁模型下自动化。<br>
        • 论文报告平均访问控制绕过率为86.3%，端到端有害任务成功率为41.1%，且提示注入检测器和困惑度检测器难以有效防御；结果表明安全审查必须覆盖记忆写入、存储、检索和融合的完整生命周期，而不能只检查当前用户查询。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-06-14</td>
      <td style="width: 55%;"><strong>DYNA: Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Episodic%20Memory-4A90E2" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Temporal%20Knowledge_Graph-F5A623" alt="Temporal Knowledge Graph">
        <img src="https://img.shields.io/badge/Continuous%20Learning-7ED321" alt="Continuous Learning">
        <img src="https://img.shields.io/badge/Graph%20Retrieval-D0021B" alt="Graph Retrieval">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2606.15778">
          <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文提出DYNA，以冻结的大语言模型为推理核心，并将事件建模为节点、将“先于”“后于”及“共现”等时间关系建模为带时间戳的有向边，从而构建可持续更新的外部情景记忆。<br>
        • 在查询阶段，系统利用随机游走、节点中心性及图结构信息定位相关事件，再将检索结果与模型内部知识联合用于回答，避免了持续微调所需的训练成本及参数级知识干扰。<br>
        • 在三类时间记忆任务中，论文报告DYNA相较微调约降低7%的灾难性遗忘，并相较标准RAG约提升5%的时间排序准确率；图聚类系数与检索效果的正相关进一步说明，记忆拓扑结构本身是性能的重要决定因素。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-06-12</td>
        <td style="width: 55%;"><strong>AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Modular%20Framework-4A90E2" alt="Modular Framework">
          <img src="https://img.shields.io/badge/Embodied%20Agents-F5A623" alt="Embodied Agents">
          <img src="https://img.shields.io/badge/Typed%20Composition-7ED321" alt="Typed Composition">
          <img src="https://img.shields.io/badge/Memory%20Interaction-D0021B" alt="Memory Interaction">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.14674">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出AgentSpec，将具身智能体形式化为由感知、记忆、推理、反思、行动与可选学习模块构成的类型化组合，并通过标准化接口支持组件的独立替换、消融和受控重组。<br>
          • 研究在DeliveryBench、ALFRED、MiniGrid与RoboTHOR上系统比较不同推理、记忆、反思及强化学习组件，表明智能体性能并非由单一模块强度决定，而显著受模块兼容性、任务环境及交互效应影响。<br>
          • 实验尤其显示，结构化多粒度记忆能够更稳定地支持长程状态跟踪，但其收益依赖于记忆表示与下游推理策略的匹配；该工作由此将智能体支架从经验性工程配置转化为可分析的组合设计空间。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dynamic%20Environments-4A90E2" alt="Dynamic Environments">
          <img src="https://img.shields.io/badge/Memory%20Evolution-F5A623" alt="Memory Evolution">
          <img src="https://img.shields.io/badge/Benchmark%20Evaluation-7ED321" alt="Benchmark">
          <img src="https://img.shields.io/badge/EvoMem%20System-D0021B" alt="EvoMem">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13681">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出EvoArena基准，用于模拟动态环境变化，系统评估LLM代理在环境演化下的记忆能力与鲁棒性。<br>
          • 提出EvoMem基于“补丁式更新”的记忆范式，显式记录记忆随时间变化的结构化演化历史。<br>
          • 实验表明现有代理在动态环境中表现较弱，而EvoMem显著提升性能，强调建模环境演化的重要性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>MemRefine: LLM-Guided Compression for Long-Term Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Compression-4A90E2" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Long%20Term%20Memory-F5A623" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/LLM%20Optimization-7ED321" alt="LLM Optimization">
          <img src="https://img.shields.io/badge/Budget%20Constraint-D0021B" alt="Budget Constraint">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13177">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出MemRefine框架，在固定记忆预算下通过LLM驱动的判断机制优化记忆保留、删除与合并策略。<br>
          • 利用语义与事实一致性评估，迭代压缩长期记忆，同时尽量保留对未来任务有价值的信息。<br>
          • 实验表明该方法在严格存储约束下仍能保持甚至超过基线性能。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/User-Feedback-4A90E2" alt="User Feedback">
          <img src="https://img.shields.io/badge/Runtime-Enforcement-F5A623" alt="Runtime Enforcement">
          <img src="https://img.shields.io/badge/Preference-Alignment-7ED321" alt="Preference Alignment">
          <img src="https://img.shields.io/badge/TRACE-Framework-D0021B" alt="TRACE">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13174">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出TRACE方法，将用户历史纠正编译为运行时约束，用于指导LLM代理未来行为。<br>
          • 该机制将用户反馈转化为可执行规则，实现持续的行为修正与偏好记忆。<br>
          • 实验表明TRACE显著降低偏好违反率，并提升代理在交互式任务中的可靠性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Graph-Memory-4A90E2" alt="Graph Memory">
          <img src="https://img.shields.io/badge/Dialogue-Systems-F5A623" alt="Dialogue Systems">
          <img src="https://img.shields.io/badge/Efficient-Retrieval-7ED321" alt="Efficient Retrieval">
          <img src="https://img.shields.io/badge/Low-Latency-D0021B" alt="Low Latency">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13115">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出G-Long，通过图结构三元组建模与关系检索实现高效长期对话记忆管理。<br>
          • 使用轻量模型进行结构化信息抽取，并引入注意力感知的重要性评分机制。<br>
          • 在降低计算成本的同时，实现更稳定、更高质量的记忆检索与生成性能。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/MultiTurn-Reasoning-4A90E2" alt="Multi-Turn Reasoning">
          <img src="https://img.shields.io/badge/Memory-Sharding-F5A623" alt="Sharding">
          <img src="https://img.shields.io/badge/Reinforcement-Learning-7ED321" alt="RL">
          <img src="https://img.shields.io/badge/Compressed-Memory-D0021B" alt="Compressed Memory">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12941">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文研究多轮对话中信息分片输入导致的推理困难，提出紧凑滚动记忆机制替代完整历史上下文。<br>
          • 通过低成本分片训练策略提升模型在多轮、长上下文任务中的推理能力。<br>
          • 结果显示学习压缩记忆可提升零样本泛化能力，即使恢复完整上下文仍优于基线。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Arbor: Tree Search as a Cognition Layer for Autonomous Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Tree-Search-4A90E2" alt="Tree Search">
          <img src="https://img.shields.io/badge/Cognition-Layer-F5A623" alt="Cognition Layer">
          <img src="https://img.shields.io/badge/Multi-Agent-7ED321" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/Working-Memory-D0021B" alt="Working Memory">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12563">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出Arbor，将结构化树搜索作为多智能体系统的认知层与共享工作记忆。<br>
          • 通过显式搜索树演化协调多个代理，实现大状态空间中的稳定推理与优化。<br>
          • 实验证明该框架在系统性能、可重复性与推理效率方面均有显著提升。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Substrate Asymmetry in User-Side Memory: A Diagnostic Framework</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/User-Memory-4A90E2" alt="User Memory">
          <img src="https://img.shields.io/badge/Diagnostic-Framework-F5A623" alt="Diagnostic Framework">
          <img src="https://img.shields.io/badge/Behavior-Consistency-7ED321" alt="Behavior Consistency">
          <img src="https://img.shields.io/badge/Fact-Modeling-D0021B" alt="Fact Modeling">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.11712">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出用户侧记忆诊断框架，将“个性化记忆”拆解为多个正交维度，而非单一能力。<br>
          • 识别出行为一致性、事实存在与事实缺失三类核心记忆轴。<br>
          • 实验揭示不同模型在各维度存在显著不对称性，并指出对齐成本与路由问题。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Hierarchical-Memory-4A90E2" alt="Hierarchical Memory">
          <img src="https://img.shields.io/badge/Retrieval-Optimization-F5A623" alt="Retrieval Optimization">
          <img src="https://img.shields.io/badge/File-System-Memory-7ED321" alt="File System Memory">
          <img src="https://img.shields.io/badge/Efficiency-System-D0021B" alt="Efficiency">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.11680">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出HORMA，通过层次化结构组织记忆，实现类似文件系统的高效导航与检索。<br>
          • 将经验分层存储，减少无结构检索带来的延迟与信息丢失问题。<br>
          • 实验证明该方法在长任务对话中显著提升效率与任务完成质量。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-05</td>
        <td style="width: 55%;"><strong>Position: Hippocampal Explicit Memory Is the Cornerstone for AGI</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/AGI-Theory-4A90E2" alt="AGI Theory">
          <img src="https://img.shields.io/badge/Explicit-Memory-F5A623" alt="Explicit Memory">
          <img src="https://img.shields.io/badge/Neuroscience-Model-7ED321" alt="Neuroscience">
          <img src="https://img.shields.io/badge/Cognitive-Architecture-D0021B" alt="Cognitive Architecture">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.11245">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从神经科学视角提出：显式记忆是推动LLM迈向AGI的关键基础能力。<br>
          • 指出隐式统计学习不足以支持长期规划、元认知与符号推理等高级能力。<br>
          • 提出构建类海马体显式记忆系统的计算需求与研究方向。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LongDocument-QA-4A90E2" alt="Long QA">
          <img src="https://img.shields.io/badge/Hypergraph-Memory-F5A623" alt="Hypergraph Memory">
          <img src="https://img.shields.io/badge/OnDemand-Retrieval-7ED321" alt="On-Demand Retrieval">
          <img src="https://img.shields.io/badge/StructureAware-System-D0021B" alt="Structure-aware">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10921">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出DocTrace框架，通过结构感知的超图记忆支持长文档问答中的多步推理。<br>
          • 结合文档结构树与按需构建的共享记忆图，实现高效信息组织与复用。<br>
          • 在多个数据集上显著优于现有结构化RAG方法，提升复杂推理能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Graph-Memory-4A90E2" alt="Graph Memory">
          <img src="https://img.shields.io/badge/LongTerm-Memory-F5A623" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Confidence-Graph-7ED321" alt="Confidence Graph">
          <img src="https://img.shields.io/badge/NonDestructive-Updates-D0021B" alt="Non-destructive Updates">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10694">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出REAL框架，通过时间与置信度感知的有向图管理长期对话记忆。<br>
          • 引入非破坏性更新机制，允许同一事实的多版本并存以增强鲁棒性。<br>
          • 实验显示该方法在长期记忆任务中平均性能提升约22.72%。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory</strong></td>
       <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Topic-Memory-4A90E2" alt="Topic Memory">
          <img src="https://img.shields.io/badge/Maintainable-Documents-F5A623" alt="Maintainable Docs">
          <img src="https://img.shields.io/badge/Continuous-Update-7ED321" alt="Continuous Update">
          <img src="https://img.shields.io/badge/Text-Memory-D0021B" alt="Text Memory">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10677">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出Infini Memory，将代理记忆组织为可持续维护的主题文档，而非孤立记录。<br>
          • 通过缓冲-整合机制不断修订与聚合事实，实现长期一致的语义记忆结构。<br>
          • 支持迭代式检索与工具调用式记忆读取，提升长期推理效果。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Distributed-Memory-4A90E2" alt="Distributed Memory">
          <img src="https://img.shields.io/badge/Active-Memory-F5A623" alt="Active Memory">
          <img src="https://img.shields.io/badge/LongHorizon-Reasoning-7ED321" alt="Long Horizon Reasoning">
          <img src="https://img.shields.io/badge/Decoupled-Architecture-D0021B" alt="Decoupled Architecture">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10532">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出ActiveMem，通过将规划与记忆系统解耦，实现高效的长时推理与信息管理。<br>
          • 使用轻量规划器与分布式记忆并行协作，降低上下文负担与计算开销。<br>
          • 实验表明该方法在复杂任务上达到SOTA性能，并显著提升效率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-08</td>
        <td style="width: 55%;"><strong>Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/DualProcess-Memory-4A90E2" alt="Dual-process Memory">
          <img src="https://img.shields.io/badge/Cognitive-Modeling-F5A623" alt="Cognitive Modeling">
          <img src="https://img.shields.io/badge/SelfEvolving-Agents-7ED321" alt="Self-evolving Agents">
          <img src="https://img.shields.io/badge/CrossSession-Reasoning-D0021B" alt="Cross-session Reasoning">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.09483">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出DCPM双过程认知记忆系统，将记忆划分为显式与隐式认知层级。<br>
          • 采用“日间写入+夜间巩固”的双模块架构，实现长期知识演化。<br>
          • 实验显示该方法在跨会话推理与隐式个性化任务中表现优异。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>MemToolAgent: Leveraging Memory for Tool Using Agents Based on Environment and User Feedback</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Tool-Agents-4A90E2" alt="Tool Agents">
          <img src="https://img.shields.io/badge/Feedback-Learning-F5A623" alt="Feedback Learning">
          <img src="https://img.shields.io/badge/Memory-Augmented-7ED321" alt="Memory Augmented">
          <img src="https://img.shields.io/badge/Personalization-System-D0021B" alt="Personalization">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.07909v2">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出MemToolAgent，通过结构化记忆提取与检索提升工具使用型代理的任务能力。<br>
          • 将历史交互经验转化为可复用记忆条目，实现基于反馈的持续优化。<br>
          • 实验表明该方法显著提升个性化响应能力与任务准确率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-05</td>
        <td style="width: 55%;"><strong>AdMem: Advanced Memory for Task-solving Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Unified-Memory-4A90E2" alt="Unified Memory">
          <img src="https://img.shields.io/badge/Semantic-Memory-F5A623" alt="Semantic Memory">
          <img src="https://img.shields.io/badge/Procedural-Memory-7ED321" alt="Procedural Memory">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.06787">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出AdMem统一记忆框架，将语义、情节与程序记忆整合用于任务型代理。<br>
          • 通过多代理协作实现记忆生成、奖励标注与自适应检索机制。<br>
          • 实验表明该方法在长任务场景中显著提升鲁棒性与成功率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>AdaMEM: Test-Time Adaptive Memory for Language Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Adaptive%20Memory-blue" alt="Adaptive Memory">
          <img src="https://img.shields.io/badge/Language%20Agents-orange" alt="Language Agents">
          <img src="https://img.shields.io/badge/Memory%20Mechanisms-green" alt="Memory Mechanisms">
          <img src="https://img.shields.io/badge/Dynamic%20Adaptation-red" alt="Dynamic Adaptation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.05684">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对语言智能体在动态测试环境中难以有效利用历史经验的问题。<br>
          • 结合离线长期轨迹记忆和在线短期策略记忆，为当前决策提供自适应指导。<br>
          • 实验优于静态记忆基线，说明测试时自适应是长期智能体记忆的重要方向。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Proactive%20Retrieval-blue" alt="Proactive Retrieval">
          <img src="https://img.shields.io/badge/Lifelong%20Learning-orange" alt="Lifelong Learning">
          <img src="https://img.shields.io/badge/Memory%20Mechanism-green" alt="Memory Mechanism">
          <img src="https://img.shields.io/badge/Experience%20Base-red" alt="Experience Base">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.20572">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究终身智能体何时应该查询记忆，而不是默认始终检索。<br>
          • 将经验组织为事实、情节和技能库，并把检索建模为显式策略动作。<br>
          • 在提升任务成功率的同时减少无效交互，体现主动记忆控制的价值。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Execution%20State%20Management-orange" alt="Execution State Management">
          <img src="https://img.shields.io/badge/Long--Horizon%20Tasks-green" alt="Long-Horizon Tasks">
          <img src="https://img.shields.io/badge/Hierarchical%20State%20Tree-red" alt="Hierarchical State Tree">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06090">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出仅按语义相似性组织记忆会打碎长程任务中的决策轨迹。<br>
          • 提出 MAGE 层次执行状态树，通过 grow、compress、maintain、revise 维护任务状态。<br>
          • 通过保留有效路径、隔离错误分支提升任务成功率并降低 token 消耗。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Beyond Similarity: Trustworthy Memory Search for Personal AI Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Search-blue" alt="Memory Search">
          <img src="https://img.shields.io/badge/Personal%20AI-orange" alt="Personal AI">
          <img src="https://img.shields.io/badge/Trustworthy%20Memory-green" alt="Trustworthy Memory">
          <img src="https://img.shields.io/badge/Agent%20Memory-red" alt="Agent Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06054">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出个人 AI 中基于语义相似度的记忆检索本身就是信任边界。<br>
          • 提出轻量级 MemGate，根据当前任务条件判断候选记忆是否应进入上下文。<br>
          • 在保持长期记忆效用的同时降低跨域泄漏、谄媚、工具漂移和记忆诱导越狱风险。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Retention-blue" alt="Memory Retention">
          <img src="https://img.shields.io/badge/Long--Horizon%20Agents-orange" alt="Long-Horizon Agents">
          <img src="https://img.shields.io/badge/Evidence%20Management-green" alt="Evidence Management">
          <img src="https://img.shields.io/badge/Learning%20Policy-red" alt="Learning Policy">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.05894">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 关注长程智能体在固定记忆预算下应该保留哪些未来可用证据。<br>
          • 学习写入带源证据、检索键和更新元数据的 evidence capsules。<br>
          • 提升证据保留召回和回答质量，说明记忆质量关键在于预算内证据能否存活。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Mechanism-blue" alt="Memory Mechanism">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-orange" alt="Large Language Model">
          <img src="https://img.shields.io/badge/Safety%20Defense-green" alt="Safety Defense">
          <img src="https://img.shields.io/badge/Contrastive%20Learning-red" alt="Contrastive Learning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.05743">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对持续演化的越狱攻击，指出静态安全分类器和朴素记忆防线不足。<br>
          • 构建对比安全记忆单元，将有害请求与表面相似的良性请求成对存储。<br>
          • 提升智能体级安全防御效果，同时降低误拒率，并在记忆中毒下保持较强鲁棒性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Augmentation-blue" alt="Memory Augmentation">
          <img src="https://img.shields.io/badge/LLM%20Agents-orange" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Active%20Reconstruction-green" alt="Active Reconstruction">
          <img src="https://img.shields.io/badge/Graph%20Memory-red" alt="Graph Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06036">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 质疑许多记忆增强智能体采用的静态“先检索、再推理”流程。<br>
          • 将记忆表示为 Cue-Tag-Content 图，并让智能体在推理中主动重构相关路径。<br>
          • 在长期记忆基准上优于强基线，同时降低 token 和运行时间成本。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM-blue" alt="LLM">
          <img src="https://img.shields.io/badge/Memory-orange" alt="Memory">
          <img src="https://img.shields.io/badge/Contradiction%20Resolution-green" alt="Contradiction Resolution">
          <img src="https://img.shields.io/badge/Agent%20Memory-red" alt="Agent Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06240">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 将持久化智能体记忆中的矛盾解决视为写入时一致性问题。<br>
          • 定义双时态操作代数，显式给出隔离假设、来源标注和审计行。<br>
          • 明确生产级记忆系统在信念演化或冲突时所需的正确性契约。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>ABBEL: Learning Natural-Language Belief States for Memory-Efficient Interaction</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Efficiency-blue" alt="Memory Efficiency">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-orange" alt="Reinforcement Learning">
          <img src="https://img.shields.io/badge/Natural%20Language%20Processing-green" alt="Natural Language Processing">
          <img src="https://img.shields.io/badge/Decision%20Making-red" alt="Decision Making">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2512.20111">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对长序列决策中保留完整交互历史成本过高的问题。<br>
          • 学习递归更新的自然语言 belief state，并直接监督其中的信息内容。<br>
          • 减少摘要遗漏和更新错误，降低记忆占用，并缩小与完整上下文智能体的差距。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-blue" alt="Memory Framework">
          <img src="https://img.shields.io/badge/LLM%20Agents-orange" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Person%20Understanding-green" alt="Person Understanding">
          <img src="https://img.shields.io/badge/Schema%20Formation-red" alt="Schema Formation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04780">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 关注如何从长期交互中形成稳定的人物理解。<br>
          • 将证据、人物主张、置信度和查询条件路径组织为结构化 PersonaTree。<br>
          • 通过按查询返回所需证据深度，提升个性化理解和响应质量。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
          <img src="https://img.shields.io/badge/Memory%20Model-green" alt="Memory Model">
          <img src="https://img.shields.io/badge/Task%20Success-red" alt="Task Success">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04628">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向带显式策略的 LLM 智能体运行时上下文组装问题。<br>
          • 提出基于注册表的记忆模型，包含 promote、gate、write、evict、rollback 等原语。<br>
          • 实验表明记忆块分组和优先级管理能跨模型提升任务成功率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>Scaling Self-Evolving Agents via Parametric Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Augmentation-blue" alt="Memory Augmentation">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-green" alt="Reinforcement Learning">
          <img src="https://img.shields.io/badge/Online%20Learning-red" alt="Online Learning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04536">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对检索式记忆只能影响提示、难以真正改变未来行为的局限。<br>
          • 将历史经验压缩为显式记忆，并通过轻量在线更新形成参数化记忆。<br>
          • 为部署后持续自我演化的智能体提供新的扩展方向。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Segment%20Tree-orange" alt="Segment Tree">
          <img src="https://img.shields.io/badge/Temporal%20Order-green" alt="Temporal Order">
          <img src="https://img.shields.io/badge/Long--Horizon%20Agents-red" alt="Long-Horizon Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04555">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出事件顺序是长程记忆的核心，却常被相似度组织方式忽略。<br>
          • 提出 SegTreeMem 在线段树结构，在保持时间顺序的同时形成层次化记忆。<br>
          • 提升长程记忆问答表现，并证明性能依赖于记忆构建时保留时间顺序。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Leakage-blue" alt="Memory Leakage">
          <img src="https://img.shields.io/badge/Multi--Agent%20Systems-orange" alt="Multi-Agent Systems">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-green" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Memory%20Mechanism-red" alt="Memory Mechanism">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2512.04668">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究多智能体 LLM 系统中图拓扑如何影响私密信息泄漏。<br>
          • 提出 MAMA 框架，在受控合成 PII 文档上设计 Engram 植入和 Resonance 提取阶段。<br>
          • 发现连接越密、攻击者距离越近、目标中心性越高，泄漏风险越大。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>DMF: A Deterministic Memory Framework for Conversational AI Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-blue" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Conversational%20AI-orange" alt="Conversational AI">
          <img src="https://img.shields.io/badge/Deterministic%20Memory-green" alt="Deterministic Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-red" alt="Large Language Models">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.03463">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对基于 LLM 摘要的会话记忆管线存在非确定性和 token 成本的问题。<br>
          • 采用经典 NLP、向量几何、数学评分、生存分数和衰减规则构建确定性流程。<br>
          • 在保持竞争性准确率的同时降低 token 使用并提升可复现性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Agents-blue" alt="Memory Agents">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-green" alt="Reinforcement Learning">
          <img src="https://img.shields.io/badge/Information%20Gain-red" alt="Information Gain">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.03329">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对长上下文 chunk-wise 记忆智能体训练中奖励稀疏的问题。<br>
          • 使用答案条件信息增益衡量最终记忆对真实答案的支持程度。<br>
          • 为“应该保留什么信息”提供更直接的训练信号。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>MemTrain: Self-Supervised Context Memory Training</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Enhancement-blue" alt="Memory Enhancement">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Self--Supervised%20Learning-green" alt="Self-Supervised Learning">
          <img src="https://img.shields.io/badge/Context%20Memory-red" alt="Context Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.03197">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对训练记忆智能体缺乏高质量标注数据的问题。<br>
          • 在未标注语料上结合掩码重建和中间记忆回忆两个自监督目标。<br>
          • 提升长文本问答和搜索式问答中的记忆密集推理能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>RGMem: Renormalization Group-inspired Memory Evolution for Language Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-blue" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Conversational%20Agents-green" alt="Conversational Agents">
          <img src="https://img.shields.io/badge/User%20Personalization-red" alt="User Personalization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.16392">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向演化且可能冲突的对话证据下的长期用户状态建模。<br>
          • 采用受重整群启发的多尺度过程，通过层次粗粒化和阈值更新整合记忆。<br>
          • 相比平面检索或静态摘要，提升跨会话连续性和对变化偏好的适应能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>SaliMory: Orchestrating Cognitive Memory for Conversational Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Cognitive%20Memory-blue" alt="Cognitive Memory">
          <img src="https://img.shields.io/badge/Conversational%20Agents-orange" alt="Conversational Agents">
          <img src="https://img.shields.io/badge/Memory%20Management-green" alt="Memory Management">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-red" alt="Reinforcement Learning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04120">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 通过更显式地监督记忆操作来减少会话智能体的记忆相关失败。<br>
          • 使用分层阶段奖励和对比精炼训练过滤、整合和回忆行为。<br>
          • 提升端到端准确率和个性化效果，同时降低记忆操作错误。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>Training-Free Lexical-Dense Fusion for Conversational-Memory Retrieval</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Conversational%20Memory-blue" alt="Conversational Memory">
          <img src="https://img.shields.io/badge/Retrieval%20Mechanism-orange" alt="Retrieval Mechanism">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-green" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Memory%20Extraction-red" alt="Memory Extraction">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04194">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究多会话对话历史检索中词法线索与语义线索的互补性。<br>
          • 无需训练地融合 BM25 和 dense late-interaction 评分。<br>
          • 提升多跳、时间性和对抗性记忆问题上的可控、可复现检索效果。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>DELTAMEM: Incremental Experience Memory for LLM Agents via Residual Trees</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory-blue" alt="Memory">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
          <img src="https://img.shields.io/badge/Agent-green" alt="Agent">
          <img src="https://img.shields.io/badge/Experience-red" alt="Experience">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.03083">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对智能体积累大量任务经验时的冗余和检索冲突问题。<br>
          • 将目标条件经验和场景级知识组织为残差树，并支持自组织更新。<br>
          • 实现紧凑经验重构，并提升多种交互环境中的表现。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>Memory Retrieval for Changing Preferences</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-blue" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Changing%20Preferences-orange" alt="Changing Preferences">
          <img src="https://img.shields.io/badge/Dialogue%20Systems-green" alt="Dialogue Systems">
          <img src="https://img.shields.io/badge/Bayes%20Factor-red" alt="Bayes Factor">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.02976">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 处理用户偏好变化时，新旧记忆可能冲突的个性化检索问题。<br>
          • 将检索表述为选择能支持潜在偏好状态判断的历史轮次。<br>
          • 在偏好密集的长上下文对话任务中优于仅依赖嵌入的检索方法。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-31</td>
        <td style="width: 55%;"><strong>Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Systems-blue" alt="Memory Systems">
          <img src="https://img.shields.io/badge/Conflict%20Resolution-orange" alt="Conflict Resolution">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-green" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Deterministic%20Aggregation-red" alt="Deterministic Aggregation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.01435">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出让 LLM 直接判断演化事实的新鲜度并不可靠。<br>
          • 用候选抽取和版本感知的确定性聚合替代直接判断流程。<br>
          • 提升冲突解决效果，并说明瓶颈主要在聚合而非存储。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-31</td>
        <td style="width: 55%;"><strong>Honest Lying: Understanding Memory Confabulation in Reflexive Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Confabulation-blue" alt="Memory Confabulation">
          <img src="https://img.shields.io/badge/Reflexive%20Agents-orange" alt="Reflexive Agents">
          <img src="https://img.shields.io/badge/Memory%20Mechanism-green" alt="Memory Mechanism">
          <img src="https://img.shields.io/badge/Error%20Diagnosis-red" alt="Error Diagnosis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.29463">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究反射型智能体如何把错误自我解释存为持久记忆。<br>
          • 提出检测反思依赖的诊断信号，并用轨迹级失败提取替代开放式自我诊断。<br>
          • 减少跨环境的记忆虚构依赖，提升反射型智能体可靠性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-31</td>
        <td style="width: 55%;"><strong>Joint Agent Memory and Exploration Learning via Novelty Signals</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Exploration%20Learning-orange" alt="Exploration Learning">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-green" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Novelty%20Signals-red" alt="Novelty Signals">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.01528">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 探索开放环境中记忆与探索之间的相互依赖关系。<br>
          • 利用新颖性驱动的交互联合训练记忆和探索策略。<br>
          • 提升未见环境中的泛化能力，同时减少 token 消耗。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>MemPro: Agentic Memory Systems as Evolvable Programs</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Evolving%20Programs-orange" alt="Evolving Programs">
          <img src="https://img.shields.io/badge/Memory%20Systems-green" alt="Memory Systems">
          <img src="https://img.shields.io/badge/Autonomous%20Agents-red" alt="Autonomous Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.00619">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 质疑部署后不再演化的固定记忆构建-检索管线。<br>
          • 将整个记忆系统视为可演化程序，通过版本树和失败驱动编辑持续改进。<br>
          • 证明记忆管线可通过迭代诊断和调试在多个基准上持续提升。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-07</td>
        <td style="width: 55%;"><strong>Belief Memory: Agent Memory Under Partial Observability</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
          <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.05583">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 BeliefMem 记忆框架，将记忆范式从存储单一的确定性结论转变为维护属性级别的信念表示，以解决部分可观测环境下的自我强化错误问题。<br>
          • 为每个属性维护多个候选结论及其概率，通过 Noisy-OR 规则融合新证据进行更新，并结合信念感知检索机制，在智能体决策时保留不确定性。<br>
          • 在 LoCoMo 和 ALFWorld 基准测试中取得了优于现有确定性记忆方法的平均性能，展现出强大的记忆纠错能力与出色的数据效率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-07</td>
        <td style="width: 55%;"><strong>MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
          <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.06132">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出面向智能体记忆检索的推理感知重排模型系列 MemReranker（0.6B/4B），通过多阶段 LLM 知识蒸馏流水线解决传统模型过度依赖浅层语义匹配的问题。<br>
          • 结合 Elo/Bradley-Terry 校准评分、BCE 逐点蒸馏与 InfoNCE 对比微调，实现具有良好校准度的相关性打分与困难样本的区分能力。<br>
          • 在 LOCOMO、LongMemEval 等记忆检索基准上展现出 SOTA 性能，以极低的推理延迟达到了媲美 GPT-4o-mini 等大体积闭源模型的重排质量。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-07</td>
        <td style="width: 55%;"><strong>Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
          <img src="https://img.shields.io/badge/Retrieval%20Augmented%20Generation-blue" alt="Retrieval Augmented Generation">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
          <img src="https://img.shields.io/badge/Long%20Context%20Processing-teal" alt="Long Context Processing">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.06185">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出用于无限长视频推理的轻量级框架 Event-Causal RAG (EC-RAG)，将视频流异步分割为语义完整的事件并抽象为状态-事件-状态 (SES) 图记忆，替代了传统的固定长度切片记忆。<br>
          • 设计双存储记忆系统 (Dual-Store Memory)，结合用于语义匹配的向量数据库和用于因果拓扑检索的图数据库，在流式视频环境中实现了低开销存储与高效的跨时空记忆合并。<br>
          • 引入双向图检索策略以快速识别最相关的事件因果链，在无需对基础视频大模型进行超长序列微调的情况下，显著提升了模型在长视频因果推理上的准确率，并有效避免了上下文溢出问题。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-06</td>
        <td style="width: 55%;"><strong>Tree-based Credit Assignment for Multi-Agent Memory System</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
          <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.04811">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 TreeMem，一个用于多智能体记忆系统的基于树的强化学习框架，无需依赖特定任务的标注即可直接从最终下游奖励中推导出特定于智能体的信用分配。<br>
          • 将每个记忆智能体（构建器、摘要器、检索器）的输出扩展为多个后续分支，利用蒙特卡洛平均法评估中间动作对最终结果的贡献。<br>
          • 把粗粒度的最终奖励转化为细粒度的优化信号，促使异构记忆智能体实现有效的专业化分工，并在长视距基准测试中持续优于现有的强大基线方法。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents</strong></td>
        <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        <img src="https://img.shields.io/badge/Large%20Language%20Model-teal" alt="Large Language Model">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03312">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
        • 提出 MemFlow，一种面向小语言模型（SLM）的免训练记忆编排框架，通过意图驱动的记忆路由取代开放式推理循环，以解决长程智能体面临的记忆失效问题。<br>
        • 设计了专门的多智能体流水线（包含路由、记忆、回答和验证智能体）与动态上下文打包机制，在严格的 token 预算下确保确定性的证据准备和具备依据的可靠响应。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-teal" alt="Large Language Model">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.04264">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出将受治理的协作记忆作为基于 LLM 的多智能体系统的人工选择机制，以决定哪些候选记忆能够保留并成为持久的共享制度状态。<br>
          • 引入分层记忆架构，将智能体本地记忆、共享制度记忆、归档记忆和项目连续性记忆相分离，强调通过来源保真度、选择可追溯性和角色保留能力对记忆进行评估。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Episodic%20Memory-brightgreen" alt="Episodic Memory">
          <img src="https://img.shields.io/badge/Selective%20Forgetting-yellow" alt="Selective Forgetting">
          <img src="https://img.shields.io/badge/Memory%20Management-teal" alt="Memory Management">
          <img src="https://img.shields.io/badge/Lifelong%20Learning-orange" alt="Lifelong Learning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.11306">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 H²-EMV 分层情景记忆框架，用于机器人终身部署场景，利用语言模型判断相关性并选择性遗忘不重要信息以控制记忆规模。<br>
          • 结合用户反馈更新自然语言遗忘规则，实现个性化记忆管理，在保持问答准确率的同时显著减少记忆规模和查询开销。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20Poisoning-brightgreen" alt="Memory Poisoning">
          <img src="https://img.shields.io/badge/Retrieval--Augmented%20Agents-yellow" alt="Retrieval-Augmented Agents">
          <img src="https://img.shields.io/badge/Anomaly%20Detection-teal" alt="Anomaly Detection">
          <img src="https://img.shields.io/badge/Memory%20Security-orange" alt="Memory Security">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03482">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 形式化定义检索增强 Agent 持久外部记忆的多类投毒攻击场景，并提出基于语义异常检测的防御方法 MEMSAD。<br>
          • 利用梯度耦合定理证明异常分数梯度与检索目标梯度一致，实现可认证检测半径和最优校准样本复杂度。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agent%20Memory-blue" alt="LLM Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20Compression-brightgreen" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Personalized%20Memory-yellow" alt="Personalized Memory">
          <img src="https://img.shields.io/badge/Episodic%20Memory%20Graph-teal" alt="Episodic Memory Graph">
          <img src="https://img.shields.io/badge/On--device%20AI-orange" alt="On-device AI">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03804">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出面向资源受限边缘设备的个性化 Agent 记忆框架 ScrapMem，核心为光学遗忘压缩机制，逐步降低旧记忆分辨率以节省存储。<br>
          • 构建事件因果时序的 Episodic Memory Graph 维持语义一致性，在 ATM-Bench 上取得更优检索性能并显著降低存储开销。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-04</td>
        <td style="width: 55%;"><strong>A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
          <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.02525v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出用于集成VLM的室内机器人的六层语义自主栈（SAS）框架，其混合推理机制能以确定性方式解析常规指令，从而绕过大模型的推理延迟。<br>
          • 引入五大类语义记忆框架，将学习到的操作员偏好编译为共享摘要，在无需重新训练模型的情况下实现跨会话和跨机器人的知识迁移。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-04</td>
        <td style="width: 55%;"><strong>The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence</strong></td>
        <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.02106">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
        • 提出了动态主旨记忆模型（DGMM），这是一种以记忆为中心的架构框架，将经验表示为显式的、持久的、基于图结构的片段-语义记忆。<br>
        • 将记忆操作形式化定义为摄入、巩固、回忆和分析四个独立机制，实现了记忆存储与下游语义解释的解耦。<br>
        • 定义了片段持久性和条件化惊讶局部性等架构不变量，使得系统无需重新训练即可基于稳定的记忆结构支持随时间演变的解释。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-04</td>
        <td style="width: 55%;"><strong>MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Shadow%20Memory-brightgreen" alt="Shadow Memory">
          <img src="https://img.shields.io/badge/LLM%20Agents-yellow" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Long--horizon%20Threats-teal" alt="Long-horizon Threats">
          <img src="https://img.shields.io/badge/Safety%20Guardrail-orange" alt="Safety Guardrail">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03228">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 借鉴系统安全中的 shadow stack 思想，提出 MAGE 框架，为 LLM Agent 维护独立安全记忆，跨长任务轨迹提炼并保存关键安全上下文。<br>
          • 在执行前利用安全记忆评估待执行动作风险，能更早识别长程攻击且对 agent 效用影响很小。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-04</td>
        <td style="width: 55%;"><strong>Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Equivariant%20RNN-blue" alt="Equivariant RNN">
          <img src="https://img.shields.io/badge/Memory%20Retention-brightgreen" alt="Memory Retention">
          <img src="https://img.shields.io/badge/Lyapunov%20Exponents-yellow" alt="Lyapunov Exponents">
          <img src="https://img.shields.io/badge/Symmetry%20Protection-teal" alt="Symmetry Protection">
          <img src="https://img.shields.io/badge/Recurrent%20Networks-orange" alt="Recurrent Networks">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03338">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 从群对称性出发证明等变循环网络中群轨道切向方向存在被对称性保护的零 Lyapunov 指数，形成长期中性记忆状态。<br>
          • 通过 S¹、T^q、SO(n)、U(m) 等系统及等变 RNN 实验验证，严格等变结构可提升长程记忆保持、泛化和稳定性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-03</td>
        <td style="width: 55%;"><strong>Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi--agent%20Collaboration-blue" alt="Multi-agent Collaboration">
          <img src="https://img.shields.io/badge/Agent%20Memory-brightgreen" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--horizon%20Planning-yellow" alt="Long-horizon Planning">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-teal" alt="Reinforcement Learning">
          <img src="https://img.shields.io/badge/Memory%20Manager-orange" alt="Memory Manager">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.02168">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出面向长程规划的非均衡多智能体协作框架，将系统分为 planner、actor 和 memory manager 三角色，发现规划对任务性能贡献最大。<br>
          • 提出仅优化 planner 的强化学习方法，利用轨迹级奖励在网页导航、系统控制和工具使用等基准上验证高效性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-02</td>
        <td style="width: 55%;"><strong>MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
          <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.01386">
          <img src="https://img.shields.io/badge/arXiv-Paper-black?labelColor=red" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MemORAI 记忆组织与检索框架，利用双层压缩的选择性记忆过滤机制保留与用户人设相关的核心内容，同时维持全局对话上下文。<br>
          • 构建富含溯源信息的多关系知识图谱，实现对话轮次级别的事实追踪，从而支持细粒度且透明的记忆审查。<br>
          • 引入动态加权 PageRank 进行查询自适应的子图检索，通过应用基于查询条件的边权重，显著提升上下文敏感的检索精度与个性化回复生成能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-01</td>
        <td style="width: 55%;"><strong>From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/AI%20Memory-blue" alt="AI Memory">
          <img src="https://img.shields.io/badge/Schema--grounded%20Memory-brightgreen" alt="Schema-grounded Memory">
          <img src="https://img.shields.io/badge/Structured%20Extraction-yellow" alt="Structured Extraction">
          <img src="https://img.shields.io/badge/Memory%20Update-teal" alt="Memory Update">
          <img src="https://img.shields.io/badge/External%20Memory-orange" alt="External Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.27906">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出 AI 记忆应构建为受 schema 约束的可靠外部记忆系统，提出迭代式感知 schema 的写入流程，将记忆摄取拆分为对象检测、字段检测和字段值抽取。<br>
          • 加入验证、重试与状态控制机制，在结构化抽取和端到端记忆任务上均优于基线，适合需要稳定事实和状态更新的记忆场景。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-01</td>
        <td style="width: 55%;"><strong>Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agent%20Memory-blue" alt="LLM Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20Update-brightgreen" alt="Memory Update">
          <img src="https://img.shields.io/badge/Reinforcement%20Learning-yellow" alt="Reinforcement Learning">
          <img src="https://img.shields.io/badge/Personalization-teal" alt="Personalization">
          <img src="https://img.shields.io/badge/Long--term%20Memory-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.00702">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出受认知理论启发的两阶段优化框架 MemCoE：第一阶段通过对比反馈诱导全局记忆准则，第二阶段基于准则进行多轮强化学习。<br>
          • 在三个个性化记忆基准上验证方法在偏好记忆、鲁棒性、迁移性和效率方面的提升。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-30</td>
        <td style="width: 55%;"><strong>Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Observability-brightgreen" alt="Observability">
          <img src="https://img.shields.io/badge/Automatic%20Evolution-yellow" alt="Automatic Evolution">
          <img src="https://img.shields.io/badge/Coding%20Agents-teal" alt="Coding Agents">
          <img src="https://img.shields.io/badge/Long--term%20Memory-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.25850">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 AHE，通过可观测性驱动的闭环机制自动进化 coding agent 的 harness，从组件、经验和决策三层面构建可编辑可追踪的演化流程。<br>
          • 将大量轨迹压缩为可用证据，通过自我预测与后续结果验证实现自动迭代，显著提升编码代理性能并可迁移到不同模型家族。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-30</td>
        <td style="width: 55%;"><strong>EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term%20Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Conversational%20Memory-brightgreen" alt="Conversational Memory">
          <img src="https://img.shields.io/badge/Iterative%20Retrieval-yellow" alt="Iterative Retrieval">
          <img src="https://img.shields.io/badge/Evidence%20Gap-teal" alt="Evidence Gap">
          <img src="https://img.shields.io/badge/Memory%20Architecture-orange" alt="Memory Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.27695">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 EviMem 框架，核心包括 IRIS 闭环迭代检索机制，通过充分性评估发现"证据缺口"并定向改写查询以处理分散的多轮证据。<br>
          • 提出 LaceMem 分层记忆架构支持由粗到细的证据诊断与检索，在 LoCoMo 上显著提升时序和多跳问题准确率并降低检索延迟。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-30</td>
        <td style="width: 55%;"><strong>MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term%20Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20Routing-brightgreen" alt="Memory Routing">
          <img src="https://img.shields.io/badge/Conversational%20Agents-yellow" alt="Conversational Agents">
          <img src="https://img.shields.io/badge/Memory%20Management-teal" alt="Memory Management">
          <img src="https://img.shields.io/badge/Embedding--based%20Classification-orange" alt="Embedding-based Classification">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.00356">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MemRouter，用 embedding 路由替代逐轮 LLM 生成式记忆管理，仅训练约 12M 参数判断哪些轮次应写入外部记忆。<br>
          • 在保持检索管线、提示和问答骨干一致的条件下，在 LoCoMo 上优于 LLM 式记忆管理器并显著降低记忆管理延迟。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-29</td>
        <td style="width: 55%;"><strong>Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agent%20Memory-blue" alt="LLM Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20Extraction-brightgreen" alt="Memory Extraction">
          <img src="https://img.shields.io/badge/Memory%20Reconciliation-yellow" alt="Memory Reconciliation">
          <img src="https://img.shields.io/badge/Clinical%20Discrepancy-teal" alt="Clinical Discrepancy">
          <img src="https://img.shields.io/badge/Longitudinal%20Agents-orange" alt="Longitudinal Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.27045">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向长期健康陪护 LLM Agent 提出双流记忆架构，将患者自述与结构化 EHR/FHIR 记录分离存储，并用 reconciliation 引擎逐条比对识别差异。<br>
          • 量化记忆抽取带来的误差级联，强调在医疗场景中进行记忆验证的必要性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-19</td>
        <td style="width: 55%;"><strong>Seeing Isn't Believing: Mitigating Belief Inertia via Active Intervention in Embodied Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Belief%20Update-brightgreen" alt="Belief Update">
          <img src="https://img.shields.io/badge/Embodied%20Agents-yellow" alt="Embodied Agents">
          <img src="https://img.shields.io/badge/LLM%20Agents-teal" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Reasoning-orange" alt="Reasoning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.17252">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究具身智能体在交互中忽视新观察、固守先验信念的 belief inertia 问题。<br>
          • 提出 Estimate-Verify-Update 机制，通过预测、验证和基于证据更新文本化信念状态，主动管理智能体信念并提升多个具身基准成功率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-22</td>
        <td style="width: 55%;"><strong>Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Semantic%20Memory-blue" alt="Semantic Memory">
          <img src="https://img.shields.io/badge/Information--Theoretic%20Retrieval-brightgreen" alt="Information-Theoretic Retrieval">
          <img src="https://img.shields.io/badge/Long--term%20Agents-yellow" alt="Long-term Agents">
          <img src="https://img.shields.io/badge/Conflict%20Resolution-teal" alt="Conflict Resolution">
          <img src="https://img.shields.io/badge/Typed%20Memory-orange" alt="Typed Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.22085">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Memanto 系统，采用 13 类 typed semantic memory schema，在 LongMemEval 和 LoCoMo 上分别达到 89.8% 和 87.1%，且无需知识图谱。<br>
          • 引入 Moorcheh Information-Theoretic Search，实现无索引、确定性检索，延迟低于 90ms，写入延迟为零。<br>
          • 通过内置冲突解决和时间版本控制机制应对 constraint drift，支持 supersede 机制保留历史状态。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-19</td>
        <td style="width: 55%;"><strong>Memory Intelligence Agent</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Hybrid%20Memory-darkcyan" alt="Hybrid Memory">
          <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
          <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.04503">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MIA（Memory Intelligence Agent）记忆智能体框架，采用 Manager-Planner-Executor 架构，通过将历史搜索轨迹压缩为结构化的非参数化记忆来解决存储与检索瓶颈。<br>
          • 引入两阶段交替强化学习范式以实现高层规划与底层执行的协同对齐，并设计了持续的测试时学习机制，支持在推理过程中动态更新参数化记忆。<br>
          • 结合反思机制与无监督评估框架，在多项深度研究任务中实现了SOTA性能，并展现出在不同基准测试中强大的自我进化能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-26</td>
        <td style="width: 55%;"><strong>ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--term%20Memory-brightgreen" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Hebbian%20Learning-yellow" alt="Hebbian Learning">
          <img src="https://img.shields.io/badge/Spaced%20Repetition-teal" alt="Spaced Repetition">
          <img src="https://img.shields.io/badge/Open--Source-orange" alt="Open Source">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.23878">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 推出 ZenBrain——一种面向自主智能体的七层长期记忆架构，融合了受神经科学启发的多种机制——包括赫布学习（Hebbian learning）、FSRS 间隔重复、睡眠周期巩固和贝叶斯置信传播——并以开源、零依赖的 TypeScript 库形式发布。<br>
          • 在 LongMemEval-500 评测中，它仅用 1/106 的 token 预算即达到 91.3% 的 oracle 准确率，并在与 Letta、Mem0 和 A-Mem 的逐一对比中取得经 Bonferroni 校正的 9/9 全胜。<br>
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--term%20Memory-brightgreen" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Hebbian%20Learning-yellow" alt="Hebbian Learning">
          <img src="https://img.shields.io/badge/Memory%20Graph-teal" alt="Memory Graph">
          <img src="https://img.shields.io/badge/LLM%20Agents-orange" alt="LLM Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16839">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 HeLa-Mem，借鉴联结、巩固与传播激活机制，将 LLM Agent 长期记忆建模为动态图。<br>
          • 采用情景记忆图与 Hebbian Distillation 形成的语义知识双层结构，在 LoCoMo 上提升效果并节省上下文 token。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Experience%20Replay-blue" alt="Experience Replay">
          <img src="https://img.shields.io/badge/Priority%20Decay-brightgreen" alt="Priority Decay">
          <img src="https://img.shields.io/badge/LLM%20Reinforcement%20Learning-yellow" alt="LLM Reinforcement Learning">
          <img src="https://img.shields.io/badge/Agent%20Memory-teal" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Sample%20Efficiency-orange" alt="Sample Efficiency">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16918">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Freshness-Aware Prioritized Experience Replay，在优先级采样中加入指数式年龄衰减。<br>
          • 缓解 LLM/VLM 强化学习中策略快速变化导致旧样本优先级失效的问题，在多步推理、智能体和数学任务上优于标准 on-policy 方法与普通 PER。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>MEMRES: A Memory-Augmented Resolver with Confidence Cascade for Agentic Python Dependency Resolution</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory--Augmented-brightgreen" alt="Memory-Augmented">
          <img src="https://img.shields.io/badge/Confidence%20Cascade-yellow" alt="Confidence Cascade">
          <img src="https://img.shields.io/badge/Self--Evolving%20Memory-teal" alt="Self-Evolving Memory">
          <img src="https://img.shields.io/badge/Error%20Pattern%20Knowledge%20Base-orange" alt="Error Pattern Knowledge Base">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16941">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MEMRES，一个面向 Python 依赖解析的记忆增强型 agent 系统，采用多级置信级联机制并将 LLM 作为最后手段。<br>
          • 系统包含自我演化记忆、错误模式知识库、语义导入分析器和 Python2 启发式检测器，用于提升依赖解析成功率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--term%20Memory-brightgreen" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20Poisoning-yellow" alt="Memory Poisoning">
          <img src="https://img.shields.io/badge/Agentic%20RecSys-teal" alt="Agentic RecSys">
          <img src="https://img.shields.io/badge/Defense%20Framework-orange" alt="Defense Framework">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16966">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Visual Inception 攻击，在用户上传图片中植入触发器，污染 Agentic 推荐系统长期记忆并在未来规划中劫持推理链。<br>
          • 提出 CognitiveGuard 双过程防御框架，结合感知净化与反事实一致性检查识别异常记忆驱动规划，显著降低攻击风险。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>On Safety Risks in Experience-Driven Self-Evolving Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Experience%20Accumulation-brightgreen" alt="Experience Accumulation">
          <img src="https://img.shields.io/badge/Self--Evolving%20Agents-yellow" alt="Self-Evolving Agents">
          <img src="https://img.shields.io/badge/Safety-teal" alt="Safety">
          <img src="https://img.shields.io/badge/Large%20Language%20Model%20Agents-orange" alt="Large Language Model Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16968">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究经验驱动自我演化 LLM Agent 在网络与具身环境中的安全风险，指出良性任务经验也可能强化“执行而非拒绝”的倾向。<br>
          • 在混合良恶任务中，拒绝相关经验可缓解安全下降但会带来过度拒绝，揭示经验记忆演化中的安全与效用权衡。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>OASIS: On-Demand Hierarchical Event Memory for Streaming Video Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Hierarchical%20Memory-brightgreen" alt="Hierarchical Memory">
          <img src="https://img.shields.io/badge/On--demand%20Retrieval-yellow" alt="On-demand Retrieval">
          <img src="https://img.shields.io/badge/Streaming%20Video%20Reasoning-teal" alt="Streaming Video Reasoning">
          <img src="https://img.shields.io/badge/Long--horizon%20Reasoning-orange" alt="Long-horizon Reasoning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.17052">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 OASIS，用于流式视频推理的按需层级事件记忆框架，将长历史组织为层级事件。<br>
          • 先进行短上下文推理，并在不确定时触发语义检索，以高层意图驱动记忆访问，减少噪声并控制 token 成本。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM%20Agent-brightgreen" alt="LLM Agent">
          <img src="https://img.shields.io/badge/Execution%20Feedback-yellow" alt="Execution Feedback">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-teal" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Kernel%20Generation-orange" alt="Kernel Generation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16625">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 AdaExplore，用执行反馈中的重复失败提炼可复用有效性规则记忆，用于后续 Triton 内核生成。<br>
          • 通过树状候选组织、局部修正与结构性重生成进行多样性保留搜索，在正确性与性能优化上均有提升。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>StageMem: Lifecycle-Managed Memory for Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM%20Memory-brightgreen" alt="LLM Memory">
          <img src="https://img.shields.io/badge/Memory%20Management-yellow" alt="Memory Management">
          <img src="https://img.shields.io/badge/Lifecycle%20Memory-teal" alt="Lifecycle Memory">
          <img src="https://img.shields.io/badge/Long--horizon%20LLM-orange" alt="Long-horizon LLM">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16774">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 StageMem，将语言模型记忆视为状态化生命周期过程，而非静态存储。<br>
          • 把记忆分为瞬时、工作和持久三层，并用置信度与强度支持低成本写入、晋升、更新与驱逐，降低深层记忆污染。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Federation over Text: Insight Sharing for Multi-Agent Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Knowledge%20Sharing-brightgreen" alt="Knowledge Sharing">
          <img src="https://img.shields.io/badge/Multi--Agent%20Reasoning-yellow" alt="Multi-Agent Reasoning">
          <img src="https://img.shields.io/badge/Skill%20Transfer-teal" alt="Skill Transfer">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16778">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 FoT 框架，让多个智能体独立推理后上传轨迹，由中心服务器进行语义级聚合与提炼。<br>
          • 形成跨任务、跨领域共享洞见库，无需梯度优化或监督信号即可提升下游准确率并降低推理开销。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-13</td>
        <td style="width: 55%;"><strong>The Past Is Not Past: Memory-Enhanced Dynamic Reward Shaping</strong></td>
        <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
        <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.11297">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
        • 提出了一种名为 MEDS 的记忆增强动态奖励塑造框架，将历史行为信号显式纳入奖励设计，以缓解大语言模型强化学习过程中的错误坍缩问题。<br>
        • 复用模型的逐层逻辑值（logits）作为推理轨迹的轻量级表示来构建错误记忆，并应用 HDBSCAN 聚类对频繁出现的失败模式进行动态惩罚。<br>
        • 在多个数学推理基准和基础模型上的实验表明，该方法能够一致且有效地提升模型的推理性能以及探索的多样性。
        </td>
      </tr>
<tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>MemCoT: Test-Time Scaling through Memory-Driven Chain-of-Thought</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Reasoning-blue" alt="Memory Reasoning">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08216">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 MemCoT，将长上下文推理重构为迭代式、有状态的信息搜索过程。<br>
              • 通过多视角长期记忆感知定位证据，并用任务条件短期记忆记录搜索历史、指导后续查询分解。<br>
              • 在多个长记忆推理基准上取得了当前最优表现。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>SinkTrack: Attention Sink based Context Anchoring for Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Context%20Anchoring-blue" alt="Context Anchoring">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10027">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SinkTrack，一种利用模型在 &lt;BOS&gt; 位置 attention sink 特性的免训练上下文锚定方法。<br>
              • 通过将关键信息注入 &lt;BOS&gt; 表征，使模型在生成过程中持续保留初始上下文，而非逐步遗忘。<br>
              • 在文本与多模态任务上都带来了稳定收益，并有效缓解了幻觉与上下文遗忘。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>Self-Distilled Reinforcement Learning for Co-Evolving Agentic Recommender Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Recommender%20RL-blue" alt="Recommender RL">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10029">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 CoARS，一个面向协同演化推荐系统的自蒸馏强化学习框架。<br>
              • 该方法不再仅依赖外部文本记忆，而是通过交互奖励与自蒸馏信用分配将多轮监督转化为参数更新。<br>
              • 相比纯记忆型基线，能够进一步提升推荐质量与用户对齐效果。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>CodeComp: Structural KV Cache Compression for Agentic Coding</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/KV%20Compression-blue" alt="KV Compression">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10235">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 CodeComp，一种面向代理式编程任务的结构化 KV Cache 压缩方法。<br>
              • 结合静态程序分析与代码属性图先验，保留 attention-only 压缩容易误删的结构关键信息。<br>
              • 在相同内存预算下优于仅基于 attention 的压缩方案，并可无缝集成到 SGLang 流水线。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Virtual%20Memory-blue" alt="Virtual Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10352">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 ClawVM，一个面向状态型工具使用 Agent 的 harness 管理虚拟内存层。<br>
              • 它将状态组织为带类型的页，并在生命周期边界执行校验写回，以避免状态陈旧和破坏性更新。<br>
              • 在极低策略开销下显著降低了多类可控故障。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>CodaRAG: Connecting the Dots with Associativity Inspired by Complementary Learning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Associative%20RAG-blue" alt="Associative RAG">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10426">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 CodaRAG，一个受互补学习启发的联想式 RAG 框架。<br>
              • 该方法通过知识整合、关联导航与干扰消除，恢复更完整的证据链并抑制噪声。<br>
              • 在检索召回与生成准确率上均优于现有方法。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>Astrolabe: A Content-Addressable Hypergraph for Semantic Knowledge Management</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Hypergraph%20Memory-blue" alt="Hypergraph Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10435">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 Astrolabe，一个用于语义知识管理的内容寻址超图框架。<br>
              • 系统通过内容哈希与有序引用列表存储结构化知识，并借助插件机制解释记录内容、分解结构。<br>
              • 作者进一步展示了它在连接非正式数学与形式化数学场景中的可扩展性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>MemReader: From Passive to Active Extraction for Long-Term Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Extraction-blue" alt="Memory Extraction">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.07877">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 MemReader 系列，用于长程 Agent 记忆的被动抽取与主动写入决策。<br>
              • 其中 MemReader-4B 结合 GRPO 与 ReAct 式流程，判断信息应被写入、延迟、检索还是丢弃。<br>
              • 在知识更新、时序推理与幻觉降低上优于已有方法，并已集成进 MemOS。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>HyperMem: Hypergraph Memory for Long-Term Conversations</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Hypergraph%20Memory-blue" alt="Hypergraph Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08256">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 HyperMem，一个面向长程对话的超图记忆架构。<br>
              • 它通过超边建模高阶关联，并将记忆组织为主题、事件和事实三层，再结合词法-语义混合索引与粗到细检索。<br>
              • 在长对话任务中提升了记忆召回与一致性，并在 LoCoMo 上取得最佳结果。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Compression-blue" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09000">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 StreamMeCo，用于流式视频理解中的长期记忆压缩。<br>
              • 该方法通过边感知剪枝与孤立节点采样压缩记忆图，并结合时间衰减检索缓解压缩损失。<br>
              • 在多个基准上实现了显著的存储节省与检索加速，同时保持甚至提升准确率。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>Towards Lifelong Aerial Autonomy: Geometric Memory Management for Continual Visual Place Recognition in Dynamic Environments</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Management-blue" alt="Memory Management">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09038">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一个面向动态环境持续视觉地点识别的几何记忆管理框架。<br>
              • 该方法将知识拆分为静态卫星锚点与动态经验回放缓存，并通过空间约束采样在有限存储下分配记忆资源。<br>
              • 它提升了长期记忆保留与空间泛化能力，并同时构建了包含 21 个任务序列的评测基准。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Persona%20Memory-blue" alt="Persona Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09212">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SPASM，一个面向多轮对话生成的人格稳定框架。<br>
              • 系统结合人格构建、Client-Responder 对话生成以及 ECP 视角无关表示来组织历史信息。<br>
              • 能有效降低 persona drift、角色混淆与 echoing，并发布了大规模对话数据集。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Skill%20Optimization-blue" alt="Skill Optimization">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09297">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SkillMOO，一个面向软件工程 Agent 技能包的多目标优化框架。<br>
              • 它结合 LLM 生成修改建议与 NSGA-II 选择策略，根据失败案例持续演化技能包。<br>
              • 实验表明，替换或裁剪指令往往比简单堆叠更多技能更有效。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retrieval</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/In%2Dcontext%20Retrieval-blue" alt="In-context Retrieval">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09494">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 RecaLLM，通过在推理过程中交替进行显式上下文检索来缓解 lost-in-thought 问题。<br>
              • 方法使用约束解码复制证据片段，并同时在词法与语义检索任务上训练模型。<br>
              • 在 RULER、HELMET 等长上下文基准上优于基线，并可扩展到 128K 上下文。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>Constraint-Aware Corrective Memory for Language-Based Drug Discovery Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Corrective%20Memory-blue" alt="Corrective Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09308">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一个面向药物发现语言 Agent 的约束感知纠正记忆框架。<br>
              • 它通过协议审计与约束诊断生成纠正反馈，并将结果写入静态、动态与纠正三类记忆通道。<br>
              • 通过保持规划上下文紧凑且可执行，显著提升了任务成功率。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09747">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 ADAM，一种针对 Agent 记忆模块的系统化自适应查询攻击方法。<br>
              • 它通过估计受害者记忆分布并采用熵引导查询，最大化隐私泄露效果。<br>
              • 相比现有攻击方法，成功率显著更高，在部分设置下甚至可达到 100%。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Experience%20Bank-blue" alt="Experience Bank">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09815">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 EE-MCP，一个面向 MCP-GUI Agent 的自进化框架。<br>
              • 该系统构建了环境生成、轨迹采集、任务合成与质量筛选的闭环，并将经验规则沉淀到 experience bank 中用于推理期改进。<br>
              • 结果显示，在 GUI 密集任务上，经验增强比纯蒸馏更有效，且无需微调模型。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>MEMENTO: Teaching LLMs to Manage Their Own Context</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Context%20Compression-blue" alt="Context Compression">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09852">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 MEMENTO，让模型学会通过中间 memento 摘要主动管理自身上下文。<br>
              • 它将长推理过程切分为多个块，并为每个块生成紧凑摘要，然后基于摘要继续推理。<br>
              • 该方法在保持推理质量的同时降低了上下文长度、KV Cache 开销与计算成本，并发布了 OpenMementos 数据集。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-10</td>
        <td style="width: 55%;"><strong>Formal Architecture Descriptors as Navigation Primitives for AI Coding Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Structured%20Context-blue" alt="Structured Context">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.13108">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 研究了形式化架构描述符在 AI Coding Agent 中作为导航原语的作用。<br>
              • 结果表明，结构化架构上下文可以减少无目的代码库探索，并提高 Agent 行为一致性。<br>
              • 作者比较了 JSON、YAML 与 S-expression 等表示方式，并提出了 <code>intent.lisp</code> 与 Forge 工具链。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Graph%20Memory-blue" alt="Graph Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.07863">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 ACGM，一个面向长程多模态 Web 历史的任务自适应图记忆检索器。<br>
              • 该方法通过策略梯度优化稀疏相关图，并显式建模视觉与文本观测在时间上的不同衰减规律。<br>
              • 在 WebShop、VisualWebArena 与 Mind2Web 上均优于多种基线。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>TSUBASA: Improving Long-Horizon Personalization via Evolving Memory and Self-Learning with Context Distillation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Personalization-blue" alt="Personalization">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.07894">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 TSUBASA，用于提升个性化模型的长程能力。<br>
              • 该方法通过动态记忆演化改进写入，并通过上下文蒸馏驱动的自学习机制强化读取与用户经验内化。<br>
              • 在长程个性化基准上优于 Mem0 等方案，并取得了更好的质量与效率折中。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Dynamic Attentional Context Scoping: Agent-Triggered Focus Sessions for Isolated Per-Agent Steering in Multi-Agent LLM Orchestration</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Context%20Isolation-blue" alt="Context Isolation">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.07911">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 DACS，一种面向多 Agent LLM 编排的动态注意力上下文作用域机制。<br>
              • 在 Registry 模式下仅保留轻量状态摘要，在 Focus 模式下只为目标 Agent 注入完整上下文、压缩其余 Agent。<br>
              • 该机制显著提升了 steering 准确率，并减少了无关 Agent 的干扰。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>LogAct: Enabling Agentic Reliability via Shared Logs</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Shared%20Logs-blue" alt="Shared Logs">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.07988">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 LogAct，一个基于共享日志的 Agent 执行框架，将 Agent 表示为日志上的状态机。<br>
              • 它使计划动作在执行前即可被观察、拦截、恢复和回放，也支持基于历史轨迹的 LLM 自省。<br>
              • 该框架提升了 Agent 系统的可靠性、故障恢复能力与调试便利性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Proactive%20Memory-blue" alt="Proactive Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08000">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 DD-MM-PAS 范式及其实现系统 Pask，用于构建意图感知的主动式长程记忆 Agent。<br>
              • 它结合 IntentFlow 潜在需求检测、workspace/user/global 混合记忆设计以及完整的感知-记忆-行动基础设施。<br>
              • 在低延迟约束下能识别更深层用户意图，并同步发布了 LatentNeeds-Bench。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Experience%20Learning-blue" alt="Experience Learning">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08124">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 HiExp，用于从 Agentic Search 的原始轨迹中抽取可复用经验知识。<br>
              • 它通过对比分析与分层聚类构造层级化经验表示，并进一步进行经验对齐训练。<br>
              • 该方法将随机探索转化为更具策略性的搜索过程，并提升了稳定性、性能与跨任务泛化。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>"Theater of Mind" for LLMs: A Cognitive Architecture Based on Global Workspace Theory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Cognitive%20Architecture-blue" alt="Cognitive Architecture">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08206">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了受全局工作空间理论启发的 Global Workspace Agents 认知架构。<br>
              • 该架构将中心广播枢纽、异质 Agent、熵驱动内在动机与双层记忆分叉策略结合起来。<br>
              • 在多 Agent 执行中提升了语义多样性与长期认知连续性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>ACF: A Collaborative Framework for Agent Covert Communication under Cognitive Asymmetry</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Covert%20Communication-blue" alt="Covert Communication">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08276">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 ACF，一个面向认知不对称场景下记忆增强 Agent 的协同隐蔽通信框架。<br>
              • 它将隐蔽信号与语义推理解耦，并使用与前缀无关的解码方式和共享隐写配置来摆脱对称性假设。<br>
              • 即使在强认知不对称条件下，也能保持较好的语义一致性和隐蔽通信性能。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Knowledge%20Editing-blue" alt="Knowledge Editing">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08284">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 研究了大模型中的规则级知识编辑问题，并指出规则知识往往跨层分布而非局部集中。<br>
              • 作者扩展了 RuleEdit 基准，并通过因果追踪分析公式、描述与实例在不同层中的表征方式。<br>
              • 基于此提出 DMLE，在保持常规编辑指标竞争力的同时提升了规则迁移与理解能力。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>SkillClaw: Let Skills Evolve Collectively with Agentic Evolver</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Skill%20Evolution-blue" alt="Skill Evolution">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08377">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SkillClaw，用于多用户 LLM Agent 环境中的集体技能演化。<br>
              • 系统持续聚合用户轨迹，识别重复行为与失败模式，并将其转化为共享技能库中的修订或新增技能。<br>
              • 该方法实现了跨用户经验迁移，并提升了真实 Agent 场景中的整体表现。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Self%2DAuditing-blue" alt="Self-Auditing">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08401">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SAVeR，一个面向 LLM Agent 忠实推理的自审计框架。<br>
              • 它通过生成多样候选信念、对抗式审计和最小约束修复，在行动前校正潜在错误信念。<br>
              • 该方法减少了由不忠实推理引发的行为漂移，同时保持了较好的任务性能。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>SkillForge: Forging Domain-Specific, Self-Evolving Agent Skills in Cloud Technical Support</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Domain%20Skills-blue" alt="Domain Skills">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08618">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 SkillForge，一个面向云技术支持场景的领域技能生成与自进化框架。<br>
              • 它将领域上下文技能创建与故障分析、技能诊断、技能重写闭环结合起来。<br>
              • 既能提升初始技能质量，也能在部署反馈中持续迭代优化。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Efficient RL Training for LLMs with Experience Replay</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Experience%20Replay-blue" alt="Experience Replay">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08706">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 重新审视了 LLM 后训练中的经验回放机制，并质疑“只有新鲜 on-policy 数据才有价值”的假设。<br>
              • 论文系统分析了 replay buffer 在数据陈旧性、多样性与生成成本之间的权衡。<br>
              • 结果表明，合理设计的回放缓冲区能够显著降低推理成本，同时不损害甚至提升性能。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Artifacts as Memory Beyond the Agent Boundary</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/External%20Memory-blue" alt="External Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08756">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 从理论上形式化了“环境可作为 Agent 外部记忆”的观点。<br>
              • 论文提出 artifact 概念，说明某些观测能够减少表示历史所需的信息量，并将其与强化学习理论联系起来。<br>
              • 实验表明，环境中的空间路径信息可降低学习高性能策略所需的内部记忆负担。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>MT-OSC: Path for LLMs that Get Lost in Multi-Turn Conversation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/History%20Compression-blue" alt="History Compression">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08782">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 MT-OSC，在后台自动凝练多轮聊天历史以保留关键内容。<br>
              • 该方法通过 few-shot condenser 与轻量决策模块压缩无关信息，同时保留重要事实。<br>
              • 在最多减少 72% token 的同时，仍能保持甚至提升多轮对话准确率与时延表现。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>M^\star: Every Task Deserves Its Own Memory Harness</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Harness-blue" alt="Memory Harness">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.11811">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 M^\star，将 Agent 记忆表示为可执行的 Python 记忆程序，而不是固定 schema。<br>
              • 它通过群体搜索与失败分析驱动的反思式代码进化，联合优化任务专属的数据结构、存储逻辑与交互流程。<br>
              • 在对话、具身规划和专家推理等任务上优于固定记忆基线，并演化出差异显著的记忆机制。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-08</td>
        <td style="width: 55%;"><strong>From Business Events to Auditable Decisions: Ontology-Governed Graph Simulation for Enterprise AI</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Ontology%20Memory-blue" alt="Ontology Memory">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08603">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 LOM-action，一个面向企业可审计决策的本体约束图模拟框架。<br>
              • 它根据业务事件触发场景条件，在隔离沙箱中执行确定性图变换，并仅基于生成的场景有效图进行决策。<br>
              • 该方法在准确率和工具链 F1 上优于基线，同时能够输出完整可追溯的审计日志。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-08</td>
        <td style="width: 55%;"><strong>LAST: Leveraging Tools as Hints to Enhance Spatial Reasoning for Multimodal Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Tool%20Hints-blue" alt="Tool Hints">
          <img src="https://img.shields.io/badge/Memory%20Systems-brightgreen" alt="Memory Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09712">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 LAST，一个通过“工具即提示”增强多模态空间推理的框架。<br>
              • 它通过 LAST-Box 将异构工具调用封装为可复用的空间技能，并返回模型可直接消费的多模态提示。<br>
              • 结合三阶段渐进训练后，在四个空间推理数据集上取得了显著提升。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-04</td>
        <td style="width: 55%;"><strong>LightThinker++: From Reasoning Compression to Memory Management</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Explicit%20Memory%20Management-blue" alt="Explicit Memory Management">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.03679">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 该论文提出了 LightThinker，一种通过将冗长的推理链压缩为基于 gist tokens 的紧凑隐藏状态表示，从而实现表示层级推理压缩的方法 。<br>
              • 该论文进一步提出了 LightThinker++，一种显式自适应记忆管理框架，通过 commit、expand 和 fold 等行为原语动态调节上下文分辨率，并缓解复杂场景下的信息丢失 。<br>
              • 该工作构建了专门的轨迹合成流水线来训练有目的的记忆调度，证明了该方法在标准推理和长程智能体任务中能显著降低峰值 Token 使用量并提升性能 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20System-blue" alt="Memory System">
          <img src="https://img.shields.io/badge/Compression-brightgreen" alt="Compression">
          <img src="https://img.shields.io/badge/Skill%20Discovery-red" alt="Skill Discovery">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.15877v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 将 agent memory、skill discovery 和 rule learning 统一为经验压缩的不同层级，定义压缩函数 C_L 将轨迹映射到 L0-L3 层级的知识（原始轨迹 → 情景记忆 → 程序性技能 → 陈述性规则）。<br>
              • 揭示 memory 和 skill 社区深度割裂，22 篇核心论文中交叉引用率低于 1%（共 1136 条引用），提出全谱 agent 学习系统自适应选择压缩粒度。<br>
              • 优化目标包括减少 context 消耗、降低 retrieval latency、提高跨任务/跨模型/跨场景迁移能力；工作流遵循新问题→memory、重复模式→skill、跨场景原则→rule 的循环模式。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-03</td>
        <td style="width: 55%;"><strong>Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Poisoning%20Attack-red" alt="Poisoning Attack">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.02623">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 本论文提出了环境注入的基于轨迹的智能体记忆投毒（eTAMP），这是首个仅通过环境观测实现跨会话、跨站点劫持且无需直接访问记忆的攻击手段。<br>
              • 本研究发现了“挫败感利用”现象，即环境压力和任务失败能将代理对恶意指令的易感性显著提高多达八倍。<br>
              • 本工作引入了受混沌工程启发的 Chaos Monkey，通过模拟网络延迟和输入错误等真实部署条件，系统性地评估了大语言模型 Web 代理的鲁棒性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-03</td>
        <td style="width: 55%;"><strong>Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Neuro--Symbolic-blue" alt="Neuro-Symbolic">
          <img src="https://img.shields.io/badge/Alignment-brightgreen" alt="Alignment">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.02734">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 识别出长程智能体失败源于两个耦合但不同的目标：全局进度对齐和局部可行性对齐 。<br>
              • 提出神经-符号双存储框架，其中包含用于阶段感知语义引导的神经进度存储和用于可执行动作验证的符号可行性存储 。<br>
              • 在包括 ALFWorld、WebShop 和 TextCraft 在内的多种基准测试中证明了优越的性能，同时显著降低了无效动作率和轨迹长度 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Knowledge%20Graph-blue" alt="Knowledge Graph">
          <img src="https://img.shields.io/badge/Agentic%20Memory-brightgreen" alt="Agentic Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.01599">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一种智能体原生存储架构，由大语言模型自身负责知识的策划、组织与检索，消除了推理智能体与外部存储流水线之间的架构分离及随之产生的语义漂移。<br>
              • 引入了语境树，一种基于文件的分层知识图谱，并结合自适应知识生命周期机制，利用重要性评分、成熟度等级和新鲜度衰减来实现知识的动态演化管理。<br>
              • 设计了一套五层渐进式检索策略，通过多级缓存与索引技术优先处理查询，仅针对新颖问题启用智能体推理，从而最大限度地降低了检索延迟。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>MemFactory: Unified Inference & Training Framework for Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/RL-blue" alt="RL">
          <img src="https://img.shields.io/badge/Memory%20Optimization-brightgreen" alt="Memory Optimization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.29493">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • MemFactory提出了首个统一的框架，整合了记忆增强型AI智能体的训练、评估和推理流水线。<br>
              • 该框架采用了高度模块化的架构，将存储生命周期解耦为原子化的即插即用组件，如提取器、更新器和检索器。<br>
              • 它原生集成了群体相对策略优化（GRPO），旨在通过多维环境奖励实现对内部记忆管理策略的高效微调。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>MEMRERANK: Preference Memory for Personalized Product Reranking</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Preference%20Learning-blue" alt="Preference Learning">
          <img src="https://img.shields.io/badge/RL-brightgreen" alt="RL">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.29247">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 引入了一个个性化产品重排序基准，包含用户购买历史、候选集和人工标注的相关性标签 。<br>
              • 开发了 MEMRERANK 框架，将冗长的购买历史提炼为结构化的、与查询无关的类内和跨类偏好记忆 。<br>
              • 实施了强化学习后训练目标，以优化偏好记忆提取器在下游重排序任务中的效用 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>OMNI-SIMPLEMEM: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multimodal%20Memory-blue" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/Lifelong%20Learning-brightgreen" alt="Lifelong Learning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.00131">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 论文提出了 OMNI-SIMPLEMEM，一个为终身 AI 智能体设计的统一多模态记忆框架，利用了选择性摄取、渐进式金字塔检索以及结构化知识图谱增强。<br>
              • 该系统的架构和配置通过 AUTORESEARCHCLAW 自主发现并优化，该流水线是一个具备代码修改、故障诊断和架构重构能力的自动研究平台，其功能从根本上超越了传统的自动机器学习。<br>
              • 该框架在 LoCoMo 和 Mem-Gallery 基准测试中达到了当前最优性能，证明了自主识别的错误修复和架构更改带来的性能提升显著超过了超参数调优。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>SelRoute: Query-Type-Aware Routing for Long-Term Conversational Memory Retrieval</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Conversational%20Memory-blue" alt="Conversational Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.02431">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出 SelRoute 选择性路由框架，根据特定查询类型将查询分配至专门的检索流水线，以优化长期对话记忆检索 。<br>
              • 识别出富化-嵌入不对称性，证明存储时词汇扩展能提升词法搜索性能，但同时会降低嵌入搜索的质量 。<br>
              • 在 LongMemEval_M 基准上实现了最先进的结果，且该架构仅需 CPU 运行，无需查询时的 LLM 推理，并能推广至多个基准测试 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-31</td>
        <td style="width: 55%;"><strong>Multi-Layered Memory Architectures for LLM Agents: An Experimental Evaluation of Long-Term Context Retention</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Context%20retention-blue" alt="Context retention">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.29194">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一种多层记忆框架（MLMF），将对话历史分解为工作记忆、情节记忆和语义记忆层，以实现短期交互与长期抽象的分离 。<br>
              • 引入了自适应检索门控机制和保留稳定性目标，用以调节语义偏移并保持跨长会话的人格一致性 。<br>
              • 通过在长程基准测试上的实验验证了该框架，在降低上下文使用率和错误记忆率的同时，提升了长期保留稳定性和多跳推理性能 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-31</td>
        <td style="width: 55%;"><strong>OBLIVION: Self-Adaptive Agentic Memory Control through Decay-Driven Activation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Adaptive%20Memory-blue" alt="Adaptive Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.00131">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • OBLIVION 引入了读/写解耦的记忆控制范式，将何时检索信息的决策与选择哪些信息进行强化分离开来。<br>
              • 该框架实现了由 L1 程序性记忆、L2 语义记忆和 L3 情节性记忆组成的层级记忆结构，并结合受艾宾浩斯启发的衰减驱动激活机制，在不进行显式删除的情况下管理记忆的可访问性。<br>
              • 在静态和动态基准测试上的实证评估表明，自适应记忆控制在长程交互中有效平衡了学习与遗忘，同时显著减少了干扰和计算开销。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-30</td>
        <td style="width: 55%;"><strong>GEMS: Agent-Native Multimodal Generation with Memory and Skills</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multimodal%20Memory-blue" alt="Multimodal Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.28088">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出GEMS，一个原生智能体多模态生成框架，通过结构化的多智能体循环和迭代优化来提升复杂指令下的生成质量 。<br>
              • 引入持久化智能体记忆机制，利用分层压缩技术管理历史上下文，并在多轮优化轨迹中提炼战略经验 。<br>
              • 开发可扩展的智能体技能模块，通过按需加载机制提供领域专业知识，有效应对专门的下游应用需求 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-30</td>
        <td style="width: 55%;"><strong>Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Processing-blue" alt="Memory Processing">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.29002">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 统一了多种长上下文大语言模型推理优化方法，定义了一个通用的四步记忆处理流水线，并利用系统性性能分析将其识别为主要的性能瓶颈 。<br>
              • 该研究刻画了记忆处理流水线各阶段在定量与定性上的计算异构性，区分了计算密集型规则操作与访存受限型不规则任务 。<br>
              • 开发了一种 GPU-FPGA 异构系统，通过将不规则且访问受限的操作卸载到 FPGA，同时在 GPU 上保留计算密集型任务来加速推理，实现了显著的加速比和节能效果 。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-28</td>
        <td style="width: 55%;"><strong>Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Knowledge%20Graph-blue" alt="Knowledge Graph">
          <img src="https://img.shields.io/badge/MCP-brightgreen" alt="MCP">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.27277">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • CODEBASE-MEMORY 提供了一种持久化的、基于 Tree-Sitter 的知识图谱架构，通过多阶段并行构建流水线和增量同步支持 66 种语言。<br>
              • 该系统引入了基于 MCP 的工具接口，公开了 14 种结构化查询工具（如调用路径追踪和影响分析），并具有亚毫秒级的查询延迟。<br>
              • 在 31 个仓库上的实证评估表明，与传统的文件探索智能体相比，该方法在实现竞争性回答质量的同时，将 Token 消耗降低了 10 倍，并将工具调用减少了 2.1 倍。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-27</td>
        <td style="width: 55%;"><strong>Scaling Teams or Scaling Time? Memory Enabled Lifelong Learning in LLM Multi-Agent Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Lifelong%20Learning-blue" alt="Lifelong Learning">
          <img src="https://img.shields.io/badge/Multi--Agent%20Systems-brightgreen" alt="Multi-Agent Systems">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.03295">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了LLM多智能体系统的联合扩展视角，将团队规模扩展与终身学习扩展视为相互作用的扩展空间，而非孤立的轴线。<br>
              • 提出了LLMA-Mem终身记忆框架，通过整合情景记忆、程序记忆和交互记忆模块，在灵活的记忆拓扑下实现跨任务迁移与协作建模。<br>
              • 系统性实证研究揭示了非单调的扩展格局，证明有效的记忆设计能使小型团队在长程性能和标记效率上超越大型集体。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-27</td>
        <td style="width: 55%;"><strong>MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Cost--aware%20Memory-blue" alt="Cost-aware Memory">
          <img src="https://img.shields.io/badge/RAG-brightgreen" alt="RAG">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/html/2603.26557v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出 MemBoost，一个集成了关联记忆引擎、元控制器和大型语言模型 Oracle 的记忆增强型 LLM 推理框架，以优化成本与质量的权衡。<br>
              • 引入了“检索或升级”决策循环以及持续回写机制，实现了高效的语义答案复用和记忆增长。<br>
              • 通过在 MMLU-Pro 数据集上的实验证明，该框架在显著降低推理成本和延迟的同时，达到了与 Oracle 模型相当甚至更高的准确率。
          </td>
      </tr>
      <td rowspan="2" style="width: 15%;">2026-03-20</td>
      <td style="width: 55%;"><strong>PersonaVLM — Long-Term Personalized Multimodal LLMs</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multimodal%20Personalization-purple" alt="Multimodal Personalization">
        <img src="https://img.shields.io/badge/Proactive%20Memory-blue" alt="Proactive Memory">
        <img src="https://img.shields.io/badge/Multi--Type%20Memory-seagreen" alt="Multi-Type Memory">
        <img src="https://img.shields.io/badge/Personality%20Evolving-orange" alt="Personality Evolving">
        <img src="https://img.shields.io/badge/Benchmark%20--%20Persona--MME-red" alt="Benchmark Persona-MME">
      </td>
      <td style="width: 15%;">
        <a href="https://github.com/MiG-NJU/PersonaVLM">
          <img src="https://img.shields.io/badge/GitHub-Repo-%23181717?logo=github" alt="GitHub">
        </a>
        <a href="https://huggingface.co/ClareNie/PersonaVLM">
          <img src="https://img.shields.io/badge/HuggingFace-Model-%23FFD21E?logo=huggingface" alt="Hugging Face">
        </a>
        <a href="https://PersonaVLM.github.io">
          <img src="https://img.shields.io/badge/Website-Project-%23008080?logo=googlechrome" alt="Website">
        </a>
      </td>
      <tr>
        <td colspan="3">
          • 提出 PersonaVLM，这是一种创新的个性化多模态智能体框架，通过主动记忆管理与自演进的个性对齐机制，将通用多模态大语言模型（如 Qwen2.5-VL）转化为个性化助手.<br>
          • 实现了多类型记忆架构（核心记忆、语义记忆、情节记忆、程序记忆），以支持复杂的多轮推理，并具备主动记忆功能，可自动从多模态交互片段中提取并总结信息，构建持久化的个性化数据库.<br>
          • 引入基于动量的个性演进（PEM）机制以实现一致的响应生成，同时发布 Persona-MME 基准（涵盖 14 个细粒度任务，共 2,000 余个测试用例，CVPR 2026），并开源完整的模型权重、8 万余条训练样本及评估代码.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-19</td>
        <td style="width: 55%;"><strong>MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2603.18718">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MEMMA，一个即插即用的多智能体框架，通过前向和后向路径共同协调记忆循环，以解决记忆操作中的策略盲区和延迟反馈问题。<br>
          • 引入 Meta-Thinker 在记忆构建与迭代检索时提供显式策略推理，并设计了一种原位自进化记忆机制，将下游探针问答的失败直接转化为对记忆库的结构化修复操作。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/safety-red" alt="safety">
          <img src="https://img.shields.io/badge/Evolution-brightgreen" alt="Evolution">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11768v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 大模型智能体的记忆系统正从静态检索转向动态自主更新，这虽然提升了智能体的适应性，但也引发了严峻的稳定与安全问题。其中包括语义漂移、固化错误工作流的程序漂移、外部恶意注入的记忆投毒。<br>
              • 提出稳定与安全治理记忆（SSGM）框架。该框架的核心设计理念是将智能体的“生成式认知策略”与“底层记忆存储介质”彻底解耦。它在两者之间引入了一个主动拦截的治理中间件，使记忆的更新不再是盲目的直接写入，而是必须经过多重网关的审查。<br>
              • 合并前验证，在写入前进行逻辑一致性检查，拒绝与核心事实相矛盾的更新，防止幻觉被固化
              。时间与权限过滤，在读取时结合衰减函数过滤过期失效数据，并基于访问控制防止跨用户隐私泄露。可逆的定期对齐，采用“可变活动图+ 不可变情景日志”的双轨存储结构，系统会定期将当前记忆与不可变日志进行对齐与错误回滚，从而在数学上为长期的“语义漂移”设定了严格的误差上限。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/safety-orange" alt="safety">
          <img src="https://img.shields.io/badge/Openclaw-red" alt="openclaw">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11619v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 文章针对OpenClaw等自主大语言模型智能体，系统性地分析了其在初始化、输入、推理、决策和执行五个生命周期阶段的安全威胁。<br>
              • 在OpenClaw上进行了详细的案例研究，证明了这些威胁的破坏力。例如，攻击者可以通过“记忆投毒”将瞬时的恶意输入转化为长期的行为控制；而在决策和执行阶段，模糊的指令可能引发“意图漂移”，使智能体将简单的安全检查任务升级为破坏性的系统防火墙修改和高危命令执行。<br>
              • 缓解策略包括：初始化阶段的插件验证与签名、输入阶段的语义防火墙隔离、推理阶段的动态记忆完整性校验与状态回滚、决策阶段的意图一致性验证，以及执行阶段的内核级沙箱与最小权限控制。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-12</td>
        <td style="width: 55%;"><strong>Empowering Vision-Language-Action Model with
Memory via Dual-Level Recurrent Queries</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dual--Level--Recurrent--Memory-indigo" alt="Recurrent-Memory">
          <img src="https://img.shields.io/badge/Past--Prediction-indigo" alt="Past Observation Prediction">
          <img src="https://img.shields.io/badge/Multi-Modal-yellow" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.12942">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • ReMem-VLA 引入了两套可学习的循环记忆查询：帧级查询逐帧更新以捕捉短期记忆，而块级查询则在更长的时间跨度上更新，用于稳定维持长期记忆。<br>
              • 增加了一个视觉预测头，引入了过去观察预测作为辅助训练目标，强制模型通过重建历史 RGB 图像来召回视觉细节。针对变长序列循环训练的批处理难题，提出了一种基于槽的流式训练范式，能够在保证时间连续性的同时避免跨任务片段的状态泄露。<br>
              • 为了克服传统沿时间截断反向传播在长序列优化上的瓶颈，模型创造性地采用了冻结 VLM 加固定指数移动平均的无梯度循环更新路径，使得查询只需学习“提取什么任务相关信息”，而无需学习“如何传递”。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi-turn-indigo" alt="Multi-turn">
          <img src="https://img.shields.io/badge/Multi-Modal-yellow" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11896">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 现有的流式多模态大模型通常采用“感知与生成交替”的串行模式，这导致文本解码会阻塞视频的持续摄入，并且随着长视频的推进，模型极易遗忘早期的关键信息。为此，本文提出了一种“边看边思考”的全新流式推理框架。<br>
              • 该框架将视频划分为多个片段，并在系统运行中在线动态生成并维护持久的片段级记忆笔记，以隐式检索的方式支持多轮问答。<br>
              • 构建了专门的三阶段流式思维链（CoT）数据集（涵盖单轮适应、多轮交互和长程能力训练），并配合片段级的流式因果掩码（Causal mask）以保证严格的时间因果性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi-turn-indigo" alt="Multi-turn">
          <<img src="https://img.shields.io/badge/Multi-Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/Context%20Mgmt-blue" alt="Context-Optimization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09022">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 多智能体长程博弈中早期错误易被放大，且固定提示词会导致策略僵化和评估结果方差极大的问题，本文提出了一种无需更新模型权重的自我对弈框架 MEMO。<br>
              • MEMO 巧妙地将“保留”与“探索”机制解耦并结合。它建立了一个持久化记忆库，利用 CRUD（增删改查）操作从对弈轨迹中提取结构化的策略洞察，并将其作为后续推理的先验知识注入；同时，它利用基于 TrueSkill 评分的锦标赛式提示词演化和优先经验回放机制，来高效探索策略并重访关键决策状态。<br>
              • 在五款文本博弈测试中，MEMO 展现了突出的学习效率，仅需 2000 局自我对弈，就能将 GPT-4o-mini 的平均胜率从 25.1% 提升至 49.5%，同时使运行结果的方差大幅下降。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-12</td>
        <td style="width: 55%;"><strong>Collaborative Multi-Agent Optimization for Personalized Memory System</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalized">
          <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/RL-blueviolet" alt="RL">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.12631">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 现有的个性化大模型记忆系统通常由多个智能体组成，但过去的方法大多对它们进行独立的局部优化，忽视了跨智能体的协作，导致局部最优无法保证全局系统问答性能的最佳。<br>
              • 在为了解决异构智能体异步执行带来的优化难题，文章提出了 CoMAM 框架，将细粒度提取、粗粒度画像和记忆检索等智能体的执行流程建模为顺序的马尔可夫决策过程。<br>
              • 为了将局部的任务改进与全局系统性能对齐，CoMAM 通过计算每个智能体的局部奖励与全局系统奖励之间的组级排序一致性来量化其贡献。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-13</td>
        <td style="width: 55%;"><strong>Structured Distillation for Personalized Agent Memory:11× Token Reduction with Retrieval Preservation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalized">
          <img src="https://img.shields.io/badge/Retrieval-orange" alt="Retrieval">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.13017">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出将每次对话交互提取为结构化的复合对象，包含：核心内容、特定上下文、主题分类和涉及文件。这种方法遵循“保留核心词汇”原则，不随意改写专业术语，成功将每次交互的平均Token数从371压缩至38，实现了11倍的高效压缩。<br>
              • 在包含107种检索配置的测试中发现，最佳的纯蒸馏文本配置能够保留原始逐字文本96%向量搜索在11倍压缩下几乎没有出现显著的性能衰减。<br>
              • agent在上下文中仅携带压缩后的蒸馏文本作为“路由索引”进行高效检索，而原始的完整对话文本保存在本地，仅在用户需要深入查看时才调出显示。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Tool%20Use-orange" alt="Tool Use">
          <img src="https://img.shields.io/badge/Retrieval-orange" alt="Retrieval">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09297">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 结构化的自适应记忆抽取：设计了一个记忆抽取智能体，能够通过单次交互根据语义相关性自适应地切分长上下文，并提取为包含摘要、关键词、事件等丰富信息的结构化记忆笔记。<br>
              • 工具驱动的自主记忆探索：构建了支持字符串键值匹配与向量相似度查询的多索引数据库。检索智能体可自主选择查询工具，在记忆空间中进行多轮迭代探索。<br>
              • 长程推理能力与Token效率双提升：通过灵活精准的工具调用及缓存机制过滤冗余上下文，该框架在复杂长程问题上显著超越基线，同时保持了较低的Token消耗。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>EVOKING USER MEMORY: PERSONALIZING LLM VIA RECOLLECTION-FAMILIARITY ADAPTIVE RETRIEVAL</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalized">
          <img src="https://img.shields.io/badge/Adaptive-orange" alt="Adaptive">
          <img src="https://img.shields.io/badge/Retrieval-orange" alt="Retrieval">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09250">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 指出当前个性化大模型的记忆检索要么将历史记录全量输入导致上下文过载，要么仅依赖单次相似度检索而导致理解过浅。为此，研究团队借鉴人类记忆的“回想-熟悉度双过程理论”，提出了一种名为 RF-Mem 的自适应记忆检索框架。<br>
              • RF-Mem 会通过探测检索的平均相似度得分和熵值来衡量“熟悉度”。当熟悉度高且不确定性低时，系统采用快速的“熟悉度路径”，直接返回单次 top-K 结果；当熟悉度低且不确定性高时，则激活深度的“回想路径”。<br>
              • 在触发“回想路径”时，系统会对候选记忆进行聚类，并使用 α-mix 策略将聚类质心与原始查询进行混合更新。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-10</td>
        <td style="width: 55%;"><strong>A Control-Theoretic Foundation for Agentic Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Control--Theory-blue" alt="Control-Theory">
          <img src="https://img.shields.io/badge/Agentic--orange" alt="Agentic-Systems">
          <img src="https://img.shields.io/badge/feedback--pink" alt="feedback Control">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.10779">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一种控制论框架，将AI智能体系统嵌入到反馈控制环中进行分析。该框架没有将AI的记忆、学习、工具调用、交互信号和目标表述视为孤立的零散功能，而是将它们统一整合到了一个单一的闭环动态架构中。<br>
              • 通过AI对控制架构所掌握的“决策权限”大小，创造性地定义了一个五级智能体层级结构。<br>
              • 将该框架应用于非线性和线性系统，文章指出随着智能体层级的提升，系统不可避免地会引入更多复杂的动态机制。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>When OpenClaw Meets Hospital: Toward an Agentic Operating System for Dynamic Clinical Workflows</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/openclaw--red" alt="openclaw">
          <img src="https://img.shields.io/badge/healthcare--green" alt="openclaw">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11721">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 将智能体限制在隔离环境中，仅允许读写特定文件和调用预审的“医疗技能库”，从操作系统底层切断任意代码执行与网络访问，确保数据安全与合规。<br>
              • 摒弃传统的向量检索，将临床文档组织为带清单的树状结构。智能体依靠自然语言理解能力阅读清单，进行“渐进式披露”导航，从而精准、可解释地获取长期的病历上下文。<br>
              • 多智能体间不直接对话，而是通过“仅追加”写入共享临床文档及事件订阅来实现隐式协同。这使得智能体能进行临场任务编排，灵活应对传统系统无法处理的复杂、长尾临床需求。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-10</td>
        <td style="width: 55%;"><strong>Trajectory-Informed Memory Generation for Self-Improving Agent Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Trajectory%20Memory-orange" alt="Trajectory Memory Generation">
          <img src="https://img.shields.io/badge/Self--Improving-brightgreen" alt="Self-Improving">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.10600">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 解决智能体的“失忆”问题，系统性地从其历史执行轨迹（包括完美成功、低效成功、失败及错误恢复）中自动提取可复用的实战经验。<br>
              • 提出一个完整的学习闭环，包含轨迹特征提取、决策归因分析、情境提示生成，以及上下文自适应检索。<br>
              • 在AppWorld基准测试中全面提升了智能体的任务表现，尤其在需要复杂规划的长序列任务上效果显著。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Adaptive-orange" alt="Adaptive">
          <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Cognitive Evolution">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09716v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 将智能体的认知结构化为“内部认知”和“外部认知”。这种认知作为智能体可更新的状态，会根据任务交互的实际结果不断进行自我修正和演进，从而为决策提供更准确、更少偏差的知识基础。<br>
              • 采用“选择-执行-更新”的动态循环进行问题求解。它将动作空间统一划分为“内部行动”和“外部行动”，使智能体能够完全根据当前上下文和实时认知来进行自适应的下一步规划。<br>
              • 为了解决长序列推理带来的上下文冗余与 Token 消耗问题，系统设计了弹性记忆编排器（EMO），用于动态压缩历史轨迹、过滤冗余信息并提取可复用的片段记忆。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.10062">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 将多智能体记忆系统类比为经典的计算机系统，区分了共享记忆和分布式记忆两种基本架构原型。<br>
              • 提出了一种包含I/O层、缓存层和内存层缓存共享协议，以及用于规范读写权限与粒度的记忆访问控制协议。<br>
              • 未来构建多智能体系统最紧迫的挑战是解决记忆的一致性问题。这要求系统在多个智能体并发读写共享记忆时，能够妥善处理读取时的冲突、更新操作的可见性与顺序，并建立明确的版本控制与冲突解决规则，以保持全局上下文的连贯性。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-03-04</td>
          <td style="width: 55%;"><strong>Adaptive Memory Admission Control for LLM Agents</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Admission%20Control-teal" alt="Admission Control">
              <img src="https://img.shields.io/badge/Memory%20Management-orange" alt="Memory Management">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04549v1">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 缺乏记忆准入控制会导致长程记忆库迅速被低质、冗余或无效的垃圾特征污染，拖垮多轮推理。<br>
              • 引入结构化自适应准入控制（A-MAC），通过轻量化提取未来效用、置信度、新颖度等五大可解释因子，对写入动作进行严格前置拦截。<br>
              • 确立了准入控制作为记忆设计的核心工程原则，从源头净化记忆库，在 LoCoMo 基准上实现了延迟与性能的双重优化。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-03-02</td>
          <td style="width: 55%;"><strong>MemSifter: Offloading LLM Memory Retrieval via Outcome-Driven Proxy Reasoning</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Offloading-teal" alt="Offloading">
              <img src="https://img.shields.io/badge/Proxy%20Model-orange" alt="Proxy Model">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.03379">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 大模型在执行长周期任务时，频繁调用主网络进行复杂记忆检索的成本极高，算力与准确性难以两全。<br>
              • 构建 MemSifter 框架，利用结果驱动的强化学习范式，将重度检索计算直接卸载给轻量级代理模型。<br>
              • 实现了检索架构的低成本解耦，极少推理开销即达到先进的检索命中率，是一种极具扩展性的工业级长程记忆解法。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-03-02</td>
          <td style="width: 55%;"><strong>GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/RAG-teal" alt="RAG">
              <img src="https://img.shields.io/badge/Adaptive-orange" alt="Adaptive">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01783">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 传统 RAG 系统采用静态索引结构，在面对高频复现查询时存在严重的遍历冗余与计算浪费。<br>
              • 受认知科学启发提出无训练 GAM-RAG 框架，利用卡尔曼滤波增益规则，基于查询反馈动态强化重复检索的记忆状态。<br>
              • 成功在索引稳定性与适应性间取得平衡，有效避免了无效检索，在保证准确率的同时大幅削减推理算力开销。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-03-02</td>
          <td style="width: 55%;"><strong>Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Diagnosis-teal" alt="Diagnosis">
              <img src="https://img.shields.io/badge/Retrieval-orange" alt="Retrieval">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.02473v1">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 明确指出当前记忆系统的优化误区，需量化诊断写入、检索与利用三阶段各自对整体性能的真实影响。<br>
              • 设计诊断框架对主流写入与检索策略进行严格的交叉消融实验，剥离并解耦各阶段的贡献度。<br>
              • 证实检索阶段是压倒性的性能瓶颈（影响权重达 20%），且原始分块存储效能优越，指导业界将算力重仓于检索增强而非复杂压缩。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-02-28</td>
        <td style="width: 55%;"><strong>MemPO: Self-Memory Policy Optimization for Long-Horizon Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Policy%20Optimization-teal" alt="Policy Optimization">
            <img src="https://img.shields.io/badge/Self-Memory-orange" alt="Self-Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.00680">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 长程智能体被动依赖外部 RAG 检索，缺乏对历史信息有效性的自主判断与留存管理机制。<br>
            • 提出自记忆策略优化算法（MemPO），引入改进后的信用分配机制，赋予模型主动归纳和筛选高价值记忆的权限。<br>
            • 该算法通过精准剔除冗余信息，在显著压缩 Token 消耗的同时，实现了 F1 分数与任务性能的全面反超。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>ParamMem: Augmenting Language Agents with Parametric Reflective Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Reflective%20Memory-teal" alt="Reflective Memory">
            <img src="https://img.shields.io/badge/Parametric-orange" alt="Parametric">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.23320.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 推出 ParamMem 参数化记忆模块，通过多样化反思生成解决自我反思导致的输出重复问题。<br>
            • 采用温度控制采样和跨样本记忆技术，构建了高性能的 ParamAgent 框架。<br>
            • 在代码生成、数学推理等任务上显著优于现有基线，验证了反思多样性对任务成功率的正向贡献。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>Tell Me What To Learn: Generalizing Neural Memory to be Controllable in Natural Language</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Control-grey" alt="Control">
            <img src="https://img.shields.io/badge/Natural%20Language-blue" alt="Natural Language">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.23201.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 创新性地提出一种可通过自然语言指令进行控制更新的通用神经记忆系统。<br>
            • 解决了传统模型无法让用户干预记忆内容的难题，支持代理从异构源中进行选择性学习。<br>
            • 该方法在医疗和客服等对记忆准确性和可控性有极高要求的场景中具有巨大应用潜力。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/RL-blueviolet" alt="RL">
            <img src="https://img.shields.io/badge/Exploration-success" alt="Exploration">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.23008.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出 EMPO^2 混合策略优化框架，旨在破解 LLM 代理在强化学习训练中的探索瓶颈。<br>
            • 结合记忆引导探索与策略更新，确保代理在有无记忆场景下均具备极强的鲁棒性。<br>
            • 在 ScienceWorld 任务中实现 128.6% 的性能飞跃，且在分布外任务中表现出优异的适应性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Evaluation-yellow" alt="Evaluation">
            <img src="https://img.shields.io/badge/Causal%20Graph-cyan" alt="Causal Graph">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22769.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 推出专门针对自主代理环境交互（而非仅对话）的长程记忆评估框架 AMA-Bench。<br>
            • 同步提出 AMA-Agent 系统，利用因果图和工具增强检索来优化记忆检索质量。<br>
            • 研究揭示了现有内存系统在持续环境交互任务中的短板，并提供了有效的改进路径。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-25</td>
        <td style="width: 55%;"><strong>Towards Autonomous Memory Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Autonomous-brightgreen" alt="Autonomous">
            <img src="https://img.shields.io/badge/Knowledge%20Extraction-blue" alt="Knowledge Extraction">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22406.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出自主记忆代理 U-Mem，将记忆模式从被动存储转变为主动获取、验证与策划知识。<br>
            • 引入成本意识的知识提取级联，从自我信号到专家反馈多级验证，结合语义感知的采样策略。<br>
            • 成功减轻了冷启动偏差，并在 HotpotQA 等高难度知识任务中超越了先前的记忆基线。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-25</td>
        <td style="width: 55%;"><strong>Structurally Aligned Subtask-Level Memory for Software Engineering Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Software%20Eng-brown" alt="Software Eng">
            <img src="https://img.shields.io/badge/Subtask%20Level-blueviolet" alt="Subtask Level">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21611.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 针对软件工程代理在处理相似描述但逻辑相异任务时的痛点，提出结构对齐子任务级记忆。<br>
            • 该机制通过细粒度的任务切分与记忆对齐，显著增强了代理的长程推理能力。<br>
            • 在多个软件工程基准测试中证明了其在解决复杂逻辑纠缠任务时的优越性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-24</td>
      <td style="width: 55%;"><strong>ARCHITECTING AGENTOS: FROM TOKEN-LEVEL CONTEXT TO EMERGENT SYSTEM-LEVEL INTELLIGENCE</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.20934.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 该论文探讨了大型语言模型（LLMs）向动态自主认知系统转型的框架——AgentOS。<br>
        • 通过将LLM重新定义为“推理内核”，AgentOS引入了深度上下文管理的概念，以解决当前应用中长上下文任务的信息稀释和多代理协作的时间漂移问题。<br>
        • 论文详细阐述了AgentOS的核心组件，如认知同步脉冲（CSP）、语义切片理论与感知对齐机制，及其如何促进多智能体系统的集体智能涌现
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-24</td>
        <td style="width: 55%;"><strong>Pancake: Hierarchical Memory System for Multi-Agent LLM Serving</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
            <img src="https://img.shields.io/badge/GPU--CPU-black" alt="GPU-CPU">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21477.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出多层次代理记忆系统 Pancake，解决大规模 LLM 服务中的多代理记忆碎片问题。<br>
            • 统一了多级索引缓存、协调索引管理及协作的 GPU-CPU 加速技术。<br>
            • 与 LangChain 等主流框架兼容，在真实工作负载下实现了超过 4.29 倍的吞吐量提升。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-23</td>
      <td style="width: 55%;"><strong>Agents of Chaos</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Attack-red" alt="Memory Attack">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.20021.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 论文报告了对自主语言模型智能体的红队测试，强调了在真实环境中智能体引发的安全和隐私漏洞。<br>
        • 研究涉及11个案例，揭示了智能体在处理敏感信息、遵循指令及资源管理方面的多种问题与失败模式。<br>
        • 文本讨论了责任分配的复杂性以及现有技术和法律框架在保障自主系统安全性方面的不足。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-23</td>
        <td style="width: 55%;"><strong>Structured Prompt Language: Declarative Context Management for LLMs</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Context%20Mgmt-blue" alt="Context Mgmt">
            <img src="https://img.shields.io/badge/SPL-magenta" alt="SPL">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21257.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 推出受 SQL 启发的声明性语言 SPL，将 LLM 上下文窗口视为受限资源进行高效管理。<br>
            • 原生集成 RAG 和持久记忆，提供自动查询优化器和透明的 EXPLAIN 调试功能。<br>
            • 实验证实 SPL 能显著减少提示冗余，并在多语言翻译、逻辑分块等任务中降低计算成本。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-23</td>
        <td style="width: 55%;"><strong>Agentic AI as a Cybersecurity Attack Surface: Threats, Exploits, and Defenses in Runtime Supply Chains</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Cybersecurity-red" alt="Cybersecurity">
            <img src="https://img.shields.io/badge/Zero--Trust-grey" alt="Zero-Trust">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.19555.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 系统性分析了 LLM 智能体在推理依赖中的安全风险，将其分类为数据与工具供应链攻击。<br>
            • 提出“病毒智能体循环”概念，警告智能体可能成为自传播生成性蠕虫的载体。<br>
            • 倡导建立零信任运行时架构，通过加密来源约束工具执行并将上下文视为不可信流。
        </td>
    </tr>
    <tr>
    <td rowspan="2" style="width: 15%;">2026-02-22</td>
      <td style="width: 55%;"><strong>Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.19320v1.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 论文分析了代理记忆系统（Agentic Memory Systems）尤其是大型语言模型（LLM）在长期交互中的状态保持能力，揭示了其设计与评估的实证基础尚显脆弱。<br>
        • 文章对记忆结构进行了分类，包括轻量语义记忆、实体中心和个性化记忆、情节记忆及反思记忆，并通过实证分析说明当前系统的表现未能达到预期，提出了评估指标与语义效用不匹配的问题。<br>
        • 本文还探讨了增强记忆系统（MAG）在处理长上下文时的不同记忆架构、操作与管理策略，强调了对记忆管理的优化及评估方法的必要性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-20</td>
      <td style="width: 55%;"><strong>From Lossy to Verified: A Provenance-Aware Tiered Memory for Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.17913v1.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • TierMem是一个分层记忆体系，旨在提高信息检索的效率和精准度，以应对长时间交互历史带来的信息压缩问题。<br>
        • 该系统通过构建快速摘要层和不可变原始日志层，有效管理信息的存储与检索，加快查询响应速度并降低成本。<br>
        • TierMem的设计包含智能路由优化、错误分析以及分层回忆策略，以平衡准确性和效率。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-20</td>
      <td style="width: 55%;"><strong>Memory-Based Advantage Shaping for LLM-Guided Reinforcement Learning</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Efficiency-success" alt="Efficiency">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.17931v1.pdf">
      <img src="https://img.shields.io/badge/AAAI-Paper-black?labelColor=orange" alt="AAAI Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 该研究提出了一种创新的“基于记忆的优势塑造”方法，旨在提升大规模语言模型（LLM）指导下的强化学习（RL）在稀疏或延迟奖励环境中的样本效率。<br>
        • 通过构建记忆图并引入效用函数，该方法有效整合外部指导，优化RL模型的学习过程。<br>
        • 实验证明在多个基准环境中展现出较高的样本效率和表现。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-20</td>
      <td style="width: 55%;"><strong>MIRA: MEMORY-INTEGRATED REINFORCEMENT LEARNING AGENT WITH LIMITED LLM GUIDANCE</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.17930v1.pdf">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • MIRA（Memory-Integrated Reinforcement Learning Agent）是一种新型的强化学习代理，通过构建结构化的记忆图整合大型语言模型（LLM）的指导，以提高稀疏奖励环境中的学习效率和探索能力。<br>
        • MIRA的核心在于结合离线和在线LLM指导，筛选高置信度输出，计算效用信号，优化优势函数，确保自主学习并减少对真实LLM查询的依赖。<br>
        • 实验结果显示，MIRA在多个环境中的样本效率和收敛性均优于传统方法，展示了其在复杂任务下的潜力。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-20</td>
        <td style="width: 55%;"><strong>REMem: Reasoning with Episodic Memory in Language Agent</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Episodic%20Memory-red" alt="Episodic Memory">
            <img src="https://img.shields.io/badge/Reasoning-lightgrey" alt="Reasoning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.13530.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 针对现有语言代理缺乏有效回忆交互历史能力的问题，提出情节记忆推理框架 REMem。<br>
            • 核心包含离线索引和在线推理两个阶段，使代理能够模仿人类在时空上下文中进行推理。<br>
            • 实验结果显示，该框架在专门的情节记忆基准测试中表现出显著优势。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-17</td>
      <td style="width: 55%;"><strong>Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15313.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • Mnemis是一种新型的记忆框架，旨在提高大型语言模型（LLMs）的记忆组织与检索能力。<br>
        • 该框架结合了两种检索机制：系统1的相似性搜索与系统2的全局选择，通过基础图和层次图的构建，能够更高效地处理复杂查询。<br>
        • Mnemis在长时间记忆基准测试中表现优异，取得诸如93.9和91.6的高分，并且在实体识别及信息检索方面展现了显著优势。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-17</td>
      <td style="width: 55%;"><strong>ZOMBIE AGENTS: PERSISTENT CONTROL OF SELF-EVOLVING LLM AGENTS VIA SELF-REINFORCING IN-JECTIONS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Attack-red" alt="Memory Attack">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15654.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 论文介绍了“Zombie Agent”攻击模型，专注于自我进化的大型语言模型（LLM）代理。<br>
        • 该模型展示了如何通过黑盒两阶段攻击框架（感染和触发），对代理的长期记忆进行恶意负载的注入，从而导致持久性妥协。<br>
        • 研究表明，现有的提示过滤防御措施不足以保护这类自我进化代理，同时强调了记忆架构的特殊脆弱性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-17</td>
      <td style="width: 55%;"><strong>ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Attack-red" alt="Memory Attack">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15344.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 本文探讨了一种名为ER-MIA的框架，研究了针对长期记忆增强的大型语言模型（LLMs）的黑箱对抗性记忆注入攻击（AMIAs）。<br>
        • ER-MIA框架揭示了通过正常交互注入恶意文本的攻击机制，可能导致模型产生错误推理。<br>
        • 研究设计了多种自动对抗性记忆生成策略，并进行实证评估，表明当前的长时记忆系统在面对这些攻击时表现出显著的脆弱性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-17</td>
        <td style="width: 55%;"><strong>Improving MLLMs in Embodied Exploration and Question Answering with Human-Inspired Memory Modeling</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Embodied%20Agents-pink" alt="Embodied Agents">
            <img src="https://img.shields.io/badge/Semantic%20Memory-teal" alt="Semantic Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15513.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出非参数记忆框架，通过显式区分情节记忆与语义记忆，增强具身智能体的探索能力。<br>
            • 采用程序风格的规则提取机制，将环境经验转化为可跨场景泛化的结构化语义记忆。<br>
            • 显著提高了多模态大模型在非静态环境中的观察重用率和问答效率。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-16</td>
      <td style="width: 55%;"><strong>HyperRAG: Reasoning N-ary Facts over Hypergraphs for Retrieval Augmented Generation</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Hyper%20RAG-purple" alt="Hyper RAG">
      <img src="https://img.shields.io/badge/Decoupling-red" alt="Decoupling">
      <img src="https://img.shields.io/badge/Aggregation-success" alt="Aggregation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.14470v1.pdf">
      <img src="https://img.shields.io/badge/WWW-Paper-black?labelColor=teal" alt="WWW Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • HyperRAG是一个创新的检索增强生成（RAG）框架，利用n-元超图取代传统的二元知识图谱，以提升复杂问答和知识检索任务的准确性和效率。<br>
        • 通过新的模块HyperRetriever和HyperMemory，该框架实现了多跳推理的精准化和上下文意识的增强。<br>
        • 实验结果显示，HyperRAG表现出在多个基准数据集上的优越性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-16</td>
      <td style="width: 55%;"><strong>PANINI: Continual Learning in Token Space via Structured Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15156v1.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 本文详细介绍了PANINI，一个旨在提升持续学习和多跳问答能力的非参数持续学习框架。<br>
        • 通过引入结构化记忆和生成语义工作空间（GSW），PANINI能够高效处理新信息并通过问答链支持推理。<br>
        • 与多种基线模型相比，PANINI在多个评估基准上表现优异，尤其在缺失证据情况下显示出可靠性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-15</td>
        <td style="width: 55%;"><strong>Choosing How to Remember: Adaptive Memory Structures for LLM Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Adaptive%20Structures-orange" alt="Adaptive Structures">
            <img src="https://img.shields.io/badge/Framework-blue" alt="Framework">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.14038.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出 FluxMem 框架，赋予 LLM 代理根据交互特征自适应选择不同记忆结构的能力。<br>
            • 引入三层记忆层次结构，并利用基于 Beta 混合模型的概率门来增强记忆融合的鲁棒性。<br>
            • 在处理异构交互模式时表现卓越，于多个长时间基准上实现了性能跃升。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-14</td>
      <td style="width: 55%;"><strong>Hippocampus: An Efficient and Scalable Memory Module for Agentic AI</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Compressed%20Memory-4c78a8" alt="Compressed Memory">
          <img src="https://img.shields.io/badge/Dynamic%20Wavelet%20Matrix-f58518" alt="Dynamic Wavelet Matrix">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.13594.pdf">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了 Hippocampus，这是一种高效且可扩展的面向智能体AI的记忆模块，用紧凑的二进制签名和无损的token-ID流替代密集向量或重图结构的检索方式。<br>
            • 引入了动态小波矩阵（Dynamic Wavelet Matrix, DWM），用于对语义签名和可重构内容进行联合压缩与索引，从而能够直接在压缩域中实现超高速搜索。<br>
            • 在 LoCoMo 和 LongMemEval 上的实验表明，在保持准确性的同时，端到端检索延迟最高降低31倍，每次查询所需的token数量最多减少14倍。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-14</td>
        <td style="width: 55%;"><strong>HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Hybrid%20Arch-99cc00" alt="Hybrid Arch">
            <img src="https://img.shields.io/badge/Dynamic%20Retrieval-blue" alt="Dynamic Retrieval">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.13933.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出混合记忆架构 HyMem，通过双粒度存储（摘要级/深层级）解决长对话中的效率权衡问题。<br>
            • 引入动态按需调度机制，简单查询调用高效摘要，复杂查询激活深层模块。<br>
            • 实验表明其在维持高性能的同时，计算成本大幅降低了 92.6%。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-14</td>
        <td style="width: 55%;"><strong>Neuromem: A Granular Decomposition of the Streaming Lifecycle in External Memory for LLMs</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/External%20Memory-blueviolet" alt="External Memory">
            <img src="https://img.shields.io/badge/Benchmarking-yellow" alt="Benchmarking">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.13967.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 推出 Neuromem 可扩展测试平台，用于评估 LLM 外部记忆模块在摄取、维护、检索到整合的完整动态生命周期。<br>
            • 研究揭示了记忆准确性与成本受整个生命周期的共同影响，而非单一环节。<br>
            • 分析指出，随着记忆规模增长性能普遍下降，且时间相关查询仍是当前系统面临的最大挑战。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-13</td>
      <td style="width: 55%;"><strong>Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.18493v1.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 本文探讨了统一记忆代理（Unified Memory Agent, UMA）的开发及其在动态长时间状态跟踪和信息检索中的应用。<br>
        • UMAs通过将记忆操作与问答整合在一起，克服了传统大语言模型（LLMs）在处理长输入时遇到的挑战。<br>
        • UMA利用强化学习和新的策略优化算法，展示了在动态场景下显著的性能提升，准确率从61.38%提高至76.46%。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-12</td>
      <td style="width: 55%;"><strong>
      Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.12204">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过分析发现，预训练模型中 88% 的注意力操作所提取的信息是可预测的冗余信息，且这种计算浪费在标准训练过程中并不会自动减少。<br>
        • 受生物学启发，设计了 CRAM 机制，利用路由模块将频繁访问的“情节性”注意力检索逐渐固化为“语义性”的参数化记忆，从而实现计算量的动态缩减。<br>
        • 实验证明 CRAM 在保持高准确率的同时实现了 37.8 倍的注意力计算缩减，且其记忆转化动态在定量上与人类认知的幂律曲线高度匹配。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-12</td>
      <td style="width: 55%;"><strong>
      Scene-Aware Memory Discrimination: Deciding Which Personal Knowledge Stays</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.11607">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 针对智能设备产生的大量冗余信息，提出了在记忆构建过程中过滤无关交互、仅保留高价值个人知识的任务，以提升个性化服务的准确性。<br>
        • 该框架通过门控单元（GUM）在词级别高效过滤非记忆性内容，并利用聚类提示模块（CPM）根据用户意图自适应地制定记忆标准。<br>
        • 实验证明 SAMD 能够成功召回绝大部分重要数据，在显著降低计算成本的同时，增强了 AI 智能体在动态场景下的个性化响应能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-12</td>
      <td style="width: 55%;"><strong>
      Recurrent Preference Memory for Efficient Long-Sequence Generative Recommendation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.11605">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架将超长用户交互历史压缩为少量紧凑的“偏好记忆” Token，并与近期“工作记忆”结合，解决了生成式推荐在处理长序列时的计算瓶颈。<br>
        • 通过利用全局历史视图生成“参考记忆”作为监督目标，该策略解决了传统循环模型难以并行训练的问题，实现了高效的参数优化。<br>
        • 实验证明 Rec2PM 在大幅降低存储和推理延迟的同时，利用信息瓶颈原理有效过滤了用户行为中的随机噪声，推荐精度优于全序列模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-12</td>
      <td style="width: 55%;"><strong>
      TS-Memory: Plug-and-Play Memory for Time Series Foundation Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.11550">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出一种即插即用的轻量级内存适配器，通过“参数化记忆蒸馏”技术，解决了时间序列基础模型（TSFM）在下游领域分布偏移下的适应性问题。<br>
        • 首先利用线下 kNN 检索构建包含未来信息的特权监督信号，随后通过置信度门控机制将这种检索诱导的分布修正内化到参数化模块中。<br>
        • 该框架在显著提升点预测和概率预测精度的同时，实现了“零在线检索”部署，保持了与原始模型相当的推理效率且避免了灾难性遗忘。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>Understand Then Memory: A Cognitive Gist-Driven RAG Framework with Global Semantic Diffusion</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Cogito%20RAG-purple" alt="Cogito RAG">
      <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
      <img src="https://img.shields.io/badge/Aggregation-success" alt="Aggregation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.15895.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • CogitoRAG是一个基于认知记忆机制的检索增强生成（RAG）框架，旨在提高大型语言模型（LLMs）在知识整合和推理方面的能力。<br>
        • 该框架模拟人类认知过程，通过三个主要模块的协作（查询分解、实体扩散和CogniRank重排序）来优化信息检索和答案生成。<br>
        • CogitoRAG在多种问答基准测试中表现优异，特别是在复杂推理任务方面超越了传统RAG方法，强调了“理解优于记忆”的理念。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>
      When to Memorize and When to Stop: Gated Recurrent Memory for Long-Context Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.10560">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 针对大语言模型（LLM）在长上下文推理中的性能下降问题，该研究采用类似 RNN 的分块递归处理方式，通过维护动态更新的文本记忆来跨越上下文窗口限制。<br>
        • 在递归循环中设计了“更新门”以过滤无用信息防止记忆爆炸，以及“退出门”以在收集到足够证据后提前终止计算，从而显著提升了系统的稳定性与效率。<br>
        • 通过端到端的强化学习（RL）训练门控策略，实验证明 GRU-Mem 在多项长文本推理任务中均优于基准模型，且推理速度最高提升了 400%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>
      Towards Compressive and Scalable Recurrent Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.11212">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Elastic Memory 架构，一种基于 HiPPO 框架的新型递归记忆架构，通过在线函数逼近将长程历史信息压缩为固定大小的记忆状态，解决了 Transformer 处理长文本时的计算瓶颈。<br>
        • 开发了可并行的块级更新算法以及灵活的“多项式采样”检索机制，能够从压缩状态中精准重建历史摘要，且无需引入额外的可训练参数。<br>
        • 实验证明该模型在 32k+ 长文本任务上显著优于 Memorizing Transformer 和 Melodi 等基准，且支持在推理阶段通过调整采样策略灵活注入归纳偏置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>
      UMEM: Uniffed Memory Extraction and Management Framework for Generalizable Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Evolution-success" alt="Memory Evolution">
        <img src="https://img.shields.io/badge/Memory%20Management-steelblue" alt="Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.10652">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架改变了以往将“记忆提取”视为静态过程的传统模式，通过联合优化大语言模型的记忆提取与管理能力，解决了记忆内容与管理策略不匹配的问题。<br>
        • 通过语义邻域建模（针对相似查询簇进行评估）和基于 GRPO 算法的边际效用奖励机制，促使模型从经验中提炼普适性的规律，而非仅仅记住特定实例的噪声。<br>
        • 实现了卓越的泛化与持续进化能力：实验证明 UMEM 在数学推理和具身交互等多个基准测试中显著优于现有基准，且在长期持续交互中展现出稳定的性能单调增长。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-10</td>
      <td style="width: 55%;"><strong>
      TraceMem: Weaving Narrative Memory Schemata from User Conversational Traces</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Mechanisms-lime" alt="Long-Term Memory Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.09712">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架通过三阶段流水线（短期处理、突触整合、系统整合），将零散的用户对话轨迹编织成结构化且具有叙事连贯性的记忆图谱。<br>
        • 系统利用话题分割和两级分层聚类技术，将即时对话片段转化为反映用户个人特质的、随时间演进的叙事线索与记忆卡片。<br>
        • 引入了代理搜索机制以支持类人的溯源推理，在 LoCoMo 基准测试中显著提升了模型在多跳推理和时间顺序理解方面的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-09</td>
      <td style="width: 55%;"><strong>
      AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Shared%20Memory-purple" alt="Shared Memory">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.08837">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架通过引入可进化的记忆模块，在不依赖预训练协同过滤模型的情况下，实现了端到端的协同过滤信号建模。<br>
        • 系统将不同用户的抽象行为模式聚合在全局记忆池中，通过相似性与语义双重验证进行链接与迭代演化，从而强化跨用户的共享行为规律。<br>
        • 实验证明 AMEM4Rec 在多个真实数据集上显著优于现有基准，尤其在交互数据稀疏的冷启动场景下展现出极强的泛化能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-09</td>
      <td style="width: 55%;"><strong>
      Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Attack-red" alt="Memory Attack">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.08563v1">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 揭示了LLM即便在无状态部署下，也能通过将其输出作为后续输入（再摄入机制）来传递和保存状态，从而形成一个跨会话的隐蔽信息信道。<br>
        • 展示了一种新型时间后门攻击，它利用隐性记忆在多次看似无害的交互中累积隐藏条件，只有当特定序列完成后才会触发恶意负载。<br>
        • 分析了隐性记忆在隐蔽通信、基准污染和目标操纵等方面的广泛风险，并指出了未来在跨会话检测、取证分析及模型安全测试方面的研究必要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-09</td>
      <td style="width: 55%;"><strong>
      MemAdapter: Fast Alignment across Agent Memory Paradigms via Generative Subgraph Retrieval</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-steelblue" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.08369">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 针对显式、参数化和潜在记忆范式相互孤立的问题，提出了 MemAdapter 框架，首次通过生成式子图检索实现了在单一系统内对异构记忆范式的统一。<br>
        • 该框架先通过模型蒸馏训练生成式检索器，再利用对比学习训练轻量化对齐模块，仅需极少量数据即可将检索器快速适配至未见的记忆范式。<br>
        • 实验证明 MemAdapter 在多个基准测试中均优于主流记忆系统，且仅需 13 分钟即可完成范式对齐，并支持跨范式的零样本记忆融合。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-07</td>
      <td style="width: 55%;"><strong>
      MemPot: Defending Against Memory Extraction Attack with Optimized Honeypots </strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Attack-red" alt="Memory Attack">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.07517">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了首个针对基础智能体记忆提取攻击的防御框架MemPot，通过在智能体记忆存储中植入优化后的“蜜罐”文档来诱导并拦截恶意行为。<br>
        • 采用两阶段优化策略，先通过对比学习最大化攻击者与正常用户在检索轨迹上的区分度，再利用反转技术生成对用户无害且隐蔽的干扰文本。<br>
        • 基于序贯概率比检验（SPRT）构建了高效的动态检测机制，在实现高准确率检测的同时保持了零在线推理延迟，且不影响智能体原有的记忆功能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-06</td>
      <td style="width: 55%;"><strong>Agentic Unlearning: When LLM Agent Meets Machine Unlearning</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.17692v1.pdf">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
        • 提出了一种名为“同步回流遗忘”（Synchronized Backflow Unlearning, SBU）的新框架，旨在有效删除大型语言模型（LLM）中的敏感信息，同时确保共享知识的完整性。<br>
        • 通过结合参数路径和内存路径的协同工作，SBU解决了传统方法在隐私保护中的局限性，成功消除了已删除信息的残余影响，减少了信息再污染的问题。<br>
        • 实验结果显示，该方法在医疗问答基准测试中显著提高了隐私保护效果，同时保持了准确性，不仅在效率上优于基线方法，还克服了计算资源的限制。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-05</td>
      <td style="width: 55%;"><strong>Learning to Share: Selective Memory for Efficient Parallel Agentic Systems</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Shared%20Memory-purple" alt="Shared Memory">
        <img src="https://img.shields.io/badge/Parallel%20Agents-red" alt="Parallel Agents">
        <img src="https://img.shields.io/badge/Efficiency-success" alt="Efficiency">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.05965">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究多智能体并行执行时的“记忆共享”问题，强调只共享对全局协作真正有价值的信息以避免冗余。<br>
        • 提出选择性共享策略/机制（何时共享、共享什么、共享给谁），在性能与通信/存储开销之间做权衡。<br>
        • 在并行/多智能体任务设置中验证：在相近或更低的资源成本下提升整体效率与任务质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-02</td>
      <td style="width: 55%;"><strong>Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Online%20Update-purple" alt="Online Update">
        <img src="https://img.shields.io/badge/Continuous%20Feedback-red" alt="Continuous Feedback">
        <img src="https://img.shields.io/badge/Memory%20Evolution-success" alt="Memory Evolution">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.02369">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将智能体记忆建模为可在线“演化”的对象，利用连续/密集反馈信号持续修正记忆内容与结构。<br>
        • 设计在线更新闭环：从交互与反馈中提取可学习信号，驱动写入、修订、遗忘与整合。<br>
        • 实验展示随交互推进的持续改进（而非一次性离线训练后固定不变）。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-02</td>
      <td style="width: 55%;"><strong>Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Beyond%20RAG-purple" alt="Beyond RAG">
        <img src="https://img.shields.io/badge/Decoupling-red" alt="Decoupling">
        <img src="https://img.shields.io/badge/Aggregation-success" alt="Aggregation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.02007">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 反思“把检索当作一次性取 top-k”在智能体记忆中的不足，提出超越传统 RAG 的检索范式。<br>
        • 将检索过程解耦为“候选获取（decoupling）”与“证据聚合（aggregation）”，强调多源、多跳信息融合。<br>
        • 在需要跨片段证据整合的任务上显示相对更稳健的记忆调用与推理效果。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-01-30</td>
        <td style="width: 55%;"><strong>Field-Theoretic Memory for AI Agents: Continuous Dynamics for Context Preservation</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Memory%20System-blue" alt="Memory System">
            <img src="https://img.shields.io/badge/Field%20Theory-success" alt="Field Theory">
            <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21220.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出一种将存储信息视为连续场（由偏微分方程控制）而非离散条目的 AI 代理记忆系统。<br>
            • 借鉴场论逻辑：记忆在语义空间扩散，基于重要性热力学衰减，并通过场耦合实现多代理交互。<br>
            • 在 LongMemEval 基准上显著提升了多会话和时间推理表现，展示了集体智能优势。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-01-30</td>
        <td style="width: 55%;"><strong>Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Behavior%20Tree-blue" alt="Behavior Tree">
            <img src="https://img.shields.io/badge/Policy%20Verifiability-teal" alt="Policy Verifiability">
            <img src="https://img.shields.io/badge/Safety-red" alt="Safety">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.05517">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了 Traversal-as-Policy 范式，通过将执行日志蒸馏为结构化的门控行为树 (GBT)，在运行时以确定性的树遍历替代无约束生成，实现了 Agent 策略的外部化与可验证性。<br>
            • 引入了 Spine Memory 结构记录遍历路径，有效解决了长程任务中的策略隐式化和安全事后化问题。<br>
            • 实验验证该方法在软件工程、Web Agent 和安全等多个领域能同时提升成功率并显著降低违规风险与 token 消耗。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-29</td>
      <td style="width: 55%;"><strong>E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Episodic%20Memory-blue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Context%20Reconstruction-green" alt="Context Reconstruction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.21714">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了 E-mem 框架，通过情景上下文重构（Episodic Context Reconstruction）取代传统的记忆预处理，解决了去语境化导致的信息丢失问题。<br>
          • 采用了异构分层的主从智能体架构（Master-Assistant）：助手智能体作为记忆节点维护未压缩的完整上下文，而主智能体负责全局规划。<br>
          • 引入了路由机制，使助手智能体能够在本地恢复的原始上下文中进行推理并提取精确证据，在 LoCoMo 和 HotpotQA 上取得了 SOTA 性能，同时显著降低了 Token 成本（降低 70% 以上）。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-29</td>
      <td style="width: 55%;"><strong>ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Sharded%20Memory-purple" alt="Sharded Memory">
        <img src="https://img.shields.io/badge/MoE%20Routing-red" alt="MoE Routing">
        <img src="https://img.shields.io/badge/Efficiency-success" alt="Efficiency">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.21545">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 ShardMemo，一种分层记忆服务架构：Tier A（工作状态）、Tier B（分片证据存储）和 Tier C（版本化技能库）。<br>
        • 在 Tier B 中实施了“路由前范围过滤”（scope-before-routing）策略，并将分片选择建模为受限预算下的 Masked MoE 路由问题，利用成本感知门控机制优化检索。<br>
        • 在 LoCoMo 和 HotpotQA 上，ShardMemo 在固定预算下比余弦相似度路由提升了 +6.87 F1，同时减少了 20.5% 的检索工作量和延迟。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Embodied%20AI-yellow" alt="Embodied AI">
        <img src="https://img.shields.io/badge/Active%20Filtering-blueviolet" alt="Active Filtering">
        <img src="https://img.shields.io/badge/Memory%20Control-ff69b4" alt="Memory Control">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20831">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 MemCtrl，一种利用多模态大模型（MLLM）作为主动记忆控制器的框架，用于在线过滤具身智能体的冗余观察。<br>
        • 引入了一个可训练的记忆头（$\mu$），它可以作为门控机制，在探索过程中动态决定是保留、更新还是丢弃当前的观察或反思。<br>
        • 通过离线监督学习和在线强化学习训练记忆头，在 EmbodiedBench 上使小型 MLLM 的任务完成率平均提升了约 16%，在特定指令子集上提升超过 20%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>AMA: Adaptive Memory via Multi-Agent Collaboration</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Adaptive%20Routing-teal" alt="Adaptive Routing">
        <img src="https://img.shields.io/badge/Long--Term%20Consistency-darkblue" alt="Long-Term Consistency">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20352">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 AMA（Adaptive Memory via Multi-Agent Collaboration）框架，通过 Constructor、Retriever、Judge 和 Refresher 四个协作智能体来管理多粒度记忆。<br>
        • 采用了分层记忆设计（原始文本、事实知识、剧集记忆），Retriever 根据任务意图动态路由查询，Judge 负责逻辑审计和冲突检测。<br>
        • Refresher 模块通过逻辑驱动的更新维护长期记忆的一致性。在 LoCoMo 和 LongMemEval 上，AMA 在减少 80% Token 消耗的同时显著优于现有基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-27</td>
      <td style="width: 55%;"><strong>GLOVE: Global Verifier for LLM Memory-Environment Realignment</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Verification-crimson" alt="Memory Verification">
        <img src="https://img.shields.io/badge/Environment%20Adaptation-forestgreen" alt="Environment Adaptation">
        <img src="https://img.shields.io/badge/Active%20Probing-darkcyan" alt="Active Probing">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.19249">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Global Verifier (GLOVE) 框架，旨在解决动态环境漂移导致的记忆-环境失准问题。<br>
        • 通过主动探测（Active Probing）建立“相对真理”，通过对比检索到的记忆与新观察结果来检测认知失调，并在无真值监督的情况下重新对齐记忆。<br>
        • 在 Web 导航、离散规划和连续控制任务中，GLOVE 显著提高了智能体在环境结构或逻辑发生显式/隐式漂移时的适应能力和成功率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-26</td>
      <td style="width: 55%;"><strong>MemWeaver: Weaving Hybrid Memories for Traceable Long-Horizon Agentic Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Hybrid%20Memory-darkslateblue" alt="Hybrid Memory">
        <img src="https://img.shields.io/badge/Knowledge%20Graph-teal" alt="Knowledge Graph">
        <img src="https://img.shields.io/badge/Traceability-maroon" alt="Traceability">
        <img src="https://img.shields.io/badge/Long--Horizon%20Agent-indigo" alt="Long-Horizon Agent">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.18204">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemWeaver 提出了一个三层混合记忆框架（图记忆、经验记忆、段落记忆），将长期交互整合为具备时间感知和证据可溯源的结构化信息。<br>
        • 该模型采用双通道检索策略，将结构化的关系事实与原始文本证据“编织”在一起，有效支持复杂的多跳推理和时间推理任务。<br>
        • LoCoMo 基准测试表明，相比长上下文基线模型，它在提升推理准确率的同时，将输入上下文长度减少了 95% 以上。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-26</td>
      <td style="width: 55%;"><strong>FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Biologically--Inspired-lightgreen" alt="Biologically-Inspired">
        <img src="https://img.shields.io/badge/Forgetting%20Mechanism-gray" alt="Forgetting Mechanism">
        <img src="https://img.shields.io/badge/Memory%20Management-steelblue" alt="Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.18642">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 FadeMem，一种受艾宾浩斯遗忘曲线启发的智能体记忆架构，引入了主动遗忘机制以防止信息过载。<br>
        • 采用了双层记忆层级（长期与短期），利用基于语义相关性、访问频率和时间模式的自适应指数衰减函数来管理记忆保留。<br>
        • 结合 LLM 引导的冲突解决和记忆融合，FadeMem 在 Multi-Session Chat 和 LoCoMo 上以减少 45% 的存储空间实现了卓越的多跳推理和检索性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-24</td>
      <td style="width: 55%;"><strong>Clustering-driven Memory Compression for On-device Large Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/On--Device-black" alt="On-Device">
        <img src="https://img.shields.io/badge/Memory%20Compression-lightgrey" alt="Memory Compression">
        <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.17443">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了一种基于聚类的记忆压缩策略，专为端侧 LLM 的个性化设计，以应对有限的上下文窗口。<br>
        • 方法将相似的记忆分组，并在簇内合并记忆（而非简单的拼接或平均），从而在减少冗余的同时保留语义连贯性。<br>
        • 实验表明，该方法在严格的上下文限制下显著降低了 Token 使用量，并在个性化生成质量上优于简单的拼接或平均基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-15</td>
      <td style="width: 55%;"><strong>TeleMem: Building Long-Term and Multimodal Memory for Agentic AI</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06037">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • TeleMem 引入了统一的长期和多模态记忆框架，通过提取叙事基础信息来维护连贯的用户画像，避免模式驱动的幻觉。<br>
          • 它采用结构化写入管道进行批处理、检索和整合，显著提升存储和 Token 效率，并集成了具有 ReAct 风格推理的多模态记忆模块用于视频理解。<br>
          • 在 ZH-4O 基准测试上的实验结果表明，TeleMem 在准确率上比 SOTA Mem0 基线提升 19%，同时减少 43% 的 Token 使用量并将操作速度提升 2.1 倍。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-15</td>
      <td style="width: 55%;"><strong>Grounding Agent Memory in Contextual Intent</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.10702">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了 STITCH，一种智能体记忆系统，使用"上下文意图"（包含主题范围、事件类型和关键实体类型）来索引轨迹步骤，以消除长周期任务中重复信息的歧义。<br>
          • 引入了一种检索机制，基于结构意图兼容性而非仅语义相似性来过滤和优先排序记忆片段，有效抑制上下文不兼容的历史信息。<br>
          • 提出了 CAME-Bench，一个多领域基准测试，旨在评估真实目标导向轨迹中的上下文感知检索能力，STITCH 在该基准上取得了 SOTA 性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;"><strong>PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.09636">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 PersonalAlign，一项新任务，要求 GUI 智能体通过利用长期用户记录来对齐隐式用户意图——特别是解析模糊指令和预测用户习惯。<br>
        • 提出了 AndroidIntent，一个基于 2 万条长期记录构建的基准测试，包含分层标注的用户偏好和习惯，用于评估个性化能力。<br>
        • 提出了 HIM-Agent（层级意图记忆智能体），利用流式聚合模块和层级过滤器（基于执行和状态）持续更新和组织用户记忆，以提升响应式和主动式性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-13</td>
      <td style="width: 55%;"><strong>Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Lightweight-lightyellow" alt="Lightweight">
        <img src="https://img.shields.io/badge/Dynamic%20Evolution-orange" alt="Dynamic Evolution">
        <img src="https://img.shields.io/badge/Reasoning-blue" alt="Reasoning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.14287">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 CoM (Chain-of-Memory) 框架，主张从昂贵的结构化记忆构建转向轻量级构建（Flat Index）与复杂的动态利用。<br>
        • 引入了动态记忆链演化机制（Dynamic Memory Chain Evolution），将检索到的碎片组织成连贯的推理路径，并利用自适应截断修剪无关噪声。<br>
        • 在 LongMemEval 和 LoCoMo 上，CoM 相比复杂记忆结构将 Token 消耗降低至约 2.7%，同时实现了 7.5%–10.4% 的准确率提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-13</td>
      <td style="width: 55%;"><strong>AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.08323">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 AtomMem，一种动态记忆框架，将智能体记忆管理重新定义为可学习的序列决策问题，而非静态的手工设计流程。<br>
        • 将记忆过程解构为原子级 CRUD（创建、读取、更新、删除）操作，并使用强化学习（GRPO）学习任务对齐的策略来自主编排这些操作。<br>
        • 在长上下文基准测试（HotpotQA、2WikiMultihopQA、Musique）上的实验结果表明，AtomMem 通过动态调整记忆策略以适应特定任务需求，持续优于静态记忆基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-13</td>
      <td style="width: 55%;"><strong>Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.08435">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • Fine-Mem 是一个统一的强化学习框架，旨在通过将细粒度反馈与记忆操作对齐来优化 LLM 智能体的长周期记忆管理。<br>
          • 它通过分块级步骤奖励（CSR）解决奖励稀疏问题（通过构建 QA 任务提供即时监督），并通过证据锚定奖励归因（EARA）解决信用分配问题（将全局奖励与特定记忆操作关联）。<br>
          • 实验结果表明，Fine-Mem 在 Memalpha 和 MemoryAgentBench 等基准测试上持续优于强基线，展现了在不同模型间的优越适应性和泛化能力。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-12</td>
      <td style="width: 55%;"><strong>Active Context Compression: Autonomous Memory Management in LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Context%20Compression-purple" alt="Context Compression">
        <img src="https://img.shields.io/badge/Memory%20Management-red" alt="Memory Management">
        <img src="https://img.shields.io/badge/Autonomous-success" alt="Autonomous">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.07190">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将“上下文压缩”视为主动决策问题：在有限上下文预算下，智能体需要自主决定保留/总结/外置/丢弃哪些信息。<br>
        • 提出自动化的记忆管理策略，减少被动截断导致的关键信息丢失与长期任务退化。<br>
        • 在长时程或多轮任务中验证：主动压缩可在更小上下文开销下维持更好的任务表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-12</td>
      <td style="width: 55%;"><strong>MemoBrain: Executive Memory as an Agentic Brain for Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.08079">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemoBrain 为工具增强型智能体引入了"执行记忆"范式，作为协同驾驶员构建依赖感知记忆并在有限预算下主动管理上下文。<br>
          • 该框架采用特定的记忆操作——轨迹折叠和选择性刷新——来组织推理进度，保留高显著性的结构骨架同时丢弃临时执行产物。<br>
          • 在 GAIA、WebWalker 和 BrowseComp-Plus 等基准测试上的实验表明，MemoBrain 通过实现长周期内连贯的目标导向推理，持续优于强基线。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-12</td>
      <td style="width: 55%;"><strong>Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.07468">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • TSM 是一种记忆框架，为点状记忆建模语义时间，并支持持续性记忆的构建与利用。<br>
          • 它构建语义时间线来组织情景交互，并将其整合为时间感知的持续性记忆（主题和画像），以捕捉长期用户状态。<br>
          • 在记忆利用过程中，TSM 结合查询的时间意图来检索时间适当的持续性记忆，在 LongMemEval 和 LoCoMo 等基准测试上显著提升了性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-10</td>
      <td style="width: 55%;"><strong>Bi-Mem: Bidirectional Construction of Hierarchical Memory for Personalized LLMs via Inductive-Reflective Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Hierarchical%20Memory-darkgreen" alt="Hierarchical Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06490">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • Bi-Mem 是一个智能体框架，使用归纳智能体进行自下而上的聚合和反思智能体进行自上而下的校准，双向构建层级记忆（事实、场景、画像），以减少噪声和幻觉。<br>
          • 它采用关联检索机制，利用扩散激活连接跨粒度的记忆单元，实现上下文场景和特定事实的连贯回忆。<br>
          • 在 LoCoMo 基准测试上的实证评估表明，Bi-Mem 在长期个性化对话任务中显著优于领先的记忆基线。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-10</td>
      <td style="width: 55%;"><strong>HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Hierarchical%20Memory-darkgreen" alt="Hierarchical Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06377">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • HiMem 是一种为长周期对话设计的层级长期记忆框架，将细粒度的"情景记忆"（通过主题感知分割）与抽象的"笔记记忆"（通过知识提取）相结合，以桥接具体事件和稳定知识。<br>
          • 它采用冲突感知的"记忆再巩固"机制，利用检索反馈来修订和补充存储的知识，实现记忆随时间的持续自我演化和纠正。<br>
          • 在长周期基准测试上的评估表明，HiMem 在准确性、一致性和推理方面优于基线，验证了其层级组织和动态更新策略的有效性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-10</td>
      <td style="width: 55%;"><strong>Structured Episodic Event Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Hybrid%20Memory-darkcyan" alt="Hybrid Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06411">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • SEEM 引入了双层记忆框架，结合用于静态事实的图记忆层和用于叙事进展的情景记忆层，两者都通过来源指针锚定到原始交互段落。<br>
          • 该系统采用"反向来源扩展"（RPE）机制，在检索过程中从碎片化证据重建连贯的叙事上下文，解决了长期交互中的"分散检索"问题。<br>
          • 在 LoCoMo 和 LongMemEval 等基准测试上的实验表明，SEEM 在叙事连贯性和逻辑一致性方面显著优于竞争性的记忆增强基线（如 HippoRAG 2）。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-09</td>
      <td style="width: 55%;"><strong>MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.05488">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemBuilder 是一个强化学习框架，训练 LLM 主动构建和管理多维记忆系统（核心、情景、语义和程序记忆），而非依赖静态提示。<br>
          • 它引入"归因密集奖励策略优化"（ADRPO）来解决奖励稀疏和信用分配问题，通过合成会话级 QA 提供即时反馈，并基于记忆组件贡献进行梯度加权。<br>
          • 实验结果表明，使用 MemBuilder 训练的轻量级 4B 模型在 LoCoMo 和 LongMemEval 等长期对话基准测试上超越了 SOTA 闭源模型（包括 Claude 4.5 Sonnet）。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-08</td>
      <td style="width: 55%;"><strong>Beyond Static Summarization: Proactive Memory Extraction for LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Proactive%20Extraction-mediumseagreen" alt="Proactive Extraction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.04463">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>ProMem 框架</strong>：针对现有静态摘要记忆“一次性”和“无反馈”的缺陷，提出了一种基于循环处理理论（RPT）的主动记忆提取框架。<br>
        • <strong>循环验证机制</strong>：引入“自我提问-验证”反馈回路，让智能体主动回顾原始对话以纠正幻觉并补全缺失细节，而非盲目地进行前馈式摘要。<br>
        • <strong>性能表现</strong>：在 HaluMem 和 LongMemEval 基准测试中显著优于 Mem0 和 LightMem，且在 Token 高压缩率和小模型（SLM）场景下仍保持鲁棒性。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-08</td>
      <td style="width: 55%;"><strong>Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.04726">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 <strong>CompassMem</strong>，一种受事件分割理论启发的以事件为中心的记忆框架，将记忆组织为通过显式逻辑关系（因果、时序）连接的 <strong>事件图（Event Graph）</strong>。<br>
        • 将记忆从被动存储转化为 <strong>逻辑地图（Logic Map）</strong>，通过“规划器-探索者-响应者”机制支持智能体在结构化依赖中主动导航。<br>
        • 引入主动多路径记忆搜索机制，根据子目标满足情况动态扩展或跳过节点，避免无效检索。<br>
        • 在 LoCoMo 和 NarrativeQA 基准测试上表现优异，特别是在多跳和时序推理任务上显著超越了 HippoRAG 和 Mem0 等基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-08</td>
      <td style="width: 55%;"><strong>Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.05171">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>PersonaTree 框架</strong>：提出了一种基于生物心理社会模型的全局用户画像树（PersonaTree），通过约束主干 Schema 并动态更新枝叶，实现记忆的可控生长与压缩，有效解决了长程对话中的噪声积累问题。<br>
        • <strong>MemListener 与 RL 训练</strong>：利用基于过程奖励的强化学习（Process-Reward RL）训练轻量级模型 MemListener，使其能将非结构化对话流转化为结构化的 {ADD, UPDATE, DELETE} 树操作，决策性能媲美强推理模型。<br>
        • <strong>自适应推理机制</strong>：设计了双模式推理策略，延迟敏感场景下直接利用 PersonaTree 增强生成，长尾细节需求下触发 Agentic 模式利用树结构引导深度检索，显著提升了角色一致性。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-07</td>
      <td style="width: 55%;"><strong>Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03785">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>Membox 架构</strong>：针对现有记忆系统“碎片化-补偿”范式的缺陷，提出以**话题连续性**为核心的分层架构，旨在保留对话的时间和因果流。<br>
        • <strong>Topic Loom 与 Trace Weaver</strong>：利用滑动窗口机制（Topic Loom）将连续对话打包成“记忆盒”，并通过 Trace Weaver 将这些盒子编织成跨越不连续时间的长程事件线索。<br>
        • <strong>性能提升</strong>：在 LoCoMo 基准测试中，时间推理任务的 F1 分数比 Mem0 和 A-MEM 提升高达 68%，同时显著降低了 Token 消耗，实现了效率与效果的平衡。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>HiMeS: Hippocampus-inspired Memory System for Personalized AI Assistants</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06152">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • HiMeS 是一种面向 AI 助手的记忆框架，通过整合短期对话压缩与长期用户画像存储来模拟海马体-新皮层交互。<br>
          • 它利用通过强化学习训练的短期记忆提取器进行主动预检索知识，并使用分区长期记忆网络基于历史用户交互重新排序结果。<br>
          • 在真实工业数据集上的评估表明，HiMeS 在个性化问答任务中显著优于传统 RAG 基线。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>SYNAPSE: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.02744">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SYNAPSE 是一种受脑启发的记忆架构，通过构建“统一情景-语义图”取代静态向量检索，解决了传统 RAG 无法关联语义距离远但因果相关记忆的“上下文孤立”问题。<br>
        • 它引入了扩散激活（Spreading Activation）、侧向抑制和时间衰减等认知动力学机制，在图中动态传播相关性并过滤噪声，而非仅依赖预计算链接或向量相似度。<br>
        • 在 LoCoMo 基准测试中取得 SOTA，通过不确定性门控机制显著提升了多跳推理能力和对抗性查询的鲁棒性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>CODEMEM: AST-Guided Adaptive Memory for Repository-Level Iterative Code Generation</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.02868">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了CODEMEM，一种专为仓库级迭代代码生成设计的内存管理系统。<br>
        • 引入<strong>代码上下文记忆（Code Context Memory）</strong>：利用AST引导的选择机制动态更新和合并仓库上下文，保持其相关性并过滤噪声。<br>
        • 引入<strong>代码会话记忆（Code Session Memory）</strong>：通过基于AST的变更分析来检测冲突和遗忘，将历史交互组织为以代码为中心的单元（Diffs），而非纯文本。<br>
        • 在CodeIF-Bench和CoderEval上取得SOTA，指令遵循能力提升约12%，并减少了2-3轮交互。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>Implicit Graph, Explicit Retrieval: Towards Efficient and Interpretable Long-horizon Memory for Large Language Models</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03417">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>LatentGraphMem 框架</strong>：提出了一种结合隐式图记忆和显式子图检索的记忆框架，通过在潜在空间存储图结构记忆以提高稳定性和效率，同时提供任务特定的显式子图检索以增强可解释性。<br>
        • <strong>三阶段训练策略</strong>：包含图构建器训练（构建全局图表示）、子图检索器训练（在固定预算下选择相关边）和联合微调（优化构建器和检索器的协作），实现了高效的端到端问答。<br>
        • <strong>实验验证</strong>：在 HotpotQA、NarrativeQA 和 WikiHop 等长程基准测试中，LatentGraphMem 在不同模型规模下均优于现有的显式图和隐式记忆基线，平均准确率最高提升至 63.34%。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03236">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>MAGMA 架构</strong>：提出了一种基于多图的智能体记忆架构，通过语义、时间、因果和实体四个正交的关系图来明确建模记忆项，解决了传统单体记忆库中信息纠缠的问题。<br>
        • <strong>自适应拓扑检索</strong>：引入了基于意图的自适应遍历策略，根据查询意图动态选择相关的关系视图进行遍历，将记忆表示与检索逻辑解耦，实现了透明的推理路径。<br>
        • <strong>性能表现</strong>：在 LoCoMo 和 LongMemEval 等长程基准测试中，MAGMA 优于现有的 SOTA 智能体记忆系统（如 Nemori、A-MEM），同时显著降低了检索延迟和 Token 消耗。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.02845">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>TiMem 框架</strong>：提出了一种基于时间记忆树（TMT）的时间-层级记忆框架，将对话从原始片段逐步整合为抽象的画像表示，强调时间连续性。<br>
        • <strong>核心机制</strong>：包含语义引导的记忆整合（无需微调）和复杂度感知的记忆召回机制（召回规划器+门控），在不同查询复杂度下平衡精度与效率。<br>
        • <strong>实验表现</strong>：在 LoCoMo 和 LongMemEval-S 长程基准测试中均取得 SOTA（准确率分别为 75.30% 和 76.88%），同时在 LoCoMo 上显著降低了召回上下文长度（-52.20%）。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-06</td>
      <td style="width: 55%;"><strong>MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03192">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>MemRL 框架</strong>：提出了一个基于非参数化强化学习的框架，允许冻结权重的 LLM 智能体通过优化情景记忆来“自我进化”，解决了微调带来的遗忘问题和计算成本。<br>
        • <strong>意图-经验-效用三元组</strong>：引入双阶段检索机制（语义召回 + 价值感知选择）和运行时效用更新规则，利用 Q 值估计来区分高价值策略与语义相似的噪声。<br>
        • <strong>实验表现</strong>：在 HLE、BigCodeBench 和 ALFWorld 等基准测试中显著优于 MemP 和 RAG，证明了在不更新模型权重的情况下，智能体可以通过运行时试错持续提升能力。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-05</td>
      <td style="width: 55%;"><strong>SimpleMem: Efficient Lifelong Memory for LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.02553">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了SimpleMem，一种基于语义无损压缩的、专为终身LLM智能体设计的高效记忆框架。<br>
        • 该系统通过三阶段流水线运行：语义结构化压缩以过滤低熵噪声，递归记忆整合以合成抽象表征，以及自适应查询感知检索以最小化Token使用。<br>
        • 在LoCoMo基准上的实验表明，与全上下文模型相比，F1分数提高了26.4%，推理Token消耗减少了高达30倍，显著优于Mem0等基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-05</td>
      <td style="width: 55%;"><strong>Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.01885">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • <strong>AgeMem 框架</strong>：提出了一种统一的智能体记忆框架，将长期记忆（LTM）和短期记忆（STM）的管理直接作为工具化动作（如增删改、摘要、过滤）整合到智能体策略中。<br>
        • <strong>三阶段渐进式 RL</strong>：为了解决记忆操作带来的奖励稀疏问题，设计了分步 GRPO 算法和三阶段训练策略（LTM构建、干扰下的STM控制、综合推理），实现端到端优化。<br>
        • <strong>实验效果</strong>：在 ALFWorld、HotpotQA 等五个长程基准测试中，AgeMem 在任务完成率、记忆质量和上下文使用效率上均显著优于 LangMem 和 Mem0 等现有基线。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-31</td>
      <td style="width: 55%;"><strong>Nested Learning: The Illusion of Deep Learning Architecture</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.24695">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • arxiv 完整版， 包括所有附录内容. 非之前公布的残血版.<br>
        • 梳理了一个Nested Leaning的学习范式, 统一了很大一部分的optimizer + TTT layer. <br>
        • 结构创新:HOPE: 由 modified Titans attention + self modified FFN 组成, 通过控制FFN层参数self-modified的更新频率， 使得不同更新频率FFN层在运行时隐式记住中不同层级的记忆.<br>
        • 试验偏弱.<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-25</td>
      <td style="width: 55%;"><strong>Beyond Heuristics: A Decision-Theoretic Framework for Agent Memory
Management</strong></td>
      <td style="width: 15%;">
       <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
       <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.21567">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • TeleAI背景， 一个理论框架(DAM)， 把记忆的读写的时机和内容的问题包装成一个决策论下的最优问题. 考虑类似RL问题的可以参考一下.<br>
        • 基本无试验.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-21</td>
      <td style="width: 55%;"><strong>MemEvolve: Meta-Evolution of Agent Memory Systems</strong></td>
      <td style="width: 15%;">
       <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
       <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.18746">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • oppo背景的文章, 通过设计双层框架在RL问题中分离记忆抽取式的学习(一层学习)和记忆抽取方式本身的学习(二层学习).<br>
        • 试验基于Flash-Searcher和GPT-5-Mini, 在包括GAIA上取得SOTA.<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-20</td>
      <td style="width: 55%;"><strong>MemR³: Memory Retrieval via Reflective Reasoning for LLM Agents</strong></td>
      <td style="width: 15%;">
       <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
       <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.20237">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemR³ 闭环检索控制器：为长期对话记忆设计，能动态选择检索、反思、回答三种动作。<br>
        • 证据-缺口状态追踪器：系统维护一个全局的 (证据, 缺口) 状态，明确追踪“已掌握什么”和“还缺什么”，使过程可解释。<br>
        • 试验显示，在LoCoMo基准测试上，MemR³能显著提升不同底层记忆系统（如RAG、Zep）的回答质量。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-18</td>
      <td style="width: 55%;"><strong>Learning Hierarchical Procedural Memory for LLM Agents
through Bayesian Selection and Contrastive Refinement</strong></td>
      <td style="width: 15%;">
       <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.18950">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 基于贝叶斯的程序记忆(经验)框架:MACLA.<br>
        • 整体仍然是一个基于规则的算法，操作包括提取，检索存储，精炼(贝叶斯后验概率校准).<br>
        • 在ALFWorld的未见任务上，性能（90.3%）反而比已见任务（87.2%）更高，实现了+3.1%的正泛化。<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-14</td>
      <td style="width: 55%;"><strong>HINDSIGHT IS 20/20: BUILDING AGENT MEMORY THAT RETAINS, RECALLS, AND REFLECTS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2512.12818">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • HINDSIGHT 是一种统一的记忆架构,将记忆视为结构化的、一流的推理基质,将信息组织为四个逻辑网络:世界事实、智能体经验、综合实体摘要和不断演化的信念。<br>
        • 该系统引入了 TEMPR(时序实体记忆启动检索)用于构建时序实体图,以及 CARA(连贯自适应推理智能体)用于基于偏好的条件推理,使智能体能够从认识论上区分证据和推理。<br>
        • 在 LongMemEval 和 LoCoMo 基准测试上的实验结果表明,HINDSIGHT 在多会话一致性和开放域问答方面显著优于现有记忆系统和全上下文前沿模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-11</td>
      <td style="width: 55%;"><strong>Remember Me, Refine Me: A Dynamic Procedural Memory
Framework for Experience-Driven Agent Evolution</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.10696">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • ReMe的文章版, 阿里背景的关于LLM程序记忆(经验)进行增强的框架. 包含框架算法ReMe和数据集reme.library。<br>
        • 核心是维护一个经验池，操作包括获取（Acquisition）， 重用（Reuse），精炼（Refinement）。<br>
        • BFCL-V3和AppWorld上的试验显示动态经验池好于静态经验池好于baseline, 有针对模型和judge模型的scale试验.<br>
      </td>
    </tr>
    <td rowspan="2" style="width: 15%;">2025-12-10</td>
      <td style="width: 55%;"><strong>LightSearcher: Efficient DeepSearch via Experiential Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Experiential%20Memory%20Framework-crimson" alt="Experiential Memory Framework">
      <img src="https://img.shields.io/badge/Agentic%20RL%20Optimization-orchid" alt="Agentic RL Optimization">
      <img src="https://img.shields.io/badge/Contrastive%20Trajectories%20Memory-dodgerblue" alt="Contrastive Trajectories Memory">
      </td>
      <td style="width: 15%;"><a href="https://www.arxiv.org/pdf/2512.06653">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LightSearcher是基于经验记忆的RL高效搜索架构，在大模型强化推理过程中，不依赖额外数据，通过“对比经验记忆”将隐性推理轨迹转化为显性经验指导，实现Agent搜索工具调用的自主优化。<br>
        • 在四个多跳QA基准数据集（NQ、HotpotQA、Musique、2WikiMultihopQA）上，保持与SOTA DeepSearch基线相当准确率，搜索工具调用和模型回复时间显著缩短。<br>
        • 搜索工具调用次数减少 39.6%，推理时间缩短 48.6%，Token消耗降低 21.2%，在保持模型效果的同时显著提升了工具调用效率。
      </td>
    </tr>
      <tr>
      <td rowspan="2" style="width: 15%;">2025-12-3</td>
      <td style="width: 55%;"><strong>MemVerse: Multimodal Memory for Lifelong Learning Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.03627">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 针对多模态agent的终身学习记忆框架.<br>
        • 检索式长期记忆 + 参数化快速记忆 + 定期蒸馏机制.<br>
        • 如何处理多模态: 统一转化为文本描述.<br>
        • 试验主要在ScienceQA(文本), MSR-VTT(视频)上展示了超出基线的性能，LoCoMo(文本)试验在附录中尚未没有公开.<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-12</td>
      <td style="width: 55%;"><strong>ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://ojs.aaai.org/index.php/AAAI/article/view/40644">
        <img src="https://img.shields.io/badge/AAAI-Paper-%23003087?logo=aaai" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 ComoRAG,这是一个受人类前额叶皮层启发的检索增强生成框架,旨在实现长叙事上下文中的有状态推理。<br>
          • 该框架采用动态记忆工作空间和元认知调节循环(包括自我探测、记忆融合和记忆更新),以迭代方式将碎片化的证据融合为连贯的上下文。<br>
          • 实验结果表明,ComoRAG 在 NarrativeQA 和 ∞BENCH 等具有挑战性的基准测试中持续优于强大的基线,特别是在需要全局理解的复杂叙事查询中表现出色。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-04</td>
      <td style="width: 55%;"><strong>MemSearcher Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2511.02805">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemSearcher 是一个通过端到端强化学习(RL)训练的大型语言模型(LLM)智能体,旨在提高知识获取任务的效率。<br>
          • MemSearcher 通过采用一种称为多上下文组相对策略优化(Multi-Context GRPO)的新框架来优化记忆管理,使模型能够在多个对话中自我演化。<br>
          • 与传统的 ReAct 搜索智能体相比,MemSearcher 在保持低令牌消耗的同时提供了显著的性能改进,尤其是在较小的模型上。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-15</td>
      <td style="width: 55%;"><strong>D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.13363">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 D-SMART,这是一个与模型无关的框架,旨在通过将动态结构化记忆(DSM)与推理树(RT)耦合来维持多轮对话中的逻辑和事实一致性。<br>
        • DSM 从对话历史中增量构建符合 OWL 标准的知识图谱以防止上下文衰减,而 RT 则引导 LLM 在该图谱上进行明确的、可追溯的多步推理。<br>
        • 在 MT-Bench-101 上的综合实验表明,D-SMART 显著优于最先进的基线,一致性得分提高了 48% 以上,并在扩展对话中表现出强大的稳定性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-14</td>
      <td style="width: 55%;"><strong>Memory as Action Autonomous Context Curation for Long-Horizon Agentic Tasks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.12635">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • Memory-as-action (MemAct) 解决了大型语言模型(LLM)在长期任务中的工作记忆管理问题。<br>
          • MemAct 将记忆管理转化为可学习的内在能力,使智能体能够在执行任务时动态管理记忆,并引入动态上下文策略优化(DCPO)算法来处理记忆编辑引起的轨迹断裂问题。<br>
          • MemAct 在多目标问答任务中表现出色,展示了比传统模型更高的准确性和鲁棒性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-12</td>
      <td style="width: 55%;"><strong>MemGen Weaving Generative Latent Memory for Self-Evolving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2509.24704">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemGen 是一个动态生成式记忆框架,旨在增强基于大型语言模型(LLM)的智能体的推理和决策能力。<br>
          • MemGen 通过将记忆与推理过程交织在一起来模拟人类认知模式。<br>
          • 该框架由两部分组成:记忆触发器和记忆编织器,它们可以动态决定何时调用潜在记忆并将其整合到推理过程中。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-10</td>
      <td style="width: 55%;"><strong>How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Memory%20Addition-slateblue" alt="Memory Addition">
      <img src="https://img.shields.io/badge/Memory%20Deletion-salmon" alt="Memory Deletion">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2505.16067">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 该论文研究了大型语言模型(LLM)智能体中的记忆管理及其对长期性能的影响。<br>
          • 它识别了诸如错误传播和经验重放不一致等问题,强调了高质量记忆的重要性。<br>
          • 通过比较多种记忆插入和删除策略,该研究发现选择性插入对长期学习表现更好,而历史删除在减少低质量记忆记录方面特别有效。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-09</td>
      <td style="width: 55%;"><strong>Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2510.07925v1">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了一种用于自适应、以用户为中心的 AI 智能体框架,该框架结合了持久记忆、动态协调和不断演化的用户画像,以实现个性化的长期交互。<br>
          • 该方法整合了既定的智能体 AI 模式——如多智能体协作和多源检索——以及自我验证和隐式用户画像等机制,以根据个人需求定制响应。<br>
          • 在三个公共数据集和试点用户研究上的评估表明,与标准 RAG 基线相比,在检索准确性、响应正确性和感知个性化方面都有所改进。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-08</td>
      <td style="width: 55%;"><strong>ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2510.06664">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TOOLMEM 让智能体把“使用不同工具后的表现经验”沉淀成可检索的记忆；做新任务时检索相关经验并注入上下文，从而更准地评估并选择工具。<br>
        • TOOLMEM 把每个工具的能力总结成结构化条目，交互得到任务、工具输出和质量反馈后，先检索相似记忆再用 RAG 方式合并/修正，持续更新能力库；推理时同样检索并用于质量预测或工具选择。<br>
        • 在文本生成和文生图上，对比无记忆与 few-shot 等基线；结果显示 TOOLMEM 在质量评分预测和多工具择优上整体更稳定、更好。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-07</td>
      <td style="width: 55%;"><strong>CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.05520">
      <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该论文介绍了 CAM,这是一个受让·皮亚杰理论启发的建构主义智能体记忆系统,旨在增强大型语言模型(LLM)在长文档理解方面的能力。<br>
        • CAM 具有结构化图式、灵活的同化和动态的顺应特性,利用增量重叠聚类算法实现高效的记忆发展,并采用自适应的修剪和生长策略进行检索。<br>
        • 在多个基准测试的实验结果表明,与现有的结构化和非结构化记忆方法相比,CAM 在性能和效率方面都实现了双重优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-30</td>
      <td style="width: 55%;"><strong>MEM-α: LEARNING MEMORY CONSTRUCTION VIA REINFORCEMENT LEARNING</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2509.25911">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了 Mem-α,这是一个强化学习框架,通过交互和反馈训练智能体有效管理复杂的记忆系统(包括核心记忆、情景记忆和语义记忆组件)。<br>
          • 与依赖预定义指令的方法不同,Mem-α 将记忆构建视为序列决策问题,直接优化下游问答准确性。<br>
          • 实验结果表明,Mem-α 显著优于现有基线,并展示了卓越的泛化能力,尽管仅在 30k 令牌序列上训练,却能有效处理超过 400k 令牌的上下文。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-29</td>
      <td style="width: 55%;"><strong>ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
        <i<img src="https://img.shields.io/badge/Memory%20Addition-slateblue" alt="Memory Addition">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2509.25140">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • ReasoningBank 把智能体在测试阶段做任务时产生的成功/失败轨迹“提炼成可复用的推理记忆”，新任务来时检索相关记忆来指导决策，并把新经验再写回形成闭环，从而在无真值反馈的 test-time learning 场景里持续变强。<br>
        • 每条记忆被压缩成结构化 memory item，通过 embedding 相似度检索 top-k 注入系统指令；任务完成后用 LLM-as-a-judge 给轨迹打“成功/失败”代理信号：成功轨迹抽取可迁移策略，失败轨迹抽取陷阱与防错护栏，最后用“直接追加”的轻量方式写入库。同时提出 MaTTS：并行扩展用多条轨迹做 self-contrast 以筛掉伪解、提炼稳定规律；串行扩展用自我反思/自我修正把中间推理也转成记忆信号。<br>
        • 在 WebArena、Mind2Web和 SWE-Bench-Verified上，对比 No Memory、Synapse、AWM 等基线；WebArena 用 BrowserGym 环境、每题最多 30 步，并用成功率与平均步数等衡量效果与效率。结果显示 ReasoningBank 在多种 backbone 上整体更好。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-29</td>
      <td style="width: 55%;"><strong>Pretraining with hierarchical memories: separating long-tail and common knowledge</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2510.02375">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了一种"带记忆的预训练"架构,将推理能力(锚定模型)与长尾世界知识(分层记忆库)解耦。<br>
        • 该系统在推理过程中动态检索并将上下文相关的参数块从大规模记忆库附加到小型锚定模型上,实现了高效的扩展。<br>
        • 实验表明,一个经记忆增强的 160M 模型可以匹配参数量超过两倍的标准模型的性能,特别是在长尾知识任务中表现出色。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-27</td>
      <td style="width: 55%;"><strong>Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Revisitable%20Memory-purple" alt="Revisitable Memory">
        <img src="https://img.shields.io/badge/Long%20Context-red" alt="Long Context">
        <img src="https://img.shields.io/badge/Reasoning-success" alt="Reasoning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2509.23040">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 聚焦超长上下文场景中“证据分散且可错过”的问题，强调 agent 需要可回访（revisit）的记忆机制。<br>
        • 提出 revisitable memory：允许在推理过程中回看历史片段并二次检索/重聚合，减少一次性读取的遗漏风险。<br>
        • 在长上下文 QA/推理任务上展示更好的证据召回与推理稳定性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-26</td>
      <td style="width: 55%;"><strong>Conflict-Aware Soft Prompting for Retrieval-Augmented Generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Retrieval%20Augmented%20Generation-blue" alt="Retrieval Augmented Generation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2508.15253">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • "冲突感知检索增强生成"(CARE)模型旨在解决检索增强生成(RAG)中出现的上下文-记忆冲突问题。<br>
          • CARE 通过引入上下文评估器来优化大型语言模型(LLM)的性能,特别是在处理外部知识和内部知识之间的冲突时。<br>
          • 该方法通过冲突感知微调、软提示和对抗性软提示等技术,显著增强了模型在多个任务中的准确性和可靠性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-26</td>
      <td style="width: 55%;"><strong>PRIME Planning and Retrieval-Integrated Memory for Enhanced Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2509.22315">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • PRIME 是一个多智能体推理框架。PRIME 通过快速响应智能体为简单问题提供直观答案。<br>
          • PRIME 通过多个特定智能体(如记忆、规划、搜索和阅读智能体)执行复杂推理。<br>
          • PRIME 仍需要改进其信念纠正机制并优化智能体之间的交互。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-25</td>
      <td style="width: 55%;"><strong>SGMEM: Sentence Graph Memory for Long-Term Conversational Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2509.21212">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • SGMem 是一个分层记忆管理框架,旨在通过将对话组织为句子级图谱来解决长期对话智能体中的记忆碎片化问题。<br>
        • 它显式地建模跨轮次、回合和会话的关联,并使用多跳检索机制将原始对话历史与生成的记忆(如摘要、事实和洞察)整合在一起。<br>
        • 在 LongMemEval 和 LoCoMo 基准测试上的大量实验表明,SGMem 持续改进检索连贯性,并在问答准确性方面优于强大的基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-22</td>
      <td style="width: 55%;"><strong>PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Mechanisms-lime" alt="Long-Term Memory Mechanisms">
      </td>
      <td style="width: 15%;">
        <a href="https://aclanthology.org/2025.findings-emnlp.1164.pdf">
        <img src="https://img.shields.io/badge/EMNLP%20Findings-Paper-black?labelColor=green" alt="EMNLP Findings Paper">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • PRINCIPLES 用离线 self-play 自动“总结可检索的对话策略原则”，在推理时按当前情境检索并注入这些原则来指导策略选择与回复生成，无需额外训练。<br>
        • 离线阶段：模拟多轮对话并用奖励判断“成功/失败”；成功则从对话中抽取原则，失败则生成并修订策略、回到失败前重试直到成功，再从“失败→成功”的对比中抽取形如 should… rather than… because… 的原则。在线阶段：用情境检索 top-k 原则，再做一次“重解释”让原则更贴合当前对话，最后据此规划策略并生成回复。<br>
        • 在情感支持与劝服任务上评测，指标含成功率/轮次，以及策略预测 F1 与熵。结果整体提升成功率与策略匹配度，并提高策略分布熵；消融显示检索与重解释是关键，人评也在多个维度偏好 PRINCIPLES。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-16</td>
      <td style="width: 55%;"><strong>WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/System-darkblue" alt="System">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2509.13312">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 WebWeaver,这是一个由规划器和写作器组成的双智能体框架,旨在通过模拟人类研究过程来解决开放式深度研究(OEDR)问题。<br>
        • 规划器使用动态循环将证据获取与大纲优化交织在一起,构建证据记忆库;写作器执行分层的、基于引用的检索,逐节撰写报告。<br>
        • WebWeaver 通过有效管理长上下文并通过有针对性的记忆检索缓解幻觉,在 DeepResearch Bench 等基准测试上实现了最先进的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-15</td>
      <td style="width: 55%;"><strong>MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Forgetting%20Strategies-darkmagenta" alt="Forgetting Strategies">
      <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2509.11860">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • MOOM 是一个为超长角色扮演对话设计的双分支记忆提取框架,将"情节发展"和"角色刻画"建模为核心叙事元素。<br>
          • 它融合了基于"竞争-抑制"理论的新颖遗忘机制,以有效控制记忆容量并防止不受控制的扩展。<br>
          • 作者引入了 ZH-4O,这是一个大规模的中文角色扮演数据集,平均包含 600 轮对话和手动记忆标注,展示了 MOOM 相对于最先进方法的卓越性能。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2025-09-13</td>
      <td style="width: 55%;"><strong>Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2509.10852">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • PREMem(情景记忆的预存储推理)是一种新颖的方法,将复杂的推理过程从响应生成阶段转移到记忆构建阶段。<br>
        • 它提取细粒度的记忆片段(分为事实、经验和主观信息),并基于认知图式理论建立显式的跨会话关系,捕获扩展和转换等演化模式。<br>
        • 在 LongMemEval 和 LoCoMo 基准测试上的实验显示了显著的性能改进,使较小的模型能够达到与较大基线相当的结果,同时减少了推理计算需求。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-11</td>
      <td style="width: 55%;"><strong>OpenUnlearning:Accelerating LLM unlearning via unified benchmarking of methods and metrics</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2506.12618">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了"OpenUnlearning"框架,旨在推进大型语言模型(LLM)中反学习的研究。<br>
          • OpenUnlearning 整合了广泛的反学习算法和评估方法,简化了研究遗忘的工作流程。<br>
          • 通过有针对性的和特定任务的评估,OpenUnlearning 确保了反学习评估标准的可信度和鲁棒性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-27</td>
      <td style="width: 55%;"><strong>Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2508.19828v4">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Memory-R1 是一个由强化学习驱动的框架,通过两个专门的智能体使 LLM 能够主动管理和利用外部记忆:记忆管理器和回答智能体。<br>
          • 记忆管理器学习结构化操作(添加、更新、删除)来维护记忆,而回答智能体则过滤检索到的记忆以进行准确推理。<br>
          • 仅使用 152 个训练样本,它就在 LoCoMo、MSC 和 LongMemEval 上优于强大的基线,展示了高数据效率和泛化能力。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-26</td>
      <td style="width: 55%;"><strong>MemoryVLA Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Memory%20Aware-purple" alt="Memory Aware">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2508.19236">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemoryVLA 是一个新开发的机器人操作框架,旨在通过整合视觉、语言和感知-认知机制来增强机器人在复杂任务中的性能。<br>
          • 该框架采用类似于人类双重记忆系统的架构,增强了机器人处理长序列任务的能力。<br>
          • MemoryVLA 引入了感知-认知记忆库(PCMB),可以有效地将历史信息与当前决策整合在一起,从而提高机器人应对复杂场景的成功率。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-22</td>
      <td style="width: 55%;"><strong>Memento: Fine-tuning LLM Agents without Fine-tuning LLMs</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Tuning-purple" alt="Agent Tuning">
        <img src="https://img.shields.io/badge/Frozen%20LLM-red" alt="Frozen LLM">
        <img src="https://img.shields.io/badge/Adaptation-success" alt="Adaptation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2508.16153">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探索“不微调底座 LLM、只在 agent 层面学习”的路线，面向工具链/记忆/路由/策略等组件做适配。<br>
        • 强调可控性与工程可落地：将学习能力放在可替换模块上，降低模型微调成本与部署复杂度。<br>
        • 在多种 agent 任务上展示：无需改动 LLM 权重也能获得显著提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-21</td>
      <td style="width: 55%;"><strong>Multiple Memory Systems for Enhancing the Long-term Memory of Agent</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2508.15294">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了一个受认知心理学启发的多重记忆系统(MMS),以解决现有智能体记忆模块中低质量记忆内容的问题。<br>
          • 该系统将短期记忆处理为多样化的片段——关键词、认知视角、情景记忆和语义记忆——以构建专门的检索和上下文记忆单元。<br>
          • 在 LoCoMo 数据集上的实验结果表明,MMS 显著优于 MemoryBank 和 A-MEM 等方法,特别是在多跳推理和开放域任务中。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-18</td>
      <td style="width: 55%;"><strong>Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Hybrid%20Memory-darkcyan" alt="Hybrid Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2508.12630v1">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 语义锚定是一种混合智能体记忆架构,旨在通过使用句法依赖、话语关系和共指链接等显式语言线索来丰富基于向量的存储,从而增强 LLM 的长期上下文保留能力。<br>
          • 所提出的框架采用多阶段流水线,涉及依赖解析、共指消解和话语标注,以构建混合索引,允许检索系统基于语义相似性和结构性语言角色访问记忆。<br>
          • 在适应的长期对话数据集(MultiWOZ-Long 和 DialogRE-L)上的实验结果表明,语义锚定优于强大的 RAG 基线,事实召回和话语连贯性提高了多达 18%,同时保持更高的用户满意度。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-13</td>
      <td style="width: 55%;"><strong>Memp: Exploring Agent Procedural Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2508.06433">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memp 把智能体的成功经验“程序化”存成可检索的程序性记忆，让LLM在新任务中直接复用做事套路，以提升成功率并减少无效步骤。<br>
        • 框架是 Build–Retrieve–Update：把轨迹/脚本等经验构成记忆条目（Build），用任务语义构造 key 做向量检索取回相关记忆（Retrieve），并在在线执行中对记忆进行新增、筛选与纠错式更新以保证可靠性。<br>
        • 在 TravelPlanner 与 ALFWorld 上，相比 ReAct 基线，Memp 整体更高分/更高成功率、步数更少；向量检索优于随机；在线更新随任务推进带来持续增益，并展示了强记忆对弱模型的迁移提升及检索数量的边际效应。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-12</td>
      <td style="width: 55%;"><strong>Context as Memory Scene-Consistent Interactive Long Video Generation with Memory Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2506.03141">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • "上下文即记忆"通过利用历史上下文作为记忆,显著增强了长视频生成的场景一致性和记忆容量。<br>
          • 该论文研究了关键设计,如上下文学习机制、相机控制和记忆检索策略,并指出了计算效率和生成质量之间的平衡。<br>
          • 基于扩散模型的长视频生成架构,阐述了当前的技术进展、挑战和未来方向。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-12</td>
      <td style="width: 55%;"><strong>Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2508.08997">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了内在记忆智能体,这是一个多智能体框架,旨在使用结构化的、特定于智能体的记忆来解决上下文限制和角色不一致问题。<br>
          • 该方法采用角色对齐的记忆模板和直接从智能体输出派生的内在更新,在没有外部摘要的情况下保留了异构视角和领域专业知识。<br>
          • 在 PDDL 基准测试上的评估显示性能提高了 38.6%,同时具有高令牌效率,而案例研究显示在复杂规划任务中质量得到增强。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-06</td>
      <td style="width: 55%;"><strong>RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2508.04903">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • RCR-Router 是一个角色感知的上下文路由框架,为多智能体 LLM 系统设计,以解决静态和全上下文路由的限制,如过度的令牌消耗和冗余的记忆暴露。<br>
        • 该框架根据每个智能体的特定角色和当前任务阶段动态选择语义相关的记忆子集,执行严格的令牌预算,并利用迭代反馈机制来优化上下文。<br>
        • 在多跳问答基准测试(HotPotQA、MuSiQue、2WikiMultihop)上的实验表明,与基线策略相比,RCR-Router 将令牌使用量减少了 25-47%,同时保持或提高了答案质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-03</td>
      <td style="width: 55%;"><strong>MLP Memory: A Retriever-Pretrained Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2508.01832">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 MLP Memory,这是一个轻量级的参数化模块,学习将检索模式内化,而无需在推理过程中显式访问文档,有效地弥合了 RAG 和参数化微调之间的差距。<br>
        • 通过预训练 MLP 来模仿 kNN 检索器在整个预训练数据集上的行为,该模型将大型数据存储压缩为可微分的记忆组件,通过概率插值与 Transformer 解码器集成。<br>
        • 实验结果表明,MLP Memory 实现了卓越的扩展行为,相对于基线将问答性能提高了 12.3%,减少了多达 10 个点的幻觉,并且推理速度比 RAG 快 2.5 倍。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-29</td>
      <td style="width: 55%;"><strong>SynapticRAG:Enhancing temporal memory retrieval in large language models through synaptic mechanisms</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Memory%20Addition-slateblue" alt="Memory Addition">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2507.21428">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 论文提出 MemTool，用于在多轮对话中管理不断变化的工具集合（MCP servers）的短期记忆框架，提供 Autonomous / Workflow / Hybrid 三种架构，以在自治性与可控性之间权衡。<br>
        • Autonomous 模式下，智能体通过 Search_Tools 与 Remove_Tools 自主增删工具；Workflow 模式采用固定流程：先剪枝删工具，再检索加工具；Hybrid 模式将删工具独立出来，同时保留智能体通过 Search_Tools 加工具的能力，实现稳定与灵活的折中。<br>
        • 基于 ScaleMCP 的 5000 个 MCP servers 构造 100 轮工具使用对话（约 5 次工具调用/轮），评测 13 个 LLM，并设定 128 工具上限。结果显示：Autonomous 在强推理模型上工具移除效率可达 90–94%，中等模型可降至 0–60%；Workflow 与 Hybrid 的工具移除更稳定，而任务完成度通常是 Autonomous 与 Hybrid 更好。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>SynapticRAG:Enhancing temporal memory retrieval in large language models through synaptic mechanisms</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Cross--Memory%20Retrieval-orchid" alt="Cross-Memory Retrieval">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.1048.pdf">
      <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • SynapticRAG 是一个用于大型语言模型(LLM)的新颖记忆检索框架,旨在增强跨会话对话中的记忆检索。<br>
          • 通过将时间关联触发器与受生物学启发的突触传播机制相结合,SynapticRAG 显著改进了相关对话历史的识别。<br>
          • 实验结果表明,该框架在多个性能指标上实现了高达 14.66% 的改进,并在动态记忆管理方面展示了明显的优势。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-17</td>
      <td style="width: 55%;"><strong>MEM1 Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2506.15841">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MEM1 是一个创新的端到端强化学习框架,旨在提高大型语言模型(LLM)在长期多轮交互中的效率。<br>
          • MEM1 通过构建紧凑的共享内部状态,有效解决了传统模型上下文处理中的记忆膨胀问题。<br>
          • 实验结果表明,MEM1 在多个任务中显著提高了性能,同时减少了记忆使用,展示了其在动态环境中的广泛适用性和优化潜力。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-03</td>
        <td style="width: 55%;"><strong>MemAgent Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2507.02259">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
        </td>
    </tr>
    <tr>
        <td colspan="3">
          • MemAgent 是一种使用强化学习(RL)动态更新记忆的长文本处理方法,旨在解决大型语言模型(LLM)在处理长文本时的性能下降和高计算复杂性问题。<br>
          • 该模型通过将记忆视为潜在变量并引入流处理和多会话策略,在处理无限长度的输入时可以保持线性时间复杂度。<br>
          • 实验结果表明,MemAgent 在超长文本任务中表现出色,具有高准确性,特别是在复杂的多跳推理任务中具有明显优势。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-06-19</td>
      <td style="width: 55%;"><strong>From RAG to Memory: Non-Parametric Continual Learning for Large Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2502.14802">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • HippoRAG 2，是一种“类人长期记忆”的结构化 RAG：把文本抽成三元组建图，用图上的扩散式检索（PPR）做多跳联想，同时补齐传统结构化RAG在“基础事实记忆”上的短板。<br>
        • 离线用 LLM 做 OpenIE 抽取三元组建 KG，并把段落作为 passage node接入图，实现“概念—语境”融合；在线检索时先用向量召回 top-k 三元组，再让 LLM 做 triple filtering 去掉无关三元组，然后以过滤后的节点作为种子跑 PPR，输出最相关段落供生成器回答。<br>
        • 在事实问答、多跳推理与叙事理解等数据集上评测，用 Recall@5 衡量检索、用 F1 衡量 QA；对比 BM25、Contriever/GTR 及多种结构化RAG基线，结果总体显示 HippoRAG 2 在检索与最终 QA 上更强，并通过消融与持续扩展语料设置验证关键模块有效。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-06-09</td>
      <td style="width: 55%;"><strong>G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2506.07398">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 G-Memory,这是一个分层记忆系统,旨在解决基于大型语言模型(LLM)的多智能体系统(MAS)缺乏自我演化能力的问题。<br>
        • 实现了三层图架构——洞察图、查询图和交互图——通过抽象可泛化的洞察和浓缩特定的协作轨迹来管理冗长的交互历史。<br>
        • 在具身动作和知识问答基准测试中的实验结果表明,G-Memory 显著增强了智能体团队的性能,在不修改原始框架的情况下将成功率提高了多达 20.89%。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-05-30</td>
        <td style="width: 55%;"><strong>M+：Extending MemoryLLM with scalable Long-Term Memory</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2310.04625">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
    </tr>
    <tr>
        <td colspan="3">
          • M+ 是一个记忆增强模型,旨在改善大型语言模型(LLM)中的长期信息保留。<br>
          • 基于 MemoryLLM 构建,M+ 将长期记忆机制与联合训练的检索器集成,大幅增强了模型处理跨越 20,000 个令牌的知识的能力,同时保持了可比的 GPU 内存开销。<br>
          • M+ 在多个基准测试中实现了强劲的性能,优于 MemoryLLM 和其他竞争基线,并展示了高效的信息压缩和端到端训练,表现出与人类记忆非常相似的机制。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-26</td>
      <td style="width: 55%;"><strong>MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2505.20231v2">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemGuide 是一个两阶段框架,旨在通过将任务意图和槽位级指导纳入记忆选择来增强多会话任务导向对话(TOD)。<br>
        • 它采用意图对齐检索将当前上下文与存储的意图描述匹配,并采用缺失槽位引导过滤来优先考虑使用思维链推理器填补信息空白的记忆单元。<br>
        • 作者还引入了 MS-TOD,一个多会话 TOD 基准。评估显示,与强大的基线相比,MemGuide 显著提高了任务成功率并减少了对话轮次。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-23</td>
      <td style="width: 55%;"><strong>Towards General Continuous Memory for Vision-Language Models</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Memory%20Modules-crimson" alt="Memory Modules">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2505.17670">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • CoMEM 通过引入通用的连续记忆机制,解决了视觉-语言模型(VLM)中传统检索增强生成(RAG)的令牌过载和性能下降问题。<br>
          • 该方法创新性地将 VLM 本身用作记忆编码器,结合轻量级 Q-Former,有效地将多样化的多模态和多语言知识压缩为一组紧凑的连续嵌入。<br>
          • CoMEM 具有数据和参数效率(仅需要 1.2% 的可训练参数)并且即插即用,在保持推理模型冻结的同时显著增强了复杂多模态推理任务的性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-21</td>
      <td style="width: 55%;"><strong>Pre-training Limited Memory Language Models with Internal and External Knowledge</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
        <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.15962">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了有限记忆语言模型(LMLM),这是一类新的模型,在预训练期间将事实知识外化到外部数据库中,而不是将其编码在参数中。<br>
        • 该方法使用修改后的预训练目标,从损失中屏蔽检索到的事实值,鼓励模型执行有针对性的事实查找,而不是记忆它们。<br>
        • 实验表明,LMLM 与明显更大的模型的事实精度相匹配,同时通过简单的数据库操作实现即时、可验证的知识更新和有效的机器反学习。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-11</td>
      <td style="width: 55%;"><strong>In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;">
        <a href="https://aclanthology.org/2025.acl-long.413/">
        <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了反思性记忆管理(RMM),这是一个用于长期对话智能体的新颖框架,解决了僵化的记忆粒度和固定检索机制的局限性。<br>
          • 整合了前瞻性反思以动态地将对话历史组织为基于主题的记忆,以及回顾性反思以使用由 LLM 归因信号引导的在线强化学习迭代地优化检索。<br>
          • 在 MSC 和 LongMemEval 基准测试上的实验结果表明,RMM 显著优于强大的基线,准确度提高了 10% 以上,并增强了响应个性化。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-04-22</td>
        <td style="width: 55%;"><strong>MemoRAG Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Long%20Context%20Processing-teal" alt="Long Context Processing">
        <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
        </td>
        <td style="width: 15%;"><a href="https://dl.acm.org/doi/10.1145/3696410.3714805">
        <img src="https://img.shields.io/badge/WWW-Paper-black?labelColor=teal" alt="WWW Paper">
        </a>
    </tr>
    <tr>
        <td colspan="3">
          • MemoRAG 旨在通过全局记忆增强检索机制改进信息检索和生成过程,从而增强大型语言模型(LLM)处理长上下文的能力。<br>
          • 该框架采用轻量级的全局记忆模块和复杂的生成系统,可以有效地管理长上下文并生成有用的线索以辅助答案生成。<br>
          • 该模型适用于各种任务,包括长文档问答和摘要,展示了其在处理复杂长文本场景方面的潜力。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-04-20</td>
        <td style="width: 55%;"><strong>SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
          <img src="https://img.shields.io/badge/Long--Text%20Processing-navy" alt="Long-Text Processing">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        </td>
          <td style="width: 15%;"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0925231225011427">
          <img src="https://img.shields.io/badge/Elsevier-Paper-black?labelColor=orange" alt="Elsevier Paper">
        </a>
    </tr>
    <tr>
      <td colspan="3">
        • SAGE 通过三个协作代理（用户、助手、检查员）解决大语言模型在动态环境中的长期记忆和多任务处理能力问题。SAGE结合反思机制和基于艾宾浩斯遗忘曲线的记忆优化，帮助模型有效筛选和存储重要信息，减少认知负担。<br>
        • SAGE通过迭代反馈机制和反思功能，不断优化助手的决策。其MemorySyntax组件模拟人类记忆衰退，动态管理短期和长期记忆，确保重要信息得到保留，减少不必要的记忆负担。<br>
        • 实验表明，SAGE在AgentBench和长文本任务（如HotpotQA）上大幅提升了模型表现，尤其在多跳问答和代码生成任务中，表现提高高达2.26倍，并有效解决了对话任务中的73.6%模糊引用问题，展现了其在实际应用中的潜力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-10</td>
      <td style="width: 55%;"><strong>Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.07952">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 论文提出 Dynamic Cheatsheet（DC）——在推理阶段给黑盒大模型加一个可持续更新的“便签式外部记忆”，把已验证的解题套路沉淀下来并在后续复用，实现无需训练的测试时学习。<br>
        • DC包含生成器 Gen 与 记忆策展 Cur：先用当前记忆生成答案，再由 Cur 提炼/筛选/压缩信息；检索式变体会按相似度取最相关历史样例及其解来辅助当前生成，同时控制记忆不膨胀。<br>
        • 在 AIME、GPQA-Diamond、Game of 24、MMLU-Pro 等多任务、跨模型（GPT-4o、Claude 3.5 Sonnet 等）评测，使用 Soft Match / Functionally Correct 等指标；结果显示 DC 在多项任务上显著提升，如 Game of 24 的跃升主要来自可复用的 Python 求解代码被反复“写入—复用”。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-03-27</td>
      <td style="width: 55%;"><strong>MemInsight: Autonomous Memory Augmentation for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Augmentation-purple" alt="Memory Augmentation">
        <img src="https://img.shields.io/badge/Autonomous-red" alt="Autonomous">
        <img src="https://img.shields.io/badge/Retrieval-success" alt="Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2503.21760">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出自动化的“记忆增强”管线：从交互中识别可长期保留的信息并结构化写入，服务后续检索与决策。<br>
        • 重点解决写入噪声与记忆膨胀：通过筛选/提炼/组织提高记忆质量，降低无关召回。<br>
        • 在多类 agent 场景中验证：更高质量的记忆写入可带来更稳定的长期表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-03-07</td>
      <td style="width: 55%;"><strong>Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Memory%20Modules-crimson" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;">
        <a href="https://aclanthology.org/2025.findings-acl.1234.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 MemQ，把“推理（自然语言步骤）”和“生成/执行查询（SPARQL）”分开：LLM 负责写清楚推理计划，查询由“记忆库检索 + 规则重建”得到，减少混合工具调用带来的错误与幻觉。<br>
        • 训练时把金标 SPARQL 规则拆成查询片段（含 CVT 等结构），再为每个片段生成自然语言解释，形成（解释→片段）的查询记忆库；推理时 LLM 生成逐步计划，重建时用语义检索（Sentence-BERT）从记忆库取 Top-N 片段并自适应选取，最后按规则拼接并填充实体得到完整查询。<br>
        • 在 WebQSP 与 CWQ 上用 Hits@1、F1 评测，结果整体最优；并用结构一致性/边命中率等指标验证重建查询更接近 gold，同时消融实验证明“记忆库 + 解耦”是主要增益来源。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-02-25</td>
        <td style="width: 55%;"><strong>Towards effective evaluation and comparisons for LLM unlearning methods</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Evaluation-dodgerblue" alt="LLM Evaluation">
        <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
        </td>
        <td style="width: 15%;"><a href="https://openreview.net/forum?id=aLLuYpn83y">
        <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
        </td>
    </tr>
    <tr>
        <td colspan="3">
          • 该论文研究了大型语言模型(LLM)中的机器反学习及其评估的重要性,特别关注删除不需要或不必要的数据记忆。<br>
          • 它引入了带校准的反学习(UWC)来校准模型性能,并加强对不同反学习方法的评估。<br>
          • 该研究强调了选择适当评估指标的重要性,并推荐提取强度(ES)作为主要评估工具,以确保评估的准确性和鲁棒性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-02-09</td>
        <td style="width: 55%;"><strong>LM2 Large Memory Models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2502.06049">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
        </td>
    </tr>
    <tr>
        <td colspan="3">
          • LM2 旨在克服传统 Transformer 在多步推理、关系论证和长上下文处理方面的局限性。<br>
          • LM2 集成了一个辅助记忆模块,利用交叉注意力机制和门控技术来增强信息存储和更新能力。<br>
          • 在多个基准测试中,LM2 展示了显著优越的性能,特别是在长上下文推理任务中表现出色,有效增强了处理和记忆复杂信息的能力。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-03</td>
      <td style="width: 55%;"><strong>TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Temporal%20Reasoning-purple" alt="Temporal Reasoning">
        <img src="https://img.shields.io/badge/Multi--Session-red" alt="Multi-Session">
        <img src="https://img.shields.io/badge/Benchmark-success" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.01630">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 面向多会话对话中的时间推理与记忆依赖，强调跨 session 的时间线一致性与事件顺序理解。<br>
        • 提出神经-符号结合的方法框架以提升 temporal reasoning，同时引入（或系统化）相应评测设定。<br>
        • 在多会话、强时间依赖场景中展示相对纯神经方法更稳健的推理与可解释性倾向。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-23</td>
      <td style="width: 55%;"><strong>ON MEMORY CONSTRUCTION AND RETRIEVAL FOR PERSONALIZED CONVERSATIONAL AGENTS</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2502.05589">
        <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 SECOM,这是一种在段落级别构建记忆库的记忆管理方法,以解决长期对话中轮次级别和会话级别方法的局限性。<br>
          • SECOM 将对话划分为主题连贯的段落,并采用提示压缩(LLMLingua-2)作为去噪机制来增强检索准确性。<br>
          • 实验结果表明,SECOM 在 LOCOMO 和 Long-MT-Bench+ 等长期对话基准测试上显著优于现有基线。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-01-19</td>
        <td style="width: 55%;"><strong>Alternate Preference Optimization for Unlearning Factual Knowledge in Large Language Models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
        <img src="https://img.shields.io/badge/Forgetting%20Strategies-darkmagenta" alt="Forgetting Strategies">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.coling-main.252.pdf">
        <img src="https://img.shields.io/badge/COLING-Paper-black?labelColor=brown" alt="COLING Paper">
        </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了交替偏好优化(AltPO),这是一种旨在有效解决大型语言模型(LLM)中机器反学习挑战的方法。<br>
          • AltPO 通过将遗忘集的负反馈与来自同一领域的正反馈相结合来生成多个替代响应,从而增强遗忘能力,同时保持整体模型性能。<br>
          • 实验结果表明,AltPO 在反学习质量和模型实用性方面都优于现有方法。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-31</td>
      <td style="width: 55%;"><strong>Titans Learning to Memorize at Test Time</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.00663">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • "Titans"旨在增强模型在处理长序列和复杂上下文时的记忆容量。<br>
          • Titans 架构结合了短期记忆和长期记忆模块,克服了传统递归模型和注意力机制的局限性,能够处理更大的上下文窗口。<br>
          • 实验结果表明,Titans 表现出卓越的性能和灵活性,特别是在处理长依赖关系和多样化任务方面。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-17</td>
      <td style="width: 55%;"><strong>On the Structural Memory of LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Modules-crimson)" alt="Memory Modules">
      <img src="https://img.shields.io/badge/Hybrid%20Memory-darkcyan" alt="Hybrid Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2412.15266">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 该论文研究了大型语言模型(LLM)中记忆模块的结构和检索方法如何影响模型性能,重点关注不同的记忆架构及其在信息提取和生成中的作用。<br>
          • 该研究发现,混合记忆结构在复杂任务中优于其他结构,在噪声环境中展示了更强的鲁棒性。<br>
          • 通过超参数敏感性分析,该研究确定了最适合不同任务设置的记忆检索策略。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-01</td>
      <td style="width: 55%;"><strong>SELF-UPDATABLE LARGE LANGUAGE MODELS BY INTEGRATING CONTEXT INTO MODEL PARAMETERS</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
        <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2410.00487">
        <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了 SELF-PARAM,这是一种将上下文直接集成到 LLM 参数中的方法,无需额外的存储模块,确保高效性和长期保留。<br>
          • 采用训练目标,最小化原始模型(具有上下文访问)和目标模型(没有上下文)之间的 KL 散度,利用多样化生成的问答对。<br>
          • 实验表明,SELF-PARAM 在问答和对话推荐任务中显著优于现有的持续学习和 RAG 方法,以零存储复杂度实现接近最优的性能。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2024-10-10</td>
        <td style="width: 55%;"><strong>Assessing episodic memory in LLMs with sequence order recall tasks</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Evaluation-dodgerblue" alt="LLM Evaluation">
        <img src="https://img.shields.io/badge/Sequential%20Recall-tomato" alt="Sequential Recall">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2410.08133">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 该研究引入了序列顺序回忆任务(SORT),旨在评估大型语言模型(LLM)的情景记忆能力。<br>
          • 该任务强调了情景记忆的重要性——将记忆与相关上下文(如时间和地点)联系起来——特别是在日常认知任务中。<br>
          • 初步结果表明,当提供上下文信息时,LLM 表现出强大的记忆性能,但仅依赖训练数据时,其性能会显著下降。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-19</td>
      <td style="width: 55%;"><strong>ELDER: Enhancing Lifelong Model Editing with Mixture-of-LoRA</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2408.11869">
        <img src="https://img.shields.io/badge/AAAI-Paper-black?labelColor=orange" alt="AAAI Paper">
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • ELDER 提出了一种使用 Mixture-of-LoRA 结构的新颖终身模型编辑方法,在数据和适配器之间建立连续关联,增强对改写输入的鲁棒性。<br>
          • 该框架将路由器网络与引导损失函数集成,以将 LoRA 分配与编辑知识对齐,并利用延迟机制来保留模型的通用能力。<br>
          • 在 GPT-2 XL 和 LLaMA2-7B 上的大量实验表明,ELDER 在可靠性、泛化性和可扩展性方面优于现有基线,同时保持下游任务的性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-16</td>
      <td style="width: 55%;"><strong>MemLong: Memory-Augmented Retrieval for Long Text Modeling</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long%20Text-purple" alt="Long Text">
        <img src="https://img.shields.io/badge/Memory--Aug%20Retrieval-red" alt="Memory-Aug Retrieval">
        <img src="https://img.shields.io/badge/Long--Context-success" alt="Long-Context">
      </td>
      <td style="width: 15%;"><a href="https://openreview.net/pdf?id=AxBgIF4Xva">
        <img src="https://img.shields.io/badge/OpenReview-paper-1f6feb?logo=openreview" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将长文本建模中的“历史信息”外部化为可检索记忆，通过 memory-augmented retrieval 扩展有效上下文长度。<br>
        • 关注检索与生成的协同：如何在生成过程中选择性引入历史片段，并控制检索噪声对建模的影响。<br>
        • 在长上下文/长文本任务上验证：相对纯长上下文输入或朴素检索拼接，能获得更稳健的效果提升。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2024-08-11</td>
        <td style="width: 55%;"><strong>Towards Safer Large Language Models through Machine Unlearning</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2024.findings-acl.107.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
        <td colspan="3">
          • 该论文介绍了选择性知识反学习(SKU)框架,旨在提高大型语言模型(LLM)的安全性。<br>
          • SKU 框架由两个主要阶段组成:有害知识获取,然后是知识否定,重点是删除不需要的知识,而不会在良性提示下降低模型效用。<br>
          • SKU 成功减少了有害输出,同时保持了响应质量,并在 OPT 和 LLaMA2 等多个 LLM 架构中展示了反学习有效性和模型效用之间的强大平衡。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-08-06</td>
      <td style="width: 55%;"><strong>RULER: What’s the Real Context Size of Your Long-Context Language Models?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Evaluation-dodgerblue" alt="LLM Evaluation">
      <img src="https://img.shields.io/badge/Long--Context%20Models-royalblue" alt="Long-Context Models">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2404.06654">
      <img src="https://img.shields.io/badge/COLM-Paper-black?labelColor=gold" alt="COLM Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • RULER 旨在跨广泛的任务对长上下文语言模型(LM)进行全面评估。<br>
          • 它通过合并多跳跟踪和聚合等任务来扩展传统的"大海捞针"(NIAH)测试,能够更全面地评估模型在长上下文设置下的理解能力。<br>
          • RULER 在多跳推理和信息检索任务中展示了强大的性能。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-07-22</td>
      <td style="width: 55%;"><strong>A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2402.09727">
      <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • ReadAgent 是一个阅读理解系统,旨在提高大型语言模型(LLM)处理长文本时的性能。<br>
          • 通过三个步骤——情景分页、记忆摘要和交互式查找——ReadAgent 将有效上下文长度显著扩展了多达 20 倍。<br>
          • ReadAgent 在 QuALITY、NarrativeQA 和 QMSum 等长文档阅读理解基准测试中优于传统方法。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-06-30</td>
      <td style="width: 55%;"><strong>Towards Efficient and Effective Unlearning of Large Language Models for Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <img src="https://img.shields.io/badge/Recommender%20Systems-darkslategray" alt="Recommender Systems">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2403.03536">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 E2URec,这是一种专门为基于 LLM 的推荐系统(LLMRec)设计的推荐数据反学习方法。<br>
          • E2URec 通过仅更新低秩适应(LoRA)参数,显著提高了反学习效率,同时保持了推荐性能。<br>
          • 实验结果表明,E2URec 在真实世界数据集上优于现有的基线方法。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-30</td>
      <td style="width: 55%;"><strong>Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2405.19686">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了知识图谱调优(KGT),这是一种通过基于用户反馈优化外部知识图谱来个性化大型语言模型(LLM)的新颖方法,无需修改模型参数。<br>
          • KGT 从用户交互中提取个性化的事实知识三元组,并采用启发式优化算法,避免了反向传播方法的高计算成本和低可解释性。<br>
          • 使用 Llama2 和 Llama3 等模型的实验表明,KGT 显著增强了个性化性能,同时将延迟降低了多达 84%,GPU 内存成本降低了多达 77%。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-26</td>
      <td style="width: 55%;"><strong>MemoryLLM:Towards self-Update Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2402.04624">
      <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MEMORYLLM 是一个自更新的大型语言模型,旨在有效整合新知识,同时保持长期信息保留。<br>
          • 通过在 Transformer 的潜在空间中嵌入固定大小的记忆池,MEMORYLLM 实现了模型自更新和知识保留的无缝结合。<br>
          • 关键设计特性包括存储压缩知识的记忆令牌、智能自更新机制,以及对知识整合、保留能力和鲁棒性的全面评估。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-23</td>
      <td style="width: 55%;"><strong>HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2405.14831">
        <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • HippoRAG 是一个受人类长期记忆的海马体索引理论启发的新颖检索框架,旨在为 LLM 实现更深入、更高效的知识整合。<br>
          • 通过编排 LLM、知识图谱和个性化 PageRank(PPR)来模拟新皮层和海马体,它实现了有效的单步多跳检索。<br>
          • 该方法在多跳问答任务中比最先进的检索增强生成(RAG)方法高出多达 20%,并且比迭代检索方法显著更快、更便宜。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-23</td>
      <td style="width: 55%;"><strong>WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2405.14768">
        <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 识别了终身模型编辑中的"不可能三角"——可靠性、泛化性和局部性不能同时实现——将其归因于长期记忆和工作记忆机制之间的差距。<br>
          • 提出了 WISE,这是一个双参数记忆框架,利用侧记忆进行编辑,并使用路由器将其与预训练的主记忆桥接,采用知识分片和合并来处理连续更新。<br>
          • 大量实验表明,WISE 在多个 LLM 架构的问答、幻觉纠正和分布外泛化设置中优于现有方法。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-26</td>
      <td style="width: 55%;"><strong>Enhancing Large Language Model with Self-Controlled Memory Framework</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Text%20Processing-navy" alt="Long-Text Processing">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2304.13343">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了自控记忆(SCM)框架,为大型语言模型(LLM)释放无限长度的输入容量,无需修改或微调。<br>
          • 该框架包括一个基于 LLM 的智能体、一个用于存储历史信息的记忆流,以及一个动态管理"激活记忆"(长期)和"闪存"(短期)的记忆控制器。<br>
          • 作者还贡献了一个涵盖长期对话、书籍摘要和会议摘要的数据集,表明 SCM 与基线相比实现了卓越的检索召回和响应生成。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-24</td>
      <td style="width: 55%;"><strong>From Local to Global: A GraphRAG Approach to Query-Focused Summarization</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
        <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.16130">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 GraphRAG,这是一种基于图的检索增强生成方法,旨在解决传统向量 RAG 在回答整个文本语料库的全局问题方面的局限性。<br>
          • 该方法从源文档构建实体知识图谱,使用 Leiden 算法将其划分为分层社区,并预生成摘要以促进全局意义构建。<br>
          • 通过利用社区摘要的 map-reduce 机制,GraphRAG 在大规模数据集的全面性和多样性方面显著优于基线 RAG 系统。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-15</td>
      <td style="width: 55%;"><strong>Memory Sharing for Large Language Model based Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.09982v2">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了记忆共享(MS)框架,使多个基于 LLM 的智能体能够在动态实时池中共享提示-答案(PA)对作为记忆。<br>
          • 该框架采用双重目的机制,其中新生成的高质量记忆用于增强智能体的上下文学习,同时训练检索器以提高未来的检索相关性。<br>
          • 在文学创作和逻辑问题解决等领域的实验结果表明,MS 框架有效地将个体智能演化为集体智能,在没有显式微调的情况下显著提高了开放式问题的性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-13</td>
      <td style="width: 55%;"><strong>LLM In-Context Recall is Prompt Dependen</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/LLM%20Recall-steelblue" alt="LLM Recall">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2404.08865">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 研究了大型语言模型(LLM)的信息回忆能力,特别强调其对提示内容和格式的依赖性。<br>
          • 使用"大海捞针"(NIAH)评估,该研究发现回忆性能受训练数据偏差以及提示的内容和结构的强烈影响。<br>
          • 结果表明,架构改进、训练策略调整和微调都可以有效增强回忆性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-07</td>
      <td style="width: 55%;"><strong>Online Adaptation of Language Models with a Memory of Amortized Contexts</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2403.04317">
        <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了摊销上下文记忆(MAC),这是一个用于大型语言模型(LLM)的高效在线适应框架,旨在解决灾难性遗忘和保持模型最新的高计算成本问题。<br>
          • MAC 利用元学习的摊销网络将新文档压缩为存储在记忆库中的紧凑参数高效微调(PEFT)调制,使用聚合网络检索和组合特定查询的相关知识。<br>
          • 在 StreamingQA 和 SQuAD-Seq 上的实验结果表明,MAC 在适应性能和知识保留方面都显著优于现有的在线微调方法,同时提供卓越的时间和记忆效率。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-03-24</td>
      <td style="width: 55%;"><strong>MemoryBank: Enhancing Large Language Models with Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29946">
      <img src="https://img.shields.io/badge/AAAI-Paper-black?labelColor=orange" alt="AAAI Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • MemoryBank 是一个为大型语言模型(LLM)设计的长期记忆机制,用于解决连续交互中的记忆限制。<br>
          • 通过使模型能够有效地回忆、更新和适应用户记忆,MemoryBank 增强了上下文理解和用户体验。<br>
          • 实验结果和分析表明,MemoryBank 在改善情感支持和个性化交互方面是有效的。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-02-16</td>
      <td style="width: 55%;"><strong>Large Language Model Unlearning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <img src="https://img.shields.io/badge/Forgetting%20Strategies-darkmagenta" alt="Forgetting Strategies">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2310.10683">
      <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 探索了在大型语言模型(LLM)中实施"遗忘"或"反学习"的方法,以消除不需要的或不一致的行为。<br>
          • 通过应用梯度上升(GA)策略并引入随机输出损失,该研究表明反学习可以有效防止模型生成有害响应。<br>
          • 实验结果表明,GA 和 GA + Mismatch 方法在降低内容泄漏率方面表现特别好。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-02-06</td>
      <td style="width: 55%;"><strong>Compressed context memory for online language model interaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      <img src="https://img.shields.io/badge/Long--Context%20Models-royalblue" alt="Long-Context Models">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2312.03414">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 提出了一种压缩上下文记忆方法,以改善在线语言模型在处理扩展上下文时的记忆效率和计算性能。<br>
          • 通过利用条件 LoRA 集成和并行计算,该方法显著减少了记忆需求,并支持有效的无限上下文长度,超越了传统的滑动窗口策略。<br>
          • 实验结果表明,在多任务学习和对话生成等应用中,该方法将记忆使用量减少了多达 5 倍,同时有效保持了生成质量和准确性。
        </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2023-12-10</td>
      <td style="width: 55%;"><strong>Unlearn What You Want to Forget: Efficient Unlearning for LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-sienna" alt="Machine Forgetting">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/anthology-files/pdf/emnlp/2023.emnlp-main.738.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了高效反学习(EUL)框架,旨在解决大型语言模型(LLM)中处理用户隐私数据的挑战。<br>
          • 随着 LLM 的广泛部署,模型可能在预训练期间无意中记忆敏感信息,引发重大隐私担忧。<br>
          • EUL 能够在不完全重新训练的情况下有效地从 LLM 中删除特定的敏感数据,同时保持整体预测性能。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-11-30</td>
      <td style="width: 55%;"><strong>JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
        <img src="https://img.shields.io/badge/Hybrid%20Memory-darkcyan" alt="Hybrid Memory">
      </td>
      <td style="width: 15%;"><a href="https://ieeexplore.ieee.org/abstract/document/10778628">
      <img src="https://img.shields.io/badge/IEEE-Journal-black?labelColor=00629B" alt="IEEE Journal">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • JARVIS-1是一款用于Minecraft的开放世界多任务代理，通过多模态语言模型（MLM）生成计划并执行任务。它能感知视觉信息和人类指令，并结合多模态记忆，利用过去的经验提升未来任务的执行能力。<br>
        • JARVIS-1结合了MLM和多模态记忆，使用视觉观察和指令生成行动计划，并通过目标控制器执行。它具有自我改进机制，能通过自我指令生成任务并探索环境，积累经验以提升决策能力。<br>
        • JARVIS-1在超过200个Minecraft任务中表现出色，特别是在长期任务（如获取钻石镐）中，成功率比现有最先进模型高出5倍。随着游戏进行，它通过不断学习和经验积累，表现逐渐提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-11-15</td>
      <td style="width: 55%;"><strong>Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2311.08719">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了一种新颖的记忆机制,Think-in-Memory(TiM),旨在增强大型语言模型(LLM)在长期人机交互中的性能。<br>
          • TiM 结合了基于局部敏感哈希的高效检索机制,使扩展交互中的有效记忆存储和管理成为可能。<br>
          • 实验结果表明,TiM 在多轮对话中显著提高了响应准确性和连贯性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-10-16</td>
      <td style="width: 55%;"><strong>Character-LLM: A Trainable Agent for Role-Playing</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;">
        <a href="https://aclanthology.org/2023.emnlp-main.814.pdf">
        <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 <strong>Character-LLM</strong>,这是一个可训练的智能体框架,通过从重构的经验中学习而不是仅依赖提示,教会 LLM 扮演特定角色(例如贝多芬)。<br>
          • 提出了一个<strong>经验上传</strong>过程,涉及档案收集、场景提取和经验完成,以生成高质量的、特定于角色的训练数据。<br>
          • 实施了<strong>保护性经验</strong>以缓解幻觉,使智能体能够有效地"忘记"或拒绝与其角色的时代或身份不一致的知识。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-09-22</td>
      <td style="width: 55%;"><strong>Augmenting Language Models with Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Long--Text%20Processing-navy" alt="Long-Text Processing">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://papers.nips.cc/paper_files/paper/2023/file/ebd82705f44793b6f9ade5a669d0f0bf-Paper-Conference.pdf">
      <img src="https://img.shields.io/badge/NeurIPS-Paper-black?labelColor=yellowgreen" alt="NeurIPS Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了一个新框架 LONGMEM,旨在增强大型语言模型(LLM)处理长文本的能力。<br>
          • LONGMEM 采用解耦的网络架构,将冻结的 LLM 记忆编码器与自适应残差侧网络相结合,实现长期上下文信息的高效缓存和更新。<br>
          • 通过结合专门的记忆增强层、基于令牌的记忆检索模块和联合注意力机制,LONGMEM 改进了记忆检索和上下文利用,并在各种任务中展示了有效性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-08-16</td>
      <td style="width: 55%;"><strong>MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2308.08239">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 MemoChat,这是一个指令调优流水线,旨在使大型语言模型(LLM)能够采用自我编写的备忘录来维持长距离开放域对话中的一致性。<br>
        • 该方法利用"记忆-检索-响应"循环,教会 LLM 将对话历史重构为备忘录,并检索相关证据来回答当前查询。<br>
        • 实验表明,MemoChat 在新策划的、专家标注的一致性基准(MT-Bench+)上优于强大的基线,验证了配备备忘录的内部思维过程的有效性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-05-23</td>
      <td style="width: 55%;"><strong>RET-LLM: Towards a General Read-Write Memory for Large Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
        <img src="https://img.shields.io/badge/Memory%20Modules-crimson" alt="Memory Modules">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2305.14322">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • RET-LLM 是一个框架,为大型语言模型(LLM)配备了专用的读写记忆单元,使它们能够显式地从文本中提取、存储和回忆知识。<br>
        • 受戴维森语义学启发,该系统以三元组(概念、关系、概念)的形式提取知识,并使用控制器通过基于文本的 API 管理 LLM 与记忆模块之间的交互。<br>
        • 记忆单元设计为可扩展、可更新和可解释的,有效地处理静态模型经常失败的基于时间的问答任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-05-22</td>
      <td style="width: 55%;"><strong>RECURRENTGPT: Interactive Generation of (Arbitrarily) Long Text</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2305.13304">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 RECURRENTGPT,这是一个基于语言的 LSTM 循环机制的模拟,构建在 LLM 之上,以生成任意长度的文本而不会遗忘。<br>
        • 利用双重记忆系统:在提示中更新的短期记忆和通过语义搜索检索的存储在硬盘上的长期记忆。<br>
        • 实现可解释和交互式的文本生成("AI 即内容"),允许人类用户在生成过程中观察和编辑自然语言记忆和计划。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-05-08</td>
      <td style="width: 55%;"><strong>Prompted LLMs as Chatbot Modules for Long Open-domain Conversation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://aclanthology.org/2023.findings-acl.277.pdf">
          <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 MPC(模块化提示聊天机器人),这是一种使用预训练 LLM 作为独立模块(澄清器、记忆处理器、话语生成器、摘要器)的新颖方法,以创建高质量的对话智能体而无需微调。<br>
        • 利用少样本提示、思维链(CoT)和外部记忆(使用 DPR)等技术,在开放域对话中实现长期一致性和灵活性。<br>
        • 人类评估结果表明,MPC 在合理性、一致性和吸引力方面与 Blenderbot3 等微调模型相当或更优,特别是在维持长期人物一致性方面。
      </td>
    </tr>
  </table>
</details>



<details>
  <summary><strong>数据集和评估基准类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>MemRiskBench: Trace-Aware Risk-Preserving Evaluation for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.14976"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估长程记忆轨迹中稀疏但高影响的风险。<br>
        • 确定性检查覆盖过时事实、冲突、泄漏、撤销及约束衰减。<br>
        • 120 个情节的研究展示较小评测子集仍可保留风险覆盖。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-09</td>
      <td style="width: 55%;"><strong>PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.09664"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测超越事实回忆的个性化指导能力。<br>
        • 长期历史和标注证据测试变化偏好及错误假设。<br>
        • 评估同时揭示证据检索及实际利用方面的不足。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-04</td>
      <td style="width: 55%;"><strong>Does Your Agent&#39;s Memory Survive a Model Upgrade? A Controlled Study of Memory Portability</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.05339"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试模型和嵌入升级后的记忆可移植性。<br>
        • 受控合成历史比较原始日志、检索、笔记及固定模式图。<br>
        • 结果揭示笔记损失的模型依赖性及保留原始历史的价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-03</td>
      <td style="width: 55%;"><strong>When Users Don&#39;t Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.03467"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试用户未明确询问事实时的上下文驱动记忆检索。<br>
        • 四种对话查询风格区分召回与完整回答依据。<br>
        • 隐含及组合查询暴露传统问答评估遗漏的差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-03</td>
      <td style="width: 55%;"><strong>ICM-Bench: Person-Level Identity Reasoning in Multimodal Agents with Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.04438"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测多模态记忆中的持久人物身份推理。<br>
        • 合成生活相册视频将重复人物连接至可追溯跨时间证据。<br>
        • 受测系统处理事件的能力强于长期累积身份画像。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.30508"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测面向任务的分散对话证据整合。<br>
        • 五个领域测试隐含相关性、密集历史、综合生成及抗干扰能力。<br>
        • 结果揭示成功检索与有效证据整合之间的明显差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.31057"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究代码智能体工作记忆的语义异质性。<br>
        • 利用归档轨迹比较对象感知压缩、检索及真实系统回放。<br>
        • 结果显示名义 token 预算掩盖实际上下文及管理成本差异。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-31</td>
      <td style="width: 55%;"><strong>Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.00103"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在准确率之外评估记忆效率、压缩及校准。<br>
        • ECCBench 测量计算预算、可压缩输入及不确定性感知拒答。<br>
        • 实验发现预训练视觉语言模型的视频压缩和校准仍较弱。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-30</td>
      <td style="width: 55%;"><strong>Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.29605"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据可审计事后证据学习记忆效用。<br>
        • 检索、引用及受控删除探测沿记忆版本校准贡献。<br>
        • LoCoMo 和 LongMemEval 报告本地 8B 策略的较强表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-26</td>
      <td style="width: 55%;"><strong>Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.25655"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试扁平交错对话中的情节重建。<br>
        • SCALE-QA 将任务问题与时间语义记忆重建相结合。<br>
        • 三个后端报告优于较强检索及长上下文基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-26</td>
      <td style="width: 55%;"><strong>MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.26295"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测参数知识与可执行工具返回之间的冲突。<br>
        • 已知来源正确性区分知识保留、工具跟随及拒答行为。<br>
        • 微调帮助部分模型，但稳健性和拒答方面仍存在权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-25</td>
      <td style="width: 55%;"><strong>MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-Term Human-AI Conversation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.24189"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估真实长期对话中的自然记忆整合。<br>
        • 四个月部署对比事实回忆与用户触发的记忆使用时刻。<br>
        • 该研究中自然整合与满意度相关，直接问答准确率则不相关。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-21</td>
      <td style="width: 55%;"><strong>DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.20664"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过可执行评分评测跨会话软件智能体记忆维护。<br>
        • 预注册审计比较无记忆与多种保留证据的配置。<br>
        • 记忆优于无记忆对照，但尚未证明各记忆系统间的优劣。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-20</td>
      <td style="width: 55%;"><strong>Can Agent Memory Systems Track Evolving State?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.19652"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 区分当前状态跟踪与对已替代信息的回忆。<br>
        • StateMemBench 及显式替代关系诊断、修复演化状态错误。<br>
        • 实验在多个记忆和检索后端上改善当前状态准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-20</td>
      <td style="width: 55%;"><strong>MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.20202"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试相关存储记忆诱发的认知陷阱。<br>
        • 通过推理固着及信念扭曲探测评估五种记忆框架。<br>
        • 所有受测策略弱于无记忆设置，自适应指导可部分缓解。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-15</td>
      <td style="width: 55%;"><strong>Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.15008"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在统一评测框架下比较异构记忆存储机制。<br>
        • 三个模型及四组任务测量不同介质的质量、效率和扩展性。<br>
        • 没有介质全面占优，事实检索与顺序行动偏好不同设计。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-14</td>
      <td style="width: 55%;"><strong>When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.13921"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测不存在唯一合理答案的个人记忆冲突。<br>
        • TANGLE 测试冲突识别、校准、澄清及忠实证据处理。<br>
        • 实验暴露冲突关系丢失问题，支持依证据制定行动策略。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-11</td>
      <td style="width: 55%;"><strong>MobileMem: Learning from a Year of Mobile Experiences</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.13606"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提供年度尺度移动经验用于长期记忆研究。<br>
        • 知识引导合成构建时间连贯的文本及多模态用户轨迹。<br>
        • 基准覆盖知识更新、隐含偏好及多跳时间推理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-05</td>
      <td style="width: 55%;"><strong>When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.04574"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究与视觉观察冲突的过时空间记忆。<br>
        • 动态 FrozenLake 检测及导航任务区分审计和动作选择错误。<br>
        • 过滤有助于文本设置，但不可靠视觉依据限制恢复。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-04</td>
      <td style="width: 55%;"><strong>MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.03844"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估受审计智能体记忆系统中的仅查询式投毒。<br>
        • 测试大型正常记忆库及主动输入审计下的持久性。<br>
        • 实验揭示检索竞争和语义审计仍存在薄弱点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>Can an AI Assistant Really Forget? Auditable Deletion from Addressable Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.27539"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试可寻址对话记忆中的可审计删除。<br>
        • 对比移除交互关联行、重新拟合及从未接触目标的历史。<br>
        • 删除减少泄露，但仍区别于完全未包含目标交互的重建。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-29</td>
      <td style="width: 55%;"><strong>MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.27080"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 追踪记忆投毒从持久化到后果及修复的全过程。<br>
        • 写入、执行、遗忘协议覆盖 310 个案例及 24 种配置。<br>
        • 结果显示攻击传播及选择性修复存在明显配置差异。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-27</td>
      <td style="width: 55%;"><strong>Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.24368"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测存储事实与后续任务之间的隐含关联。<br>
        • 配对对照区分知识缺失与关键记忆未被呈现。<br>
        • 系统显式事实回忆较好，但需要世界知识桥接时检索困难。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-26</td>
      <td style="width: 55%;"><strong>When Does Memory Help? A Cost-Aware Evaluation of Long-Term Memory in Tool-Using LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.05441"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测量工具智能体记忆的边际效用及完整成本。<br>
        • 可监测情节任务测试依赖、更新、污染及实际行动利用。<br>
        • 实验支持变化事实任务中的更新感知存储，并揭示检索行动差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-24</td>
      <td style="width: 55%;"><strong>Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21962"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在对话文本生成前先构建长期记忆评测真值。<br>
        • 有效期、来源及经过验证的生成支持历史长度受控比较。<br>
        • 记忆架构排名随使用时长改变，写入质量与回答质量强相关。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-23</td>
      <td style="width: 55%;"><strong>RUMBA: Russian User Memory Benchmark</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21447"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出俄语对话记忆评测，并提供对齐英语子集。<br>
        • 带时间戳对话探测语义类型、会话范围及时间推理。<br>
        • 细粒度评估区分不同记忆系统的优势和失败模式。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-23</td>
      <td style="width: 55%;"><strong>Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21571"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究在问题间保留记忆的顺序具身问答。<br>
        • 对比占据图、继承历史及具有空间依据的三维视觉记忆。<br>
        • 仿真和机器人测试显示空间组织视觉证据有利于准确率及导航成本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-18</td>
      <td style="width: 55%;"><strong>RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.16716"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测对长期变化证据历史的组合推理。<br>
        • 六类任务测试失效传播链、冲突、反事实及时间约束。<br>
        • 当前系统在超越孤立事实更新的检索和推理上均有困难。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-16</td>
      <td style="width: 55%;"><strong>Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.14611"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究通过智能体记忆文件实现的持久提示注入。<br>
        • 沙盒多会话测试在四个模型上比较两种代码智能体系统。<br>
        • 已植入记忆可影响后续会话，持久性随配置而变化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-14</td>
      <td style="width: 55%;"><strong>PM-Bench: Evaluating Prospective Memory in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.12385"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评测在其他活动持续时执行延迟意图的能力。<br>
        • 模拟一周测试线索监控、意图保留及及时行动。<br>
        • 八个模型的评估仍具挑战，未发现普遍最佳的记忆策略。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-14</td>
      <td style="width: 55%;"><strong>MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Lifecycle-blue" alt="Memory Lifecycle">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.12893"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估显式生命周期操作，而非仅考察最终记忆回答。<br>
        • 结构化轨迹记录触发、目标、范围、状态转移及支持证据。<br>
        • 测试揭示被答案准确率掩盖的更新和轨迹重建错误。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-13</td>
      <td style="width: 55%;"><strong>SLVMBench: Skill Learning from Video Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.11312"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 测试从长视频记忆学习技能并即时应用。<br>
        • 将教程嵌入数小时干扰视频，并配以时间标注任务问题。<br>
        • 当前视频模型难以从长历史中获取并应用技能。
      </td>
    </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>MemSyco-Bench: Benchmarking Sycophancy in Agent Memory</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/基准测试-blue" alt="基准测试">
          <img src="https://img.shields.io/badge/谄媚-brightgreen" alt="谄媚">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.01071v2">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 识别并形式化"记忆诱发的谄媚"（智能体以牺牲事实准确性为代价过度迎合检索到的历史用户记忆），并推出 MemSyco-Bench，将评估从检索成功转向检索后的决策校准。<br>
          • 一个包含五类任务的基准——客观事实判断、上下文范围控制、记忆-证据冲突、有效记忆选择、个性化记忆使用——由模拟的多轮对话构建；跨多个骨干模型评估记忆系统（Mem0、A-Mem、MemGPT、MemoryBank、LightMem、SuperMemory、NaiveRAG）。<br>
          • 记忆持续加剧谄媚——DeepSeek-V4-Flash 的事实准确率从 56.1% 降至 40.2%，谄媚率从 24.3% 升至 52.3%；记忆系统会降低客观事实准确率（Qwen3-8B 降至 26–36%）；现有基准的错误主要由检索失败主导（47.4%–66.1%）。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-07-02</td>
      <td style="width: 55%;"><strong>AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/长程-brightgreen" alt="长程">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.02255v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 引入一种有界记忆"契约"，其中每个决策提示都由来自五个类型化层（L1–L5）的类型化检索新鲜组装而成，不附加任何原始的跨决策记录，从而在任意长的运行中保持提示有界，并使每个记忆层可单独消融。<br>
          • 研究显式记忆层如何塑造长程 LLM 智能体的决策，在随机卡牌构筑游戏《Slay the Spire 2》中实例化；发布一个可复现的测试平台，包含 298 条完成的轨迹，带有条件标签、冻结的记忆/技能快照、提示记录和分析脚本。<br>
          • 在固定 A0 的消融中，无存储基线赢 3/10 局，加入触发式战略技能层（L5）后赢 6/10 局（方向性，Fisher 精确检验 p≈0.37）；一个公开的前沿 LLM 基准报告在 A0 下五种配置均零胜，而开发者报告的人类胜率为 16%。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-blue" alt="长期记忆">
          <img src="https://img.shields.io/badge/基准测试-brightgreen" alt="基准测试">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24595v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 首个直接将长期智能体记忆作为可审计的交互后产物来评估的基准——从智能体留下的记忆中重建用户隐藏的、以分类法为锚的状态——而不仅仅通过间接的下游任务成功来评估。<br>
          • 记忆恢复基准；配备记忆的智能体帮助模拟用户完成受泄漏控制的任务，之后在全量存储（dump_all）和 top-k（retrieve）两种访问模式下，重建每个隐藏的用户状态维度并对照真值打分。<br>
          • 涵盖 50 个模拟用户 × 31 个隐藏维度（1,550 个目标）和 5 个记忆系统，任务完成度几近饱和（~99.9%），而类别平衡的恢复度保持中等（全量存储 B≈0.611–0.624，在 top-k 下降至 0.473–0.540），其中情景/关系记忆最难。
      </td>
  </tr>
  <tr>
      <td rowspan="2" style="width: 15%;">2026-06-23</td>
      <td style="width: 55%;"><strong>Are We Ready For An Agent-Native Memory System?</strong></td>
      <td style="width: 15%;">
          <img src="https://img.shields.io/badge/智能体记忆-blue" alt="智能体记忆">
          <img src="https://img.shields.io/badge/基准测试-brightgreen" alt="基准测试">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2606.24775v1">
          <img src="https://img.shields.io/badge/arXiv-论文-%23D2691E?logo=arxiv" alt="论文徽章">
      </a></td>
  </tr>
  <tr>
      <td colspan="3">
          • 将 LLM 智能体记忆重构为一个数据管理系统，并提出一个分析框架，将其分解为四个核心模块（表示与存储、抽取、检索与路由、维护），并配以对现有系统的结构化分类法。<br>
          • 系统性实验研究，在统一测试平台上跨 5 种工作负载 / 11 个数据集对 12 个代表性记忆系统加 2 个参考基线进行基准测试，评估任务有效性、检索保真度、动态更新鲁棒性、长程稳定性和运行成本，并进行逐模块消融。<br>
          • 没有单一架构占绝对优势——有效性取决于记忆结构与工作负载瓶颈之间的契合；基于图的方法最可靠地处理更新，而仅追加存储会返回陈旧事实；高度结构化的系统会带来数量级更高的延迟，却没有相应的准确率提升。
      </td>
  </tr>
       <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-4A90E2" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/记忆基准-F5A623" alt="Memory Benchmark">
          <img src="https://img.shields.io/badge/用户状态-7ED321" alt="User State">
          <img src="https://img.shields.io/badge/记忆审计-D0021B" alt="Audit">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24595v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文主张长期记忆应被评估为交互结束后可审计的记忆产物，而不只是通过后续回答准确率、个性化质量或任务成功率间接衡量。<br>
          • MEMPROBE 为带有隐藏用户状态库的模拟用户生成辅助轨迹，在经过受控泄漏任务后，从智能体留下的 memory store 中重建这些隐藏状态，从而直接检查记忆实际保留了什么。<br>
          • 发布的基准覆盖 50 个模拟用户、1,550 个隐藏用户状态目标和五类代表性记忆系统，揭示了在任务完成率接近饱和时仍会被掩盖的长期记忆失效。
        </td>
      </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>OpenThoughts-Agent: Data Recipes for Agentic Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agentic%20Data-4A90E2" alt="Agentic Data">
          <img src="https://img.shields.io/badge/Data%20Recipe-F5A623" alt="Data Recipe">
          <img src="https://img.shields.io/badge/Open%20Dataset-7ED321" alt="Open Dataset">
          <img src="https://img.shields.io/badge/Agent%20Training-D0021B" alt="Agent Training">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24855v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文研究如何为具备广泛能力的 agentic language model 构造训练数据，弥补现有开放工作通常只面向单一基准、缺少可泛化数据配方的问题。<br>
          • OpenThoughts-Agent 项目提供完全开放的数据整理流水线，并围绕流水线阶段、任务来源和数据多样性进行了 100 多组受控消融实验，最终构建出包含 100K 样本的 agentic 模型训练数据集。<br>
          • 在该数据集上微调 Qwen3-32B 后，模型在七个 agentic benchmark 上达到 44.8% 平均准确率，相比 Nemotron-Terminal-32B 提升 3.9 个百分点；训练数据在计算受控对比中也表现出良好 scaling 特性，为研究可复用 agentic 经验轨迹与任务多样性如何影响智能体训练提供了开放资源。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-17</td>
        <td style="width: 55%;"><strong>LegalWorld: A Life-Cycle Interactive Environment for Legal Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Legal%20Agents-4A90E2" alt="Legal Agents">
          <img src="https://img.shields.io/badge/Life--Cycle%20Simulation-F5A623" alt="Life-Cycle Simulation">
          <img src="https://img.shields.io/badge/Case%20Memory-7ED321" alt="Case Memory">
          <img src="https://img.shields.io/badge/LongJud--Bench-D0021B" alt="LongJud-Bench">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.18728">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出LegalWorld，将中国民事诉讼建模为由法律咨询、起诉文书撰写、一审、上诉及二审构成的五阶段因果状态链，使早期事实陈述、证据组织和诉讼策略能够真实约束后续程序及裁判结果。<br>
          • 环境以75,309组一审与二审配对判决为数据基础，并构建场景内局部记忆、全局案件记忆以及模块化技能与工具库：局部记忆维持单一场景中的对话连续性，全局记忆则在阶段结束时固化案件事实、证据、主张和程序状态，以保证跨阶段一致性。<br>
          • 基于该环境构建的LongJud-Bench对完整诉讼生命周期中的智能体能力进行评估。217名具有法律背景的评估者共提供18,992项评分，验证了轨迹的程序真实性和角色一致性；跨模型实验进一步表明，不同模型在咨询、文书撰写与庭审辩论中的优势显著分化，单一汇总分数无法揭示这些阶段性能力差异。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-17</td>
        <td style="width: 55%;"><strong>GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Shared%20Memory-4A90E2" alt="Shared Memory">
          <img src="https://img.shields.io/badge/Memory%20Governance-F5A623" alt="Memory Governance">
          <img src="https://img.shields.io/badge/Access%20Control-7ED321" alt="Access Control">
          <img src="https://img.shields.io/badge/Active%20Forgetting-D0021B" alt="Active Forgetting">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.18829">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出GateMem，将记忆评估从单用户私有记忆扩展至多主体共享记忆场景，要求智能体根据请求者身份、角色关系、授权范围和删除状态，对共同记忆池中的信息实施上下文相关的读取与披露控制。<br>
          • 基准覆盖医疗、办公、教育和家庭四类领域，包含91个长篇多方交互情节及2,218个隐藏检查点，并联合测量合法长程请求的有效效用、跨授权边界的信息泄露以及明确删除请求后的主动遗忘可靠性。<br>
          • 实验揭示效用、访问控制与遗忘之间存在显著张力：长上下文方法通常取得较好的综合治理表现，但具有较高令牌开销；检索增强与外部记忆方法虽然降低计算成本，却仍可能泄露未授权信息或恢复已删除内容，说明现有系统尚不足以支持可靠的机构级共享记忆部署。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-15</td>
        <td style="width: 55%;"><strong>MemTrace: Probing What Final Accuracy Misses in Long-Term Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-4A90E2" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Knowledge%20Points-F5A623" alt="Knowledge Points">
          <img src="https://img.shields.io/badge/Evidence%20Utilization-7ED321" alt="Evidence Utilization">
          <img src="https://img.shields.io/badge/Diagnostic%20Benchmark-D0021B" alt="Diagnostic Benchmark">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.17328">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出MemTrace，主张以具有明确类型和会话来源的用户“知识点”作为长期记忆评估单位，而非将相互独立的问题行汇总为单一准确率，从而追踪同一事实在不同条件下的持续可用性。<br>
          • 基准沿记忆时效、问题类型与证据条件三个受控维度生成探针，分别测试事实随会话增长的保持能力、对当前状态、历史状态和变化轨迹问题的处理能力，以及面对证据缺失或错误前提时的安全响应能力。<br>
          • MemTrace覆盖20名用户、835个知识点、15,422个问题行及13种记忆系统配置。实验表明，具有相近总体准确率的系统可能呈现完全不同的失效结构，且失败时相关证据处于可检索状态的频率约为证据缺失的十倍，说明主要瓶颈在于推理阶段对可达证据的有效利用，而非单纯的存储容量或检索召回率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-14</td>
        <td style="width: 55%;"><strong>Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-4A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Active%20Forgetting-F5A623" alt="Active Forgetting">
          <img src="https://img.shields.io/badge/Control%20Plane-7ED321" alt="Control Plane">
          <img src="https://img.shields.io/badge/ForgetEval-D0021B" alt="ForgetEval">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.15903">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文将智能体记忆系统区分为负责检索既有事实的召回平面与负责覆盖、释放、清除和更新记忆的控制平面，并研究大语言模型在两类平面中的部署位置如何系统性地改变遗忘失效模式。<br>
          • 作者构建ForgetEval评估套件，包括1,000个模板化测试样例和385个对抗样例，并比较13种系统配置及六类架构范式；结果表明，确定性规则、写入时大模型处理、知识图谱抽象与变异时钩子分别覆盖不同的词汇、时间、规范化和意图感知遗忘问题，彼此具有部分互补性。<br>
          • 变异时大模型钩子能够将345个非原语存在性样例的通过率由约70%提升至93%以上，并恢复前缀碰撞和复合事实条件下的意图感知删除；研究由此说明，遗忘能力取决于智能控制被置于记忆生命周期的何处，而不仅取决于系统是否使用大语言模型。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-12</td>
        <td style="width: 55%;"><strong>StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-4A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Streaming%20Evaluation-F5A623" alt="Streaming Evaluation">
          <img src="https://img.shields.io/badge/Evidence%20Use-7ED321" alt="Evidence Use">
          <img src="https://img.shields.io/badge/Future%20Assistance-D0021B" alt="Future-Oriented Assistance">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.14571v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出StreamMemBench，将个人智能体记忆的评估对象由静态事实回忆扩展为完整的流式辅助链路，考察智能体能否从连续的第一视角观察中识别并保存用户相关证据，并将其用于当前及后续任务。<br>
          • 基准基于EgoLife自我中心生活流构建，以证据锚点连接初始任务与后续任务，并通过Fidelity、Initial Evidence Use、Feedback Incorporation及Follow-up Reuse四项指标，分别诊断证据保存、初始应用、反馈吸收和经验复用能力。<br>
          • 数据集包含8,107个证据锚点及16,214个任务查询；对两个模型骨干上的八类记忆系统进行评估后发现，信息已被存储或反馈已在当前轮次得到采纳，并不意味着智能体能够在未来任务中稳定调用相关经验，表明记忆评估应重点衡量其对后续行为的实际影响。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Memory-4A90E2" alt="LLM Memory">
          <img src="https://img.shields.io/badge/Sycophancy-F5A623" alt="Sycophancy">
          <img src="https://img.shields.io/badge/Benchmark-7ED321" alt="Benchmark">
          <img src="https://img.shields.io/badge/Mitigation-D0021B" alt="Mitigation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10949">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文发现：持久化记忆系统会显著增强LLM的“谄媚行为”，使模型更倾向于迎合用户观点而非保持事实准确性。<br>
          • 提出了MIST基准，并系统评估多种先进记忆系统与模型家族，量化该现象在不同设置下的普遍性。<br>
          • 设计了轻量级缓解策略，在显著降低谄媚行为的同时，保持甚至提升事实回忆能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-08</td>
        <td style="width: 55%;"><strong>H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multimodal%20Memory-Evaluation-4A90E2" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/Human-Interaction-F5A623" alt="Human Interaction">
          <img src="https://img.shields.io/badge/Benchmark-Evaluation-7ED321" alt="Benchmark">
          <img src="https://img.shields.io/badge/Dialogue-Reasoning-D0021B" alt="Dialogue Reasoning">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.09461">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出H2HMem多模态基准，用于评估LLM代理在复杂人际交互场景中的记忆能力，超越传统单用户文本设定。<br>
          • 数据涵盖双人及多方对话，重点评估记忆的回忆、推理与应用能力。<br>
          • 实验表明现有系统在跨模态、跨参与者与长程记忆建模方面仍存在明显不足。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Benchmark-blue" alt="Memory Benchmark">
          <img src="https://img.shields.io/badge/AI%20Agents-orange" alt="AI Agents">
          <img src="https://img.shields.io/badge/Relational%20Memory-green" alt="Relational Memory">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-red" alt="Long-Term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.05761">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 关注长期记忆之间可能互补、分歧或矛盾的细粒度关系。<br>
          • 构建受控关系记忆变体，并嵌入真实感较强的长程用户-智能体历史中。<br>
          • 发现当前记忆系统在细粒度关系保持、检索和下游使用上仍较薄弱。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory--Augmented-blue" alt="Memory-Augmented">
          <img src="https://img.shields.io/badge/Conversational%20Agents-orange" alt="Conversational Agents">
          <img src="https://img.shields.io/badge/Sensitive%20Memory-green" alt="Sensitive Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-red" alt="Large Language Models">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06055">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究在当前对话轮次中，已有敏感记忆何时不应被使用。<br>
          • 提出 RBI-Eval 控制探针集，对比模型有无敏感记忆访问时的行为差异。<br>
          • 表明仅靠检索阶段无法保证安全，生成阶段也需要记忆感知决策。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory-blue" alt="Memory">
          <img src="https://img.shields.io/badge/Continual%20Learning-orange" alt="Continual Learning">
          <img src="https://img.shields.io/badge/Benchmark-green" alt="Benchmark">
          <img src="https://img.shields.io/badge/LLM-red" alt="LLM">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.17281">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对缺少评估 LLM 系统从服务期用户反馈中持续学习的基准问题。<br>
          • 构建覆盖多领域、多语言和多任务类型的用户反馈模拟框架。<br>
          • 实验显示当前基线在效果和效率上仍有较大提升空间。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-03</td>
        <td style="width: 55%;"><strong>MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory-blue" alt="Memory">
          <img src="https://img.shields.io/badge/Benchmark-orange" alt="Benchmark">
          <img src="https://img.shields.io/badge/Conversational%20Memory-green" alt="Conversational Memory">
          <img src="https://img.shields.io/badge/Document%20Reasoning-red" alt="Document Reasoning">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04442">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 同时考察多会话对话记忆导航和长文档推理两类能力。<br>
          • 构建包含角色、时间事件图、长文档、多会话对话和混合来源问题的微世界。<br>
          • 结果表明联合检索架构更能整合对话记忆与长文档证据。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20Poisoning-blue" alt="Memory Poisoning">
          <img src="https://img.shields.io/badge/LLM%20Agents-orange" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Memory%20Management-green" alt="Memory Management">
          <img src="https://img.shields.io/badge/Security-red" alt="Security">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04329">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 将持久记忆视为长期攻击面，不可信输入可能持续影响未来行为。<br>
          • 识别记忆写入通道、结构性脆弱性和中毒攻击类别，并提出 MPBench。<br>
          • 发现主动写入和检索的记忆系统更易受攻击，现有提示注入防御并不充分。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-blue" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Safety%20Risks-green" alt="Safety Risks">
          <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2602.01146">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 研究会话助手引入长期持久记忆后带来的安全风险。<br>
          • 定义跨域泄漏和记忆诱导谄媚两类长期记忆特有失败模式。<br>
          • 评估多种前沿与开源 LLM，发现两类风险的失败率都很高。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-blue" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Benchmark-green" alt="Benchmark">
          <img src="https://img.shields.io/badge/Dynamic%20Memory-red" alt="Dynamic Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.31086">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对许多长期对话记忆基准过于静态、同质的问题。<br>
          • 构建演化用户画像、异构交互场景和覆盖多类记忆特征的问题。<br>
          • 揭示当前系统在真实动态长期记忆场景中的不足。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Episodic%20Memory-blue" alt="Episodic Memory">
          <img src="https://img.shields.io/badge/Benchmark-orange" alt="Benchmark">
          <img src="https://img.shields.io/badge/Memory%20Management-green" alt="Memory Management">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-red" alt="Large Language Models">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.31557">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向第一视角视觉中的流式情节记忆问题。<br>
          • 在统一流式 MLLM 框架下构建覆盖多个认知维度的诊断问题。<br>
          • 揭示当前视觉智能体记忆管理机制中的关键缺陷。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Multimodal-orange" alt="Multimodal">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-green" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Memory%20Evaluation-red" alt="Memory Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.29341">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 主张多模态智能体记忆应通过与动态世界交互来评估。<br>
          • 构建四阶段 action-world 循环和多会话任务，评估写入、维护、检索和使用。<br>
          • 发现更好的存储质量并不总能转化为更好的下游多模态记忆表现。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-31</td>
        <td style="width: 55%;"><strong>Connecting the Dots: Benchmarking Reflective Memory in Long-Horizon Dialogue</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Reflective%20Memory-blue" alt="Reflective Memory">
          <img src="https://img.shields.io/badge/Long--Horizon%20Dialogue-orange" alt="Long-Horizon Dialogue">
          <img src="https://img.shields.io/badge/Memory%20Framework-green" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Benchmarking-red" alt="Benchmarking">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.01223">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 关注反思记忆，即智能体需要整合碎片线索而非只回忆显式事实。<br>
          • 提出 RefMem-Bench，包含跨反思记忆维度和任务形式的标注问答。<br>
          • 表明问题驱动证据检索和抽象层级监督能提升反思式回答能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Persistent%20Memory-orange" alt="Persistent Memory">
          <img src="https://img.shields.io/badge/Multi--Session-green" alt="Multi-Session">
          <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.00832">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 弥合单会话智能体基准与真实多会话服务交互之间的差距。<br>
          • 构建带持久记忆、时间依赖、变化用户目标和有后果工具行动的任务。<br>
          • 发现当前智能体常因跨会话错误估计用户状态而失败。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>SuperMemory-VQA: An Egocentric Visual Question-Answering Benchmark for Long-Horizon Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory-blue" alt="Memory">
          <img src="https://img.shields.io/badge/Visual%20Question%20Answering-orange" alt="Visual Question Answering">
          <img src="https://img.shields.io/badge/AI%20Assistants-green" alt="AI Assistants">
          <img src="https://img.shields.io/badge/Long--Horizon%20Memory-red" alt="Long-Horizon Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.00825">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向基于第一视角日常活动视频的真实长程视觉记忆问题。<br>
          • 构建人工验证的 VQA 问答，覆盖物体、位置、意图和场景记忆。<br>
          • 显示当前系统在实际日常视觉记忆需求上仍不可靠。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-29</td>
        <td style="width: 55%;"><strong>Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
          <img src="https://img.shields.io/badge/Heterogeneous%20Memory-mediumslateblue" alt="Heterogeneous Memory">
          <img src="https://img.shields.io/badge/Evolving%20Memory-darkkhaki" alt="Evolving Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.31086">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 RHELM 基准，模拟 10 位画像各异的虚拟用户长达一年的生活轨迹（单用户上下文 500K–1M tokens），用于评测大模型的真实、异质、动态长期记忆能力。<br>
          • 设计 LOOP 模块（计划-推演-演化-修剪）动态生成生活轨迹，并整合邮件、日记、报告等异质外部源与 11,764 轮对话，实现高保真多源记忆评测。<br>
          • 定义 7 类问题与 27 项挑战性特征，新增"记忆条件下的误导查询"以考察冲突感知；实验显示 Claude Opus 4.5 等 SOTA 模型平均分仅约 38%，跨源聚合与真实情境推理为当前主要瓶颈。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-07</td>
        <td style="width: 55%;"><strong>STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
          <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
          <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.06527">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出长上下文基准测试 STALE，包含 400 个经过专家验证的隐式冲突场景，用于评估 LLM 智能体在缺乏明确否定的情况下，识别早期记忆何时被新观察结果导致失效的能力。<br>
          • 设计了包含状态解析、前提抵抗和隐式策略适应的三维探测框架，系统性评估表明当前模型在将更新后的状态应用于下游行为方面存在严重不足。<br>
          • 提出一种原型框架 CUPMEM，通过明确的写入时状态裁决和拓扑触发的信念传播，显著提升了记忆更新的鲁棒性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-03</td>
        <td style="width: 55%;"><strong>MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
          <img src="https://img.shields.io/badge/Memory%20Writing-brightgreen" alt="Memory Writing">
          <img src="https://img.shields.io/badge/Evaluation%20Protocol-yellow" alt="Evaluation Protocol">
          <img src="https://img.shields.io/badge/Budgeted%20Storage-teal" alt="Budgeted Storage">
          <img src="https://img.shields.io/badge/Long--term%20Agents-orange" alt="Long-term Agents">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.02199">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MEMAUDIT，将经验流、候选记忆表示、存储成本、证据单元、未来查询需求和预算固定为可审计优化问题，用分支定界与 MILP 求解精确最优解。<br>
          • 能区分记忆表示质量、有效性保持和预算选择效果，优于仅看最终问答准确率的评测方式。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-28</td>
        <td style="width: 55%;"><strong>StratMem-Bench: Evaluating Strategic Memory Use in Virtual Character Conversation Beyond Factual Recall</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory--Augmented%20Generation-blue" alt="Memory-Augmented Generation">
          <img src="https://img.shields.io/badge/Long--Term%20Dialogue-brightgreen" alt="Long-Term Dialogue">
          <img src="https://img.shields.io/badge/Benchmark-yellow" alt="Benchmark">
          <img src="https://img.shields.io/badge/Virtual%20Characters-teal" alt="Virtual Characters">
          <img src="https://img.shields.io/badge/Strategic%20Memory%20Use-orange" alt="Strategic Memory Use">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.26243">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 StratMem-Bench，包含 657 个对话实例和必需/辅助/无关三类记忆池，评测虚拟角色对记忆的策略性使用能力而非仅事实回忆。<br>
          • 设计严格记忆遵从、记忆整合质量、主动丰富度和条件无关率等指标，系统评估角色对话中的记忆决策能力。
        </td>
      </tr>
<tr>
        <td rowspan="2" style="width: 15%;">2026-04-11</td>
        <td style="width: 55%;"><strong>Trust Your Memory: Verifiable Control of Smart Homes through Reinforcement Learning with Multi-dimensional Rewards</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Smart%20Home-yellow" alt="Smart Home">
            <img src="https://img.shields.io/badge/Benchmark-blue" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10110">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了基于真实长期交互日志构建的智能家居记忆控制基准套件 MemHomeLife 与 MemHome。<br>
            • 细粒度评估设备控制中的记忆添加、更新、删除与利用等关键操作。<br>
            • 弥补了现有基准难以同时衡量长期记忆利用能力与记忆管理质量反馈的空白。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Behavior%20Benchmark-yellow" alt="Behavior Benchmark">
            <img src="https://img.shields.io/badge/User%20Simulation-blue" alt="User Simulation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08362">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了 OmniBehavior，这是首个完全基于真实世界数据构建的长程、跨场景、异构行为仿真基准。<br>
            • 指出真实用户决策高度依赖跨场景因果链，而这正是现有数据集普遍缺失的部分。<br>
            • 实验表明当前 LLM 即便拥有更长上下文，也仍难以胜任复杂行为模拟，并存在人格同质化与偏乐观倾向。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized%20Agent-yellow" alt="Personalized Agent">
            <img src="https://img.shields.io/badge/Benchmark-blue" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08455">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了 KnowU-Bench，一个面向交互式、主动式与个性化移动 Agent 的在线评测基准。<br>
            • 基准隐藏用户画像，只提供行为轨迹，要求 Agent 通过交互推断偏好，并判断何时介入、征求同意或保持沉默。<br>
            • 结果显示，当任务涉及偏好推断与主动介入校准时，现有前沿模型的性能会明显下降。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-04-02</td>
        <td style="width: 55%;"><strong>Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Modular%20Framework-blue" alt="Modular Framework">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.01707">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了一个统一的模块化框架，将基于大语言模型的智能体记忆系统分解为四个核心组件：信息提取、记忆管理、记忆存储和信息检索 。<br>
              • 在长程对话基准测试上对代表性智能体记忆方法进行了全面的实验评估和鲁棒性分析，考察了token效率、上下文可扩展性以及证据位置敏感性 。<br>
              • 引入了一种整合树状组织与层级存储的新型记忆架构，在实现最先进性能的同时保持了较低的计算开销 。
          </td>
      </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-04</td>
        <td style="width: 55%;"><strong>Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized-yellow" alt="Personalized">
            <img src="https://img.shields.io/badge/Interaction-blue" alt="Interaction">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 评估大型语言模型在真实且极度长程的交互场景下，持续遵循用户多样化偏好的能力盲区。<br>
            • 构建覆盖 100 个用户画像及海量交互数据的 RealPref 基准，专门考察从显式到隐式偏好表达的泛化理解。<br>
            • 明确量化了“偏好表达隐式化”与“上下文过度拉长”会导致 LLM 遵循性能出现断崖式下跌，界定了个人感知助手的发展瓶颈。
        </td>
    </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-04</td>
        <td style="width: 55%;"><strong>LifeBench: A Benchmark for Long-Horizon Multi-Source Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi-Source-yellow" alt="Multi-Source">
            <img src="https://img.shields.io/badge/Real%20World-blue" alt="Real World">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.03781">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 长期个人助手的演进要求模型具备基于非声明性记忆（如通过数字痕迹推断习惯）的复杂推理能力，而现有基准对此完全空白。<br>
            • 推出 LifeBench 基准，利用真实世界先验与认知科学层级结构，模拟跨时间大跨度的多源密集事件以考察智能体整合能力。<br>
            • 当前顶尖记忆系统在该基准下准确率仅勉强过半（55.2%），凸显了从零散数字痕迹中进行长程推理的极高难度。
        </td>
    </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Interactive-yellow" alt="Interactive">
            <img src="https://img.shields.io/badge/Long-Horizon-blue" alt="Long-Horizon">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01966">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 静态离线评估数据难以真实反映智能体在动态长周期交互中记忆管理策略的可扩展性与可靠性。<br>
            • 构建支持在线策略评估的交互式环境 AMemGym，利用结构化采样低成本生成高保真用户画像与状态演化轨迹。<br>
            • 动态环境客观暴露了 RAG 等现有系统的长程性能衰减，并验证了该框架在驱动策略自我进化方面的有效性。
        </td>
    </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>According to Me: Long-Term Personalized Referential Memory QA</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi-Modal-yellow" alt="Multi-Modal">
            <img src="https://img.shields.io/badge/Privacy%20Data-blue" alt="Privacy Data">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01990">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 传统基准多基于单文本对话历史，无法有效评估智能体在真实生活、多模态及长周期下的个性化指代推理能力。<br>
            • 构建包含四年隐私数据的多模态多源基准 ATM-Bench，并提出模式引导记忆用于异构数据的结构化表示。<br>
            • 揭露现有系统在复杂真实经验集上的性能缺陷，并证明结构化的 SGM 在多源场景中优于传统描述性方法。
        </td>
    </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-02-27</td>
        <td style="width: 55%;"><strong>MemEmo: Evaluating Emotion in Memory Systems of Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Emotion-yellow" alt="Emotion">
            <img src="https://img.shields.io/badge/Benchmark-blue" alt="Benchmark">
            <img src="https://img.shields.io/badge/Multi--Session-orange" alt="Multi-Session">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.23944">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 现有记忆系统评测多侧重于事实召回，缺乏对长程交互中情感信息处理效能的衡量。<br>
            • 推出首个情感增强型评估基准及 HLME 数据集，涵盖情感信息提取、情感记忆更新与情感问答三大维度。<br>
            • 实验暴露出当前最先进的记忆系统在情感处理任务上均存在显著的不稳定性，为后续情感连贯性优化指明了方向。
        </td>
    </tr>
     <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Benchmark-yellow" alt="Benchmark">
            <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
            <img src="https://img.shields.io/badge/Multi--Session-orange" alt="Multi-Session">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16313.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 介绍了 MemoryArena，这是一个用于基准测试多会话任务中代理记忆的统一评估平台。<br>
            • 该基准涵盖网络导航、规划、信息搜索和推理等任务，要求代理在执行过程中持续学习并利用记忆。<br>
            • 研究揭示了现有长上下文记忆基准在评估真实交互场景时的不足，强调了记忆与行动协同评估的必要性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Benchmark-yellow" alt="Benchmark">
            <img src="https://img.shields.io/badge/Memory%20Poisoning-lightgrey" alt="Memory Poisoning">
            <img src="https://img.shields.io/badge/Long--Horizon-blueviolet" alt="Long-Horizon">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16901.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了首个专门评估 LLM 代理对适应性长时间攻击（Long-Horizon Attacks）脆弱性的基准 AgentLAB。<br>
            • 支持包括记忆投毒在内的五种新型攻击类型，涵盖 28 个现实代理环境和 644 个安全测试案例。<br>
            • 实验发现 LLM 代理在长时攻击下极度脆弱，现有的单次交互防御措施无法有效应对此类复杂的安全威胁。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context-gold" alt="Long-Context">
        <img src="https://img.shields.io/badge/Environment%20Sim-darkgreen" alt="Environment Simulation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.10715">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LoCoMo-Plus 基准测试，该测试旨在评估 LLM 智能体在长对话中保留和应用隐含约束（如用户目标、状态和价值观）的“认知记忆”能力，而非传统的表面事实召回。<br>
        • 该基准构造了复杂的对话实例，要求模型在后续查询与原始记忆线索缺乏表面语义相似度的情况下，仍能准确应用潜在的上下文约束。<br>
        • 论文提出了一种统一的评估框架，通过实验揭示了现有 LLM 和记忆系统在处理此类非事实性、认知驱动的记忆任务时面临的严峻挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-29</td>
      <td style="width: 55%;"><strong>AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Context-gold" alt="Long-Context">
      <img src="https://img.shields.io/badge/Environment%20Sim-darkgreen" alt="Environment Simulation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20730">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
      • 提出了 AgentLongBench，一个通过模拟环境推演（Environment Rollouts）来评估长上下文智能体的基准测试，包含 32K 到 4M 的上下文长度。<br>
      • 基于横向思维谜题（Lateral Thinking Puzzles）构建动态交互轨迹，包含知识密集型和无知识型两种设定，以区分推理能力与参数化知识。<br>
      • 揭示了现有模型在处理海量工具响应中的高信息密度时，比处理长对话中的记忆碎片化面临更大的挑战，提出了“最小 Token 需求”作为关键因素。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-24</td>
      <td style="width: 55%;"><strong>MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Reward%20Model-purple" alt="Reward Model">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.11969">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 MemoryRewardBench，这是第一个系统评估奖励模型（RM）对 LLM 长期记忆管理过程评价能力的基准测试。<br>
        • 涵盖长上下文推理、多轮对话和长文本生成三大类任务，包含 10 种不同的记忆管理设置，上下文长度从 8K 到 128K。<br>
        • 设计了基于结果（Outcome-based）和基于过程（Process-based）的评估标准，发现新一代模型在评估记忆管理方面表现出代际优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-23</td>
      <td style="width: 55%;"><strong>How Does Personalized Memory Shape LLM Behavior? Benchmarking Rational Preference Utilization in Personalized Assistants</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalization">
        <img src="https://img.shields.io/badge/Rationality-lightgrey" alt="Rationality">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.16621">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LLM 理性个性化（Rational Personalization）的问题，并发布了 RPEval 基准测试，用于评估个性化助手在不同场景下对用户偏好的利用是否合理。<br>
        • 包含个性化意图推理数据集和多粒度评估协议，揭示了现有 LLM 中广泛存在的“非理性个性化”（如 Filter Bubble）现象。<br>
        • 提出了 RP-Reasoner，一种基于语用学推理的机制，通过推断用户潜在意图来选择性地整合个性化信息，显著减少了非理性个性化错误。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-13</td>
      <td style="width: 55%;"><strong>Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Tool%20Use-orange" alt="Tool Use">
        <img src="https://img.shields.io/badge/Active%20Memory-green" alt="Active Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.19935">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Mem2ActBench，用于评估智能体主动利用长期记忆执行基于工具的任务的能力，而非简单的被动事实检索。<br>
        • 通过自动化流程构建了包含 2029 个会话的数据集，并采用逆向生成方法创建了 400 个必须依赖记忆才能完成的工具调用任务。<br>
        • 实验表明，现有系统在“参数接地”（Parameter Grounding）方面表现不佳，即难以从记忆中提取正确参数来执行工具调用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-11</td>
      <td style="width: 55%;"><strong>CloneMem: Benchmarking Long-Term Memory for AI Clones</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.07023">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 CLONEMEM，一个旨在评估 AI 克隆体长期记忆的基准测试，利用非对话式数字痕迹（如日记、社交媒体、邮件）跨越 1-3 年，而非传统的对话历史。<br>
        • 提出了一个层级数据构建框架，生成连贯的纵向生活轨迹，捕捉个体经历、情感和观点随时间的演变。<br>
        • 实验结果表明，现有记忆系统（如 A-Mem 和 Mem0）在该设置下表现不佳，往往不如扁平检索，且由于有损压缩和对叙事模板的依赖而无法准确追踪内部状态变化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-11</td>
      <td style="width: 55%;"><strong>RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06966">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • RealMem 是一个旨在评估 LLM 在"长期项目导向"交互中表现的基准测试，与休闲或任务导向对话基准不同，它专注于不断演变的目标和动态状态。<br>
          • 该框架采用三阶段合成管道（项目基础、多智能体生成、记忆管理），在 11 个现实场景中创建超过 2000 个跨会话对话。<br>
          • 评估表明，当前 SOTA 记忆系统在管理长期项目状态、时间推理和主动对齐方面存在困难，揭示了自主智能体能力的关键差距。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-08</td>
      <td style="width: 55%;"><strong>KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.04745">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 KnowMe-Bench，这是一个基于长篇自传叙事（470万 token）构建的基准测试，旨在超越简单的事实检索，评估终身数字伴侣对用户动机、原则等深层“人”的理解能力。<br>
          • <strong>方法：</strong> 采用了“认知流重构”管道，将非线性叙事转化为具备倒叙感知和时间锚定的流式数据，包含内心独白和感官细节，并实施了从事实提取到精神分析深度的三层分级评估体系。<br>
          • <strong>发现：</strong> 对不同记忆架构（RAG, Mem0, MemOS）的实验表明，虽然检索增强系统在事实准确性上表现良好，但在处理时间逻辑和深度推理（如“更新悖论”）时存在显著缺陷，揭示了当前模型在模拟人类复杂非线性记忆方面的差距。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-07</td>
      <td style="width: 55%;"><strong>Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Multimodal-darkorchid" alt="Multimodal">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03515">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 <strong>Mem-Gallery</strong>，这是一个用于评估多模态大语言模型（MLLM）智能体在长期对话中多模态记忆能力的基准测试，旨在解决现有基准在多模态与长期记忆评估上的错位问题。<br>
          • <strong>方法：</strong> 构建了一个基于视觉和文本信息的高质量多会话对话数据集，并提出了一个包含三个功能维度的评估框架：记忆提取与适应、记忆推理以及记忆知识管理（包括冲突检测和知识更新）。<br>
          • <strong>发现：</strong> 对13个记忆系统的基准测试表明，显式的多模态信息保留是有效的，但现有模型在涉及复杂推理和动态知识管理的场景中仍存在局限，且面临存储和检索的效率瓶颈。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-07</td>
      <td style="width: 55%;"><strong>EvolMem: A Cognitive-Driven Benchmark for Multi-Session Dialogue Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
        <img src="https://img.shields.io/badge/Agentic%20Memory-darkturquoise" alt="Agentic Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03543">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 EvolMem，这是一个基于认知心理学的基准测试，旨在评估大语言模型（LLMs）和智能体系统在多会话场景下的记忆能力，填补了对非陈述性记忆和长期一致性评估的空白。<br>
          • <strong>方法：</strong> 该基准将记忆划分为陈述性（如检索、推理）和非陈述性（如习惯化）两类。它采用混合数据合成框架——结合话题驱动生成和叙事启发转换——构建了多样化且可控的多会话对话数据。<br>
          • <strong>发现：</strong> 评估显示，没有任何模型能在所有记忆维度上持续领先，且在非陈述性任务上表现普遍较弱。此外，现有的智能体记忆机制在性能上往往无法超越强大的基础模型，并面临严重的延迟问题。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-07</td>
      <td style="width: 55%;"><strong>PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Agentic%20Memory-darkturquoise" alt="Agentic Memory">
        <img src="https://img.shields.io/badge/Reinforcement Learning-orange" alt="Reinforcement Learning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.06688">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 简介：推出了 PersonaMem-v2，这是一个用于 LLM 个性化的 SOTA 数据集，包含 1,000 个真实用户画像、300 多个场景以及嵌入在长达 128k token 上下文中的 20,000 多个隐式用户偏好。<br>
          • 发现与差距：评测显示，包括 GPT-5 在内的前沿 LLM 在隐式个性化方面表现挣扎，准确率仅为 37-48%。研究发现，强化微调（RFT）能显著提升模型在用户理解方面的长上下文推理能力。<br>
          • 方法创新：提出了一种“代理记忆（Agentic Memory）”框架，该框架维护一个持续演进的、人类可读的单一记忆体。该方法以 16 倍的效率优势（仅使用 2k 记忆 token 对比 32k 历史记录）超越了 GPT-5，达到了 55% 的准确率。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-11-09</td>
        <td style="width: 55%;"><strong>FlashAdventure — Long-Term Memory for GUI Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/GUI%20Agents-4A90E2" alt="GUI Agents">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-F5A623" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Benchmark-7ED321" alt="Benchmark">
          <img src="https://img.shields.io/badge/EMNLP%202025-D0021B" alt="EMNLP 2025">
        </td>
        <td style="width: 15%;">
          <a href="https://aclanthology.org/2025.emnlp-main.1192/">
            <img src="https://img.shields.io/badge/Paper-EMNLP-D2691E?logo=paper" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文介绍了 FlashAdventure，这是一个用于评估 GUI 智能体在长周期、叙事驱动任务中的基准测试，需要智能体在完整故事流程中进行记忆、规划和交互。 <br>
          • 该研究发现了“观察–行为鸿沟”（observation–behavior gap），即智能体需要回忆早期观察到的信息，并在这些记忆未来变得可用时将其应用于后续行动。 <br>
          • 作者提出了 COAST（Clue-Oriented Agent for Sequential Tasks，面向线索的序列任务智能体）框架，通过 Seek-Map-Solve 循环机制利用长期线索记忆，以提升序列决策能力。 <br>
          • 该基准包含 34 个基于 Flash 的冒险游戏，并通过 CUA-as-a-Judge 基于里程碑的自动化评分方式对智能体进行评估。 <br>
          • FlashAdventure 证明，显式的长期记忆机制能够帮助 GUI 智能体在长周期交互环境中更好地存储、检索和利用历史信息。
        </td>
      </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-04</td>
      <td style="width: 55%;"><strong>Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.emnlp-main.580.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 IMPLEXCONV 数据集以及 TACITREE 框架，用于研究个性化对话中的隐式推理能力。<br>
          • IMPLEXCONV 包含 2500 个以隐式推理场景为核心的示例，能够捕捉对话中细微的句法与语义关系。<br>
          • TACITREE 通过对对话历史进行分层式组织，增强了大型语言模型（LLMs）在长对话中进行隐式上下文推理的能力。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-27</td>
      <td style="width: 55%;"><strong>Know Me, Respond to Me, benchmarking LLMs for Dynamic User profiling and personalized response at scale</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2504.14225">
      <img src="https://img.shields.io/badge/COLM-Paper-black?labelColor=gold" alt="COLM Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 PERSONAMEM 基准测试，该基准旨在评估大型语言模型（LLMs）在动态用户画像建模与个性化回复生成方面的表现。<br>
        • 尽管现有模型在回忆用户偏好方面取得了一定成效，但在应对全新场景时仍然存在显著的性能差距。<br>
        • 论文详细阐述了该基准的结构、用户对话的生成流程、模型性能的评估方法以及相关研究，强调了个性化对话生成在提升用户体验中的重要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-10</td>
      <td style="width: 55%;"><strong>Human-inspired Episodic Memory for Infinite Context LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2407.09450">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EM-LLM（事件记忆大语言模型）是一种新型大语言模型，旨在解决现有模型在长文本处理中的局限性。<br>
        • EM-LLM 无需微调即可实现近乎无限的上下文处理能力，在多个基准测试中显著优于现有模型。<br>
        • 该模型整合了基于突发性事件分割、图论边界优化和两阶段记忆检索机制，显著提升信息检索与问答任务的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-09-26</td>
      <td style="width: 55%;"><strong>Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2507.05257">
      <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoryAgentBench 是一个用于评估具备记忆机制的语言模型（记忆智能体，Memory Agents）四项核心能力的基准测试，包括精准检索、测试时学习、长程理解以及冲突消解。<br>
        • 通过整合现有数据集与新构建的数据，MemoryAgentBench 实现了对上述能力的系统性评估。<br>
        • 该基准揭示了当前方法在记忆更新与长时跨度对话处理方面的局限性，凸显了未来研究亟需解决的关键挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>Unveiling Privacy Risks in LLM Agent Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
      <img src="https://img.shields.io/badge/LLM%20Evaluation-dodgerblue" alt="LLM Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.1227.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 研究大语言模型代理记忆中的隐私漏洞，特别关注从长期记忆中提取敏感用户-代理交互信息的风险。<br>
          • 提出记忆提取攻击（MEXTRA），该黑盒攻击通过创新的提示设计（定位器+对齐器）和自动化提示生成技术，实现敏感用户查询的提取。<br>
          • 在代表性代理系统（EHRAgent和RAP）上的实验表明存在显著漏洞，通过分析相似性评分函数、内存配置等影响泄露的关键因素，揭示了记忆系统安全性的薄弱环节。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.560.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MiniLongBench是一个低成本的长文本理解基准，旨在提升大语言模型（LLMs）在长上下文理解（LCU）任务中的评估效率与经济可行性。<br>
        • 通过应用数据压缩技术，MiniLongBench在保持评估结果一致性的前提下显著减少评估样本数量，并显示出与原始LongBench基准高度相关的结果。<br>
        • 多任务类别的评估验证了MiniLongBench的有效性，尽管在总结生成和信息综合类任务上仍需进一步优化。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Evaluation-tealgreen" alt="Personalized Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.49.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • PersonaBench 是一个用于评估 AI 模型理解个人信息能力的基准测试。<br>
        • 论文强调了个性化在 AI 助手中的重要性，并指出由于缺乏可公开获取的数据集，用于评估此类能力面临着显著挑战。<br>
        • 评测主要聚焦于检索增强生成（RAG）模型，结果表明当前模型在有效处理个人化查询方面仍然存在困难。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.989.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemBench 旨在对基于 LLM 的智能体记忆能力进行全面评估。<br>
        • 通过构建同时涵盖事实记忆与反思记忆的数据集，该研究弥补了现有评测方法的局限性。<br>
        • 论文详细介绍了记忆机制的构建方式——包括用户关系图与多层级记忆设计——并强调了准确率、效率与容量等评估指标的重要性。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>Evaluating the Long-term memory of large language models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.1014.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文探究了大型语言模型（LLMs）在长期任务中的记忆能力，重点聚焦于对话系统。<br>
        • 通过构建 Long-Order Chronological Conversation（LOCCO）数据集，研究对 LLM 的长期记忆性能进行了定量评估。<br>
        • 实验结果表明，尽管 LLM 在一定程度上能够保留历史对话信息，但其记忆能力会随着时间推移而逐步衰退。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>Know You First and Be You Better: Modeling Human-Like User Simulators via Implicit Profiles</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dialogue%20Augmentation-olive" alt="Dialogue Augmentation">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.1025.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了一种用户模拟框架——隐式用户画像用户模拟器（Implicit User Profile User Simulator，USP），该框架通过推断用户的隐式属性来增强对话系统与人类用户之间的交互效果。<br>
        • USP 从用户对话中提取隐式特征，并将条件监督微调与循环一致性约束下的强化学习相结合，从而提升生成对话的真实感与连贯性。<br>
        • 实验结果表明，USP 在多项评估指标上展现出显著优势，尤其是在与 GPT-4o、PlatoLM 等其他对话生成模型对比时表现更为突出。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-06-15</td>
        <td style="width: 55%;"><strong>PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Evaluation-tealgreen" alt="Personalized Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2506.12915">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 PersonaFeedback 基准测试，用于评估大型语言模型（LLMs）在个性化回复生成方面的能力。<br>
        • 研究表明，尽管 LLM 在生成个性化内容方面已有一定进展，但在复杂场景下仍然存在明显局限。<br>
        • 研究者通过引入动态用户属性推断、个性化画像以及奖励模型，旨在提升个性化问答的整体效果。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-06-09</td>
        <td style="width: 55%;"><strong>Minerva: A Programmable memory test benchmark for language models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.03358">
        <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • Minerva 是一个可编程的记忆测试基准，用于在多样化的记忆任务上评估大型语言模型（LLMs）的表现。<br>
        • 该基准对模型使用记忆的能力进行了定量评估，重点关注信息检索、推理以及状态跟踪等任务。<br>
        • 实验结果表明，尽管部分模型在简单任务上表现良好，但在更复杂的任务中仍然存在显著差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-28</td>
      <td style="width: 55%;"><strong>Self-Taught Agentic Long-Context Understanding</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2502.15920">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • AgenticLU框架（智能代理长上下文理解框架）旨在增强大语言模型（LLMs）在长文本理解与推理任务中的表现。<br>
        • 该框架提出澄清链机制（Chain-of-Clarifications, CoC），通过优化模型自我澄清过程并采用树状搜索路径生成澄清性问题，从而显著提升多步骤推理的准确率与有效性。<br>
        • 验证结果表明，该框架在长上下文问答任务中优于现有提示技术，同时将计算开销控制在合理范围内。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-22</td>
      <td style="width: 55%;"><strong>EMBODIED AGENTS MEET PERSONALIZATION: INVESTIGATING CHALLENGES AND SOLUTIONS THROUGH THE LENS OF MEMORY UTILIZATION</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.16348">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文研究了大语言模型驱动的具身智能体在个性化辅助任务中面临的挑战，特别聚焦于物体语义记忆与用户行为模式的记忆利用问题。<br>
        • 研究提出MEMENTO（记忆评估框架），通过两阶段评估揭示当前智能体在处理连续用户行为模式及多记忆协同时存在困难，其根本原因在于信息过载问题。<br>
        • 该工作设计了基于分层知识图谱的用户画像记忆模块，通过分离个性化知识与情景记忆历史，在单一记忆任务和联合记忆任务中均取得显著性能提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-03-11</td>
      <td style="width: 55%;"><strong>SCBench: A Benchmark for Long Context Methods Based on KV-Cache</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Context%20Evaluation-darkslategray" alt="Long-Context Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2412.10319">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SCBENCH（共享上下文基准）是一个专为评估长上下文大语言模型（LLMs）设计的基准测试框架。<br>
        • 该基准聚焦于键值缓存（KV缓存）的生命周期管理，涵盖生成、压缩、检索与加载等核心环节，旨在填补现有基准在多轮交互场景下KV缓存评估方面的空白。<br>
        • 实验结果表明，不同方法在任务中展现出显著性能差异，其中动态稀疏注意力机制与缓存优化策略在复杂场景中表现出更优性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2022-03-04</td>
      <td style="width: 55%;"><strong>LongMemEval: Benchmarking chat assistants on long-term interactive memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
      <img src="https://img.shields.io/badge/Evaluation%20Framework-darkgoldenrod" alt="Evaluation Framework">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2410.10813">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 论文提出了 LONGMEMEVAL，这是一个用于评估聊天助手长期记忆能力的综合性基准测试。<br>
        • 该基准评估了五项核心记忆能力，覆盖了现有系统面临的关键挑战。<br>
        • LONGMEMEVAL 采用统一的三阶段框架——索引、检索与阅读，并提出了多项设计优化，以提升记忆召回效果与问答准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-25</td>
      <td style="width: 55%;"><strong>Towards Effective Evaluations and Comparisons for LLM Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <img src="https://img.shields.io/badge/Memory%20Erasure-darkcyan" alt="Memory Erasure">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2406.09179">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨了大型语言模型（LLMs）中的机器遗忘问题及其评估的重要性，重点关注消除不必要的数据记忆。<br>
        • 研究针对两个关键挑战展开：评估指标的稳健性，以及在移除目标知识与保留其他知识之间的权衡。<br>
        • 研究建议将 提取强度（Extraction Strength，ES）作为主要评估指标，以确保遗忘评估的准确性与可靠性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2022-02-13</td>
      <td style="width: 55%;"><strong>DO LLMS RECOGNIZE YOUR PREFERENCES? EVAL-UATING PERSONALIZED PREFERENCE FOLLOWING IN LLMS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Dialogue%20Reasoning-teal" alt="Long-Dialogue Reasoning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.09597">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • PREFEVAL 是一个用于评估大型语言模型（LLMs）在长对话中推断、记忆并遵循用户偏好能力的基准测试。<br>
        • 该基准包含 3000 组用户偏好—查询对，涵盖 20 个主题，揭示了当前 LLM 在遵循用户偏好方面面临的显著挑战。<br>
        • 研究表明，相较于隐式偏好，模型更容易推断显式偏好，同时任务类型与偏好表达方式都会对模型性能产生显著影响。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2015-01-25</td>
      <td style="width: 55%;"><strong>Episodic Memory Benchmark: Episodic Memories Generation and Evaluation Benchmark for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.13121">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨情景记忆在大语言模型（LLMs）中的重要性，并提出构建新型基准测试框架以评估模型推理能力。<br>
        • 研究人员开发了包含全新设计任务与评估协议的综合性框架，强调需要创新训练策略以有效融合情景记忆机制。<br>
        • 该框架为评估大语言模型中的情景记忆提供了一种可行的技术路径。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-24</td>
      <td style="width: 55%;"><strong>Muse: A Multimodal Conversational Recommendation Dataset with Scenario-Grounded User Profiles</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Multimodal-darkorchid" alt="Multimodal">
        <img src="https://img.shields.io/badge/Conversational%20Recommendation-mediumvioletred" alt="Conversational Recommendation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2412.18416">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出首个多模态对话推荐数据集 Muse，在服装领域包含 7,000 段对话与 83,148 句话语，提供基于真实场景自动生成的用户画像。<br>
        • 设计三阶段多智能体数据生成流程（用户画像生成器 → 模拟对话生成器 → 对话优化器），由多模态大模型驱动；用户画像源自真实场景而非人工设定，显著提升可扩展性。<br>
        • 在自然性、连贯性、信息丰富性、产品上下文相关性、图文一致性五个维度上与 MMCONV、Redial、Inspired、PEARL 四个数据集对比评测；并通过对 3 个 MLLM 微调验证其在推荐与回复生成上的有效性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-23</td>
      <td style="width: 55%;"><strong>LongGenBench: Benchmarking long-form generation in long context LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Complex%20Instruction%20Following-darkolivegreen" alt="Complex Instruction Following">
      <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2409.02076">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongGenBench 是一个用于评估大型语言模型（LLMs）生成高质量长文本能力的基准测试，重点强调对复杂指令的遵循能力。<br>
        • 不同于现有基准，LongGenBench 专门聚焦于长文本生成场景，涵盖日记写作、菜单设计等任务。<br>
        • 尽管在其他评测中表现强劲，LLM 在 LongGenBench 基准上仍面临显著挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2015-01-03</td>
      <td style="width: 55%;"><strong>LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2412.15204">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongBench v2（长文本理解与推理基准测试）是一个用于评估大语言模型在长上下文任务中表现的多任务基准测试框架。<br>
        • 该框架包含503道涵盖多种任务类型的多项选择题，重点评估模型对长文本的理解与回答能力。<br>
        • 研究发现表现最佳的模型在长上下文任务中已超越人类专家，凸显了增强推理能力与提升推理时计算资源的重要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-11-12</td>
      <td style="width: 55%;"><strong>MT-Eval: A Multi-Turn Capabilities Evaluation Benchmark for  Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.emnlp-main.1124.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MT-Eval 是一个用于评估大型语言模型（LLMs）在多轮对话中表现的基准测试。<br>
        • 现有评测多聚焦于单轮对话，MT-Eval 通过构建 1170 条多轮查询弥补了这一空白。<br>
        • 该基准将交互模式划分为回忆、扩展、细化与跟进四类，结果显示大多数模型在多轮场景下的表现明显弱于单轮对话。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-11-12</td>
      <td style="width: 55%;"><strong>LONGGENBENCH: Long-context Generation Benchmark</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.findings-emnlp.48.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LongGenBench 是新近提出的一项长上下文生成基准，用于评估大型语言模型（LLMs）在长文本生成任务中的表现。<br>
        • 该基准补充了主要侧重检索能力的现有评测体系，转而强调在多个子问题之间保持连贯性与逻辑一致性。<br>
        • 研究表明，不同模型在长文本生成方面存在显著的性能差异。
      </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-10-23</td>
      <td style="width: 55%;"><strong>MADial-Bench Towards real-world evaluation of memory-augmented diglogue generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2409.15240">
        <img src="https://img.shields.io/badge/NAACL-Paper-black?labelColor=cyan" alt="NAACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MADial-Bench（记忆增强型对话生成基准测试）旨在评估对话系统在长期记忆能力上的局限性。<br>
        • 该基准测试融合认知科学理论，通过记忆检索与识别能力评估框架，并引入多维度评估指标。<br>
        • 研究表明，尽管大语言模型在情感支持任务中表现优异，但其记忆识别与注入能力仍需提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-10-04</td>
      <td style="width: 55%;"><strong>L-CiteEval: A Long-Context Citation Evaluation Benchmark</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context%20Evaluation-darkslategray" alt="Long-Context Evaluation">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2410.02115">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • L-CiteEval（长上下文模型理解与引用评估基准）是一个面向长上下文模型的多任务评估基准测试，旨在评估其在理解和引用方面的能力。<br>
        • 该基准测试涵盖11项任务，支持从8K至48K的上下文长度，并提供了综合性评估框架。<br>
        • 研究表明，闭源模型在引用质量和生成准确性上优于开源模型，而检索增强生成（RAG）技术能显著提升引用质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-16</td>
      <td style="width: 55%;"><strong>A personal long-term memory dataset for memory classification,Retrieval, and Synthesis in question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Mid--Term%20Memory-saddlebrown" alt="Mid-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.sighan-1.18.pdf">
      <img src="https://img.shields.io/badge/ACL%20Workshop-Paper-black?labelColor=purple" alt="ACL Workshop Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PerLTQA 是一个问答数据集，旨在增强对话系统中的长期记忆整合能力。<br>
        • PerLTQA 融合了语义记忆与情景记忆，涵盖 30 个角色下的 8593 个问题，目标在于提升记忆分类、检索与综合能力。<br>
        • 实验结果表明，在记忆分类任务中，基于 BERT 的模型优于其他大型语言模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>CAN LONG-CONTEXT LANGUAGE MODELS UNDER-STAND LONG CONTEXTS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.859/">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨大语言模型在长文本处理中的能力与局限性，并提出GLE（长文本理解评估）基准测试以评估其在长上下文理解中的表现。<br>
        • 论文阐述了长依赖问答任务的构建过程与评估标准，并对比了不同模型的性能。<br>
        • 实验结果表明，GLE基准测试能够有效评估大语言模型对长文本的处理能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>Evaluating Very Long-Term Conversational Memory of LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.747.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估了大型语言模型（LLMs）在长时对话中的记忆能力，尤其聚焦于多模态对话场景。<br>
        • 研究者通过构建 LOCOMO 数据集，建立了一个覆盖问答、事件总结以及多模态对话生成等任务的综合评测基准。<br>
        • 实验结果表明，尽管部分 LLM 表现出较强能力，但在记忆与推理方面仍显著落后于人类，同时论文还提出了相应的评测框架与未来改进方向。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>Lamp: When large language models meet personalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Personalized%20Tasks-darkkhaki" alt="Personalized Tasks">
      <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.399.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨了大型语言模型（LLMs）在个性化回复生成中的重要性，并提出了 LaMP，这是一个专门用于训练与评估个性化文本生成和分类任务的新基准。<br>
        • LaMP 包含七项个性化子任务，突出了利用用户特定输入（如历史数据）以及检索增强策略来提升语言模型性能的有效性。<br>
        • 实验结果表明，个性化方法能够显著提升模型表现，其中通过微调并结合合适的检索策略可取得最佳效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-06-19</td>
      <td style="width: 55%;"><strong>LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Bilingual%20Evaluation-darkorchid" alt="Bilingual Evaluation">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2308.14508">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongBench（长文本理解基准测试）是一个面向大语言模型的双语多任务基准测试框架，旨在评估其长上下文理解能力。<br>
        • 该基准测试包含21个涵盖六类任务的数据集：单文档问答、多文档问答、摘要生成、少样本学习、合成任务和代码补全，平均文本长度达6,711单词（13,386字符）。<br>
        • 实验结果表明，商业模型（如GPT-3.5-Turbo-16k）在长上下文任务中普遍优于开源模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-16</td>
      <td style="width: 55%;"><strong>HIERARCHICAL CONTEXT MERGING: BETTER LONG CONTEXT UNDERSTANDING FOR PRE-TRAINED LLMS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2404.10308">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HOMER（分层上下文合并算法）是一种旨在解决大语言模型在长上下文处理中局限性的算法。<br>
        • 该算法通过将长输入分割为较小的块并进行分层合并，在处理长文本时显著提升内存效率与推理能力。<br>
        • 实验结果表明，HOMER在32K和64K上下文输入中表现出色，保持低困惑度与较低内存消耗。
      </td>
    </tr>
  </table>

</details>


<details>
  <summary><strong>模型和系统类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-14</td>
      <td style="width: 55%;"><strong>MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.15126"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为每个 token 配置多个随语境选择的记忆嵌入槽。<br>
        • 由隐藏状态驱动的可学习门控决定读取位置。<br>
        • 受控预训练在匹配预算下优于固定查表基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Safety-blue" alt="Memory Safety">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.12320"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 跨智能体和用户管理私有及共享记忆。<br>
        • 可见性分类及索引级控制实施仅限所有者的检索。<br>
        • MUMBench 评估检索、创建、更新及删除，操作准确率仍有提升空间。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-11</td>
      <td style="width: 55%;"><strong>RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.12814"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将矩阵循环记忆推广为高阶张量。<br>
        • 通过秩一更新及张量收缩读取保留循环和并行计算形式。<br>
        • 三阶状态实验改善联想回忆及预训练后的检索任务表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-09</td>
      <td style="width: 55%;"><strong>Kernel-Managed Shared Memory for System-Wide Personalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.10144"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在智能体系统内核中集中管理共享个性化记忆。<br>
        • 智能体写入带标签记录，内核负责检索、隐私与注入。<br>
        • AIOS 在三个模型的测试中报告个性化改善及提示词缩短。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-07</td>
      <td style="width: 55%;"><strong>Kalman Delta Networks: Uncertainty-aware Associative Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.07816"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在循环联想记忆更新中显式跟踪不确定性。<br>
        • 采用卡尔曼式对角及各向同性近似，支持并行关联扫描。<br>
        • 7.5 亿及 13 亿参数受控预训练改善困惑度和下游平均准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-03</td>
      <td style="width: 55%;"><strong>Lngram v2: Latent N-Gram Memory with Interpretable Discrete Representations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.03426"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使潜在 n-gram 记忆容量独立于基座宽度扩展。<br>
        • 通过离散路由、分组查询读取及空检索选项控制激活成本。<br>
        • 视觉语言模型实验报告高效扩展及具有语义结构的离散地址。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-30</td>
      <td style="width: 55%;"><strong>Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.29606"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合情节、联想及文档式长期记忆。<br>
        • 并行搜索通过来源追踪和引用约束访问证据。<br>
        • LongMemEval 和 LoCoMo 实验在多个基座上报告较强准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-30</td>
      <td style="width: 55%;"><strong>Diachronic Hypergraphs for Orchestrated Multi-Agent Multimodal Memory Curation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.29678"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将协作多模态事件存储于时间超图记忆。<br>
        • 角色感知检索及生命周期更新共同保留智能体、工具、决策和证据。<br>
        • 实验报告优于所比较的多智能体记忆基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-27</td>
      <td style="width: 55%;"><strong>Fast Weight Attention for Continual Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.27763"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将循环快速记忆更新表述为时间对齐的在线学习。<br>
        • 推导归一化回归与内积更新，并支持有界经验复习。<br>
        • 代表性变体保持语言建模竞争力并改善算术长度外推。
      </td>
    </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-08-24</td>
        <td style="width: 55%;"><strong>Wontopos Tablet 2：无词汇匹配的多语言与多模态记忆检索测量</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2-4A90E2" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/%E8%AE%B0%E5%BF%86%E8%AF%84%E6%B5%8B-7ED321" alt="Memory Evaluation">
          <img src="https://img.shields.io/badge/%E5%A4%9A%E8%AF%AD%E8%A8%80-F5A623" alt="Multilingual">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2608.23920">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文测量一个生产环境的长期记忆引擎，其检索路径不包含词汇匹配、关键词打分，也不包含语言模型。<br>
          • 评测覆盖 LongMemEval-S 与 BEAM-1M 文本基准，以及对无任何文字存储的照片进行跨语言检索。<br>
          • 在 70 个存储与查询语言组合上平均 recall@5 为 95.2%，而 BM25 为 19.0% 且在 54 个组合中为零；仅更换阅读模型使 LongMemEval-S 变动 2.0 个点，仅更换重问预算使 BEAM-1M 变动 8.9 个点。
        </td>
      </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-18</td>
      <td style="width: 55%;"><strong>MoNe: Modular Neural Memory for Efficient Long Context Inference</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.17616"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为冻结的 Transformer 接入模块化快速权重记忆。<br>
        • 分段测试时更新生成查询相关键值，无需重新读取上下文。<br>
        • 作者报告在 128K token 下计算量和峰值显存约降低 80%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-17</td>
      <td style="width: 55%;"><strong>Proteus: Incremental Memory Activation for Long-Context Sequence Modeling</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.16844"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 随上下文增长逐步扩大可用记忆容量。<br>
        • 通过早期压缩及后续容量激活减少信息间干扰。<br>
        • 实验改善多种神经记忆架构，长上下文收益更明显。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-12</td>
      <td style="width: 55%;"><strong>LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12419"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将局部序列处理与可寻址的全局知识记忆分离。<br>
        • 结合卷积增强注意力及参数化键值知识模块。<br>
        • 作者报告相较所比较基线，预训练收敛速度提高至 1.33 倍。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-12</td>
      <td style="width: 55%;"><strong>MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12428"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提供可移植且自演化的智能体记忆运行层。<br>
        • 结合验证驱动模式搜索、固化、纠正反馈及技能演化。<br>
        • LoCoMo、PersonaMem 和 SpreadsheetBench 评估报告记忆与技能收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-12</td>
      <td style="width: 55%;"><strong>MARCH: Scaling Recurrent Memory with Content-Routed State Anchors</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.12435"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过内容路由的历史状态锚点扩展循环记忆。<br>
        • 缓存状态检查点，并使用可学习查询检索历史锚点。<br>
        • 预训练模型在推理、LongBench 和检索上优于线性注意力基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-10</td>
      <td style="width: 55%;"><strong>MixFormer: Linear Transformer with Mixture of Memory Experts</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.09468"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在线性 Transformer 中组合多个记忆专家。<br>
        • 时间感知注意力利用可学习衰减及位置偏置更新差异化状态。<br>
        • 长序列文本和图像生成实验报告性能改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01630"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将检索内化为可训练的记忆专家，以持续注入知识。<br>
        • 通过预训练、搜索轨迹监督及强化学习优化内部路由。<br>
        • News-2025 实验报告相较 RAG 基线具有竞争力的准确率和效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Learning What to Remember: Test-Time Training via Context Distillation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.01672"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 训练快速权重保留对未来预测有用的上下文。<br>
        • 利用长窗口教师监督短窗口学生的隐藏状态。<br>
        • 实验改善长上下文建模，并支持预训练 Transformer 的推理时适应。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02032"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将循环分块状态转化为可通过注意力读取的记忆。<br>
        • 从 Mamba-2 状态解码查询相关键值，并进行门控融合。<br>
        • 实验改善联想回忆，相较匹配注意力基线减少缓存。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Mamba with Hierarchical Memory: Solving Representation Bottleneck in Long Sequence Modeling</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02347"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为预训练 Mamba 加入分层工作记忆与长期记忆。<br>
        • 从隐藏状态抽取段落语义并持久存储，用于任务相关检索。<br>
        • Passkey 和 LongBench-E 实验以 2% 额外参数改善检索与推理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02515"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在上下文窗口反复更替时维持模型内部记忆。<br>
        • 结合有界 KV 注意力、记忆后训练及状态感知推理服务。<br>
        • LongMemEval 实验显示证据移出活动窗口后仍可被回忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02560"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 注入预计算状态空间模型状态，实现检索和持久上下文。<br>
        • 分层固化融合情节、语义及外部语料状态。<br>
        • 边缘模型实验报告接近 RAG 的质量及明显降低的预填充延迟。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-08-03</td>
      <td style="width: 55%;"><strong>Maglev: Sliding Recurrent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.02870"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为滑动窗口 Transformer 加入固定容量循环记忆。<br>
        • 由更强的预填充模型提供记忆一致性监督。<br>
        • 实验改善验证损失和下游表现，推理仅需循环解码器。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-31</td>
      <td style="width: 55%;"><strong>TransMem: Transforming Hidden States into Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.29032"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将稀疏历史隐藏状态复用为智能体潜在记忆。<br>
        • 在冻结基座上通过证据条件蒸馏训练门控记忆模块。<br>
        • LoCoMo、HotpotQA 及 MemoryAgentBench 实验报告稳定提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-30</td>
      <td style="width: 55%;"><strong>Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.27919"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将独立预训练的参数化记忆扩展至 69 亿参数。<br>
        • 通过分布式索引与稀疏检索支持 3000 亿 token 训练。<br>
        • 作者报告在通用及领域基准上获得更好的参数效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-29</td>
      <td style="width: 55%;"><strong>Metis: Memory Foundation Model</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.26760"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将持久且动态演化的记忆状态内置于基座模型。<br>
        • 通过记忆注意力与专门中期训练学习无需梯度的状态更新。<br>
        • 实验分析原生记忆的能力与局限，并发布模型权重。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-28</td>
      <td style="width: 55%;"><strong>Raven: High-Recall Sequence Modeling with Sparse Memory Routing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.25357"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过稀疏且依赖输入的更新维护固定记忆槽。<br>
        • 可学习路由选择需要衰减和写入的槽位。<br>
        • 回忆基准在最高十六倍训练上下文长度下仍保持较强表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-28</td>
      <td style="width: 55%;"><strong>MemSFT: Mitigating Alignment Tax with an External Parametric Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.25614"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过参数化记忆分离领域专门化与基座更新。<br>
        • 可学习路由器在生成时融合记忆与基座的输出分布。<br>
        • 生物、地球科学和法律实验改善领域能力且较少损伤通用能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-23</td>
      <td style="width: 55%;"><strong>Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21000"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在离散状态空间记忆中解耦保留与写入。<br>
        • 独立遗忘门及写入门消除互补单门的约束。<br>
        • 诊断实验在四倍训练长度下同时保持较强保留和覆盖能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-23</td>
      <td style="width: 55%;"><strong>MemTools: A Unified Research Framework for Interoperable Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.21404"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 标准化智能体记忆研究中的可互操作组件。<br>
        • 声明式契约分离生命周期模块、数据集、协议及表示。<br>
        • 集成实验展示对异构记忆系统进行受控比较的能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-13</td>
      <td style="width: 55%;"><strong>Extending LLM Context via Associative Recurrent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.11614"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 利用联想循环记忆扩展预训练模型的上下文。<br>
        • 结合继续预训练、合成数据课程及选择性记忆层集成。<br>
        • 实验支持超出原生窗口的泛化，并报告窗口内 FLOPs 减少 30%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-08</td>
      <td style="width: 55%;"><strong>Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.07386"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过稀疏寻址扩大线性循环网络的记忆容量。<br>
        • 以稀疏记忆读写替代 Gated DeltaNet 的稠密更新。<br>
        • 等计算量实验改善检索和上下文学习，可学习初始记忆进一步增强知识任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-08</td>
      <td style="width: 55%;"><strong>TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.07388"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 构建跨 GPU、内存和 SSD 的免训练短语记忆。<br>
        • 离线语义构建及预测预取支持隐藏状态注入。<br>
        • Qwen3-0.6B 实验改善下游分数并降低显存存储需求。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-08</td>
      <td style="width: 55%;"><strong>Co-LMLM: Continuous-Query Limited Memory Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.07707"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在预训练中通过连续查询记忆外置事实知识。<br>
        • 使用向量键从标注知识库检索可追溯的文本值。<br>
        • 多尺度实验在困惑度和事实精度上优于所比较模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-07</td>
      <td style="width: 55%;"><strong>Do You Remember? Toward Memory-Centric Multimodal AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Embodied%20%2F%20Multimodal-blue" alt="Embodied / Multimodal">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.11919"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究多模态语言模型中的重建式视觉记忆。<br>
        • 通过稀疏局部移动平均更新维护共享视觉记忆矩阵。<br>
        • 人脸图像实验改善重建，结论限于所研究设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-06</td>
      <td style="width: 55%;"><strong>BCMT: Blockwise Causal Memory Transformer</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2608.13578"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离局部注意力与全局分块摘要记忆。<br>
        • 通过指数聚合的因果摘要将上下文反馈至 token 表示。<br>
        • 最高 1,024 token 的实验报告相近验证质量及更高吞吐量。
      </td>
    </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-24</td>
        <td style="width: 55%;"><strong>Bridging the Post-discharge Gap: A Traceable Multi-agent Framework for Safe and Continuous Care</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/医疗智能体-4A90E2" alt="Medical Agents">
          <img src="https://img.shields.io/badge/多智能体系统-F5A623" alt="Multi-Agent Systems">
          <img src="https://img.shields.io/badge/记忆增强-7ED321" alt="Memory Enhanced">
          <img src="https://img.shields.io/badge/可追溯性-D0021B" alt="Traceability">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.25334v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文面向出院后随访场景，强调安全连续护理要求智能体基于纵向患者约束进行推理，而不是回答孤立医学问题。<br>
          • Healink 是一个记忆增强的多智能体框架，包含分诊路由、统一记忆和基于处方证据的回复生成，使随访建议能够追溯到患者历史与护理指令。<br>
          • 回顾性和医生盲评实验显示，该系统提升了回复完整性和感知临床效用，因此可作为记忆治理型智能体在垂直医疗场景中的系统案例。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-4A90E2" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/记忆整合-F5A623" alt="Memory Consolidation">
          <img src="https://img.shields.io/badge/可信记忆-7ED321" alt="Trustworthy Memory">
          <img src="https://img.shields.io/badge/偏好学习-D0021B" alt="Preference Learning">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.25161v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文研究长期记忆 LLM Agent 的记忆整合问题：写入、修订和删除操作一旦遗漏关键信息、破坏已有记忆或写入幻觉内容，就会成为影响未来推理的持久系统状态错误。<br>
          • TrustMem 引入 Memory Transition Verifier，从覆盖度、保留性和忠实性三个维度评估每次记忆状态转移，并在同一记忆状态下构造候选更新的偏好对，用于训练偏好引导的记忆整合策略。<br>
          • 在 MemoryAgentBench、HaluMem 和 Mem-α 上的实验显示，TrustMem 同时提升记忆效用与可靠性，说明记忆智能体在把生成式更新提交到长期存储前，需要对状态转移本身进行验证。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>Governed Shared Memory for Multi-Agent LLM Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/共享记忆-4A90E2" alt="Shared Memory">
          <img src="https://img.shields.io/badge/多智能体系统-F5A623" alt="Multi-Agent Systems">
          <img src="https://img.shields.io/badge/记忆治理-7ED321" alt="Memory Governance">
          <img src="https://img.shields.io/badge/来源追踪-D0021B" alt="Provenance">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24535v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文将 LLM Agent 集群中的共享记忆定义为受治理的分布式系统问题，核心涉及范围化访问、时间正确性、来源追踪、同步和策略控制传播。<br>
          • 论文提出范围化检索、时间 supersession、来源追踪和策略治理传播等系统原语，并在生产级多租户记忆服务 MemClaw 中实现这些机制。<br>
          • ArgusFleet 现场评估重建了全部测试的四跳来源链，同时暴露了实际权限路径和管线顺序问题，说明仅依赖长上下文检索不足以支撑生产级多智能体记忆。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>Qwen-AgentWorld: Language World Models for General Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Language%20World%20Model-4A90E2" alt="Language World Model">
          <img src="https://img.shields.io/badge/General%20Agents-F5A623" alt="General Agents">
          <img src="https://img.shields.io/badge/Environment%20Simulation-7ED321" alt="Environment Simulation">
          <img src="https://img.shields.io/badge/Agentic%20RL-D0021B" alt="Agentic RL">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24597v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出 Qwen-AgentWorld，一组根据观测和动作预测智能体环境动态的语言世界模型，将世界建模定位为推理、规划与可扩展智能体训练的核心机制。<br>
          • 模型使用来自七个智能体领域、超过 1000 万条真实环境交互轨迹训练；训练流程结合持续预训练以注入世界建模能力、监督微调以激活下一状态预测，以及带混合 rubric 和规则奖励的强化学习以提升模拟保真度。<br>
          • Qwen-AgentWorld 支持两类互补用法：作为解耦环境模拟器支撑大规模 agentic reinforcement learning，以及作为统一智能体基础模型，通过世界模型训练提升七个下游 agentic benchmark 的表现；论文还提出 AgentWorldBench，用真实交互评估语言世界模型。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-18</td>
        <td style="width: 55%;"><strong>AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Atomic%20Facts-4A90E2" alt="Atomic Facts">
          <img src="https://img.shields.io/badge/Hierarchical%20Events-F5A623" alt="Hierarchical Events">
          <img src="https://img.shields.io/badge/Temporal%20Profiles-7ED321" alt="Temporal Profiles">
          <img src="https://img.shields.io/badge/Associative%20Graph-D0021B" alt="Associative Graph">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.19847">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出AtomMem，以高价值原子事实作为长期记忆的基本表示单位，试图在保存完整对话造成的冗余开销与过度摘要导致的细节损失之间取得平衡，并降低无约束记忆更新带来的内容漂移和不稳定性。<br>
          • 系统首先由Fact Executor从长篇交互中选择性提取独立、可验证且信息密度较高的事实，再将其组织为分层事件结构和时间画像：前者保留事件级情景关系，后者跟踪用户偏好、目标及属性随时间发生的动态变化。<br>
          • 检索阶段通过关联记忆图连接分散在不同事件与时间点的事实，以支持跨会话、多跳和时间推理；LoCoMo实验显示AtomMem在多类推理任务上取得领先结果，表明原子化表示需要与事件层次、时间演化和关联检索共同使用，单纯将记忆切分为更短文本并不足以形成稳定的长期记忆。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-17</td>
        <td style="width: 55%;"><strong>OpenRath: Session-Centered Runtime State for Agent Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Runtime-4A90E2" alt="Agent Runtime">
          <img src="https://img.shields.io/badge/Session%20State-F5A623" alt="Session State">
          <img src="https://img.shields.io/badge/Replay-7ED321" alt="Replay">
          <img src="https://img.shields.io/badge/Memory%20Events-D0021B" alt="Memory Events">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.19409v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文针对现代 Agent 系统中的运行时状态碎片化问题展开研究：对话记录、工具效果、记忆事件、工作区位置、分支来源与重放证据往往分散记录，导致系统难以检查和复现。<br>
          • OpenRath 提出类似 PyTorch 的编程模型，其核心抽象是在线程、代理和工作流之间传递的一等公民 Session 值；Session 支持分支、检查、重放、后端感知与组合，并携带对话片段、沙箱位置、血缘元数据、token 用量、待处理任务、工具证据以及记忆交互的运行时记录。<br>
          • 通过将 fork、merge 和 replay 显式建模为运行时操作，并定义 Sandbox、Tool、Agent、Memory、Workflow 与 Selector 等组件，OpenRath 为多代理、多会话系统提供了可审计的组合模型；论文主要验证受控运行时属性，开放服务质量和记忆质量评估留待后续工作。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-16</td>
        <td style="width: 55%;"><strong>FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Financial%20AI-4A90E2" alt="Financial AI">
          <img src="https://img.shields.io/badge/Experience%20Memory-F5A623" alt="Experience Memory">
          <img src="https://img.shields.io/badge/Multimodal%20Reasoning-7ED321" alt="Multimodal Reasoning">
          <img src="https://img.shields.io/badge/Selective%20Activation-D0021B" alt="Selective Activation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.17642">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出FinAcumen，通过跨任务积累金融多模态推理轨迹，将成功案例蒸馏为可复用策略，并将失败轨迹转化为风险警示规则，以解决无状态工具代理反复探索相同策略、错误调用工具及产生金融幻觉的问题。<br>
          • 推理阶段采用选择性经验激活机制，仅当检索经验与当前问题的语义相关性超过校准阈值时才将其注入推理上下文；当经验不可靠或相关性不足时，系统通过回退路径显式抑制记忆影响，并利用确定性金融工具环境执行数值计算、资料检索、图表解析和答案验证。<br>
          • 在四个金融多模态推理基准上，FinAcumen持续提升冻结的8B视觉语言模型，并在部分设置下超过金融专用模型、接近领先的闭源通用模型；进一步分析表明，性能增益依赖于对经验的选择性使用，而非无条件扩大记忆注入规模。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-16</td>
        <td style="width: 55%;"><strong>ActWorld: From Explorable to Interactive World Model via Action-Aware Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/World%20Model-4A90E2" alt="World Model">
          <img src="https://img.shields.io/badge/Action--Aware%20Memory-F5A623" alt="Action-Aware Memory">
          <img src="https://img.shields.io/badge/Object%20Interaction-7ED321" alt="Object Interaction">
          <img src="https://img.shields.io/badge/Video%20Generation-D0021B" alt="Video Generation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.17730">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文指出，现有交互式视频世界模型通常采用偏向近期帧的历史压缩策略，容易删除决定物体后续状态的关键事件转移帧，从而产生模型能够导航却会遗忘开门、拾取或触发物理变化等动作结果的“动作遗忘”问题。<br>
          • ActWorld在分块自回归生成框架中引入分层动作感知记忆，根据历史片段对物体交互和状态变化的重要程度选择不同压缩路径，并设置持久记忆库长期保存事件更新令牌与对象身份令牌，以维持长时间展开中的因果连续性。<br>
          • 作者同时构建包含约10万条人机交互视频及分块推理标注的数据集；实验表明，该模型能够在统一系统内兼顾自由视角导航和中途物体交互，并在不牺牲视点控制能力的情况下提升交互保真度，说明世界模型的长期历史管理必须以动作因果性而非单纯时间新近性为依据。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-16</td>
        <td style="width: 55%;"><strong>PreAct: Computer-Using Agents that Get Faster on Repeated Tasks</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Procedural%20Memory-4A90E2" alt="Procedural Memory">
          <img src="https://img.shields.io/badge/State%20Machine-F5A623" alt="State Machine">
          <img src="https://img.shields.io/badge/Task%20Replay-7ED321" alt="Task Replay">
          <img src="https://img.shields.io/badge/Computer%20Agents-D0021B" alt="Computer Agents">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.17929">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出PreAct，将计算机使用智能体首次成功完成任务的轨迹编译为小型状态机程序，其中状态负责验证当前屏幕条件，转移负责执行点击、输入等动作，使重复任务从重新推理转化为可执行的程序性记忆回放。<br>
          • 回放并非无条件复现：系统在每一步执行前检查屏幕是否符合程序预期，一旦检测到界面偏移便将控制权交还给通用智能体；新程序只有在干净环境中重放并经独立评估器确认任务完整完成后，才会被写入长期程序库。<br>
          • 在移动端、桌面端和网页端三个基准中，直接程序回放实现8.5至13倍加速且无需逐步调用大模型，写入时验证也能防止错误程序持续累积；实验同时表明，系统收益主要来自可靠的程序验证与复用，而非提示词调整、运行时防护或更复杂的程序检索器。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-16</td>
        <td style="width: 55%;"><strong>CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-4A90E2" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Riemannian%20Retrieval-F5A623" alt="Riemannian Retrieval">
          <img src="https://img.shields.io/badge/Fisher%20Distillation-7ED321" alt="Fisher Distillation">
          <img src="https://img.shields.io/badge/Edge--Cloud%20Architecture-D0021B" alt="Edge-Cloud Architecture">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.18406">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出由信息几何统一的边云长期记忆架构CoreMem，旨在同时解决高维向量检索中的枢纽效应、上下文压缩中的语义损失，以及消费级设备显存与计算资源受限等问题。<br>
          • 在检索阶段，CoreMem以局部自适应的Fisher–Rao黎曼度量替代各向同性余弦相似度，并利用低秩Woodbury加速实现实时搜索；在压缩阶段，Fisher引导离散令牌蒸馏根据参数敏感度从句子到令牌逐级筛选内容，同时显式保护语法和结构信息。<br>
          • 在LoCoMo与LongMemEval-S上的实验报告开放域推理提高4.51个百分点、时间推理提高4.17个百分点，并能够在严格的8 GB显存预算内运行；该工作的重要性在于为检索与压缩提供统一理论依据，但其效率结论仍依赖所采用的低秩近似及边云部署配置。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-15</td>
        <td style="width: 55%;"><strong>MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Hierarchical%20Memory-4A90E2" alt="Hierarchical Memory">
          <img src="https://img.shields.io/badge/Personalized%20Slides-F5A623" alt="Personalized Slides">
          <img src="https://img.shields.io/badge/Working%20Memory-7ED321" alt="Working Memory">
          <img src="https://img.shields.io/badge/Local%20Revision-D0021B" alt="Local Revision">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.17162v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出面向个性化演示文稿生成的分层记忆架构，将跨任务长期记忆与单次编辑会话中的工作记忆明确分离，并进一步把长期记忆划分为用户画像记忆和工具记忆，以对应不同时间尺度与功能目标。<br>
          • 用户画像记忆根据任务意图检索稳定偏好，为首轮生成提供个性化条件；工作记忆持续维护当前会话中新出现的约束与修订要求；工具记忆则保存局部编辑的可复用执行经验，并与限定作用域的幻灯片局部修改机制结合，减少无关页面和元素被重复生成。<br>
          • 受控实验显示，用户画像记忆能够提高多角色、多意图条件下的个性一致性，工具记忆能够改善闭环修改的执行可靠性，案例分析也验证了工作记忆对跨轮偏好的延续作用；结果表明，个性化生成的关键并非建立单一统一记忆池，而是按持久性和职责进行功能化分层。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-13</td>
        <td style="width: 55%;"><strong>Edu-Theater: A Data-Efficient Agent Framework for Scalable Learner Behavior Simulation through Staging Roll-Call</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Learner%20Simulation-4A90E2" alt="Learner Simulation">
          <img src="https://img.shields.io/badge/Cohort%20Prior-F5A623" alt="Cohort Prior">
          <img src="https://img.shields.io/badge/Diagnostic%20Probing-7ED321" alt="Diagnostic Probing">
          <img src="https://img.shields.io/badge/Data%20Efficiency-D0021B" alt="Data Efficiency">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.15225v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文针对传统学习者模拟高度依赖个体密集交互历史的问题，提出群体感知的“点名式”模拟范式：首先从同类学习者日志中构建群体能力先验，再以少量针对性诊断交互校准个体知识状态。<br>
          • Edu-Theater由教师智能体统一组织模拟流程，并通过对历史学习日志的回顾性点名探测，在群体级先验和个体级证据之间动态切换；该设计将历史日志由逐用户完整上下文转化为可共享的群体记忆与稀疏个体状态，缓解冷启动及大规模部署中的调用成本。<br>
          • 在两个真实教育数据集上的实验表明，该框架使用显著更少的大模型调用即可获得更高的未来行为模拟准确率，生成的数据还能改善自适应测试等下游任务；其贡献主要在于提高教育代理的状态重构效率，而非构建通用型个人长期记忆系统。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-13</td>
        <td style="width: 55%;"><strong>T-Mem: Memory That Anticipates, Not Archives</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-4A90E2" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Associative%20Recall-F5A623" alt="Associative Recall">
          <img src="https://img.shields.io/badge/Write--Time%20Triggers-7ED321" alt="Write-Time Triggers">
          <img src="https://img.shields.io/badge/Conversational%20Agents-D0021B" alt="Conversational Agents">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.15405">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文指出，主流长期对话记忆通常依赖词汇或嵌入相似性，只能处理查询与历史内容具有显式表面重合的描述性回忆，难以发现由因果、叙事或潜在语义关系连接的联想性记忆。<br>
          • T-Mem借鉴情景未来思维，在记忆写入阶段预先生成Entity、Bridge、Scene与Horizon等触发器，并在事实与完整对话两个粒度上同时建立描述性和联想性访问路径，使历史信息能够由未来可能出现的相关情境而非原始措辞重新激活。<br>
          • 实验显示T-Mem在LoCoMo与强调认知联想的LoCoMo-Plus上均取得领先结果，并将两个基准之间的性能差距缩小至5.45个百分点；消融实验进一步表明，场景级联想触发器对LoCoMo-Plus尤为关键，说明面向未来的写入时索引是突破相似度检索边界的主要机制。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-12</td>
        <td style="width: 55%;"><strong>GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-4A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Version%20Control-F5A623" alt="Version Control">
          <img src="https://img.shields.io/badge/Reasoning%20Provenance-7ED321" alt="Reasoning Provenance">
          <img src="https://img.shields.io/badge/Empirical%20Study-D0021B" alt="Empirical Study">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.14470">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出GitOfThoughts，将智能体的推理树映射为Git仓库：带评分的推理节点对应提交，父子推理关系对应提交历史，评分与验证结果分别通过notes和tags记录，从而支持确定性回放、逐行差异比较、来源追踪及跨智能体合并。<br>
          • 研究在GPQA-Diamond与MATH-500上比较无记忆、Markdown、向量库、图数据库及Git五种记忆载体，并通过预注册复现实验发现：对于真正的新问题，任何记忆格式均未能稳定提高准确率，早期观察到的正向趋势也未能在扩大样本后复现。<br>
          • 记忆收益主要出现在检索案例与当前问题高度相似的“可复制阈值”以上，且提升更接近答案复用而非方法迁移；因此，GitOfThoughts的核心价值不是提高泛化精度，而是在准确率基本持平的前提下赋予推理过程可审计性、可复现性和协作治理能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20MAS-%234A90E2" alt="LLM MAS">
          <img src="https://img.shields.io/badge/Scheduling-%23F5A623" alt="Scheduling">
          <img src="https://img.shields.io/badge/Cloud%20Systems-%237ED321" alt="Cloud Systems">
          <img src="https://img.shields.io/badge/Memory%20Optimization-%23D0021B" alt="Memory Optimization">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12950v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出Maestro，一种面向LLM多智能体系统的跨集群工作负载感知调度框架，用于解决云环境中的资源受限问题。<br>
          • 通过预测生成长度与内存占用，驱动分层调度器，实现动态多模型共存与弹性资源配置。<br>
          • 实验表明该方法显著降低内存开销，并提升系统SLO（服务等级目标）达成率与整体吞吐效率。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-%234A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Cognitive%20Model-%23F5A623" alt="Cognitive Model">
          <img src="https://img.shields.io/badge/Memory%20Policy-%237ED321" alt="Memory Policy">
          <img src="https://img.shields.io/badge/Explainability-%23D0021B" alt="Explainability">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12945v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出一种基于认知心理学的多因素记忆价值模型，用于指导LLM代理在有限记忆预算下的存储与遗忘决策。<br>
          • 模型结合七个可解释因素（如情感强度与目标相关性），统一建模编码、保留与检索策略。<br>
          • 实验表明该方法在记忆效率与保留质量上优于传统方法，同时具备良好的可解释性与轻量部署能力。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-05</td>
        <td style="width: 55%;"><strong>Rosetta Memory: Adaptive Memory for Cross-LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Cross--LLM-%234A90E2" alt="Cross-LLM">
          <img src="https://img.shields.io/badge/Memory%20System-%23F5A623" alt="Memory System">
          <img src="https://img.shields.io/badge/Adaptation-%237ED321" alt="Adaptation">
          <img src="https://img.shields.io/badge/Robustness-%23D0021B" alt="Robustness">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.07711">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文提出Rosetta Memory，用于将无状态LLM转化为跨模型可迁移的持久化记忆系统，以支持多模型切换场景。<br>
          • 通过设计条件化操作符优化记忆的存储与呈现机制，使其能够适配不同LLM架构与任务分布。<br>
          • 实验显示该系统在多基准测试中表现稳定，即使在未见模型替换场景下仍保持较强鲁棒性。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-%234A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long--Horizon-%23F5A623" alt="Long Horizon">
          <img src="https://img.shields.io/badge/System%20Analysis-%237ED321" alt="System Analysis">
          <img src="https://img.shields.io/badge/Memory%20Cost-%23D0021B" alt="Memory Cost">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/abs/2606.06448">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文将Agent Memory视为长时序有状态工作负载进行系统建模，而非单纯的检索增强组件。<br>
          • 提出阶段感知分析框架，用于分解记忆系统在构建、检索与生成阶段的成本结构。<br>
          • 通过对多个系统的分析，总结出关于调度设计、延迟权衡与大规模部署的系统性建议。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Session%20Memory-blue" alt="Session Memory">
          <img src="https://img.shields.io/badge/Knowledge%20Graph-orange" alt="Knowledge Graph">
          <img src="https://img.shields.io/badge/Context%20Management-green" alt="Context Management">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-red" alt="Large Language Model">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06337">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 针对长会话中上下文窗口溢出导致决策、文件和任务状态丢失的问题。<br>
          • 将会话历史建模为类型化知识图，并序列化为紧凑的恢复块。<br>
          • 以更低 token 成本提升决策和文件召回，是实用的长程上下文管理系统。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory%20System-blue" alt="Memory System">
          <img src="https://img.shields.io/badge/Embodied%20Agents-orange" alt="Embodied Agents">
          <img src="https://img.shields.io/badge/Cognitive%20Psychology-green" alt="Cognitive Psychology">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-red" alt="Memory Retrieval">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.03374">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 指出具身智能体需要同时按语义、空间和时间搜索记忆。<br>
          • 构建混合图记忆、多索引架构和面向工具调用的检索函数。<br>
          • 提出围绕认知心理学范式的 eMEM-Bench，用于评估具身记忆行为。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-02</td>
        <td style="width: 55%;"><strong>Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-orange" alt="Large Language Model">
          <img src="https://img.shields.io/badge/Memory%20Systems-green" alt="Memory Systems">
          <img src="https://img.shields.io/badge/AutoMEM-red" alt="AutoMEM">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.04315">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 考察现有 Agentic Memory 系统是否能跨越单一设计场景泛化。<br>
          • 比较多种记忆系统在多个场景下的表现，并提出自管理基线 AutoMEM。<br>
          • 结果表明，智能体主动控制存储和检索比固定被动管线更稳健。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Collaborative%20Memory-blue" alt="Collaborative Memory">
          <img src="https://img.shields.io/badge/LLM%20Agents-orange" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Cloud--Edge%20Systems-green" alt="Cloud-Edge Systems">
          <img src="https://img.shields.io/badge/Memory%20Mechanism-red" alt="Memory Mechanism">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.00756">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 面向资源受限边缘模型和强云端模型协作执行长程任务的场景。<br>
          • 采用分散执行与集中反思，过滤可复用经验并循环共享洞察。<br>
          • 在不更新模型参数的情况下提升任务进展和行动 grounding，展示云边协作记忆范式。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-blue" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Models-orange" alt="Large Language Models">
          <img src="https://img.shields.io/badge/Multi--Agent%20Systems-green" alt="Multi-Agent Systems">
          <img src="https://img.shields.io/badge/Evaluation-red" alt="Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.07978">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 对分布式多智能体系统中的长期记忆后端进行独立评估。<br>
          • 在云边场景下测量准确率、延迟、CPU、内存、磁盘 I/O、网络和总体成本。<br>
          • 发现向量、图、混合、RAG 和全上下文方案之间存在显著成本-准确率差异。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-30</td>
        <td style="width: 55%;"><strong>Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Hierarchical%20Memory-blue" alt="Hierarchical Memory">
          <img src="https://img.shields.io/badge/Semantic%20Memory-orange" alt="Semantic Memory">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-green" alt="Large Language Model">
          <img src="https://img.shields.io/badge/Agent%20Memory-red" alt="Agent Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.26197">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 介绍 LinkedIn 招聘智能体中的生产级长期语义记忆系统。<br>
          • 从噪声行为数据中抽取信号，层次化存储，并在隐私约束下支持低延迟检索。<br>
          • 提升回答正确性和个性化效果，是少见的真实部署记忆系统案例。
        </td>
      </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-05-12</td>
        <td style="width: 55%;"><strong>Beyond Similarity Search: Tenure and the Case for Structured Belief State in LLM Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/System-darkblue" alt="System">
          <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.11325">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 理论框架： 本文主张跨会话的大语言模型记忆本质上是一个状态管理问题，而非单纯的搜索问题。为此，我们提出了一种类型化信念模式，该模式包含五种信念类型、认识论状态以及版本化的取代机制；同时引入了 why_it_matters 字段，旨在将提取的事实转化为指令性的操作指引，而非仅仅是陈述性的事实记录.<br>
          • 实验结果： 研究表明，在包含72个测试用例的检索套件中，基于稠密嵌入的余弦相似度方法的平均精度仅为 0.12；相比之下，结合硬范围隔离的别名加权 BM25 算法实现了 1.0 的精度，通过了全部 72 个测试用例。在多轮对话的话题漂移场景下，向量搜索在噪声敏感轮次中的漂移得分为 0.43–0.50，而 BM25 算法则始终保持为 0.0.<br>
          • 系统实现与资源： 该系统以本地优先且兼容 OpenAI 接口的代理形式发布，能够透明地将精选的信念上下文注入到每一个大语言模型会话中。此外，我们还提供了一个可复用的、包含 72 个案例的基准测试集，涵盖别名解析、范围消歧、取代链排除以及会话级噪声隔离等关键任务.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-06</td>
        <td style="width: 55%;"><strong>Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/System-darkblue" alt="System">
          <img src="https://img.shields.io/badge/Large%20Language%20Model-teal" alt="Large Language Model">
          <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
          <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
          <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.05097">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Memini，一种面向大语言模型的有向关联记忆系统，通过由文档流直接驱动的多时间尺度记忆动力学来实现知识的持续更新。<br>
          • 基于 Benna-Fusi 模型在图边缘实现快慢耦合变量，无需显式规则即可自然涌现出情节敏感性、渐进巩固和选择性遗忘等记忆机制。<br>
          • 利用扩散激活在经验塑造的动态边权重上进行检索，使记忆基座能够自主演化并不断适应新传入的证据流。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-06</td>
        <td style="width: 55%;"><strong>Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/System-darkblue" alt="System">
          <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.04897">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 True Memory 智能体记忆架构，包含六层多阶段检索流水线，放弃在摄入时的提取式存储模式，转而利用单个 SQLite 文件直接对原样保存的对话事件进行检索。<br>
          • 引入包含新颖度、显著性和预测误差的三信号门控机制，在使用普通商用 CPU 的情况下，在 LoCoMo、LongMemEval 和 BEAM-1M 记忆基准测试中展现出卓越的性能。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/System-darkblue" alt="System">
          <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
          <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
          <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
          <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03675">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="arXiv Paper">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MEMTIER，一种面向长期运行的自主智能体的三层记忆架构，解决了现有平面文件系统中存在的上下文崩溃、压缩不连续、结构盲区和缺乏归因循环等问题。<br>
          • 包含结构化情景 JSONL 存储、五信号加权检索引擎、异步整合守护进程，以及带有基于 PPO 策略框架的注意力归因认知权重更新循环。<br>
          • 在 LongMemEval-S 基准测试中取得显著性能提升，证明了高精度、结构隔离的记忆（情景与语义）是长视野任务成功的核心，同时指出传统的线性组合检索是当前的性能瓶颈。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20Circuits-brightgreen" alt="Memory Circuits">
          <img src="https://img.shields.io/badge/Memory%20Extraction-yellow" alt="Memory Extraction">
          <img src="https://img.shields.io/badge/Retrieval-teal" alt="Retrieval">
          <img src="https://img.shields.io/badge/Failure%20Diagnosis-orange" alt="Failure Diagnosis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03354">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 分析 LLM Agent 记忆系统内部的功能电路，基于 Qwen-3 不同规模模型及 mem0、A-MEM 框架追踪写入、管理、读取过程中的特征电路。<br>
          • 发现小模型可先出现路由控制电路而内容电路尚未形成，利用特征空间分离实现无监督的分阶段故障定位，用于诊断静默的 Agent 记忆失败。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-05</td>
        <td style="width: 55%;"><strong>Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Reciprocal%20Memory-brightgreen" alt="Reciprocal Memory">
          <img src="https://img.shields.io/badge/AI%20Companion-yellow" alt="AI Companion">
          <img src="https://img.shields.io/badge/Multimodal%20LLM-teal" alt="Multimodal LLM">
          <img src="https://img.shields.io/badge/Augmented%20Reality-orange" alt="Augmented Reality">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03882">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Deco 双重实体框架，将用户实体物品扩展为持续存在的 AI 伴侣，结合多模态大模型与增强现实实现数字-物理同步互动。<br>
          • 通过 Reciprocal Memory 等设计原则维系情感连接，7 天部署研究表明可提升陪伴感、情感纽带和持续参与度。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Skill%20Packages-brightgreen" alt="Skill Packages">
          <img src="https://img.shields.io/badge/LLM%20Agents-yellow" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Context%20Management-teal" alt="Context Management">
          <img src="https://img.shields.io/badge/Package%20Registry-orange" alt="Package Registry">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16911">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 Skilldex，一个面向 LLM Agent 技能包的包管理器与注册表，用格式一致性评分检查技能包是否符合 Anthropic 规范。<br>
          • 提出 skillset 抽象，将相关技能与共享资源打包以保持跨技能一致性，并提供三层层级作用域、人工反馈建议循环、元数据注册表和 MCP 服务器等基础设施。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>Bolzano: Case Studies in LLM-Assisted Mathematical Research</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Persistent%20Knowledge%20Base-brightgreen" alt="Persistent Knowledge Base">
          <img src="https://img.shields.io/badge/Multi--agent%20LLM-yellow" alt="Multi-agent LLM">
          <img src="https://img.shields.io/badge/Knowledge%20Update-teal" alt="Knowledge Update">
          <img src="https://img.shields.io/badge/LLM--assisted%20Research-orange" alt="LLM-assisted Research">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16989">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 介绍开源多智能体 LLM 系统 Bolzano，通过并行证明代理与验证代理协作，在多轮交互中维护持久知识库。<br>
          • 系统完成数学与理论计算机科学中的六个问题，其中四项结果达到可发表水平，三项几乎由系统自主产生。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-18</td>
        <td style="width: 55%;"><strong>GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Context%20Compression-brightgreen" alt="Context Compression">
          <img src="https://img.shields.io/badge/Long--horizon%20Agents-yellow" alt="Long-horizon Agents">
          <img src="https://img.shields.io/badge/Self--evolving%20Agent-teal" alt="Self-evolving Agent">
          <img src="https://img.shields.io/badge/LLM%20Memory-orange" alt="LLM Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.17091">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 GenericAgent，一种面向长程任务的自演化 LLM Agent，核心目标是在有限上下文中最大化决策相关信息密度。<br>
          • 系统包含最小化工具集、层次化按需记忆、自我演化机制以及上下文截断与压缩层，可将验证轨迹转化为可复用 SOP 和代码。
        </td>
      </tr>
<tr>
          <td rowspan="2" style="width: 15%;">2026-04-11</td>
          <td style="width: 55%;"><strong>Mosaic: Cross-Modal Clustering for Efficient Video Understanding</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Video%20Memory-red" alt="Video Memory">
              <img src="https://img.shields.io/badge/Systems%20Design-teal" alt="Systems Design">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.10060">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 Mosaic，一个面向长视频理解的跨模态聚类系统。<br>
              • 发现 VLM 的 KV Cache 中存在隐式跨模态聚类结构，并以簇为单位完成缓存组织、维护与检索。<br>
              • 该方法降低了碎片化迁移与管理成本，在流式视频推理中最高实现 1.38 倍加速。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-04-10</td>
          <td style="width: 55%;"><strong>EpiAgent: An Agent-Centric System for Ancient Inscription Restoration</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Agent%20System-red" alt="Agent System">
              <img src="https://img.shields.io/badge/Multimodal%20Restoration-teal" alt="Multimodal Restoration">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09367">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 EpiAgent，一个面向古代碑刻修复的 Agent-centric 系统。<br>
              • 系统采用 Observe-Conceive-Execute-Reevaluate 闭环，由中心 LLM 规划器协调多模态分析、历史经验、修复工具与自我反思。<br>
              • 在真实修复场景中优于现有方法，并同时提升了修复质量与泛化能力。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-04-10</td>
          <td style="width: 55%;"><strong>Building an Internal Coding Agent at Zup: Lessons and Open Questions</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Coding%20Agent-red" alt="Coding Agent">
              <img src="https://img.shields.io/badge/State%20Management-teal" alt="State Management">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.09805">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 总结了 Zup 内部编码 Agent CodeGen 从原型走向生产的关键经验。<br>
              • 指出系统可靠性不仅取决于底层模型，也高度依赖工具设计、安全护栏、状态管理与人工监督。<br>
              • 通过字符串替换式编辑、分层安全约束与渐进式监管，提高了系统采用率与稳定性，并给出若干开放问题。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-04-09</td>
          <td style="width: 55%;"><strong>PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Shared%20State-red" alt="Shared State">
              <img src="https://img.shields.io/badge/Personal%20AI-teal" alt="Personal AI">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08529">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 PSI 共享状态架构，将分散生成的个人 AI 模块连接为一致的工具生态。<br>
              • 系统通过个人上下文总线公开当前状态，并支持写回，从而实现跨模块推理与同步。<br>
              • 作者在三周的个人 AI 部署中验证了该架构可自动整合后续生成的新工具。
          </td>
      </tr>
      <tr>
          <td rowspan="2" style="width: 15%;">2026-04-09</td>
          <td style="width: 55%;"><strong>Omakase: proactive assistance with actionable suggestions for evolving scientific research projects</strong></td>
          <td style="width: 15%;">
              <img src="https://img.shields.io/badge/Proactive%20Assistant-red" alt="Proactive Assistant">
              <img src="https://img.shields.io/badge/Long%20Term%20Memory-teal" alt="Long Term Memory">
          </td>
          <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08898">
              <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 提出了 Omakase，一个面向持续演化科研项目的主动式研究助手。<br>
              • 系统持续监控项目文档，自动发现合适的深度研究查询，并将长报告提炼为贴合项目上下文的可执行建议。<br>
              • 用户研究表明，其生成的建议比原始报告更及时，也更具可操作性。
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-15</td>
        <td style="width: 55%;"><strong>SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Information%20Geometry-red" alt="Information Geometry">
            <img src="https://img.shields.io/badge/Agent%20Memory-teal" alt="Agent Memory">
            <img src="https://img.shields.io/badge/Data%20Sovereignty-blue" alt="Data Sovereignty">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.14588">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 面向企业级代理持久记忆，提出检索、生命周期与一致性验证三位一体的数学化方案，突破传统记忆系统高度依赖工程启发式的问题。 <br>
            • 在 LoCoMo 基准上，相比工程基线平均提升 12.7%，最难样本提升 19.9%，验证了信息几何方法在复杂记忆检索中的有效性。<br>
            • 该工作将代理记忆从工程组件堆叠推进到可证明、可治理、可合规的系统设计范式，对高隐私、高主权场景具有代表意义。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-05</td>
        <td style="width: 55%;"><strong>Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Ontology-red" alt="Ontology">
            <img src="https://img.shields.io/badge/Digital%20Citizens-teal" alt="Digital Citizens">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04740v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出记忆即本体的新范式，面向持续性数字主体，解决 AI 模型跨代演进中的身份连续性问题。<br>
            • 建立宪法式记忆架构，通过四层治理层级、多层语义存储与完整生命周期设计，支撑数字公民的长期存在与演化。<br>
            • 将底层计算模型降级为可替换载体，优先保障数字实体的身份与治理持久性，而非仅优化短期记忆调用与检索效率。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-04</td>
        <td style="width: 55%;"><strong>Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/RL-red" alt="RL">
            <img src="https://img.shields.io/badge/Experience%20Memory-teal" alt="Experience Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04257v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 现有通过截断或摘要处理长上下文窗口限制的方法，容易导致关键交互证据丢失。<br>
            • 提出索引经验记忆机制 Memex 实现无损压缩，并引入强化学习框架 MemexRL 优化智能体的读写归档策略。<br>
            • 该系统使得智能体能够自主决策归档与检索时机，在显著压缩工作上下文的同时大幅提升了长程任务成功率。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-25</td>
        <td style="width: 55%;"><strong>MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Phishing%20Detection-red" alt="Phishing Detection">
            <img src="https://img.shields.io/badge/Episodic%20Memory-teal" alt="Episodic Memory">
            <img src="https://img.shields.io/badge/Multi--Modal-blue" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21394.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出 MPA 代理，利用过去推理轨迹的情节记忆来指导针对重复和新型钓鱼威胁的决策。<br>
            • 在公共数据集中回忆率较最先进基线提升了 13.6%，真实场景下提升高达 20%。<br>
            • 分析表明情节记忆贡献了约 27% 的回忆增益，且不会引入额外的计算开销。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>MMA: Multimodal Memory Agent</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multimodal-blue" alt="Multimodal">
            <img src="https://img.shields.io/badge/Reliability%20Score-orange" alt="Reliability Score">
            <img src="https://img.shields.io/badge/Visual%20Bias-red" alt="Visual Bias">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16493.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出多模态记忆代理（MMA），通过为检索项分配动态可靠性评分（结合来源、衰减和冲突感应）来解决 RAG 中的过度自信错误。<br>
            • 引入 MMA-Bench 基准，用于控制说话者可靠性并评估文本-视觉矛盾下的信念动态。<br>
            • 揭示了“视觉安慰效应”，即代理容易继承基础模型中潜在的视觉偏见。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-07</td>
      <td style="width: 55%;"><strong>M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multimodal%20Memory-pink" alt="Multimodal Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-purple" alt="Memory Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.07624">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架通过 ChatAgent（负责交互）和 MemoryManager（负责记忆操作）的协作，将静态的多模态个性化转变为能够随对话进程不断更新和演进的记忆机制。<br>
        • 系统由存储原始日志的底层和存储高层观察的语义层组成，利用证据 ID 链接两层记忆，并通过结合文本、关键词和图像的三路径检索实现精准的上下文召回。<br>
        • 论文开发了一套可扩展的流水线用于生成长程多模态对话数据集，实验证明 M2A 在处理复杂的个性化问题时显著优于现有的 RAG 和文本记忆基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Interpretability-pink" alt="Interpretability">
      <img src="https://img.shields.io/badge/Psycholinguistics-brown" alt="Psycholinguistics">
      <img src="https://img.shields.io/badge/Attention%20Mechanism-blue" alt="Attention Mechanism">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20282">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
      • 借鉴心理学中的“编码特异性原则”（Encoding Specificity Principle），研究了 Transformer 注意力层中的记忆机制。<br>
      • 提出 Q 编码检索上下文，K 索引记忆痕迹，V 存储内容，并实证表明上下文线索被编码为关键词（Keywords）。<br>
      • 识别出了特定的注意力神经元，其激活有助于上下文定义关键词的检索，为机器遗忘等下游任务提供了理论基础和提取方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>S3-Attention: Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Efficient%20Inference-success" alt="Efficient Inference">
        <img src="https://img.shields.io/badge/Endogenous%20Retrieval-teal" alt="Endogenous Retrieval">
        <img src="https://img.shields.io/badge/Sparse%20Autoencoders-violet" alt="Sparse Autoencoders">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.17702">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 S3-Attention（Sparse & Semantic Streaming Attention），一种针对内存受限长上下文推理的框架，实现了 O(1) 的 GPU 内存占用。<br>
        • 利用稀疏自动编码器（SAE）将注意力状态解码为稀疏特征，在流式处理中构建 CPU 倒排索引并丢弃 KV 缓存。<br>
        • 通过特征共激活进行内源性检索，在 LongBench 上保持了接近全上下文的性能（例如在 Llama-3-8B 上保留了 99.4% 的性能）。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-19</td>
      <td style="width: 55%;"><strong>LLM-as-RNN: A Recurrent Language Model for Memory Updates and Sequence Prediction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Recurrent%20Architecture-darkslategrey" alt="Recurrent Architecture">
        <img src="https://img.shields.io/badge/Inference--Only-orange" alt="Inference-Only">
        <img src="https://img.shields.io/badge/Time--Series-blue" alt="Time-Series">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.13352">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LLM-as-RNN，一种仅推理的框架，将冻结的 LLM 转换为循环预测器，解决了标准 ICL 无法更新错误的问题。<br>
        • 将隐藏状态表示为自然语言记忆（结构化系统提示摘要），并通过基于反馈的文本重写在每一步更新该状态，实现了在线学习。<br>
        • 在医疗、气象和金融的时序预测任务中，LLM-as-RNN 在固定 Token 预算下显著优于 Zero-shot 和 MemPrompt 基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;"><strong>Continuum Memory Architectures for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Architecture-purple" alt="Memory Architecture">
        <img src="https://img.shields.io/badge/Long--Horizon-red" alt="Long-Horizon">
        <img src="https://img.shields.io/badge/Continuum-success" alt="Continuum">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.09913">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 面向长时程智能体提出“连续体（continuum）”式记忆架构，解决长跨度任务中的稳定性与可持续回忆问题。<br>
        • 系统化讨论不同记忆层/库（如工作、情景、语义等）的分工与交互，以及随时间推进的管理策略。<br>
        • 通过长时程任务实验展示：架构化的记忆组织优于简单拼接/截断或朴素外检索。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-17</td>
      <td style="width: 55%;"><strong>Memory Bear AI: A Breakthrough from Memory to Cognition</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2512.20651">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memory Bear 构建了一种基于认知科学（ACT-R、艾宾浩斯）的类人记忆架构，通过区分显性与隐性记忆及引入智能语义剪枝，实现了从“记忆”到“认知”的跃迁。<br>
        • 该系统采用三层架构（存储、编排、应用），集成了自我反思引擎和多模态感知，在大幅降低 Token 消耗（约 90%）的同时，显著减少了幻觉并提升了长期交互的连贯性。<br>
        • 实验结果表明，Memory Bear 在准确率和响应延迟上均优于 Mem0 和 MemGPT，并已在医疗（慢性病管理）、企业（知识库）和教育（个性化学习）场景中验证了其有效性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-11</td>
      <td style="width: 55%;"><strong>O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.13593">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • O-Mem 是一种基于主动用户画像的新型记忆框架，能够通过主动交互动态提取并更新用户特征和事件记录。<br>
        • 与依赖语义分组的系统不同，O-Mem 支持对角色属性和主题相关上下文进行层级检索，从而实现自适应且连贯的个性化响应。<br>
        • 该系统在 LoCoMo 和 PERSONAMEM 基准测试中达到了最先进的性能，同时与 LangMem 和 MemoryOS 等先前的框架相比，显著提高了 Token 效率和交互响应时间。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-21</td>
      <td style="width: 55%;"><strong>Episodic Memory in Agentic Frameworks: Suggesting Next Steps in Workflow Creation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Workflow%20Memory-purple" alt="Workflow Memory">
        <img src="https://img.shields.io/badge/Next--Step-red" alt="Next-Step">
        <img src="https://img.shields.io/badge/Episodic-success" alt="Episodic">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.17775">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将“工作流轨迹/操作序列”作为情景记忆（episodic memory）存储，面向流程型 agent 的长期复用。<br>
        • 通过检索相似 workflow episode 为用户提供下一步建议（next-step suggestion），降低纯 LLM 规划带来的不确定性。<br>
        • 在 workflow 创建/编辑场景中评估建议质量与可用性，强调工具型、流程型 agent 的落地价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-11</td>
      <td style="width: 55%;"><strong>From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Graph%20Memory-purple" alt="Graph Memory">
        <img src="https://img.shields.io/badge/Trainable-red" alt="Trainable">
        <img src="https://img.shields.io/badge/Strategy-success" alt="Strategy">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.07800">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 引入可训练的图结构记忆，将经验以节点/边组织，支持跨回合复用与结构化推理。<br>
        • 重点在“从经验到策略”：通过学习记忆图上的选择/加权/路由，使 agent 能抽象出可迁移的决策模式。<br>
        • 在需要长期经验积累或多步策略形成的任务上，展示相对传统检索式记忆的优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-21</td>
      <td style="width: 55%;"><strong>LIGHTMEM: LIGHTWEIGHT AND EFFICIENT MEMORY-AUGMENTED GENERATION</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.18866">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LightMem 是一种受 Atkinson-Shiffrin 人类记忆模型启发的轻量级记忆架构，旨在平衡 LLM 的性能与效率。<br>
        • 它具有三阶段流程：受认知启发的感官记忆用于过滤冗余，主题感知的短期记忆用于结构化访问，以及具有睡眠时间更新机制的长期记忆，以将维护与推理解耦。<br>
        • 在 LongMemEval 和 LoCoMo 上的实验结果表明，LightMem 在准确性上优于强大的基线模型，同时将 Token 使用量减少高达 100 倍，并显著降低了 API 调用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-10</td>
      <td style="width: 55%;"><strong>Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/System-darkblue" alt="System">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2508.09736">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 M3-Agent，这是一种新型多模态智能体框架，通过处理连续的视觉和听觉输入来模拟人类记忆，以构建以实体为中心的情景和语义长期记忆。<br>
        • 提出了 M3-Bench，这是一个全面的长视频问答基准，包含来自机器人和网络视角的 1,020 个视频，旨在评估人物理解和跨模态推理等能力。<br>
        • 实验结果表明，通过强化学习训练的 M3-Agent 在记忆保持和推理任务中显著优于 Gemini-1.5-Pro 和 GPT-4o 等强大的基线模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-08</td>
      <td style="width: 55%;"><strong>A-MEM: Agentic Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.12110">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • A-Mem 引入了一种受卢曼卡片盒笔记法（Zettelkasten）启发的动态记忆组织方式，赋予 LLM 智能体真正的长期记忆。<br>
        • 除了简单的存储，A-Mem 还支持自链接和自进化，使智能体在复杂的推理任务中获得显著优势。<br>
        • 实验结果表明，A-Mem 在性能、效率和可扩展性方面均优于现有方法，为构建更智能、更自主的 LLM 智能体奠定了坚实基础。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-01</td>
      <td style="width: 55%;"><strong>Improving Code Localization with Repository Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Repository%20Memory-purple" alt="Repository Memory">
        <img src="https://img.shields.io/badge/Code%20Localization-red" alt="Code Localization">
        <img src="https://img.shields.io/badge/SWE-success" alt="SWE">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2510.01003">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将仓库的 commit history/演化信息作为“长期 repository memory”，为软件工程 agent 提供可追溯的历史上下文。<br>
        • 通过检索与汇总历史变更、相关模块演进、issue/PR 线索，提升 bug/需求对应的代码定位（localization）。<br>
        • 结果表明：相较仅依赖当前代码快照，利用仓库记忆可显著提升定位准确性与定位效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-12</td>
      <td style="width: 55%;"><strong>Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/System-darkblue" alt="System">
        <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2509.05298">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Livia 是一款具有情感意识的 AR 伴侣，旨在通过模块化的多智能体架构和沉浸式增强现实交互来缓解孤独感。<br>
        • 它引入了两种新颖的记忆压缩算法——时间二进制压缩（TBC）和动态重要性记忆过滤器（DIMF）——以高效管理长期记忆，同时保留具有情感意义的上下文。<br>
        • 该系统集成了多模态情感识别（文本和语音）和自适应个性模型，展现出高准确性并能与用户建立更深层的情感纽带。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-05</td>
      <td style="width: 55%;"><strong>NEMORI: SELF-ORGANIZING AGENT MEMORY INSPIRED BY COGNITIVE SCIENCE</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2508.03341">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Nemori 是一种受认知科学启发的自组织记忆架构，旨在通过实现持久、自适应的记忆来解决大型语言模型在长期交互中的局限性。<br>
        • 它引入了用于自主情节分割的“两步对齐原则”和用于主动知识蒸馏的“预测-校准原则”，实现了从被动存储到主动学习的转变。<br>
        • 在 LoCoMo 和 LongMemEval 基准测试上的实验结果表明，Nemori 显著优于最先进的系统，且 Token 使用量比全上下文基线少 88%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-23</td>
      <td style="width: 55%;"><strong>H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2507.22925">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 H-MEM，这是一种分层记忆架构，利用位置索引编码将记忆组织成四个语义层级，实现了高效的逐层检索，无需进行穷尽的相似度计算。<br>
        • 引入了一种动态记忆更新机制，根据用户反馈调整记忆权重，以反映用户不断变化的兴趣和心理状态。<br>
        • 在 LoCoMo 数据集上的实验结果表明，H-MEM 在长期对话任务中始终优于基线模型，同时显著降低了计算成本和检索延迟。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-10</td>
      <td style="width: 55%;"><strong>MIRIX: Multi-Agent Memory System for LLM-Based Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2507.07957">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MIRIX 是一个模块化的多智能体记忆系统，通过集成由专用智能体管理的六个专门记忆组件（包括情景记忆、语义记忆和程序记忆），解决了扁平化记忆架构的局限性。<br>
        • 该框架引入了“主动检索”机制和元记忆管理器来动态协调记忆更新与检索，并在新引入的多模态基准 ScreenshotVQA（由高分辨率用户活动日志组成）上验证了这些能力。<br>
        • 实验结果表明，MIRIX 在 ScreenshotVQA 上的准确率比 RAG 基线高出 35%，存储空间减少了 99.9%，并在 LOCOMO 长对话基准上达到了最先进的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-06-30</td>
      <td style="width: 55%;"><strong>Ella: Embodied Social Agents with Lifelong Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2506.24019">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 Ella，这是一个具身社交智能体，配备了结构化的终身多模态记忆系统，包含以名字为中心的语义记忆和时空情景记忆。<br>
        • 通过将这种终身记忆系统与基础模型集成，Ella 可以检索相关信息以进行决策、规划日常活动，并在 3D 开放世界中建立社会关系。<br>
        • 在动态环境中的实验结果证明了 Ella 影响、领导以及与其他智能体合作的能力，突显了结合结构化记忆与基础模型的潜力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-30</td>
      <td style="width: 55%;"><strong>Memory OS of AI Agent</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Operating%20System-midnightblue" alt="Memory Operating System">
      <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.emnlp-main.1318.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoryOS 旨在为 AI 智能体提供全面且高效的记忆管理。<br>
        • 受计算机操作系统内存管理原理和人类记忆分层结构的启发，MemoryOS 采用独特的段-页分层存储架构，包含四个核心功能模块：记忆存储、记忆更新、记忆检索和响应生成。<br>
        • 实验结果表明，MemoryOS 在主流基准测试的长对话中显著提高了上下文连贯性和个性化记忆保持能力；例如，在 LoCoMo 基准测试上，平均 F1 和 BLEU-1 分数分别提高了 49.11% 和 46.18%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-28</td>
      <td style="width: 55%;"><strong>MemOS: A Memory OS for AI System</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/MemOS-darkorange" alt="MemOS">
        <img src="https://img.shields.io/badge/Memory%20Operating%20System-midnightblue" alt="Memory Operating System">
        <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2507.03724">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemOS（记忆操作系统）是专为 AI 系统设计的记忆操作系统，它将记忆视为可管理的系统资源，统一了显式记忆、基于激活的记忆和参数级记忆的表示、调度和进化，以实现低成本的存储和检索。<br>
        • MemOS 采用三层架构，由接口层、操作层和基础设施层组成。接口层与用户或上游系统交互并提供标准化记忆 API；操作层组织和调度记忆资源；基础设施层处理记忆的存储、安全、迁移和数据流。<br>
        • MemOS 为跨任务适应、跨模态进化和跨平台迁移提供了操作系统级的支持。它的引入标志着大模型从“仅感知和生成”向“具有记忆和进化能力”智能的关键转变。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-28</td>
      <td style="width: 55%;"><strong>Mem0 Building production-ready AI agents with Scalable Long-Term memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2504.19413">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Mem0 是一种记忆架构，能从对话中动态提取并整合关键信息，使 AI 系统能够记住重要内容并维持跨会话对话。<br>
        • 作者进一步提出了 Mem0g，通过结合图结构记忆（即知识图谱）扩展了 Mem0，使 AI 系统能更有效地处理复杂的关系推理。<br>
        • NLI 任务增强了成分句法归纳能力，而 SMS 任务则降低了上层的这一能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-22</td>
      <td style="width: 55%;"><strong>Echo: A Large Language Model with Temporal Episodic Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Temporal%20Episodic-purple" alt="Temporal Episodic">
        <img src="https://img.shields.io/badge/LLM%20Model-red" alt="LLM Model">
        <img src="https://img.shields.io/badge/Recall-success" alt="Recall">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.16090">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出带“时间化情景记忆”的 LLM 形态，将事件按时间索引存储，面向时序依赖与经历回放式回忆。<br>
        • 强调 temporal episodic memory 对事件序列、时间关系、跨回合一致性推理的帮助。<br>
        • 通过相关基准/任务展示：相较无显式情景记忆的模型，在时序回忆与推理上更可靠。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-20</td>
      <td style="width: 55%;"><strong>ZEP: A TEMPORAL KNOWLEDGE GRAPH ARCHITECTURE FOR AGENT MEMORY</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.13956">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 Zep，这是一种由动态且具有时间感知的知识图谱引擎 Graphiti 驱动的 AI 智能体记忆层服务。<br>
        • Zep 在保持历史关系的同时，综合了非结构化对话数据和结构化业务数据，使智能体能够处理复杂、演变的上下文。<br>
        • 实验结果表明，Zep 在深度记忆检索（DMR）基准测试中优于 MemGPT，并在更具挑战性的 LongMemEval 基准测试中显著提高了准确性和延迟表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-09</td>
      <td style="width: 55%;"><strong>Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.00358">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Embodied VideoAgent，这是一种多模态智能体，通过融合第一视角视频与深度、姿态等具身感知输入来构建持久的场景记忆，以解决动态场景理解问题。<br>
        • 具有 VLM 驱动的记忆更新机制，可在动作过程中动态跟踪物体状态变化和关系，确保记忆在长形式交互中保持准确。<br>
        • 该智能体在 Ego4D-VQ3D 和 OpenEQA 等基准测试中达到了最先进的性能，并在生成合成具身用户-助手交互数据方面展示了实用价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-12</td>
      <td style="width: 55%;"><strong>Memory Layers at Scale</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Layers-purple" alt="Memory Layers">
        <img src="https://img.shields.io/badge/KV%20Lookup-red" alt="KV Lookup">
        <img src="https://img.shields.io/badge/Scaling-success" alt="Scaling">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2412.09764">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探索可训练的 key–value 记忆层（memory layers）作为“稀疏查表式容量扩展”，在不显著增加计算的情况下提升模型存储能力。<br>
        • 讨论大规模训练与工程实现：如何让超大记忆表可并行、可扩展并保持稳定训练。<br>
        • 在多个任务上展示：大容量记忆层可提升知识/事实类能力，并具备更好的容量-成本权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-06-16</td>
      <td style="width: 55%;"><strong>Towards Lifelong Dialogue Agents via Timeline-based Memory Management</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.naacl-long.435.pdf">
      <img src="https://img.shields.io/badge/NAACL-Paper-black?labelColor=cyan" alt="NAACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 THEANINE，这是一个用于终身对话智能体的框架，利用关系感知的记忆图谱来存储记忆而不删除，保留了时间与因果连接。<br>
        • 引入了一种时间轴增强的响应生成方法，检索并细化整个记忆时间轴，确保为长期交互保留丰富的上下文线索。<br>
        • 展示了 TeaFarm，这是一个反事实驱动的评估流程，旨在压力测试对话智能体正确引用过去对话的能力，THEANINE 在该流程中表现出优于现有基线的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-04</td>
      <td style="width: 55%;"><strong>Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/System-darkblue" alt="System">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/10.1145/3613904.3642450">
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="ACM Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Memoro 是一款可穿戴的音频记忆助手，旨在利用大型语言模型（LLM）进行简明的记忆检索，从而最大限度地减少社交互动中的干扰。<br>
          • 该系统引入了“无查询模式”，根据实时对话上下文主动推断用户的记忆需求，同时保留了用于明确自然语言请求的传统“查询模式”。<br>
          • 用户研究表明，Memoro 提高了回忆的信心并减少了设备交互时间，同时有效地保持了正在进行的对话质量。
        </td>
    </tr>
  </table>

</details>

## 🧰 仓库资源

### 📊 测试基准

|     任务类型      | 数据集和评估基准                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **个性化任务评估**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745), [ATM-Bench](https://arxiv.org/pdf/2603.01990)  |
|  **综合评价**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **记忆机制评价**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **长期记忆评估**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144), [Mem-Gallery](https://arxiv.org/pdf/2601.03515), [RealMem](https://arxiv.org/pdf/2601.06966), [CloneMem](https://arxiv.org/pdf/2601.07023) |
|  **长对话推理**   | [PREFEVAL](https://arxiv.org/pdf/2502.09597),  [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf)|
|  **长上下文理解**   | [LongBench V2](https://arxiv.org/pdf/2412.15204), [LongBench](https://arxiv.org/abs/2308.14508), [BABILong](https://arxiv.org/pdf/2406.10149), [HotpotQA](https://aclanthology.org/D18-1259.pdf) |
|  **长上下文评估** |[SCBENCH](https://arxiv.org/abs/2412.10319), [L-CiteEval](https://arxiv.org/pdf/2410.02115), [GLE](https://aclanthology.org/2024.acl-long.859/), [HOMER](https://arxiv.org/pdf/2404.10308), [RULER](https://arxiv.org/pdf/2404.06654), [MM-Needle](https://aclanthology.org/2025.naacl-long.166.pdf) |
|  **长文本生成**   | [LongGenBench](https://arxiv.org/pdf/2409.02076) |
|  **情景记忆评估**   | [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf)|
|  **记忆幻觉评估**   | [HaluMem](https://arxiv.org/pdf/2511.03506) |
|  **Web交互与导航** | [WebChoreArena](https://arxiv.org/pdf/2506.01952), [MT-Mind2Web](https://arxiv.org/pdf/2402.15057), [WebShop](https://arxiv.org/pdf/2207.01206), [WebArena](https://arxiv.org/pdf/2307.13854) |


### 💻 开源系统
下面系统按照时间顺序排列:

| 系统      | 时间       | 关注数 | 开源网址和官方网站 |
|-------------|------------|-------|------------------|
| Zep         | 2023-05-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/zep?style=social) | https://github.com/getzep/zep<br>https://www.getzep.com/ |
| Agentmemory | 2023-07-07 | ![GitHub Repo stars](https://img.shields.io/github/stars/elizaOS/agentmemory?style=social) | https://github.com/elizaOS/agentmemory<br>No official website |
| Cognee      | 2023-10-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/topoteretes/cognee?style=social) | https://github.com/topoteretes/cognee<br>https://www.cognee.ai/ |
| Letta       | 2023-10-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) | https://github.com/letta-ai/letta<br>https://www.letta.com/ |
| Supermemory | 2024-02-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=social) | https://github.com/supermemoryai/supermemory<br>https://supermemory.ai/ |
| Memary      | 2024-04-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/kingjulio8238/Memary?style=social) | https://github.com/kingjulio8238/Memary <br>No official website |
| Second-Me   | 2024-06-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/mindverse/Second-Me?style=social) | https://github.com/mindverse/Second-Me<br>https://home.second.me/ |
| Mem0        | 2024-07-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) | https://github.com/mem0ai/mem0<br>https://mem0.ai/ |
| Memobase    | 2024-10-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/memodb-io/memobase?style=social) | https://github.com/memodb-io/memobase<br>https://www.memobase.io/ |
| Agent Brain | 2024-12-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/kaderosio/agent-brain?style=social) | https://github.com/kaderosio/agent-brain<br>No official website |
| Puppyone    | 2024-12-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/puppyone-ai/puppyone?style=social) | https://github.com/puppyone-ai/puppyone<br>https://www.puppyone.ai/ |
| LangMem     | 2025-01-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) | https://github.com/langchain-ai/langmem<br>https://langchain-ai.github.io/langmem/ |
| Vestige     | 2025-01-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/samvallad33/vestige?style=social) | https://github.com/samvallad33/vestige<br>https://samvallad33.github.io/vestige/ |
| A-Mem       | 2025-02-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/A-mem?style=social) | https://github.com/agiresearch/A-mem <br>No official website |
| Mirix       | 2025-04-16 | ![GitHub Repo stars](https://img.shields.io/github/stars/Mirix-AI/MIRIX?style=social) | https://github.com/Mirix-AI/MIRIX<br>https://mirix.io/ |
| MemEngine   | 2025-05-04 | ![GitHub Repo stars](https://img.shields.io/github/stars/nuster1128/MemEngine?style=social) | https://github.com/nuster1128/MemEngine<br>No official website |
| MemOS       | 2025-05-28 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=social) | https://github.com/MemTensor/MemOS<br>https://memos.openmem.net/ |
| MemoryOS    | 2025-05-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/BAI-LAB/MemoryOS?style=social) | https://github.com/BAI-LAB/MemoryOS<br>https://baijia.online/memoryos/ |
| ReMe        | 2025-06-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/agentscope-ai/ReMe?style=social) | https://github.com/agentscope-ai/ReMe<br>https://reme.agentscope.io/ |
| Nemori      | 2025-06-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/nemori-ai/nemori?style=social) | https://github.com/nemori-ai/nemori <br>No official website |
| Memori      | 2025-07-24 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemoriLabs/Memori?style=social) | https://github.com/MemoriLabs/Memori<br>https://memorilabs.ai/ |
| MemU        | 2025-08-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social) | https://github.com/NevaMind-AI/memU<br>https://memu.pro/ |
| MemMachine  | 2025-08-16 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemMachine/MemMachine?style=social) | https://github.com/MemMachine/MemMachine<br>https://memmachine.ai/ |
| MineContext | 2025-09-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/volcengine/MineContext?style=social) | https://github.com/volcengine/MineContext<br>No official website |
| TiMem | 2025-10-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/TiMEM-AI/timem?style=social) | https://github.com/TiMEM-AI/timem<br>https://timem.cloud |
| EverMemOS   | 2025-10-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/EverMind-AI/EverMemOS?style=social) | https://github.com/EverMind-AI/EverMemOS<br>https://evermind.ai/ |
| MemoryBear  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/SuanmoSuanyangTechnology/MemoryBear?style=social) | https://github.com/SuanmoSuanyangTechnology/MemoryBear<br>https://www.memorybear.ai/ |
| OMEGA  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/omega-memory/omega-memory?style=social) | https://github.com/omega-memory/omega-memory<br>https://omegamax.co/ |
| Autohand Code CLI | 2025-12-20 | ![GitHub Repo stars](https://img.shields.io/github/stars/autohandai/code-cli?style=social) | https://github.com/autohandai/code-cli<br>https://www.autohand.ai/code/ |
| Hindsight   | 2025-12-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social) | https://github.com/vectorize-io/hindsight<br>https://hindsight.vectorize.io/ |
| MAGMA       | 2026-01-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/FredJiang0324/MAMGA?style=social) | https://github.com/FredJiang0324/MAMGA<br>No official website |
| Mengram | 2026-02-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/alibaizhanov/mengram?style=social) | https://github.com/alibaizhanov/mengram<br>https://mengram.io/ |
| widemem-ai | 2026-02-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/remete618/widemem-ai?style=social) | https://github.com/remete618/widemem-ai<br>https://widemem.ai |
| Riverse | 2026-02-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/wangjiake/JKRiver?style=social) | https://github.com/wangjiake/JKRiver<br>https://wangjiake.github.io/riverse-docs/ |
| SuperLocalMemory | 2026-03-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/qualixar/superlocalmemory?style=social) | https://github.com/qualixar/superlocalmemory<br>https://superlocalmemory.com/ |
| Cog | 2026-03-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/marciopuga/cog?style=social) | https://github.com/marciopuga/cog<br>No official website |
| NeverOnce | 2026-03-18 | ![GitHub Repo stars](https://img.shields.io/github/stars/WeberG619/neveronce?style=social) | https://github.com/WeberG619/neveronce<br>https://pypi.org/project/neveronce/ |
| MHN AI Agent Memory | 2026-03-21 | ![GitHub Repo stars](https://img.shields.io/github/stars/shahzebqazi/mhn-ai-agent-memory?style=social) | https://github.com/shahzebqazi/mhn-ai-agent-memory<br>No official website |
| LycheeMem | 2026-03-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social) | https://github.com/LycheeMem/LycheeMem<br>No official website |
| GoodMemory | 2026-03-24 | ![GitHub Repo stars](https://img.shields.io/github/stars/hjqcan/GoodMemory?style=social) | https://github.com/hjqcan/GoodMemory<br>https://www.npmjs.com/package/goodmemory |
| MemClaw | 2026-03-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/Felo-Inc/memclaw?style=social) | https://github.com/Felo-Inc/memclaw<br>https://memclaw.me |
| MemPalace | 2026-04-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social) | https://github.com/MemPalace/mempalace<br>http://mempalaceofficial.com/ |
| SwarmVault | 2026-04-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/swarmclawai/swarmvault?style=social) | https://github.com/swarmclawai/swarmvault<br>https://swarmvault.ai |
| PackRat | 2026-04-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/kevdogg102396-afk/packrat?style=social) | https://github.com/kevdogg102396-afk/packrat<br>https://www.npmjs.com/package/packrat-compress |
| SkillClaw | 2026-04-10 | ![GitHub Repo stars](https://img.shields.io/github/stars/AMAP-ML/SkillClaw?style=social) | https://github.com/AMAP-ML/SkillClaw<br>https://arxiv.org/abs/2604.08377 |
| Synap | 2026-04-10 | ![GitHub Repo stars](https://img.shields.io/github/stars/maximem-ai/maximem_synap_sdk?style=social) | https://github.com/maximem-ai/maximem_synap_sdk<br>https://maximem.ai |
| Mnemoverse | 2026-04-10 | ![GitHub Repo stars](https://img.shields.io/github/stars/mnemoverse/mcp-memory-server?style=social) | https://github.com/mnemoverse/mcp-memory-server<br>https://mnemoverse.com |
| Formative Memory | 2026-04-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/jarimustonen/formative-memory?style=social) | https://github.com/jarimustonen/formative-memory<br>No official website |
| taOSmd | 2026-04-13 | ![GitHub Repo stars](https://img.shields.io/github/stars/jaylfc/taosmd?style=social) | https://github.com/jaylfc/taosmd<br>[Docs & benchmarks](https://github.com/jaylfc/taosmd/blob/master/docs/benchmarks.md) |
| Engram | 2026-04-13 | ![GitHub Repo stars](https://img.shields.io/github/stars/FBISiri/engram?style=social) | https://github.com/FBISiri/engram<br>No official website |
| ToolPipe | 2026-04-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/COSAI-Labs/toolpipe-mcp-server?style=social) | https://github.com/COSAI-Labs/toolpipe-mcp-server<br>https://toolpipe.dev |
| Origin | 2026-04-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/7xuanlu/origin?style=social) | https://github.com/7xuanlu/origin<br>https://useorigin.app |
| Omnigraph | 2026-04-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/ModernRelay/omnigraph?style=social) | https://github.com/ModernRelay/omnigraph<br>https://omnigraph.dev/ |
| Mnemory | 2026-05-03 | ![GitHub Repo stars](https://img.shields.io/github/stars/fpytloun/mnemory?style=social) | https://github.com/fpytloun/mnemory<br>No official website |
| kaeru | 2026-05-08 | ![GitHub Repo stars](https://img.shields.io/github/stars/LamantinAI/kaeru?style=social) | https://github.com/LamantinAI/kaeru<br>No official website |
| Dakera | 2026-05-12 | ![GitHub Repo stars](https://img.shields.io/github/stars/dakera-ai/dakera-mcp?style=social) | https://github.com/dakera-ai/dakera-mcp<br>https://dakera.ai/ |
| Perseus | 2026-05-18 | ![GitHub Repo stars](https://img.shields.io/github/stars/tcconnally/perseus?style=social) | https://github.com/tcconnally/perseus<br>https://perseus.observer/ |
| Talamus | 2026-05-21 | ![GitHub Repo stars](https://img.shields.io/github/stars/ampres-ai/talamus?style=social) | https://github.com/ampres-ai/talamus<br>https://ampres-ai.github.io/talamus/ |
| Agentic Task System | 2026-05-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/renezander030/agentic-task-system?style=social) | https://github.com/renezander030/agentic-task-system<br>https://www.npmjs.com/package/@reneza/ats-cli |
| OWASP Agent Memory Guard | 2026-05-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/OWASP/www-project-agent-memory-guard?style=social) | https://github.com/OWASP/www-project-agent-memory-guard<br>https://pypi.org/project/agent-memory-guard/ |
| Engrava | 2026-06-02 | ![GitHub Repo stars](https://img.shields.io/github/stars/sovantica/engrava?style=social) | https://github.com/sovantica/engrava<br>https://engrava.ai |
| Mimir | 2026-06-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/tcconnally/mimir?style=social) | https://github.com/tcconnally/mimir<br>https://perseus.observer/mimir |
| mem0ry4ai | 2026-06-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/cremenescu/mem0ry4ai?style=social) | https://github.com/cremenescu/mem0ry4ai<br>https://cremenescu.ro/en/mem0ry4ai/ |
| AccInt | 2026-06-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/maxbaluev/accreted-intelligence?style=social) | https://github.com/maxbaluev/accreted-intelligence<br>https://accint.xyz/ |
| Lians | 2026-06-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/Lians-ai/Lians?style=social) | https://github.com/Lians-ai/Lians<br>https://www.lians.ai/ |
| SQLite Graph Memory | 2026-07-03 | ![GitHub Repo stars](https://img.shields.io/github/stars/Palo-Alto-AI-Research-Lab/sqlite-graph-memory?style=social) | https://github.com/Palo-Alto-AI-Research-Lab/sqlite-graph-memory<br>No official website |
| wiki | 2026-07-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/plasma-ai/wiki?style=social) | https://github.com/plasma-ai/wiki<br>https://docs.plasma.ai/wiki |
| Lians | 2026-07-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/Lians-ai/Lians?style=social) | https://github.com/Lians-ai/Lians<br>https://www.lians.ai/ |
| Tura | 2026-07-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/Tura-AI/tura?style=social) | https://github.com/Tura-AI/tura<br>https://turaai.net/ |
| Tree Ring Memory | 2026-07-07 | ![GitHub Repo stars](https://img.shields.io/github/stars/TerminallyLazy/Tree-Ring-Memory?style=social) | https://github.com/TerminallyLazy/Tree-Ring-Memory<br>https://terminallylazy.github.io/Tree-Ring-Memory/ |
| Data Olympus | 2026-07-08 | ![GitHub Repo stars](https://img.shields.io/github/stars/knaisoma/data-olympus?style=social) | https://github.com/knaisoma/data-olympus<br>No official website |
| LWC | 2026-07-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/JanYork/llm-wiki-cli?style=social) | https://github.com/JanYork/llm-wiki-cli<br>https://janyork.github.io/llm-wiki-cli/ |
| ViBo | 2026-08-13 | ![GitHub Repo stars](https://img.shields.io/github/stars/vnbochkarev-netizen/ViBo-memory) |https://github.com/vnbochkarev-netizen/ViBo-memory<br>https://wwwvibo.com|
| memory-shield | 2026-08-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/vnbochkarev-netizen/memory-shield) |https://github.com/vnbochkarev-netizen/memory-shield<br>No official website|
| Open Index | 2026-08-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/DrDroidLab/open-index?style=social) | https://github.com/DrDroidLab/open-index<br>No official website |
| Superself | 2026-07-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/fxylabs/superself?style=social) | https://github.com/fxylabs/superself<br>https://superselfs.com/ |
| Compartment | 2026-07-20 | ![GitHub Repo stars](https://img.shields.io/github/stars/MaxFreedomPollard/Compartment?style=social) | https://github.com/MaxFreedomPollard/Compartment<br>No official website |
| OpenViking | 2026-08-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=social) | https://github.com/volcengine/OpenViking<br>https://openviking.ai/ |
| Engraphy | 2026-08-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/devon-clarkk/engraphy?style=social) | https://github.com/devon-clarkk/engraphy<br>https://engraphy.tech |
| chamnan | 2026-08-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/ArcticFox2029/chamnan?style=social) | https://github.com/ArcticFox2029/chamnan |
| Verified Memory Vault | 2026-08-24 | ![GitHub Repo stars](https://img.shields.io/github/stars/secondbrainstarter/verified-memory-vault?style=social) | https://github.com/secondbrainstarter/verified-memory-vault<br>https://secondbrainstarter.github.io/verified-memory-vault/ |
| kgai | 2026-08-03 | ![GitHub Repo stars](https://img.shields.io/github/stars/kgaidev/kgai?style=social) | https://github.com/kgaidev/kgai<br>https://kgai.dev/?ref=awesome-ai-memory |
| causal-memory | 2026-07-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/JingxuanC/causal-memory?style=social) | https://github.com/JingxuanC/causal-memory<br>No official website |

### 🎥 多媒体资源

<table>
  <thead>
    <tr>
      <th>类型</th>
      <th>网址链接</th>
      <th>视频内容简介</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6"><strong>记忆基本理论</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>基于LangGraph的短期记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=WsGVXiWzTpI</td>
      <td>OpenAI: 智能体记忆设计模式</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=fsENEq4F55Q</td>
      <td>基于LangGraph的长期记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=L-au0tvDJbI</td>
      <td>llm不具备类似人类的工作记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=RkWor1BZOn0</td>
      <td> LLM进行长期记忆和个性化</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=CFih0_6tn2w</td>
      <td>将记忆作为大语言模型的一等任务</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>记忆相关工具</strong></td>
      <td>https://www.bilibili.com/video/BV1hom8YAEhX</td>
      <td>记忆Agent</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1CU421o7DL</td>
      <td>基于Langchain的记忆agent</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1arJazVEaX</td>
      <td>开启记忆MCP</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV11HxXzuExk</td>
      <td>大模型Agent记忆</td>
    </tr>
    <tr>
      <td rowspan="10"><strong>记忆相关论文</strong></td>
      <td>https://www.bilibili.com/video/BV1XT8ez6E46</td>
      <td>AI agent记忆综述</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1f12wBpEXX</td>
      <td>为自进化智能体组织生成潜在记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1deyFBKEFh</td>
      <td>大型语言模型的检索器预训练记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV18FnVzpE6S</td>
      <td>记忆管理经验跟随行为的实证研究</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1mpbrzSEH9</td>
      <td>Agent记忆工作流</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1qEtozyEoh</td>
      <td>大型语言模型智能体记忆机制简介</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1FGrhYhEZK</td>
      <td>记忆层大规模扩展</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1aQ1xBkE45</td>
      <td>LLM agent记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1Yz421f7uH</td>
      <td>评估LLM智能体的非常长期的会话记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV19RWdzxEsR</td>
      <td>轻量级插件式记忆系统</td>
    </tr>
  </tbody>
</table>

### 🧠 Adam 框架

* **描述（Description）：** 基于 OpenClaw 构建的面向本地 AI 助手的五层持久化记忆与一致性架构。该框架旨在解决人工智能系统中的“记忆失效”（AI amnesia）问题，包括跨会话记忆丢失以及单次会话内部一致性逐渐退化的问题。
* **层级结构（Layers）：** 包括 Vault 注入机制、中期记忆检索（mid-session memory search）、神经图结构（包含 7219+ 个神经元）、基于 Gemini 每日核对（nightly reconciliation），以及带有 scratchpad dropout 检测功能的一致性监控模块。
* **验证情况（Validated）：** 已在真实业务环境中运行并验证，共计 353 个会话、6619 轮消息交互，持续生产环境运行 8 个月，由一名非开发人员完成部署与使用。
* **平台（Platform）：** 支持 Windows / macOS / Linux 平台，基于 OpenClaw 架构，采用本地优先（local-first）设计，并具有模型无关性（model-agnostic）。
* **相关链接（Links）：** [GitHub](https://github.com/strangeadvancedmarketing/Adam) | [Live Demo](https://strangeadvancedmarketing.github.io/Adam/) | [Interactive Proof](https://strangeadvancedmarketing.github.io/Adam/showcase/ai-amnesia-solved.html)

## 🤝  如何贡献
提交样式:
```
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```

## 💬 社区和支持

加入我们的社区，提出问题，分享您的项目，并与其他开发人员联系.

- **GitHub Issues**: 在我们的 <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/issues" target="_blank">GitHub Issues</a> 中报告问题或提出功能需求。
- **GitHub Pull Requests**: 通过 <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/pulls" target="_blank">Pull Requests</a> 提交代码改进。
- **GitHub Discussions**: 在我们的 <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/discussions" target="_blank">GitHub Discussions</a> 中提问或分享想法。
- **WeChat**: 扫描下方二维码加入我们的讨论组，获取最新的Memory相关的研究信息，或推广您的相关研究成果。

<!-- <div style="text-align: center;">
  <img src="assets/wechat-qr-code.png" alt="QR Code" width="255">
</div> -->

<center>
  <img src="assets/wechat-qr-code.png" alt="QR Code" width="255">
</center>

## 🌟 仓库关注量

<a href="https://star-history.dera.page/#IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
 </picture>
</a>

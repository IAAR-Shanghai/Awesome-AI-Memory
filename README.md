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

+ 2025-12-24 – 🎉 发布仓库-V(1.0)
+ 2025-12-10 – 🎉 仓库初始化

---

🗺️ 目录表
- [简介](#-简介)
- [仓库目标](#-仓库目标)
- [项目范围](#-项目范围)
- [近期热点研究与新闻](#-近期热点研究与新闻)
- [核心概念](#-核心概念)
- [论文列表](#-论文列表)
  - [综述](#综述)
  - [方法类与框架类论文](#方法类与框架类论文)
  - [数据集和评估基准类论文](#数据集与评估基准类论文)
  - [模型和系统类论文](#模型和系统类论文)
- [仓库资源](#-仓库资源)
  - [测试基准](#测试基准)
  - [开源系统](#开源系统)
  - [多媒体资源](#多媒体资源)
- [如何贡献](#-如何贡献)
- [仓库关注量](#-仓库关注量)

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
        <a href="https://arxiv.org/pdf/2508.10419">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
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
      <td rowspan="2" style="width: 15%;">2025-04-14</td>
      <td style="width: 55%;"><strong>ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
        <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2508.10419">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
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
| **个性化任务评估**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745)  |
|  **综合评价**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **记忆机制评价**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **长期记忆评估**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144), [Mem-Gallery](https://arxiv.org/pdf/2601.03515) |
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
| LangMem     | 2025-01-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) | https://github.com/langchain-ai/langmem<br>https://langchain-ai.github.io/langmem/ |
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
| EverMemOS   | 2025-10-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/EverMind-AI/EverMemOS?style=social) | https://github.com/EverMind-AI/EverMemOS<br>https://evermind.ai/ |
| MemoryBear  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/SuanmoSuanyangTechnology/MemoryBear?style=social) | https://github.com/SuanmoSuanyangTechnology/MemoryBear<br>https://www.memorybear.ai/ |

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
      <td rowspan="5"><strong>记忆基本理论</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>基于LangGraph的短期记忆</td>
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

<a href="https://www.star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
 </picture>
</a>


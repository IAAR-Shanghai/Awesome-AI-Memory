# Awesome-AI-Memory

[![Awesome](https://awesome.re/badge.svg)](https://github.com/zjunlp/ModelEditingPapers) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)


## 👋 Introduction
Large Language Models (LLMs) have rapidly evolved into powerful general-purpose reasoning and generation engines. Nevertheless, despite their continuously advancing capabilities, LLMs remain fundamentally constrained by a critical limitation: the finite length of their context window. This constraint defines the scope of information directly accessible during a single inference process, endowing models with only short-term memory capabilities. Consequently, they struggle to support extended conversations, personalized interactions, continuous learning, and complex multi-stage tasks.

To transcend the inherent limitations of context windows, AI memory and memory systems for LLMs have emerged as a vital and active research and engineering frontier. By introducing external, persistent, and controllable memory structures beyond model parameters, these systems enable large models to store, retrieve, compress, and manage historical information during generation processes. This capability allows models to continuously leverage long-term experiences within limited context windows, achieving cross-session consistency and continuous reasoning abilities.

Awesome-AI-Memory is a comprehensive repository dedicated to AI memory and memory systems for large language models, systematically curating relevant research papers, framework tools, and practical implementations. This repository endeavors to map the rapidly evolving research landscape in LLM memory systems, bridging multiple disciplines including natural language processing, information retrieval, intelligent agent systems, and cognitive science.

---

## 🎯 Goal of Repository
Our mission is to establish a centralized, continuously evolving knowledge base that serves as a valuable reference for researchers and practitioners, ultimately accelerating the development of intelligent systems capable of long-term memory retention, sustained reasoning, and adaptive evolution over time.

---

## 📏 Project Scope
This repository focuses on memory mechanisms and system designs that extend or augment the context window capabilities of large language models, rather than merely addressing model pre-training or general knowledge learning. The content encompasses both theoretical research and engineering practices.

🌀 Included Content (In Scope)
- Memory and memory system designs for large language models
- External explicit memory beyond model parameters
- Short-term memory, long-term memory, episodic memory, and semantic memory
- Retrieval-Augmented Generation (RAG) as a memory access mechanism
- Memory management strategies (writing, updating, forgetting, compression)
- Memory systems in intelligent agents (Agents)
- Shared and collaborative memory in multi-agent systems
- Memory models inspired by cognitive science and biological memory
- Evaluation methods, benchmarks, and datasets related to LLM memory
- Open-source frameworks and tools for memory-enhanced LLMs

🌀 Excluded Content (Out of Scope)
- General model pre-training or scaling research without direct memory relevance
- Purely parameterized knowledge learning without memory interaction
- Traditional databases or information retrieval systems unrelated to LLMs
- Generic memory systems outside the LLM context (unless demonstrating direct transfer value)

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

## 🔔 News

+ 2025-12-10 – 🎉 Initial Repo
+ 2025-07-04 – 🎉 MemOS Paper Released: MemOS: A Memory OS for AI System was published on arXiv.
+ 2025-05-28 – 🎉 Short Paper Uploaded: MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models was published on arXiv.
+ 2024-07-01 – 🎉 Memory3 Paper Released: Memory3: Language Modeling with Explicit Memory introduces the new approach to structured memory in LLMs.

---

🗺️ Table of Contents
- [Introduction](#introduction)
- [Goal of Repository](#goal-of-repository)
- [Project Scope](#project-scope)
- [News](#news)
- [Introduction of Core Concept](#introduction-of-core-concept)
- [Paper List](#paper-list)
  - [Survey](#survey)
  - [Framework & Methods](#framework--methods)
  - [Benchmark & Datasets](#benchmark--datasets)
  - [Memory Evaluation](#memory-evaluation)
  - [System & model](#system--model)
- [Resource](#resource)
  - [Benchmarks and tasks](#benchmarks-and-tasks)
  - [Systems and open sources](#systems-and-open-sources)
  - [Star Trends](#star-trends)

---

## 🧠 Core Concepts

- LLM Memory: A fusion of implicit knowledge encoded within parameters (acquired during training) and explicit storage outside parameters (retrieved at runtime), enabling models to transcend token limitations and possess human-like abilities to "remember the past, understand the present, and predict the future."

- Memory System: The complete technical stack implementing memory functionality for large language models, comprising four core components:
  - Memory Storage Layer: Vector databases (e.g., Chroma, Weaviate), graph databases, or hybrid storage solutions
  - Memory Processing Layer: Embedding models, summarization generators, and memory segmenters
  - Memory Retrieval Layer: Multi-stage retrievers, reranking modules, and context injectors
  - Memory Control Layer: Memory prioritization managers, forgetting controllers, and consistency coordinators

- Memory Operations: Atomic memory operations executed through tool calling in memory systems:
  - Writing: Converting dialogue content into vectors for storage, often combined with summarization to reduce noise
  - Retrieval: Generating queries based on current context to obtain Top-K relevant memories
  - Updating: Finding relevant memories via vector similarity and replacing or enhancing them
  - Deletion: Removing specific memories based on user instructions or automatic policies (e.g., privacy expiration)
  - Compression: Merging multiple related memories into summaries to free storage space

- Memory Management: The methodology for managing memories within memory systems, including:
  - Memory Lifecycle: End-to-end management from creation, active usage, infrequent access, to archiving/deletion
  - Conflict Resolution: Arbitration mechanisms for contradictory information (e.g., timestamp priority, source credibility weighting)
  - Resource Budgeting: Allocating memory quotas to different users/tasks to prevent resource abuse
  - Security Governance: Automatic detection and de-identification of PII (Personally Identifiable Information)

- Memory Classification: A multi-dimensional classification system unique to memory systems:
  - By Access Frequency: Working memory (current tasks), frequent memory (personal preferences), archived memory (historical records)
  - By Structured Degree: Structured memory (database records), semi-structured memory (dialogue summaries), unstructured memory (raw conversations)
  - By Sharing Scope: Personal memory (single user), team memory (collaborative spaces), public memory (shared knowledge bases)
  - By Temporal Validity: Permanent memory (core facts), temporary memory (conversation context), time-sensitive memory (e.g., "user is in a bad mood today")

- Memory Mechanisms: Core technical components enabling memory system functionality:
  - Retrieval-Augmented Generation (RAG): Enhancing generation by retrieving relevant information from knowledge bases
  - Memory Reflection Loop: Models periodically "review" conversation history to generate high-level summaries
  - Memory Routing: Automatically selecting retrieval sources based on query type (personal memory/public knowledge base)

- Explicit Memory: Memory stored as raw text outside the model, implemented through vector databases with hybrid indexing strategies:
  - Dense Vector Indexing: Handling semantic similarity queries
  - Sparse Keyword Indexing: Processing exact match queries
  - Multi-vector Indexing: Segmenting long documents into multiple parts, each independently indexed

- Parametric Memory: Knowledge and capabilities stored within the fixed weights of a language model's architecture, characterized by:
  - Serving as the model's core long-term semantic memory carrier
  - Being activatable without external retrieval or explicit contextual support
  - Providing the foundational capability for zero-shot reasoning, general responses, and language generation

- Long-Term Memory: Key information designed for persistent storage, typically implemented as external knowledge bases with capabilities including:
  - Automatic Summarization: Distilling multi-turn dialogues into structured memory
  - Context Binding: Recording memory context to prevent erroneous generalization
  - Multimodal Storage: Simultaneously preserving text, images, audio, and other multimodal memories

- Short-Term Memory: Active information within the LLM's context window, constrained by attention mechanisms. Key techniques include:
  - KV Cache Management: Reusing key-value caches to reduce redundant computation
  - Context Compression: Using summaries instead of detailed history (e.g., "the previous 5 dialogue rounds discussed project budget")
  - Sliding Window Attention: Focusing only on the most recent N tokens while preserving special markers
  - Memory Summary Injection: Dynamically inserting summaries of long-term memory into short-term context

- Episodic Memory: Memory type recording specific user interaction history, fundamental to personalized AI:
  - User Identity Recognition: Identifying the same user across sessions
  - Interaction Trajectory Recording: Preserving user decision paths and feedback
  - Emotional State Tracking: Recording patterns of user mood changes
  - Preference Evolution Modeling: Capturing long-term changes in user interests

- Memory Forgetting: Deliberately designed forgetting mechanisms in large models, including:
  - Selective Forgetting (Machine Unlearning): Removing the influence of specific information from training data, such as covering specific knowledge with forgetting layers
  - Privacy-Driven Forgetting: Automatically identifying and deleting PII information, or setting automatic expiration
  - Memory Decay: Automatically lowering the priority of infrequently accessed memories based on usage frequency
  - Conflict-Driven Forgetting: Strategically updating or discarding old memories when new evidence conflicts with them

- Memory Retrieval: The complex process of precisely locating relevant information from massive memory repositories:
  - Semantic Pre-filtering: Vector similarity matching to obtain Top-100 candidates
  - Contextual Reranking: Reordering results based on current query context
  - Temporal Filtering: Prioritizing the most recent relevant information

- Memory Compression: A collection of techniques maximizing memory utility under limited resources:
  - Content-level Compression: Extracting core information while discarding redundant details
  - Representation-level Compression: Vector quantization (e.g., PQ coding), dimensionality reduction
  - Organization-level Compression: Clustering similar memories, building hierarchical memory structures
  - Knowledge Distillation: Transferring key patterns from external memory into parametric memory

---

## 📚 Paper List
Papers below are ordered by **publication date**:

<details>
  <summary><strong>Survey</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-18</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/full/10.1145/3749987">
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 深入探讨了机器遗忘（machine unlearning）的概念、背景及其在现代机器学习中的重要性.<br>
          • 机器遗忘旨在使学习算法能够有效删除特定数据的影响，而无需进行全面的模型重新训练.<br>
          • 论文分析了机器遗忘的必要性、挑战、设计要求，以及目前的研究进展，同时强调了该领域在算法有效性、公平性和隐私保护方面的复杂性和多样性。
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
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了基于大语言模型（LLM）的智能体的记忆机制，强调记忆在智能体自我进化及复杂交互中的重要性.<br>
          • 系统性地总结并分类当前的记忆模块设计和评估，同时分析了其在不同应用场景中的作用及局限性.<br>
          • 智能体能够改进决策和任务处理.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文探讨了大语言模型（LLMs）中的机器遗忘（LLM unlearning）技术，旨在在不完全重训练的情况下，有效去除模型中不良数据（如敏感或非法信息）的影响，同时保持整体效用.<br>
          • 定义了LLM遗忘的目标和范式，并建立了全面的分类体系.<br>
          • 回顾了现有方法，评估其优缺点，并探讨未来研究的机遇.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了人工智能（AI）中有关记忆的多维度研究，特别是大语言模型（LLMs）中的记忆操作及其管理.<br>
          • 对记忆表示的多种类型及操作进行分类，包括整合、更新、索引、遗忘、检索和压缩，系统化地分析了记忆在AI中的重要性与实现方式.<br>
          • 对大量文献的分析，识别出长期记忆、参数化记忆、长上下文记忆及多源记忆整合等四个关键研究主题.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 全面探讨了大语言模型（LLMs）中的记忆机制，重点分析了不同类型的记忆及其在模型中的作用.<br>
          • LLMs在信息检索和交互总结方面表现出色，但其长期记忆不够稳定.<br>
          • 将记忆整合进人工智能系统对于提供丰富的上下文响应，减少幻觉现象，提高数据处理效率以及推动AI系统自我进化至关重要.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-23</td>
      <td style="width: 55%;"><strong>From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs </strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.15965">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨人类记忆与基于大语言模型（LLMs）的人工智能（AI）系统的记忆机制之间的关系.<br>
          • 主要贡献包括对LLM驱动AI系统的记忆进行系统定义，与人类记忆建立联系.<br>
          • 论文提出一种基于对象、形式和时间的三维记忆分类方法，并总结当前个人记忆和系统记忆研究的关键问题.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 本文系统性探讨了人类长期记忆机制与AI长期记忆之间的相互关系，并提出了一种自适应长期记忆的认知架构（SALM）.<br>
          • 文章介绍了人类记忆的结构，包括感官记忆、工作记忆及长期记忆的不同类型（情节记忆、语义记忆和程序记忆）.<br>
          • 文章分析了AI长期记忆的分类（参数化记忆与非参数化记忆）及其存储与检索机制.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-02</td>
      <td style="width: 55%;"><strong>Digital Forgetting in Large Language Models: A Survey of Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.02062">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文探讨了大语言模型（LLMs）中的数字遗忘及其去学习方法，聚焦于解决隐私、版权和社会伦理等问题.<br>
          • 文中解析了不同类型的模型架构和训练过程，以及数字遗忘的实现方法，如数据重训、机器遗忘、提示工程等.<br>
          • 通过“遗忘保证”的概念，强调了精确与近似遗忘的有效机制.
        </td>
    </tr>  
  </table>

</details>


<details>
  <summary><strong>Framework & Methods</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
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
          • 论文探讨了大语言模型（LLM）代理的记忆管理及其对长期性能的影响.<br>
          • 论文发现了错误传播和不对齐经验重放的问题，强调了高质量记忆的重要性.<br>
          • 比较了多种记忆添加和删除策略，发现选择性添加策略在长期学习中表现优越，而历史删除策略在减少低质量记忆记录方面效果显著.
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
          • “OpenUnlearning”框架，旨在推动大语言模型（LLM）遗忘（unlearning）研究.<br>
          • OpenUnlearning整合了多种去学习算法和评估方法，简化了遗忘研究的流程.<br>
          • 通过具有针对性的评估，OpenUnlearning确保去学习评估标准的可信度和鲁棒性.
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
          • SynapticRAG是一个针对大型语言模型（LLMs）的新型记忆检索框架，旨在提升其在跨会话对话中的记忆检索能力.<br>
          • SynapticRAG通过结合时间关联触发和生物启发的突触传播机制，显著提高了对话历史的相关性识别.<br>
          • 实验结果表明，该框架在多个性能指标上提高了最多14.66%，并在动态管理记忆方面展现了优势.
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
          • M+是一种记忆增强模型，旨在提高大型语言模型（LLMs）在长期信息保留方面的能力.<br>
          • M+基于MemoryLLM，通过整合长期记忆机制和共同训练的检索器，显著增强了模型处理超过20,000 tokens知识的能力，同时保持相似的GPU内存开销.<br>
          • M+在多个基准测试中表现优异，超越了MemoryLLM及其他强基线模型，展现出高效的信息压缩和端到端训练能力，接近人类记忆的机制.
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
          • 论文探讨了在大语言模型（LLMs）中的机器遗忘及其评估的重要性，尤其关注如何消除不必要的数据记忆.<br>
          • 引入“控制反学习”（UWC）方法，以校准模型性能，增强不同遗忘方法的评估能力.<br>
          • 研究强调选择合适的评估指标的重要性，推荐使用“提取强度”（ES）作为主要评估工具，从而保证评估的准确性和鲁棒性.
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
          • 提出方法“Alternate Preference Optimization”（AltPO），旨在有效解决大语言模型（LLMs）在“机器遗忘”过程中的挑战.<br>
          • AltPO方法通过结合遗忘集的负反馈和来自同领域的正反馈，生成多个可替代答案，从而提高遗忘能力，保持模型的整体性能.<br>
          • 实验结果显示，AltPO在遗忘质量和模型实用性方面的表现超越了现有方法.
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
          • 论文探讨了大语言模型（LLM）中记忆模块的结构与检索方法如何影响其性能，重点分析了不同的记忆结构及其在信息提取和生成中的应用.<br>
          • 研究发现，混合记忆结构在复杂任务中表现优越，尤其在噪声环境下更具韧性.<br>
          • 通过对超参数的敏感性分析，研究识别出在不同任务背景下适合的记忆检索策略.
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
          • 本研究介绍了序列顺序回忆任务(SORT),旨在评估大语言模型（LLMs）的情节记忆能力.<br>
          • 该任务强调了情节记忆的重要性，即将记忆与相关上下文（如时间和地点）相结合，尤其是在日常认知任务中的应用中.<br>
          • 初步结果表明，LLMs在提供上下文的情况下能够表现出较好的记忆能力，但在仅依赖训练数据时，性能显著降低.
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
          • 本文介绍了选择性知识否定遗忘框架（SKU），旨在提升大语言模型（LLMs）的安全性.<br>
          • SKU框架分为两个主要阶段：第一阶段为有害知识获取；第二阶段为知识否定，重点去除不良知识而不损害正常提示下模型的效用.<br>
          • SKU成功地在减少有害输出的同时，保持了模型的响应质量，并在多个LLM架构（如OPT、LLAMA2）上展示了良好的去学习与效用性能平衡.
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
          • RULER是用于全面评估长上下文语言模型（LMs）在多种任务中的性能.<br>
          • RULER扩展了传统的（NIAH）测试，加入了多跳追踪、聚合等任务，以便更好地衡量模型在长上下文下的理解能力.<br>
          • RULER在多跳推理和信息检索任务上表现出色.
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
          • ReadAgent是一个旨在提升大型语言模型（LLMs）在处理长文本时性能的阅读理解系统.<br>
          • 通过情节分页、记忆摘要和互动查找三种步骤，ReadAgent显著增加了有效上下文长度，最多可达20倍.<br>
          • ReadAgent在长文档阅读理解任务（如QuALITY、NarrativeQA和QMSum）中表现优于传统方法.
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
          • 介绍了一种推荐数据遗忘方法E2URec，专为大语言模型（LLMs）推荐系统（LLMRec）设计.<br>
          • E2URec通过仅更新低秩适应（LoRA）参数，显著提高了遗忘效率，并保持推荐性能.<br>
          • 实验结果表明，E2URec在实际数据集上超越了现有基线方法.
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
          • MEMORYLLM是一种自我更新的大型语言模型，旨在有效整合新知识并保持长期信息保留能力.<br>
          • 通过在transform的潜在空间中嵌入固定大小的记忆池，MEMORYLLM实现了模型自我更新与知识保留的有机结合.<br>
          • 模型的设计特点包括：包含压缩知识的记忆令牌、智能的自我更新机制以及针对知识整合、保留能力和鲁棒性的详细评估.
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
          • 探讨了大语言模型（LLMs）在信息回忆能力方面的表现，尤其强调其对提示内容和格式的依赖性.<br>
          • 通过采用(NIAH)测试方法，发现模型的召回能力受训练数据偏差、提示内容和格式影响显著.<br>
          • 通过优化模型架构、调整训练策略及实施微调，均能有效提升召回性能.
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
          • “MemoryBank”，一种为大语言模型（LLMs）设计的长时记忆机制，旨在解决LLMs在持续互动中记忆不足的问题.<br>
          • MemoryBank通过允许模型有效召回、更新和适应用户记忆，以提升上下文理解和用户体验.<br>
          • 通过实验和分析，MemoryBank在提高情感支持和个性化互动方面显示出其有效性.
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
          • 探讨了在大语言模型（LLMs）中实施“遗忘”或“反学习”的方法，以去除不希望出现的（误）行为.<br>
          • 通过应用梯度上升（GA）策略和引入随机输出损失，研究展示了反学习能停止模型生成有害答案的能力.<br>
          • 实验结果表明，GA和GA+Mismatch方法在降低内容泄漏率方面表现优异.
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
          • 提出一种压缩上下文记忆方法，用于提高在线语言模型在处理扩展上下文时的内存效率和计算性能.<br>
          • 通过采用条件LoRA集成和并行计算，显著减少内存需求，实现了对无限上下文长度的处理能力，超越了传统滑动窗口策略.<br>
          • 实验结果表明，在多任务学习和对话生成等应用场景中，该方法的内存需求降低了五倍，同时有效保持了生成性能和准确性.
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
          • “遗忘”框架（Efficient Unlearning, EUL），旨在解决大语言模型（LLMs）在处理用户隐私数据时的挑战.<br>
          • 随着LLMs的广泛应用，模型在预训练过程中可能会记住敏感信息，从而引发隐私问题.<br>
          • EUL允许在不完全重训模型的情况下，有效地从LLMs中删除特定的敏感数据，同时保持模型的预测性能.
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
          • 一种新的记忆机制“Think-in-Memory”（TiM），旨在提升大语言模型（LLMs）在长期人机交互中的表现.<br>
          • TiM引入了基于局部敏感哈希的高效检索机制，以支持长期交互中的记忆存储和管理.<br>
          • 实验结果显示，TiM在多轮对话中显著改善了LLMs的响应准确性和连贯性.
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
          • 介绍了一种新的框架LONGMEM，旨在增强大语言模型（LLMs）在长文本处理中的能力.<br>
          • LONGMEM通过设计一个解耦的网络架构，结合冻结的LLM记忆编码器与自适应的残差侧网络，有效地缓存和更新长时间的上下文信息.<br>
          • 通过引入特殊的记忆增强层、基于令牌的记忆检索模块和联合注意力机制，LONGMEM提高了模型的记忆检索能力和上下文利用效果，验证了其在多种任务中的有效性.
        </td>
    </tr>

  </table>

</details>

<details>
  <summary><strong>Datasets & Benchmark</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
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
          • 提出了IMPLEXCONV数据集和TACITREE框架，用于研究个性化对话中的隐性推理.<br>
          • IMPLEXCONV包含2500个示例，专注于隐性推理场景，捕捉对话中微妙的句法和语义关系.<br>
          • TACITREE通过层次化组织对话历史，提高了大型语言模型（LLM）在长对话中的隐性上下文推理能力.
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
          • 介绍PERSONAMEM基准测试，旨在评估大语言模型（LLMs）在动态用户画像和个性化响应中的表现.<br>
          • 尽管现有模型在回忆用户偏好方面取得了一定成功，但在处理新场景时仍存在显著性能不足.<br>
          • 文本详细描述了基准的结构、生成用户对话的过程、评估模型性能的方法以及一些相关研究，强调了个性化对话生成在提升用户体验中的重要性.
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
          • MemoryAgentBench基准用于评估具有记忆机制的语言模型（Memory Agents）的四大核心能力：准确检索、测试时学习、长范围理解和冲突解决.<br>
          • 通过整合现有数据集和新构建的数据，MemoryAgentBench旨在系统性地评估这些能力.<br>
          • MemoryAgentBench旨在系统性地评估这些能力，揭示了现有方法在记忆更新和长对话处理中存在的不足之处.
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
          • "PersonaBench"是一个用于评估AI模型在理解个人信息方面的基准.<br>
          • 论文指出个性化在AI助手中的重要性，并强调了缺乏公开数据集以评估对此类信息的理解能力这一挑战.<br>
          • 评估主要集中在检索增强生成（RAG）模型上，结果显示当前模型对于处理个人问题的能力尚显不足.
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
          • MemBench旨在全面评估基于大语言模型（LLM）代理的记忆能力.<br>
          • 通过建立涵盖事实记忆和反思记忆的数据集，研究解决了现有评估方法的局限性.<br>
          • 文本详细描述了记忆机制的构建，包括用户关系图和多层记忆的设计，强调评估准确性、效率、容量等指标的重要性.
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
          • 本文研究了大语言模型（LLMs）在长期任务中的记忆能力，特别是在对话系统中的应用表现.<br>
          • 通过构建“长期时间顺序对话”（LOCCO）数据集，量化评估了LLMs的长期记忆能力.<br>
          • 实验结果表明，LLMs能够在一定程度上保留历史对话信息，但随着时间推移，其记忆能力逐渐衰减.
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
          • 介绍了一种用户模拟框架“隐式用户档案用户模拟器”（USP），旨在通过推断用户的隐式特征来增强对话系统与人类用户的交互.<br>
          • USP通过提取用户对话中的隐式特征，并结合条件监督微调和循环一致性的强化学习，优化了对话的真实性和一致性.<br>
          • 实验结果表明，USP在多个指标上，尤其是与其他对话生成模型（如GPT-4o和PlatoLM）的比较中，显示出显著优势.
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
          • 提出基准PersonaFeedback，用于评估大语言模型（LLMs）在个性化响应方面的能力.<br>
          • 研究表明，尽管LLMs在生成个性化内容方面有进展，但在复杂情境中依然存在局限性.<br>
          • 通过使用动态用户特征推断、个性化档案和奖励模型，研究者们努力提升个性化问答的效果.
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
          • Minerva是一个可编程记忆测试基准，旨在评估大型语言模型（LLM）在不同记忆任务中的能力.<br>
          • 通过定量评估模型在记忆使用方面的表现，特别是信息检索、推理和状态跟踪等任务.<br>
          • 实验结果显示，尽管部分模型在简单任务上表现良好，但在复杂任务中存在明显差距.
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
        • 论文介绍了LONGMEMEVAL，一个用于评估聊天助手长期记忆能力的综合基准.<br>
        • 该基准评估五种核心记忆能力，可反映现有系统存在的挑战.<br>
        • LONGMEMEVAL采用一种统一的三阶段框架（索引、检索、阅读），并提出多项设计优化策略以提高记忆召回率和问答准确性.
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
        • 探讨了在大语言模型（LLMs）中的机器遗忘及其评估的重要性，尤其关注如何消除不必要的数据记忆.<br>
        • 研究主要面对两个挑战：一是评估指标的稳健性，二是消除目标知识与保留其他知识之间的权衡.<br>
        • 研究推荐使用“提取强度”（ES）作为主要评估工具，从而保证评估的准确性和鲁棒性.
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
        • PREFEVAL基准旨在评估大语言模型（LLMs）在长对话中推断、记忆和遵循用户偏好的能力.<br>
        • 该基准包含3000个用户偏好和查询对，覆盖20个主题，揭示了当前LLMs在遵循用户偏好方面显著的挑战.<br>
        • 研究表明，显式偏好相较于隐式偏好更易于模型推断，而不同任务类型和偏好表达方式对模型效果有显著影响.
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
        • LongGenBench基准测试旨在评估大语言模型（LLMs）在生成高质量长文本中的能力，尤其是在遵循复杂指令方面.<br>
        • 与现有基准不同，LongGenBench专注于长文本生成场景，涵盖日记写作、菜单设计等多个任务.<br>
        • 尽管LLMs在其他测试中表现良好，但在LongGenBench的测试中，它们面临显著的挑战.
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
        • MT-Eval 基准旨在评估大语言模型（LLMs）在多轮对话中的表现.<br>
        • 当前的评估主要集中在单轮对话上，MT-Eval 通过构建1,170个多轮查询填补了这一空白.<br>
        • 这一基准将交互模式分为回忆、扩展、精炼和跟进，展示了大多数模型在多轮设置中的表现普遍低于单轮设置.
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
        • LongGenBench是新提出的长上下文生成基准，旨在评估大型语言模型（LLMs）在处理长文本生成任务中的表现.<br>
        • 这一基准补充了现有主要关注检索技能的评估方法，重点测试模型对多问题的连贯性和逻辑一致性.<br>
        • 研究表明，不同模型在长文本生成过程中表现出显著的能力差异.
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
        • 一个旨在提升对话系统中长期记忆整合的问题回答数据集PerLTQA.<br>
        • PerLTQA结合了语义记忆和情节记忆，包含8593个问题，涉及30个角色，目的是改善记忆分类、检索和合成.<br>
        • 实验表明，基于BERT的模型在记忆分类任务中优于其他大型语言模型.
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
        • 评估了大型语言模型（LLMs）在长时间对话中的记忆能力，尤其是在多模态对话场景中.<br>
        • 通过开发名为LOCOMO的数据集，研究者建立了一个综合评估基准，涵盖了问答、事件总结和多模态对话生成等任务.<br>
        • 实验结果表明，尽管一些LLMs表现出色，但在记忆和推理能力上仍显著落后于人类，同时提出了评估框架和未来改进的方向.
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
        • 探讨了大语言模型（LLMs）在个性化响应生成中的重要性，并引入了LaMP基准，这是一个专为训练和评估个性化文本生成与分类任务而设计的新框架.<br>
        • LaMP包含七个个性化子任务，强调了通过用户特定输入（如历史数据）和检索增强策略提升语言模型的效果.<br>
        • 实验结果表明，个性化方法显著提高了模型性能，尤其在微调和合适的检索策略使用上表现最佳.
      </td>
    </tr>
  </table>

</details>

<details>
  <summary><strong>Memory Evaluation</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
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
        • EM-LLM（事件记忆大语言模型）是一种新型大型语言模型，旨在解决当前模型在处理长上下文时的局限性.<br>
        • EM-LLM实现了无需微调的几乎无限上下文处理能力，表现出在多个基准测试中相较于现有模型的显著提升.<br>
        • 该模型结合了基于惊讶的事件分割、图论边界细化以及双阶段的记忆检索机制，显著改善了信息检索和问答任务的性能.
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
        • 低成本长文本理解基准MiniLongBench旨在提升大型语言模型（LLMs）在长文本理解（LCU）能力评估的效率和降低成本.<br>
        • MiniLongBench通过数据压缩技术显著减少了测试样本数量，保持了评估一致性，并与现有的LongBench基准的结果高度相关.<br>
        • MiniLongBench在多个任务类别下的评估显示出良好的效果，尽管仍需在总结和合成任务方面进行改进.
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
        • “Agentic Long-Context Understanding” (AgenticLU) 框架旨在提升大语言模型（LLMs）在长文本理解和推理方面的能力.<br>
        • AgenticLU通过引入“Chain-of-Clarifications” (CoC) 机制，优化了模型的自我澄清过程，并采用树状搜索路径生成澄清问题，从而显著提高了多步推理的准确性和效果.<br>
        • 评估结果显示，该模型在长文本问答中超越现有提示技术，同时计算开销得到了有效控制.
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
        • SCBENCH（Shared Context BENCH）是一个专为评估长上下文大语言模型（LLMs）设计的基准测试.<br>
        • SCBENCH重点关注键值（KV）缓存的生命周期，包括生成、压缩、检索和加载四个阶段，旨在填补现有基准测试在多轮交互中对KV缓存评估的空白.<br>
        • 实验结果表明，不同方法在处理不同任务时存在显著差异，同时动态稀疏注意力和缓存优化策略在复杂场景下展现出更好的表现.
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
        • 探讨了情景记忆在大语言模型（LLMs）中的重要性，提出了构建新基准测试以评估模型的推理能力.<br>
        • 作者建立了一个综合框架，设计了新的任务与评估方式，强调需要新的训练策略来有效整合情节记忆.<br>
        • Some attention heads track specific syntactic dependencies better than baselines, but no head performs holistic parsing significantly better.
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
        • LongBench v2是一个用于评估大型语言模型（LLMs）在长上下文理解及推理能力的多任务基准.<br>
        • LongBench v2由503个多项选择题构成，涵盖多种任务类型，专注于长文本的理解与回答.<br>
        • 研究发现最优模型在处理长上下文时表现优于人类专家，提示推理的增强与时间计算规模的关键性.
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
        • MADial-Bench是一个用于评估记忆增强对话生成的基准，主要针对当前对话系统在长期记忆方面的不足.<br>
        • MADial-Bench结合认知科学概念，评估记忆检索与识别，并引入多元评分标准.<br>
        • 研究表明，尽管大型语言模型（LLM）在情感支持上表现良好，记忆识别和注入能力仍需提升.
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
        • L-CiteEval是一个针对长上下文模型（LCMs）的多任务评估基准，旨在衡量这些模型在理解和引用方面的能力.<br>
        • 该基准涵盖11个任务，支持8K至48K的上下文长度，并提供了全面的评估框架.<br>
        • 研究表明，闭源模型在引用质量和生成准确率上优于开源模型，而检索增强生成（RAG）技术能有效提升模型的引用质量.
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
        • 探讨了大语言模型（LLMs）在长文本处理方面的能力及其局限性，介绍了GLE基准的创建，以评估LLMs在长文本上下文理解中的表现.<br>
        • 论文描述了长依赖问答任务的构建过程和评估标准，并比较了不同模型的表现.<br>
        • Lower layers capture syntax, while higher layers encode more semantic information.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-06-19</td>
      <td style="width: 55%;"><strong>LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding</strong></td>
      <td style="width: 15%;"><td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Bilingual%20Evaluation-darkorchid" alt="Bilingual Evaluation">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2308.14508">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongBench是一个双语多任务基准，旨在评估大型语言模型（LLMs）在长上下文理解上的能力.<br>
        • 该基准包含21个数据集，涵盖单文档问答、多文档问答、摘要、少样本学习、合成任务和代码补全等六个任务类别，平均文本长度达到6,711个单词和13,386个字符.<br>
        • 实验结果表明，尽管商业模型（如GPT-3.5-Turbo-16k）在长上下文任务上表现优于开放源代码模型.
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
        • HOMER（Hierarchical cOntext MERging）算法旨在解决大型语言模型（LLMs）在处理长上下文时的局限性.<br>
        • 通过将长输入分割为小块并逐层合并，HOMER在处理长文本时提升了模型的记忆效率与推理能力.<br>
        • 在实验中，HOMER在32K和64K上下文输入中展现了卓越的性能，维持了较低的困惑度和内存需求.
      </td>
    </tr>

  </table>

</details>

<details>
  <summary><strong>Systems & Models</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-04</td>
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
        • MemoryOS旨在为AI智能体实现全面、高效的记忆管理.<br>
        • MemoryOS从计算机操作系统的内存管理原理中汲取灵感，同时借鉴人脑记忆存储的分层机制，构建了独特的段页式分层存储架构，并包含四大核心功能模块：记忆存储、记忆更新、记忆检索、响应生成.<br>
        • 实验结果表明，MemoryOS 在主流基准测试中显著提升了AI在长对话中的上下文连贯性和个性化记忆保留能力，例如在LoCoMo基准上，模型的F1和BLEU-1分数平均提升了49.11%和46.18%.
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
        • A-Mem通过引入Zettelkasten式的动态记忆组织机制，为LLM代理提供了真正意义上的“长期记忆”.<br>
        • A-Mem不仅能存储信息，还能自我链接、自我进化，从而在复杂推理任务中取得显著优势.<br>
        • 实验证明，其在性能、效率和可扩展性方面均优于现有方法，为构建更智能、更自主的LLM代理奠定了重要基础.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-04</td>
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
        • MemOS（Memory Operating System）是一个为AI系统设计的记忆操作系统，将记忆视为可管理的系统资源，统一了明文、基于激活的和参数级记忆的表示、调度和演化，实现成本高效的存储和检索.<br>
        • MemOS采用三层架构，包括接口层、操作层和基础设施层。接口层负责与用户或上游系统交互，提供标准化的记忆API；操作层负责组织和调度记忆资源；基础设施层处理记忆数据的存储、安全、迁移和流动.<br>
        • Memos为模型实现跨任务适应、跨形态演化与跨平台迁移提供操作系统级支持。MemOS的提出，标志着大模型从”仅感知与生成“迈向”可记忆与进化“的关键跃迁.
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
        • Mem0是一种记忆架构，它能够动态地提取和整合对话中的关键信息，让 AI 系统能记住重要内容并跨会话持续对话.<br>
        • 作者还提出Mem0g，它在 Mem0 的基础上加入了图结构记忆(就是知识图谱)，使得 AI 在处理复杂关系时更得心应手.<br>
        • NLI tasks increase constituency grammar inducing ability, while SMS tasks decrease it in upper layers.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-09-21</td>
      <td style="width: 55%;"><strong>Memory3: Language modeling with explict memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Base%20Model-darkred" alt="Base Model">
      <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
      <img src="https://img.shields.io/badge/Memory%20Circuit-slateblue" alt="Memory Circuit">
      <img src="https://img.shields.io/badge/Long--Context%20Models-royalblue" alt="Long-Context Models">
      </td>
      <td style="width: 15%;"><a href="https://doi.org/10.4208/jml.240708">
      <img src="https://img.shields.io/badge/Journal%20of%20ML-Paper-black?labelColor=blueviolet" alt="Journal of ML Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 一种新型大型语言模型Memory3，它通过引入显式记忆来降低训练和推理成本.<br>
        • 研究提出了记忆回路理论，描述了记忆的外部化过程，明确了知识的定义，强调了模型在处理长上下文时的优势.<br>
        • Memory3有效管理知识写入和读取成本，并采用压缩技术使得显式记忆的存储需求显著降低.
      </td>
    </tr>

  </table>

</details>

## 🧰 Resources

### 📊 Benchmarks and Tasks

|     Edit Type      | Benchmarks \& Datasets                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **个性化任务评估**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf)  |
|  **综合性评估**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257) |
|  **记忆机制评估**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358)|
|  **长期记忆评估**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240)|
|  **长对话推断**   | [PREFEVAL](https://arxiv.org/pdf/2502.09597),  [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf)|
|  **长上下文理解**   | [LongBench V2](https://arxiv.org/pdf/2412.15204), [LongBench](https://arxiv.org/abs/2308.14508) |
|  **长上下文评估** |[SCBENCH](https://arxiv.org/abs/2412.10319), [L-CiteEval](https://arxiv.org/pdf/2410.02115), [GLE](https://aclanthology.org/2024.acl-long.859/), [HOMER](https://arxiv.org/pdf/2404.10308) |
|  **长文本生成**   | [LongGenBench](https://arxiv.org/pdf/2409.02076) |
|  **情节记忆评估**   | [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf)|
|  **多模态记忆评估**   | [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf) |


### 💻 Systems and Open Sources

| System    | Open Sources  | Official Website                 |
|-----------|---------------------------------------------|----------------------------------|
| MemOS     | https://github.com/MemTensor/MemOS          | https://memos.openmem.net/       |
| MemoryOS  | https://github.com/BAI-LAB/MemoryOS         | https://baijia.online/memoryos/  |
| mem0      | https://github.com/mem0ai/mem0              | https://mem0.ai/                 |
| A-mem     | https://github.com/agiresearch/A-mem        | No                               |
| zep       | https://github.com/getzep/zep               | https://www.getzep.com/          |
| Letta     | https://github.com/letta-ai/letta           | No                               |
| memobase  | https://github.com/memodb-io/memobase       | https://www.memobase.io/         |
| Memary    | https://github.com/kingjulio8238/Memary     | No                               |
| memoryOS  | No    | https://memoryos.com/               |


### 🎥 Multi-media resource

| Paper / System | Website Link |
|---------------|--------------|
| **MemOS** | https://www.youtube.com/watch?v=R3v0fnqC5H8<br>https://www.bilibili.com/video/BV1PBuyzBENt |
| **mem0** | https://www.youtube.com/watch?v=jbc-N4_D-k0 |
| **A-mem** | https://www.youtube.com/watch?v=49ERSQeHC-Y<br>https://www.youtube.com/watch?v=ZYz_UpjEut8 |
| **zep** | https://www.youtube.com/watch?v=kNsX2qu8jHY |
| **Letta** | https://www.youtube.com/watch?v=MK3H_Y-l4QU |
| **memobase** | https://www.youtube.com/watch?v=HNGhjojsCpQ |



## 🤝  Make a Contribution
Issue Template: 
```
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result: 
```

## 🌟 Star Trends

<a href="https://star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date" />
  </picture>
</a>


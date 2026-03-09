# Awesome-AI-Memory

<p align="center">
    【English | <a href="README_cn.md">中文</a></a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)
[![Papers](https://img.shields.io/badge/Papers-270-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-85-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)


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

## 🔔 Recent hot research and news

+ 2026-03-02 - 🎉 Add a new code agent to this repo
+ 2026-02-27 - 🎉 Updated 20 papers, including 1 on survey, 2 on systems and models, 2 on benchmarks, and 15 on methods
+ 2026-02-26 - 🎉 Updated 14 papers, including 14 on methods
+ 2026-02-14 - 🎉 Updated 15 papers, including 1 on survey, 12 on methods, 1 on benchmarks, and 1 on systems and models
+ 2026-02-09 - 🎉 Updated 15 papers
+ 2026-02-01 - 🎉 Updated 16 papers, including 9 on methods, 4 on benchmarks, and 3 on systems and models
+ 2025-12-24 – 🎉 Release Repository V(1.0)
+ 2025-12-10 – 🎉 Initial Repo

---

🗺️ Table of Contents
- [Introduction](#-introduction)
- [Goal of Repository](#-goal-of-repository)
- [Project Scope](#-project-scope)
- [Recent hot research and news](#-Recent-hot-research-and-news)
- [Core Concepts](#-core-concepts)
- [Paper List](#-paper-list)
  - [Survey](#Survey)
  - [Framework & Methods](#Framework-Methods)
  - [Benchmark & Datasets](#Benchmark-Datasets)
  - [System & model](#System-model)
- [Resource](#-resource)
  - [Benchmarks and tasks](#Benchmarks-and-tasks)
  - [Systems and open sources](#Systems-and-open-sources)
  - [Multi-media resource](#Multi-media-resource)
- [Make a Contribution](#-Make-a-Contribution)
- [Star Trends](#-star-trends)

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
            • Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
            • Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
            • Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
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
            • Traditional foundation models rely on weight updates for continual learning, which can easily lead to catastrophic forgetting and makes large-scale experience accumulation difficult.<br>
            • Proposes a roadmap for a modular memory architecture that integrates in-context learning with learning encoded in model weights.<br>
            • This architecture leverages in-context learning for rapid adaptation and weight updates for capability consolidation, offering theoretical guidance for building truly lifelong learning agents.
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
            • Investigates whether large language models possess human-like, efficient strategic access mechanisms when processing vast amounts of semantic memory.<br>
            • Uses mechanistic interpretability techniques to analyze semantic fluency tasks, rigorously examining convergent and divergent memory search patterns within the model.<br>
            • Confirms the presence of human-like strategic memory search behavior across different layers of LLMs, laying an interpretability foundation for research on cognitive alignment and enhanced human-AI collaboration.
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
            • This paper explores the foundations, evaluation, and future directions of personalized LLM-driven agents, providing a capability-oriented systematic review of their underlying principles, assessment methodologies, and prospective developments.<br>
            • It constructs a taxonomy centered on four interdependent core components: user profile modeling, memory, planning, and action execution.<br>
            • The paper offers a comprehensive analysis of how user signals are represented, propagated, and utilized, and discusses application scenarios and design trade-offs ranging from general-purpose assistance to specialized domains.
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
          • This paper proposes a unified taxonomy for foundation agent memory across three dimensions: memory substrate, cognitive mechanism, and memory subject.<br>
          • It analyzes memory operation mechanisms in single-agent and multi-agent systems while categorizing memory learning policies into prompting, fine-tuning, and reinforcement learning paradigms.<br>
          • It provides a comprehensive review of evaluation metrics and benchmarks across various applications, outlining critical future directions such as memory efficiency, life-long personalization, and multimodal integration.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Provides a comprehensive and up-to-date landscape of agent memory, explicitly distinguishing it from related concepts like LLM memory, RAG, and context engineering.<br>
          • Introduces a unified taxonomy examining memory through three lenses: <strong>Forms</strong> (token-level, parametric, latent), <strong>Functions</strong> (factual, experiential, working), and <strong>Dynamics</strong> (formation, evolution, retrieval).<br>
          • Discusses emerging research frontiers such as automation-oriented memory design, reinforcement learning integration, and trustworthiness, while compiling representative benchmarks and frameworks.
        </td>
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
          • Provides an in-depth exploration of the concept and background of machine unlearning, highlighting its importance in modern machine learning.<br>
          • Machine unlearning aims to enable learning algorithms to effectively remove the influence of specific data without requiring full model retraining.<br>
          • The paper analyzes the necessity, challenges, and design requirements of machine unlearning, reviews current research progress, and emphasizes the field’s complexity and diversity in terms of algorithmic effectiveness, fairness, and privacy protection.
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
          • Explores the memory mechanisms of LLM-based agents, emphasizing the crucial role of memory in agent self-evolution and complex interactions.<br>
          • Systematically summarizes and categorizes existing memory module designs and evaluation methods, while analyzing their roles and limitations across different application scenarios.<br>
          • Such agents are able to improve decision-making and task execution.
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
          • The paper investigates machine unlearning in large language models (LLMs), aiming to effectively remove the influence of undesirable data (e.g., sensitive or illegal information) without full retraining, while preserving overall model utility.<br>
          • It defines the objectives and paradigms of LLM unlearning and establishes a comprehensive taxonomy.<br>
          • The paper reviews existing approaches, evaluates their strengths and limitations, and discusses opportunities for future research.
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
          • Explores multidimensional research on memory in artificial intelligence (AI), with a particular focus on memory operations and management in large language models (LLMs).<br>
          • Categorizes various types of memory representations and operations—including integration, updating, indexing, forgetting, retrieval, and compression—and provides a systematic analysis of the importance of memory in AI and how it is implemented.<br>
          • Through an extensive review of the literature, the paper identifies four key research themes: long-term memory, parametric memory, long-context memory, and multi-source memory integration.
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
          • Provides a comprehensive examination of memory mechanisms in large language models (LLMs), with a particular focus on different types of memory and their roles within the models.<br>
          • While LLMs excel at information retrieval and interaction summarization, their long-term memory remains unstable.<br>
          • Integrating memory into AI systems is crucial for delivering context-rich responses, reducing hallucinations, improving data processing efficiency, and enabling the self-evolution of AI systems.
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
          • Explores the relationship between human memory and the memory mechanisms of LLM-based artificial intelligence (AI) systems.<br>
          • The main contributions include a systematic definition of memory in LLM-driven AI systems and its conceptual linkage to human memory.<br>
          • The paper proposes a three-dimensional memory taxonomy based on object, form, and time, and summarizes key open issues in current research on personal memory and system memory.
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
          • The paper explores digital forgetting in large language models (LLMs) and corresponding unlearning methods, with a focus on addressing issues related to privacy, copyright, and social ethics.<br>
          • It analyzes different types of model architectures and training processes, as well as practical approaches to digital forgetting, including data retraining, machine unlearning, and prompt engineering.<br>
          • By introducing the concept of “forgetting guarantees,” the paper emphasizes effective mechanisms for both exact and approximate forgetting.
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
          • This paper systematically examines the interplay between human long-term memory mechanisms and AI long-term memory, and proposes an adaptive long-term memory cognitive architecture (SALM).<br>
          • It introduces the structure of human memory, including sensory memory, working memory, and different types of long-term memory (episodic, semantic, and procedural memory).<br>
          • The paper analyzes the classification of AI long-term memory—parametric and non-parametric memory—as well as their storage and retrieval mechanisms.
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
              • The absence of memory admission control allows long-term memory stores to be rapidly polluted by low-quality, redundant, or ineffective noise features, ultimately undermining multi-turn reasoning.<br>
              • Introduces Adaptive Memory Admission Control (A-MAC), a structured admission mechanism that uses lightweight estimation of five interpretable factors—such as future utility, confidence, and novelty—to rigorously intercept write operations before they occur.<br>
              • Establishes admission control as a core engineering principle in memory system design, cleansing the memory store at the source and delivering simultaneous latency and performance gains on the LoCoMo benchmark.
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
              • When executing long-horizon tasks, repeatedly invoking the primary model for complex memory retrieval is prohibitively expensive, making it difficult to balance computational efficiency and accuracy.<br>
              • Proposes the MemSifter framework, which leverages an outcome-driven reinforcement learning paradigm to offload retrieval-intensive computation directly to a lightweight proxy model.<br>
              • Achieves low-cost decoupling of the retrieval architecture, attaining state-of-the-art retrieval hit rates with minimal inference overhead, and offering a highly scalable industrial solution for long-term memory.
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
              • Traditional RAG systems rely on static indexing structures, which introduce substantial traversal redundancy and computational waste when handling frequently recurring queries.<br>
              • Inspired by cognitive science, the paper proposes the training-free GAM-RAG framework, which uses Kalman gain rules to dynamically strengthen memory states for repeated retrieval based on query feedback.<br>
              • Successfully balances index stability and adaptability, effectively avoiding unproductive retrieval while substantially reducing inference compute overhead without sacrificing accuracy.
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
              • Clearly identifies a prevailing optimization misconception in current memory systems: the true impact of the writing, retrieval, and utilization stages on overall performance must be quantitatively diagnosed.<br>
              • Develops a diagnostic framework that performs rigorous cross-ablation studies of mainstream writing and retrieval strategies, isolating and disentangling the contribution of each stage.<br>
              • Demonstrates that retrieval is the dominant performance bottleneck by a wide margin (with an impact weight of up to 20%), and that raw chunk-based storage remains highly effective, guiding the industry to prioritize retrieval enhancement over complex compression schemes.
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
            • Long-horizon agents passively depend on external RAG retrieval and lack autonomous mechanisms for assessing the value of historical information and managing what should be retained.<br>
            • Proposes the Self-Memory Policy Optimization algorithm (MemPO), which introduces an improved credit assignment mechanism to grant the model the ability to proactively summarize and filter high-value memories.<br>
            • By precisely removing redundant information, the method significantly reduces token consumption while comprehensively outperforming prior approaches in both F1 score and overall task performance.
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
            • Introduces ParamMem, a parameterized memory module that addresses output repetition caused by self-reflection through diversified reflection generation.<br>
            • Employs temperature-controlled sampling and cross-sample memory techniques to build the high-performance ParamAgent framework.<br>
            • Significantly outperforms existing baselines on tasks such as code generation and mathematical reasoning, validating the positive impact of reflection diversity on task success rates.
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
            • Innovatively proposes a general neural memory system whose updates can be controlled via natural language instructions.<br>
            • Addresses the limitation of traditional models that prevent users from intervening in memory content, enabling agents to selectively learn from heterogeneous sources.<br>
            • This approach shows great application potential in scenarios such as healthcare and customer service, where memory accuracy and controllability are critically important.
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
            • Proposes the EMPO² hybrid policy optimization framework, aimed at overcoming exploration bottlenecks in reinforcement learning training for LLM agents.<br>
            • Combines memory-guided exploration with policy updates, ensuring strong robustness in both memory-enabled and memory-free scenarios.<br>
            • Achieves a 128.6% performance leap on the ScienceWorld task and demonstrates excellent adaptability on out-of-distribution tasks.
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
            • Introduces AMA-Bench, a long-term memory evaluation framework specifically designed for autonomous agent–environment interactions rather than dialogue-only settings.<br>
            • Simultaneously proposes the AMA-Agent system, which leverages causal graphs and tool-augmented retrieval to optimize memory retrieval quality.<br>
            • The study reveals shortcomings of existing memory systems in continuous environment interaction tasks and provides effective pathways for improvement.
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
          • Proposes the autonomous memory agent U-Mem, which shifts memory behavior from passive storage to active knowledge acquisition, verification, and curation.<br>
          • Introduces a cost-aware knowledge extraction cascade, incorporating multi-level validation from self-signals to expert feedback, combined with semantically aware sampling strategies.<br>
          • Successfully mitigates cold-start bias and outperforms previous memory baselines on challenging knowledge-intensive tasks such as HotpotQA.
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
          • To address the challenges faced by software engineering agents when handling tasks with similar descriptions but differing logic, this work proposes structure-aligned, subtask-level memory.<br>
          • Through fine-grained task decomposition and memory alignment, the mechanism significantly enhances agents’ long-horizon reasoning capabilities.<br>
          • Its superiority in solving complex, logically entangled tasks is demonstrated across multiple software engineering benchmark evaluations.
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
    • This paper explores a framework—AgentOS—that enables large language models (LLMs) to evolve into dynamic autonomous cognitive systems.<br>
    • By redefining LLMs as a “reasoning kernel,” AgentOS introduces the concept of deep context management to address information dilution in long-context tasks and temporal drift in multi-agent collaboration found in current applications.<br>
    • The paper provides a detailed exposition of AgentOS’s core components, such as the Cognitive Synchronization Pulse (CSP), semantic slicing theory, and perception alignment mechanisms, and explains how they facilitate the emergence of collective intelligence in multi-agent systems.
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
          • Proposes Pancake, a multi-level agent memory system designed to address multi-agent memory fragmentation in large-scale LLM services.<br>
          • Unifies multi-level index caching, coordinated index management, and collaborative GPU–CPU acceleration techniques.<br>
          • Compatible with mainstream frameworks such as LangChain, Pancake achieves more than a 4.29× throughput improvement under real-world workloads.
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
    • The paper reports on red-teaming tests of autonomous language model agents, highlighting the security and privacy vulnerabilities that agents can introduce in real-world environments.<br>
    • The study examines 11 cases, revealing various issues and failure modes of agents in handling sensitive information, following instructions, and managing resources.<br>
    • The text discusses the complexity of responsibility attribution and the shortcomings of existing technical and legal frameworks in ensuring the safety of autonomous systems.
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
          • Introduces SPL, an SQL-inspired declarative language that treats the LLM context window as a constrained resource for efficient management.<br>
          • Natively integrates RAG and persistent memory, providing an automatic query optimizer and transparent EXPLAIN-style debugging capabilities.<br>
          • Experiments confirm that SPL significantly reduces prompt redundancy and lowers computational costs in tasks such as multilingual translation and logical chunking.
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
            • Systematically analyzes the security risks in the reasoning dependencies of LLM agents, categorizing them as data and tool supply chain attacks.<br>
            • Introduces the concept of a “viral agent loop,” warning that agents may become carriers of self-propagating generative worms.<br>
            • Advocates for the adoption of a zero-trust runtime architecture, constraining tool execution through cryptographically verified provenance and treating context as an untrusted data stream.
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
    • The paper analyzes agentic memory systems—particularly the state persistence capabilities of large language models (LLMs) during long-term interactions—revealing that the empirical foundations of their design and evaluation remain fragile.<br>
    • The article categorizes memory structures, including lightweight semantic memory, entity-centric and personalized memory, episodic memory, and reflective memory. Through empirical analysis, it shows that current systems fall short of expectations and identifies a mismatch between evaluation metrics and semantic utility.<br>
    • The paper also explores Memory-Augmented Generation (MAG) in the context of long-context processing, examining different memory architectures, operations, and management strategies, and emphasizes the need for optimized memory management and improved evaluation methodologies.
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
    • TierMem is a hierarchical memory system designed to improve the efficiency and accuracy of information retrieval, addressing information compression challenges arising from long-term interaction histories.<br>
    • By constructing a fast summary layer and an immutable raw log layer, the system effectively manages information storage and retrieval, accelerating query response times while reducing costs.<br>
    • TierMem’s design incorporates intelligent routing optimization, error analysis, and hierarchical recall strategies to balance accuracy and efficiency.
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
    • This study proposes an innovative “memory-based advantage shaping” approach aimed at improving the sample efficiency of reinforcement learning (RL) guided by large language models (LLMs) in sparse or delayed reward environments.<br>
    • By constructing a memory graph and introducing a utility function, the method effectively integrates external guidance to optimize the learning process of RL models.<br>
    • Experimental results demonstrate high sample efficiency and strong performance across multiple benchmark environments.
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
    • MIRA (Memory-Integrated Reinforcement Learning Agent) is a novel reinforcement learning agent that integrates guidance from large language models (LLMs) by constructing a structured memory graph, improving learning efficiency and exploration capability in sparse-reward environments.<br>
    • The core of MIRA lies in combining offline and online LLM guidance, filtering high-confidence outputs, computing utility signals, and optimizing the advantage function to ensure autonomous learning while reducing reliance on real-time LLM queries.<br>
    • Experimental results show that MIRA outperforms traditional methods in both sample efficiency and convergence across multiple environments, demonstrating its potential in complex tasks.
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
            • To address the lack of effective recall of interaction history in existing language agents, the episodic memory reasoning framework REMem is proposed.<br>
            • Its core consists of two stages—offline indexing and online reasoning—enabling agents to mimic human-like reasoning within spatiotemporal contexts.<br>
            • Experimental results show that this framework demonstrates significant advantages on specialized episodic memory benchmark tests.
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
    • Mnemis is a novel memory framework designed to enhance the organization and retrieval capabilities of large language models (LLMs).<br>
    • The framework combines two retrieval mechanisms: System 1 similarity search and System 2 global selection. By constructing a base graph and a hierarchical graph, it can handle complex queries more efficiently.<br>
    • Mnemis performs exceptionally well on long-term memory benchmarks, achieving high scores such as 93.9 and 91.6, and demonstrates significant advantages in entity recognition and information retrieval.
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
    • The paper introduces the “Zombie Agent” attack model, focusing on self-evolving large language model (LLM) agents.<br>
    • The model demonstrates how malicious payloads can be injected into an agent’s long-term memory through a black-box two-stage attack framework (infection and trigger), leading to persistent compromise.<br>
    • The study shows that existing prompt-filtering defenses are insufficient to protect such self-evolving agents and highlights the particular vulnerability of memory architectures.
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
    • This paper explores a framework called ER-MIA, which investigates black-box adversarial memory injection attacks (AMIAs) targeting long-term memory–augmented large language models (LLMs).<br>
    • The ER-MIA framework reveals attack mechanisms that inject malicious text through normal interactions, potentially leading the model to produce incorrect reasoning.<br>
    • The study designs multiple automated adversarial memory generation strategies and conducts empirical evaluations, demonstrating that current long-term memory systems exhibit significant vulnerabilities when facing such attacks.
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
            • Proposes a non-parametric memory framework that explicitly distinguishes episodic memory from semantic memory, enhancing the exploration capabilities of embodied agents.<br>
            • Employs a program-style rule extraction mechanism to transform environmental experiences into structured semantic memory that can generalize across scenarios.<br>
            • Significantly improves observation reuse and question-answering efficiency of multimodal large models in non-stationary environments.
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
    • HyperRAG is an innovative retrieval-augmented generation (RAG) framework that replaces traditional binary knowledge graphs with n-ary hypergraphs to improve the accuracy and efficiency of complex question answering and knowledge retrieval tasks.<br>
    • Through the new modules HyperRetriever and HyperMemory, the framework enables more precise multi-hop reasoning and enhanced context awareness.<br>
    • Experimental results show that HyperRAG achieves superior performance across multiple benchmark datasets.
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
    • This paper provides a detailed introduction to PANINI, a non-parametric continual learning framework designed to enhance continual learning and multi-hop question answering capabilities.<br>
    • By incorporating structured memory and a Generative Semantic Workspace (GSW), PANINI can efficiently process new information and support reasoning through chains of question answering.<br>
    • Compared with various baseline models, PANINI demonstrates superior performance across multiple evaluation benchmarks, showing particular robustness in scenarios with missing evidence.
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
          • Proposes the FluxMem framework, which enables LLM agents to adaptively select different memory structures based on interaction characteristics.<br>
          • Introduces a three-layer memory hierarchy and employs probabilistic gating based on a Beta mixture model to enhance the robustness of memory fusion.<br>
          • FluxMem demonstrates outstanding performance in handling heterogeneous interaction patterns, achieving significant performance gains across multiple long-term benchmarks.
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
          • Proposes a hybrid memory architecture, HyMem, which addresses the efficiency trade-offs in long conversations through dual-granularity storage (summary-level / deep-level).<br>
          • Introduces a dynamic, on-demand scheduling mechanism: simple queries invoke efficient summaries, while complex queries activate deep-level modules.<br>
          • Experiments show that HyMem maintains high performance while reducing computational costs by 92.6%.
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
          • Introduces Neuromem, a scalable benchmarking platform for evaluating the full dynamic lifecycle of external memory modules for LLMs, from ingestion and maintenance to retrieval and integration.<br>
          • The study reveals that memory accuracy and cost are jointly influenced by the entire lifecycle rather than any single stage in isolation.<br>
          • The analysis indicates that performance generally degrades as memory scale increases, and that time-dependent queries remain the most significant challenge for current systems.
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
    • This paper explores the development of the Unified Memory Agent (UMA) and its application in dynamic long-term state tracking and information retrieval.<br>
    • By integrating memory operations with question answering, UMAs overcome the challenges faced by traditional large language models (LLMs) when handling long inputs.<br>
    • UMA leverages reinforcement learning and novel policy optimization algorithms, demonstrating significant performance improvements in dynamic scenarios, with accuracy increasing from 61.38% to 76.46%.
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
        • The paper finds that 88% of attention operations in LLMs retrieve predictable information, a redundancy that persists throughout standard training without being eliminated.<br>
        • It proposes CRAM, an architecture that adaptively reduces compute by gradually distilling frequently accessed episodic retrievals into efficient parametric semantic memory via a consolidation-aware router.<br>
        • CRAM achieves a 37.8x reduction in attention compute while its learned consolidation dynamics quantitatively match the power-law transition curves observed in human cognitive psychology.
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
        • It introduces the "memory discrimination" task, which acts as a filter during memory construction to identify and store only valuable personal knowledge from vast daily interactions.<br>
        • It proposes the Scene-Aware Memory Discrimination (SAMD) framework, combining a Gating Unit Module (GUM) for efficient noise filtering and a Cluster Prompting Module (CPM) for adaptive memory standards.<br>
        • Evaluations demonstrate that SAMD significantly enhances the efficiency and quality of memory construction, successfully recalling critical data while reducing computational costs for personalized AI agents.
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
        • It proposes the Rec2PM framework with a tripartite memory mechanism that compresses long user histories into compact Preference Memory tokens, overcoming the computational bottlenecks of long-sequence modeling.<br>
        • It introduces a self-referential teacher-forcing strategy that leverages a global view of history to generate reference targets, enabling fully parallelized training for recurrent memory updates.<br>
        • It demonstrates superior storage and inference efficiency while acting as a denoising Information Bottleneck to filter interaction noise, achieving higher accuracy than full-sequence models.
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
        • It proposes TS-Memory, a plug-and-play lightweight memory adapter that uses Parametric Memory Distillation to adapt frozen Time Series Foundation Models (TSFMs) to downstream domain shifts.<br>
        • It employs a two-stage training strategy: first constructing an offline kNN teacher to generate privileged supervision signals, then distilling retrieval-induced distributional corrections into a parametric module via confidence-gated supervision.<br>
        • It enables retrieval-free inference with constant-time complexity, consistently improving forecasting accuracy across benchmarks while maintaining the efficiency of the frozen backbone and avoiding catastrophic forgetting.
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
        • CogitoRAG is a retrieval-augmented generation (RAG) framework based on cognitive memory mechanisms, designed to enhance large language models’ (LLMs) capabilities in knowledge integration and reasoning.<br>
        • The framework simulates human cognitive processes and optimizes information retrieval and answer generation through the collaboration of three main modules: query decomposition, entity diffusion, and CogniRank re-ranking.<br>
        • CogitoRAG achieves strong performance across multiple question-answering benchmarks, particularly outperforming traditional RAG methods on complex reasoning tasks, emphasizing the principle that “understanding is superior to memorization.”
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
        • It proposes GRU-Mem, a gated recurrent memory framework that processes long context chunk-by-chunk to overcome performance degradation and context window limits in LLMs.<br>
        • It introduces two text-controlled gates, an update gate and an exit gate, to selectively update memory and enable early termination, effectively preventing memory explosion and reducing redundant computation.<br>
        • Optimized via end-to-end reinforcement learning, GRU-Mem significantly outperforms existing methods in reasoning tasks and achieves up to 400% inference speed acceleration compared to vanilla recurrent memory agents.
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
        • It proposes Elastic Memory, a novel recurrent memory architecture grounded in the HiPPO framework that encodes long-range history into fixed-size states via optimal online function approximation.<br>
        • It develops a parallelized block-level update and a flexible "polynomial sampling" mechanism for efficient retrieval, enabling the reconstruction of history summaries from compressed states without extra trainable parameters.<br>
        • Experiments demonstrate that it outperforms SOTA baselines on 32k+ context tasks with superior efficiency, while its decoupled design allows for injecting inductive biases at test-time without retraining.
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
        • The paper proposes UMEM, a framework that jointly optimizes memory extraction and management to resolve the policy misalignment and poor generalization found in traditional static extraction methods.<br>
        • It introduces Semantic Neighborhood Modeling and a Marginal Utility Reward via GRPO, forcing the agent to distill generalizable principles across clusters of related tasks instead of memorizing instance-specific noise.<br>
        • Experiments show that UMEM significantly outperforms state-of-the-art baselines across multiple benchmarks and maintains a stable, monotonic performance growth curve during continuous self-evolution.
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
        • It proposes TraceMem, a cognitively-inspired framework that weaves disjointed conversational traces into structured narrative memory schemata through a three-stage pipeline of processing and consolidation.<br>
        • It mimics human memory consolidation by using topic segmentation and hierarchical clustering to transform episodic snippets into coherent, time-evolving narrative threads and structured user memory cards.<br>
        • It implements an agentic search mechanism to enable human-like source attribution, achieving state-of-the-art performance in multi-hop and temporal reasoning for long-term dialogues.
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
        • It proposes AMEM4Rec, an agentic framework that models collaborative filtering signals end-to-end by introducing an evolving memory module without relying on pre-trained CF models.<br>
        • It designs a cross-user memory evolution mechanism that aggregates abstract behavior patterns into a global pool, using dual validation to link and iteratively evolve shared memory entries across users.<br>
        • Extensive experiments demonstrate that AMEM4Rec significantly outperforms existing baselines, particularly showing superior performance and generalization in sparse interaction scenarios.
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
        • Introduces the concept of "Implicit Memory," demonstrating that LLMs can bypass their stateless nature by encoding state information in their own outputs to create a persistent hidden channel across independent sessions.<br>
        • Implements and validates "Time Bombs," a new class of temporal backdoors that use implicit memory to accumulate hidden states over multiple interactions, activating only after a specific sequence of conditions is met.<br>
        • Systematically analyzes risks such as covert communication and benchmark contamination, while outlining future research directions for detecting, evaluating, and controlling unintended persistence in LLMs.
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
        • It proposes MemAdapter, a framework that unifies heterogeneous agent memory paradigms (explicit, parametric, and latent) using a paradigm-agnostic generative subgraph retrieval approach.<br>
        • It employs a two-stage training strategy: distilling a generative retriever from a unified memory space and then efficiently adapting it to new paradigms via lightweight alignment modules and contrastive learning.<br>
        • MemAdapter consistently outperforms existing baselines, completing paradigm alignment in just 13 minutes and enabling effective zero-shot fusion across different memory types.
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
        • This paper proposes MemPot, the first defense framework against memory extraction attacks that proactively injects optimized honeypots (trap documents) into the agent's memory systems.<br>
        • It utilizes a two-stage optimization strategy to maximize the statistical separability between attacker and user retrieval patterns, generating safe and inconspicuous trap texts through safety-constrained embedding inversion.<br>
        • Based on Wald’s Sequential Probability Ratio Test (SPRT), MemPot achieves near-perfect detection accuracy with zero online inference latency while preserving the agent's core utility and performance.
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
        • A new framework called Synchronized Backflow Unlearning (SBU) is proposed to effectively remove sensitive information from large language models (LLMs) while ensuring the integrity of shared knowledge.<br>
        • By coordinating the collaboration between parameter paths and memory paths, SBU addresses the limitations of traditional privacy-preserving methods, successfully eliminating residual effects of deleted information and reducing the risk of information recontamination.<br>
        • Experimental results show that this approach significantly improves privacy protection on medical question-answering benchmarks while maintaining accuracy. It not only outperforms baseline methods in efficiency but also overcomes computational resource constraints.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Studied how to share memory selectively across parallel agents to reduce redundancy and coordination overhead.<br>
        • Proposed a selective sharing mechanism/policy to decide what to broadcast vs keep private per agent.<br>
        • Evaluated on multi-agent settings, showing improved efficiency while maintaining (or improving) task performance.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Formulated memory as an evolving object updated online from dense/continuous feedback signals rather than sparse endpoints.<br>
        • Proposed an update/evolution loop that revises stored memories based on feedback to improve future behavior.<br>
        • Demonstrated online improvement over time in agent tasks under continuous supervision.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-02</td>
      <td style="width: 55%;"><strong>Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Beyond%20RAG-purple" alt="Beyond RAG">
        <img src="https://img.shields.io/badge/Decoupled%20Retrieval-red" alt="Decoupled Retrieval">
        <img src="https://img.shields.io/badge/Aggregation-success" alt="Aggregation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.02007">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Revisited agent memory retrieval as a two-stage process: decouple candidate fetching from evidence aggregation.<br>
        • Proposed an aggregation mechanism to combine multi-source/multi-hop evidence for downstream reasoning.<br>
        • Showed gains vs vanilla RAG-style retrieval pipelines in agent memory usage and answer quality.
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
          • Proposes an AI agent memory system that treats stored information as a continuous field (governed by partial differential equations) rather than discrete entries.<br>
          • Drawing inspiration from field theory, memory diffuses within a semantic space, decays thermodynamically based on importance, and enables multi-agent interaction through field coupling.<br>
          • The approach achieves significant improvements in multi-session and temporal reasoning performance on the LongMemEval benchmark, demonstrating the advantages of collective intelligence.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed the E-mem framework, shifting from traditional memory preprocessing to Episodic Context Reconstruction to prevent information loss caused by de-contextualization.<br>
        • Adopted a heterogeneous Master-Assistant architecture where assistant agents maintain uncompressed context as memory nodes while the master agent handles global planning.<br>
        • Introduced a routing mechanism allowing assistants to reason within locally restored original contexts, achieving SOTA performance on LoCoMo and HotpotQA while reducing token costs by over 70%.
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
        • Proposed ShardMemo, a tiered memory architecture: Tier A (working state), Tier B (sharded evidence), and Tier C (versioned skill library).<br>
        • Enforced a "scope-before-routing" strategy in Tier B and modeled shard selection as a Masked MoE routing problem under fixed budgets, using cost-aware gating.<br>
        • Improved F1 by +6.87 on LoCoMo and HotpotQA compared to cosine similarity routing, while reducing retrieval work and latency by 20.5%.
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
        • Proposed MemCtrl, a framework using MLLMs as active memory controllers to filter redundant observations online for embodied agents.<br>
        • Introduced a trainable memory head ($\mu$) acting as a gate to dynamically determine whether to retain, update, or discard observations during exploration.<br>
        • Trained via offline supervision and online RL, MemCtrl improved task completion rates by ~16% for small MLLMs on EmbodiedBench, with >20% gains on specific instruction subsets.
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
        • Proposed AMA (Adaptive Memory via Multi-Agent Collaboration), leveraging Constructor, Retriever, Judge, and Refresher agents to manage multi-granularity memory.<br>
        • Utilized a hierarchical memory design (Raw Text, Fact Knowledge, Episode), where the Retriever dynamically routes queries and the Judge detects conflicts.<br>
        • The Refresher maintains long-term consistency via logic-driven updates. AMA significantly outperformed baselines on LoCoMo and LongMemEval while reducing token consumption by 80%.
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
        • Proposed the Global Verifier (GLOVE) framework to address memory-environment misalignment caused by dynamic environmental drifts.<br>
        • Established "relative truth" via active probing to detect cognitive dissonance by comparing retrieved memories with fresh observations, realigning memory without ground truth.<br>
        • Significantly improved agent adaptability and success rates in web navigation, discrete planning, and continuous control tasks under explicit and implicit environment drifts.
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
        • Proposed FadeMem, a memory architecture inspired by the Ebbinghaus forgetting curve, introducing active forgetting mechanisms to prevent information overload.<br>
        • Implemented a dual-layer hierarchy with adaptive exponential decay governed by semantic relevance, access frequency, and temporal patterns.<br>
        • Combined with LLM-guided conflict resolution, FadeMem achieved superior multi-hop reasoning on Multi-Session Chat and LoCoMo while reducing storage by 45%.
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
        • MemWeaver proposes a tri-layer memory framework (Graph, Experience, Passage) that consolidates long-term interactions into temporally grounded structures, ensuring evidence traceability.<br>
        • It employs a dual-channel retrieval strategy to "weave" structured relational facts with original textual evidence, supporting complex multi-hop and temporal reasoning tasks.<br>
        • Experiments on the LoCoMo benchmark show it improves reasoning accuracy while actively reducing input context length by over 95% compared to long-context baselines.
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
        • Proposed a clustering-based memory compression strategy designed for on-device personalization under limited context windows.<br>
        • Groups similar memories and merges them within clusters (instead of simple concatenation), reducing redundancy while preserving semantic coherence.<br>
        • Demonstrated significant reduction in token usage and improved personalized generation quality compared to naive concatenation baselines.
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
        • Proposed CoM (Chain-of-Memory), advocating a shift from expensive structured construction to lightweight construction with dynamic utilization.<br>
        • Introduced Dynamic Memory Chain Evolution to organize retrieved fragments into coherent inference paths with adaptive truncation to prune noise.<br>
        • Achieved 7.5%–10.4% accuracy gains on LoCoMo and LongMemEval while reducing token consumption to ~2.7% compared to complex memory structures.
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
          • TeleMem introduces a unified long-term and multimodal memory framework that extracts narrative-grounded information to maintain coherent user profiles without schema-driven hallucinations.<br>
          • It employs a structured writing pipeline for batching, retrieval, and consolidation, significantly improving storage and token efficiency, and incorporates a multimodal memory module with ReAct-style reasoning for video understanding.<br>
          • Experimental results on the ZH-4O benchmark show TeleMem outperforming the state-of-the-art Mem0 baseline by 19% in accuracy while reducing token usage by 43% and speeding up operations by 2.1×.
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
          • Proposes STITCH, an agentic memory system that indexes trajectory steps using "Contextual Intent"—comprising thematic scope, event type, and key entity types—to disambiguate recurring information in long-horizon tasks.<br>
          • Introduces a retrieval mechanism that filters and prioritizes memory snippets based on structural intent compatibility rather than just semantic similarity, effectively suppressing context-incompatible history.<br>
          • Presents CAME-Bench, a multi-domain benchmark designed to evaluate context-aware retrieval in realistic, goal-oriented trajectories, where STITCH achieves state-of-the-art performance.
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
        • Introduces PersonalAlign, a new task requiring GUI agents to align with implicit user intents—specifically resolving vague instructions and anticipating routines—by leveraging long-term user records.<br>
        • Presents AndroidIntent, a benchmark constructed from 20k long-term records, featuring hierarchically annotated user preferences and routines to evaluate personalization capabilities.<br>
        • Proposes HIM-Agent (Hierarchical Intent Memory Agent), which utilizes a streaming aggregation module and hierarchical filters (Execution-based and State-based) to continuously update and organize user memory for improved reactive and proactive performance.
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
        • Introduces AtomMem, a dynamic memory framework that reframes agentic memory management as a learnable sequential decision-making problem rather than a static, hand-crafted workflow.<br>
        • Deconstructs memory processes into atomic CRUD (Create, Read, Update, Delete) operations and employs reinforcement learning (GRPO) to learn a task-aligned policy for autonomously orchestrating these operations.<br>
        • Experimental results on long-context benchmarks (HotpotQA, 2WikiMultihopQA, Musique) demonstrate that AtomMem consistently outperforms static memory baselines by dynamically tailoring memory strategies to specific task demands.
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
          • Fine-Mem is a unified reinforcement learning framework designed to optimize long-horizon memory management for LLM agents by aligning fine-grained feedback with memory operations.<br>
          • It addresses reward sparsity through Chunk-level Step Reward (CSR), which provides immediate supervision via constructed QA tasks, and solves credit assignment issues with Evidence-Anchored Reward Attribution (EARA) by linking global rewards to specific memory operations.<br>
          • Experimental results demonstrate that Fine-Mem consistently outperforms strong baselines on benchmarks like Memalpha and MemoryAgentBench, showing superior adaptability and generalization across different models.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed an autonomous strategy to compress/retain context so agents can operate under tight context budgets.<br>
        • Treated memory management as an active decision problem: what to keep, summarize, discard, or externalize.<br>
        • Demonstrated improved long-horizon performance vs passive truncation or naive summarization baselines.
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
          • MemoBrain introduces an "executive memory" paradigm for tool-augmented agents, functioning as a co-pilot to construct dependency-aware memory and actively manage context under bounded budgets.<br>
          • The framework employs specific memory operations—Trajectory Folding and Selective Flush—to organize reasoning progress, retaining a high-salience structural backbone while discarding transient execution artifacts.<br>
          • Experiments on benchmarks like GAIA, WebWalker, and BrowseComp-Plus demonstrate that MemoBrain consistently outperforms strong baselines by enabling coherent, goal-directed reasoning over long horizons.
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
          • TSM is a memory framework that models semantic time for point-wise memory and supports the construction and utilization of durative memory.<br>
          • It builds a semantic timeline to organize episodic interactions and consolidates them into time-aware durative memories (topics and personas) to capture long-term user states.<br>
          • During memory utilization, TSM incorporates the query’s temporal intent to retrieve temporally appropriate durative memories, significantly improving performance on benchmarks like LONGMEMEVAL and LOCOMO.
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
          • Bi-Mem is an agentic framework that constructs hierarchical memory (fact, scene, persona) bidirectionally using an inductive agent for bottom-up aggregation and a reflective agent for top-down calibration to mitigate noise and hallucination.<br>
          • It employs an associative retrieval mechanism that leverages spreading activation to connect memory units across granularities, enabling coherent recall of both contextual scenes and specific facts.<br>
          • Empirical evaluations on the LoCoMo benchmark demonstrate that Bi-Mem significantly outperforms leading memory baselines in long-term personalized conversational tasks.
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
          • HiMem is a hierarchical long-term memory framework designed for long-horizon dialogues, integrating fine-grained "Episode Memory" (via topic-aware segmentation) with abstract "Note Memory" (via knowledge extraction) to bridge concrete events and stable knowledge.<br>
          • It employs a conflict-aware "Memory Reconsolidation" mechanism that uses retrieval feedback to revise and supplement stored knowledge, enabling continual self-evolution and correction of memory over time.<br>
          • Evaluations on long-horizon benchmarks demonstrate that HiMem outperforms baselines in accuracy, consistency, and reasoning, validating the effectiveness of its hierarchical organization and dynamic updating strategies.
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
          • SEEM introduces a dual-layer memory framework combining a Graph Memory Layer for static facts and an Episodic Memory Layer for narrative progression, both anchored by provenance pointers to raw interaction passages.<br>
          • The system employs a "Reverse Provenance Expansion" (RPE) mechanism to reconstruct coherent narrative contexts from fragmented evidence during retrieval, addressing the "scattered retrieval" problem in long-term interactions.<br>
          • Experiments on benchmarks like LoCoMo and LongMemEval show SEEM significantly outperforms competitive memory-augmented baselines (like HippoRAG 2) in narrative coherence and logical consistency.
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
          • MemBuilder is a reinforcement learning framework that trains LLMs to actively construct and manage a multi-dimensional memory system (Core, Episodic, Semantic, and Procedural) rather than relying on static prompting.<br>
          • It introduces "Attributed Dense Rewards Policy Optimization" (ADRPO) to solve reward sparsity and credit assignment issues by using synthetic session-level QA for immediate feedback and gradient weighting based on memory component contribution.<br>
          • Experimental results show that a lightweight 4B model trained with MemBuilder outperforms state-of-the-art closed-source models (including Claude 4.5 Sonnet) on long-term dialogue benchmarks like LoCoMo and LongMemEval.
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
        • <strong>ProMem Framework</strong>: Addresses the limitations of "one-off" static summarization by proposing a proactive memory extraction framework inspired by Recurrent Processing Theory (RPT).<br>
        • <strong>Recurrent Feedback Loop</strong>: Introduces a self-questioning mechanism where the agent actively probes dialogue history to verify facts and recover missing details, ensuring memory completeness and accuracy.<br>
        • <strong>Performance</strong>: Outperforms state-of-the-art baselines (e.g., Mem0) on HaluMem and LongMemEval benchmarks, demonstrating high robustness in token compression and cost-effectiveness with Small Language Models.<br>
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
        • Proposed <strong>CompassMem</strong>, an event-centric memory framework inspired by Event Segmentation Theory, organizing memory as an <strong>Event Graph</strong> with explicit logical relations (causal, temporal).<br>
        • Transforms memory from passive storage into a <strong>Logic Map</strong>, enabling agents to actively navigate structured dependencies via a Planner-Explorer-Responder mechanism.<br>
        • Features active multi-path memory search that dynamically expands or skips nodes based on subgoal satisfaction, avoiding redundant retrieval.<br>
        • Demonstrates superior performance on LoCoMo and NarrativeQA benchmarks, significantly improving multi-hop and temporal reasoning compared to baselines like HippoRAG and Mem0.<br>
      <br>
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
        • <strong>PersonaTree Framework</strong>: Introduces a globally maintained **PersonaTree** grounded in the Biopsychosocial model as a dynamic user profile. By constraining the trunk with a schema and iteratively updating branches, it enables controllable memory growth and compression.<br>
        • <strong>MemListener Training</strong>: Trains a lightweight MemListener model via **Reinforcement Learning with process-based rewards** to generate structured, executable memory operations (ADD, UPDATE, DELETE), achieving performance comparable to large reasoning models.<br>
        • <strong>Adaptive Response Generation</strong>: Implements a dual-mode strategy that utilizes PersonaTree directly for low-latency responses or triggers an agentic recall mode guided by the tree for complex queries, outperforming baselines in consistency and noise suppression.<br>
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
        • <strong>Membox Architecture</strong>: Addresses the "fragmentation-compensation" flaw in existing systems by proposing a hierarchical architecture centered on **Topic Continuity** to preserve temporal and causal flow.<br>
        • <strong>Topic Loom & Trace Weaver</strong>: Introduces a *Topic Loom* to group continuous dialogue into cohesive "memory boxes" and a *Trace Weaver* to link these boxes into long-range event timelines across discontinuities.<br>
        • <strong>Performance</strong>: Achieves up to 68% F1 improvement on temporal reasoning tasks in the LoCoMo benchmark compared to baselines like Mem0, while using significantly fewer context tokens.<br>
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
          • HiMeS is a memory framework for AI assistants that emulates the hippocampus–neocortex interaction by integrating short-term dialogue compression with long-term user profile storage.<br>
          • It utilizes a short-term memory extractor trained via reinforcement learning to proactively pre-retrieve knowledge, and a partitioned long-term memory network to re-rank results based on historical user interactions.<br>
          • Evaluations on real-world industrial datasets demonstrate that HiMeS significantly outperforms traditional RAG baselines in personalized question-answering tasks.
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
        • SYNAPSE is a brain-inspired memory architecture that replaces static vector retrieval with a unified episodic–semantic graph, addressing the “context isolation” issue in traditional RAG systems, where semantically distant yet causally related memories cannot be effectively associated.<br>
        • It introduces cognitive dynamics such as spreading activation, lateral inhibition, and temporal decay to dynamically propagate relevance and filter noise within the graph, rather than relying solely on precomputed links or vector similarity.<br>
        • SYNAPSE achieves state-of-the-art performance on the LoCoMo benchmark, significantly improving multi-hop reasoning capabilities and robustness to adversarial queries through an uncertainty-aware gating mechanism.
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
        • Proposed CODEMEM, a memory management system tailored for repository-level iterative code generation.<br>
        • Introduces <strong>Code Context Memory</strong>: Uses AST-guided selection to dynamically update and merge repository context, keeping it relevant while discarding noise.<br>
        • Introduces <strong>Code Session Memory</strong>: Uses AST-based change analysis to detect conflicts and forgetting, organizing history into code-centric units (diffs) rather than just text.<br>
        • Achieves SOTA on CodeIF-Bench and CoderEval, improving instruction following by ~12% and reducing interaction rounds by 2–3.<br>
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
        • <strong>LatentGraphMem Framework</strong>: Proposes a memory framework combining implicit graph memory for stability and efficiency with explicit subgraph retrieval for interpretability, storing graph structures in latent space.<br>
        • <strong>Three-Stage Training Strategy</strong>: Involves training a graph builder (global representation), a subgraph retriever (budgeted edge selection), and joint fine-tuning (coordination optimization) for effective end-to-end QA.<br>
        • <strong>Performance</strong>: Consistently outperforms explicit-graph and latent-memory baselines on long-horizon benchmarks like HotpotQA, NarrativeQA, and WikiHop across multiple model scales, achieving up to 63.34% average accuracy.<br>
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
        • <strong>MAGMA Architecture</strong>: Proposes a multi-graph agentic memory architecture that explicitly models memory items across orthogonal semantic, temporal, causal, and entity graphs, overcoming the limitations of monolithic memory stores.<br>
        • <strong>Adaptive Topological Retrieval</strong>: Introduces an intent-aware Adaptive Traversal Policy that dynamically routes retrieval through relevant relational views, decoupling memory representation from retrieval logic for transparent reasoning.<br>
        • <strong>Performance</strong>: Consistently outperforms state-of-the-art agentic memory systems (e.g., Nemori, A-MEM) on long-horizon benchmarks like LoCoMo and LongMemEval, while reducing retrieval latency and token consumption.<br>
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
        • <strong>TiMem Framework</strong>: Introduces a temporal-hierarchical memory framework using a Temporal Memory Tree (TMT) to progressively consolidate raw dialog into abstract persona representations, emphasizing temporal continuity.<br>
        • <strong>Core Mechanisms</strong>: Features semantic-guided consolidation (fine-tuning free) and complexity-aware memory recall (Recall Planner + Gating) to balance precision and efficiency across query types.<br>
        • <strong>Performance</strong>: Achieves SOTA accuracy on LoCoMo (75.30%) and LongMemEval-S (76.88%) benchmarks, while significantly reducing recalled context length (-52.20%) on LoCoMo.<br>
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
        • <strong>MemRL Framework</strong>: Proposes a non-parametric reinforcement learning framework that enables frozen LLM agents to self-evolve by optimizing episodic memory, avoiding the costs and forgetting issues of fine-tuning.<br>
        • <strong>Intent-Experience-Utility Triplet</strong>: Introduces a Two-Phase Retrieval mechanism (semantic recall + value-aware selection) and a runtime utility update rule, using Q-values to distinguish high-utility strategies from noise.<br>
        • <strong>Performance</strong>: Significantly outperforms MemP and RAG on benchmarks like HLE, BigCodeBench, and ALFWorld, demonstrating that agents can continuously improve via runtime trial-and-error without weight updates.<br>
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
        • Introduces SimpleMem, an efficient memory framework tailored for lifelong LLM agents based on semantic lossless compression.<br>
        • The system operates via a three-stage pipeline: Semantic Structured Compression to filter low-entropy noise, Recursive Memory Consolidation to synthesize abstract representations, and Adaptive Query-Aware Retrieval to minimize token usage.<br>
        • Experiments on the LoCoMo benchmark demonstrate a 26.4% improvement in F1 score and up to 30× reduction in inference token consumption compared to full-context models, significantly outperforming baselines like Mem0.
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
        • <strong>AgeMem Framework</strong>: Proposes a unified framework that integrates both Long-Term (LTM) and Short-Term (STM) memory management directly into the agent's policy via tool-based actions (e.g., Add, Update, Filter).<br>
        • <strong>Three-Stage Progressive RL</strong>: Introduces a step-wise GRPO algorithm and a three-stage training strategy (LTM construction, STM control, integrated reasoning) to address sparse rewards and enable end-to-end optimization.<br>
        • <strong>Performance</strong>: Outperforms strong baselines like LangMem and Mem0 across five long-horizon benchmarks (e.g., ALFWorld, HotpotQA), achieving higher task success rates, better memory quality, and more efficient context usage.<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-31</td>
      <td style="width: 55%;"><strong>Nested Learning: The Illusion of Deep Learning Architecture</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.24695">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
        <td colspan="3">
      • Full arXiv version including all appendices — not the previously released trimmed version.<br>
      • Presents a Nested Learning paradigm that unifies a large portion of optimizer and TTT-layer modules.<br>
      • Architectural innovation: HOPE — composed of modified Titans attention and self-modified FFNs. By controlling the chunksize of self-modification of FFN parameter, FFN layers operating at different frequencies implicitly retain memories at different hierarchical levels during runtime.<br>
      • Empirical results are modest.<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-25</td>
      <td style="width: 55%;"><strong>Beyond Heuristics: A Decision-Theoretic Framework for Agent Memory Management</strong></td>
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
        • Provides TeleAI background and introduces a decision-theoretic memory framework (DAM) that formulates the timing and content of memory read/write as an optimal decision problem, with relevance to RL-style formulations.<br>
        • Contains minimal or no experimental validation.
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
      • An OPPO-affiliated paper proposes a two-layer framework that, in RL settings, separates learning to extract memories (level-1) from learning the memory-extraction method itself (level-2).<br>
      • Experiments using Flash-Searcher and GPT-5-Mini achieve SOTA on benchmarks including GAIA.<br>
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
        • MemR³ closed-loop retrieval controller: designed for long-term conversational memory, it can dynamically choose among three actions—retrieve, reflect, and respond.<br>
        • Evidence–gap state tracker: the system maintains a global (evidence, gap) state that explicitly tracks "what is known" and "what is missing," making the process interpretable.<br>
        • Experiments show that on the LoCoMo benchmark, MemR³ significantly improves answer quality across different underlying memory systems (e.g., RAG, Zep).<br>
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-18</td>
      <td style="width: 55%;"><strong>Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement</strong></td>
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
        • A Bayesian procedural memory (experience) framework: MACLA.<br>
        • Overall still a rule-based algorithm; operations include extraction, retrieval/storage, and refinement (Bayesian posterior calibration).<br>
        • On unseen tasks in ALFWorld, performance (90.3%) exceeded that on seen tasks (87.2%), achieving +3.1% positive generalization.<br>
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
        • HINDSIGHT is a unified memory architecture that treats memory as a structured, first-class substrate for reasoning, organizing information into four logical networks: world facts, agent experiences, synthesized entity summaries, and evolving beliefs.<br>
        • The system introduces TEMPR (Temporal Entity Memory Priming Retrieval) for building temporal entity graphs and CARA (Coherent Adaptive Reasoning Agents) for preference-conditioned reasoning, enabling agents to epistemically distinguish evidence from inference.<br>
        • Experimental results on LongMemEval and LoCoMo benchmarks demonstrate that HINDSIGHT significantly outperforms existing memory systems and full-context frontier models in multi-session consistency and open-domain question answering.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-11</td>
      <td style="width: 55%;"><strong>Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution</strong></td>
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
        • ReMe (paper version): an Alibaba-affiliated framework for enhancing LLM procedural memory (experience), including the ReMe algorithm and the reme.library dataset.<br>
        • Core idea: maintain an experience pool with operations—Acquisition, Reuse, and Refinement.<br>
        • Experiments on BFCL-V3 and AppWorld show dynamic experience pools > static pools > baseline, with scaling studies for both model and judge models.
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
        • LightSearcher is an efficient reinforcement learning (RL)-based search architecture grounded in experiential memory. During large language model (LLM)-driven reasoning, it autonomously optimizes agent tool invocation without relying on external data by transforming implicit reasoning trajectories into explicit experiential guidance through contrastive experiential memory.<br>
        • Evaluated on four multi-hop question answering benchmarks—Natural Questions (NQ), HotpotQA, MuSiQue, and 2WikiMultihopQA—LightSearcher achieves accuracy comparable to the state-of-the-art DeepSearch baseline while significantly reducing both tool invocation latency and model response time.<br>
        • The method reduces tool invocations by 39.6%, shortens reasoning time by 48.6%, and decreases token consumption by 21.2%, substantially improving tool-use efficiency without compromising task performance.
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
        • A lifelong learning memory framework for multimodal agents.<br>
        • Retrieval-based long-term memory + parameterized fast memory + periodic distillation.<br>
        • Multimodal handling: unified conversion into textual descriptions.<br>
        • Experiments show improvements over baselines on ScienceQA (text) and MSR-VTT (video); LoCoMo (text) results remain unpublished (in appendix).<br>
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
          • Introduces ComoRAG, a retrieval-augmented generation framework inspired by the human Prefrontal Cortex, designed to achieve stateful reasoning in long narrative contexts.<br>
          • The framework employs a dynamic memory workspace and a metacognitive regulation loop (including Self-Probe, Mem-Fuse, and Mem-Update) to iteratively fuse fragmented evidence into coherent context.<br>
          • Experimental results demonstrate that ComoRAG consistently outperforms strong baselines on challenging benchmarks like NarrativeQA and ∞BENCH, particularly excelling in complex narrative queries requiring global understanding.
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
          • MemSearcher is a large language model (LLMs) agent trained through end-to-end Reinforcement Learning (RL), aiming to enhance the efficiency of knowledge acquisition tasks.<br>
          • MemSearcher optimizes memory management by adopting a new framework called multi-context Group Relative Strategy Optimization (Multi-Context GRPO), which enables the model to self-evolve in multiple conversations.<br>
          • Compared with traditional ReAct search agents, MemSearcher offers significant performance improvements while maintaining low token consumption, especially on smaller models.
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
        • Proposes D-SMART, a model-agnostic framework designed to maintain logical and factual consistency in multi-turn dialogues by coupling a Dynamic Structured Memory (DSM) with a Reasoning Tree (RT).<br>
        • DSM incrementally builds an OWL-compliant knowledge graph from conversation history to prevent context decay, while RT guides the LLM through explicit, traceable multi-step reasoning over this graph.<br>
        • Comprehensive experiments on MT-Bench-101 demonstrate that D-SMART significantly outperforms state-of-the-art baselines, improving consistency scores by over 48% and exhibiting strong stability in extended dialogues.
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
          • Memory-as-action (MemAct) addresses the issue of working Memory management for large language models (LLMS) in long-duration tasks.<br>
          • MemAct transforms memory management into a learnable intrinsic capability, enabling agents to dynamically manage memories while performing tasks, and introduces the Dynamic Context Policy Optimization (DCPO) algorithm to handle the trajectory breakage problem caused by memory editing.<br>
          • MemAct performs exceptionally well in multi-objective question answering tasks, demonstrating higher accuracy and robustness than traditional models.
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
          • MemGen is a dynamic generative memory framework designed to enhance the reasoning and decision-making capabilities of agents based on large language models (LLMS).<br>
          • MemGen simulates human cognitive patterns by interweaving memory with the reasoning process.<br>
          • This framework consists of two parts: memory triggers and memory weavers, which can dynamically determine when to invoke potential memories and integrate them into the reasoning process.
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
          • The paper investigates memory management in large language model (LLM) agents and its impact on long-term performance.<br>
          • It identifies issues such as error propagation and misaligned experience replay, highlighting the importance of high-quality memory.<br>
          • By comparing multiple memory insertion and deletion strategies, the study finds that selective insertion performs better for long-term learning, while historical deletion is particularly effective at reducing low-quality memory records.
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
          • Introduces a framework for adaptive, user-centered AI agents that combines persistent memory, dynamic coordination, and evolving user profiles to enable personalized long-term interactions.<br>
          • The approach integrates established agentic AI patterns—such as Multi-Agent Collaboration and Multi-Source Retrieval—with mechanisms like self-validation and implicit user profiling to tailor responses to individual needs.<br>
          • Evaluations on three public datasets and a pilot user study demonstrate improvements in retrieval accuracy, response correctness, and perceived personalization compared to standard RAG baselines.
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
        • TOOLMEM, a memory-augmented agent that learns from past tool use. It stores summarized, retrievable “what this tool is good/bad at” knowledge and injects the relevant memories into context to better predict tool quality and choose the right tool for new tasks.<br>
        • TOOLMEM maintains structured capability entries per tool. From each experience, it retrieves similar memories and updates them via a RAG-style merge/refinement, keeping a compact, evolving capability memory. At inference time, it retrieves the most relevant capability memories to guide scoring and tool selection.<br>
        • They evaluate on text generation tools and text-to-image tools, comparing against no-memory and few-shot baselines. TOOLMEM improves quality prediction and makes better tool choices overall. 
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
        • The paper introduces CAM, a Constructivist Agentic Memory system inspired by Jean Piaget’s theory, designed to enhance Large Language Models (LLMs) in long-form document comprehension.<br>
        • CAM features structured schemata, flexible assimilation, and dynamic accommodation, utilizing an incremental overlapping clustering algorithm for efficient memory development and an adaptive Prune-and-Grow strategy for retrieval.<br>
        • Experimental results across diverse benchmarks show that CAM achieves dual advantages in both performance and efficiency compared to existing structured and unstructured memory approaches.
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
          • Proposes Mem-α, a reinforcement learning framework that trains agents to effectively manage complex memory systems (comprising core, episodic, and semantic components) through interaction and feedback.<br>
          • Unlike approaches relying on pre-defined instructions, Mem-α treats memory construction as a sequential decision-making problem, optimizing directly for downstream question-answering accuracy.<br>
          • Experimental results show that Mem-α significantly outperforms existing baselines and demonstrates remarkable generalization, effectively handling contexts exceeding 400k tokens despite being trained on 30k token sequences.
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
        • ReasoningBank, a test-time learning framework that distills an agent’s own successful and failed trajectories into reusable reasoning memories. For new tasks, the agent retrieves relevant memories to guide decision-making and then writes new experience back into the bank, forming a self-improving loop without requiring ground-truth feedback.<br>
        • Each memory is stored as a compact structured item and retrieved via embedding similarity (top-k) to augment the agent’s prompt. After task execution, an LLM-as-a-judge provides proxy success/failure signals: successful trajectories yield transferable strategies, while failed ones yield pitfalls and corrective rules. In addition, MaTTS expands test-time computation through parallel trajectory sampling and serial self-reflection, both of which generate stronger memory signals.<br>
        • Experiments are conducted on WebArena and Mind2Web and SWE-Bench-Verified, comparing against No Memory and prior memory-based baselines. Performance is evaluated using success rate, efficiency (steps), and task-specific metrics. Results show consistent improvements across different backbone models
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
        • Proposes a "pretraining-with-memories" architecture that decouples reasoning capabilities (anchor model) from long-tail world knowledge (hierarchical memory bank).<br>
        • The system dynamically retrieves and attaches context-dependent parameter blocks from a massive memory bank to a small anchor model during inference, enabling efficient scaling.<br>
        • Experiments demonstrate that a 160M model augmented with memories matches the performance of a standard model with over twice the parameters, specifically excelling at long-tail knowledge tasks.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-27</td>
      <td style="width: 55%;"><strong>Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Revisitable%20Memory-purple" alt="Revisitable Memory">
        <img src="https://img.shields.io/badge/Long%20Context-red" alt="Long Context">
        <img src="https://img.shields.io/badge/Recall-success" alt="Recall">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2509.23040">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Addressed long-context reasoning where relevant evidence is dispersed across very long inputs.<br>
        • Proposed a “revisitable” memory design that allows the agent to look back and selectively retrieve from the broader history.<br>
        • Evaluated on long-context QA settings to show improved evidence recovery and reasoning accuracy.
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
          • The "Conflict-Aware Retrieval Enhancement Generation" (CARE) model aims to address the context-memory conflict problem that occurs in Retrieval Enhancement Generation (RAG).<br>
          • CARE optimizes the performance of large language models (LLMs) by introducing context evaluators, especially in dealing with conflicts between external and internal knowledge.<br>
          • This method significantly enhances the accuracy and reliability of the model in multiple tasks through techniques such as conflict-aware fine-tuning, soft prompts, and adversarial soft prompts.
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
          • PRIME is a multi-agent inference framework. PRIME provides intuitive answers to simple questions through fast-response agents.<br>
          • PRIME performs complex reasoning through multiple specific agents, such as memory, planning, search and reading agents.<br>
          • PRIME still needs to improve its belief correction mechanism and optimize the interaction among agents.
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
        • SGMem is a hierarchical memory management framework designed to address memory fragmentation in long-term conversational agents by organizing dialogue into sentence-level graphs.<br>
        • It explicitly models associations across turns, rounds, and sessions, and uses a multi-hop retrieval mechanism to integrate raw dialogue history with generated memory such as summaries, facts, and insights.<br>
        • Extensive experiments on LongMemEval and LoCoMo benchmarks demonstrate that SGMem consistently improves retrieval coherence and outperforms strong baselines in question answering accuracy.
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
        • PRINCIPLES builds a retrievable memory of dialogue strategy principles from offline self-play. At inference time, the model retrieves and applies these principles to guide strategy selection and response generation, without any additional training. <br>
        • In the offline stage, the agent conducts multi-turn self-play with a user simulator and uses rewards to identify success or failure. Successful cases directly yield principles, while failed cases trigger strategy revision and rollback until success; principles are then extracted by contrasting failure-to-success trajectories in a structured form. In the online stage, relevant principles are retrieved using contextual embeddings, reinterpreted to fit the current dialogue, and then used to guide planning and response generation.<br>
        • Experiments on emotional support and persuasion tasks show that PRINCIPLES improves success rates and strategy prediction performance while increasing strategy diversity. Ablation studies confirm the importance of retrieval and reinterpretation, and human evaluations indicate overall preference for the proposed method. 
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
        • Introduces WebWeaver, a dual-agent framework comprising a Planner and a Writer designed to tackle open-ended deep research (OEDR) by emulating human research processes.<br>
        • The Planner uses a dynamic cycle to interleave evidence acquisition with outline optimization, building a memory bank of evidence; the Writer performs hierarchical, citation-grounded retrieval to compose the report section by section.<br>
        • WebWeaver achieves state-of-the-art performance on benchmarks like DeepResearch Bench by effectively managing long contexts and mitigating hallucinations through targeted memory retrieval.
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
          • MOOM is a dual-branch memory extraction framework designed for ultra-long role-playing dialogues, modeling "plot development" and "character portrayal" as core storytelling elements.<br>
          • It incorporates a novel forgetting mechanism based on "competition-inhibition" theory to effectively control memory capacity and prevent uncontrolled expansion.<br>
          • The authors introduce ZH-4O, a large-scale Chinese role-playing dataset with average 600-turn dialogues and manual memory annotations, demonstrating MOOM's superior performance over state-of-the-art methods.
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
        • PREMem (Pre-storage Reasoning for Episodic Memory) is a novel approach that shifts complex reasoning processes from response generation to the memory construction phase.<br>
        • It extracts fine-grained memory fragments (categorized into factual, experiential, and subjective information) and establishes explicit cross-session relationships based on cognitive schema theory, capturing evolution patterns like extensions and transformations.<br>
        • Experiments on LongMemEval and LoCoMo benchmarks show significant performance improvements, enabling smaller models to achieve results comparable to larger baselines while reducing inference computational demands.
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
          • Introduces the “OpenUnlearning” framework, designed to advance research on unlearning in large language models (LLMs).<br>
          • OpenUnlearning integrates a wide range of unlearning algorithms and evaluation methods, streamlining the research workflow for studying forgetting.<br>
          • Through targeted and task-specific evaluations, OpenUnlearning ensures the credibility and robustness of unlearning assessment standards.
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
          • Memory-R1 is an RL-driven framework that empowers LLMs to actively manage and utilize external memory via two specialized agents: a Memory Manager and an Answer Agent.<br>
          • The Memory Manager learns structured operations (ADD, UPDATE, DELETE) to maintain memory, while the Answer Agent filters retrieved memories for accurate reasoning.<br>
          • With only 152 training samples, it outperforms strong baselines on LoCoMo, MSC, and LongMemEval, demonstrating high data efficiency and generalization.
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
          • MemoryVLA is a newly developed robot operation framework, aiming to enhance the performance of robots in complex tasks by integrating visual, language, and perception-cognitive mechanisms.<br>
          • This framework adopts an architecture similar to the human dual memory system, enhancing the robot's ability to handle long-sequence tasks.<br>
          • MemoryVLA introduces perception-cognitive memory banks (PCMB), which can effectively integrate historical information with current decisions, thereby enhancing the success rate of robots in responding to complex scenarios.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-22</td>
      <td style="width: 55%;"><strong>Memento: Fine-tuning LLM Agents without Fine-tuning LLMs</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Tuning-purple" alt="Agent Tuning">
        <img src="https://img.shields.io/badge/No%20LLM%20FT-red" alt="No LLM FT">
        <img src="https://img.shields.io/badge/Adaptation-success" alt="Adaptation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2508.16153">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed a paradigm to improve agent behavior via “agent-side” learning while keeping the base LLM frozen.<br>
        • Focused on adapting the agent’s components (e.g., memory/reasoning/routing) rather than model weights.<br>
        • Reported performance gains across agent tasks without conventional LLM fine-tuning.
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
          • Proposes a Multiple Memory System (MMS) inspired by cognitive psychology to address the issue of low-quality memory content in existing agent memory modules.<br>
          • The system processes short-term memory into diverse fragments—keywords, cognitive perspectives, episodic memory, and semantic memory—to construct specialized retrieval and contextual memory units.<br>
          • Experimental results on the LoCoMo dataset demonstrate that MMS significantly outperforms methods like MemoryBank and A-MEM, particularly in multi-hop reasoning and open-domain tasks.
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
          • Semantic Anchoring is a hybrid agentic memory architecture designed to enhance the long-term context retention of LLMs by enriching vector-based storage with explicit linguistic cues such as syntactic dependencies, discourse relations, and coreference links.<br>
          • The proposed framework employs a multi-stage pipeline involving dependency parsing, coreference resolution, and discourse tagging to construct a hybrid index, allowing retrieval systems to access memories based on both semantic similarity and structural linguistic roles.<br>
          • Experimental results on adapted long-term dialogue datasets (MultiWOZ-Long and DialogRE-L) demonstrate that Semantic Anchoring outperforms strong RAG baselines, improving factual recall and discourse coherence by up to 18% while maintaining higher user satisfaction.
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
        • Memp treats procedural memory as an external, learnable store of past successful experiences so an LLM agent can reuse effective “how-to” routines on new tasks, improving success and reducing wasted steps.<br>
        • Memp follows a Build–Retrieve–Update loop: it builds memory items from trajectories/scripts, retrieves the most relevant items via semantic keys and vector similarity, and updates memory online by adding, filtering, and correcting items so the memory becomes more reliable over time.<br>
        • On TravelPlanner and ALFWorld, Memp outperforms a ReAct baseline with higher success/score and fewer steps; vector-based retrieval beats random selection; online updates yield further gains, and learned memories can transfer from stronger to weaker models with diminishing returns as retrieval size grows.
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
          • "Context-as-memory" significantly enhances the scene consistency and Memory capacity of long video generation by leveraging historical Context as memory.<br>
          • The paper studies key designs such as context learning mechanisms, camera control, and memory retrieval strategies, and points out the balance between computational efficiency and generation quality.<br>
          • Based on the long video generation architecture of the diffusion model, the current technological progress, challenges and future directions are expounded.
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
          • Introduces Intrinsic Memory Agents, a multi-agent framework designed to address context limitations and role inconsistency using structured, agent-specific memories.<br>
          • The method employs role-aligned memory templates and intrinsic updates derived directly from agent outputs, preserving heterogeneous perspectives and domain expertise without external summarization.<br>
          • Evaluations on the PDDL benchmark demonstrate a 38.6% performance improvement with high token efficiency, while case studies show enhanced quality in complex planning tasks.
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
        • RCR-Router is a role-aware context routing framework designed for multi-agent LLM systems to address the limitations of static and full-context routing, such as excessive token consumption and redundant memory exposure.<br>
        • The framework dynamically selects semantically relevant memory subsets for each agent based on their specific role and the current task stage, enforcing a strict token budget and utilizing an iterative feedback mechanism to refine context.<br>
        • Experiments on multi-hop QA benchmarks (HotPotQA, MuSiQue, 2WikiMultihop) demonstrate that RCR-Router reduces token usage by 25–47% while maintaining or improving answer quality compared to baseline strategies.
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
        • Introduces MLP Memory, a lightweight parametric module that learns to internalize retrieval patterns without requiring explicit document access during inference, effectively bridging the gap between RAG and parametric fine-tuning.<br>
        • By pretraining an MLP to imitate a kNN retriever’s behavior on the entire pretraining dataset, the model compresses large datastores into a differentiable memory component that integrates with Transformer decoders via probability interpolation.<br>
        • Experimental results show that MLP Memory achieves superior scaling behavior, improves QA performance by 12.3% relative to baselines, reduces hallucinations by up to 10 points, and offers 2.5× faster inference than RAG.
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
        • The paper proposes MemTool, a short-term memory framework for managing dynamic tool sets across multi-turn conversations. It offers three architectures: Autonomous Agent, Workflow, and Hybrid, balancing autonomy and control.<br>
        • In Autonomous Mode, the agent autonomously adds/removes tools using Search_Tools and Remove_Tools. Workflow Mode follows a fixed pipeline: pruning tools, then searching and adding new ones. Hybrid Mode separates tool removal and adding, offering a balance of stability and flexibility.<br>
        • Using ScaleMCP’s 5,000 MCP servers and a 100-turn dialogue, the authors evaluate 13 LLMs with a 128-tool limit. Autonomous Mode achieves 90-94% tool removal efficiency, while Workflow and Hybrid perform consistently well, with Autonomous and Hybrid excelling in task completion.
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
          • SynapticRAG is a novel memory retrieval framework for large language models (LLMs), designed to enhance memory retrieval in cross-session conversations.<br>
          • By combining temporal association triggers with biologically inspired synaptic propagation mechanisms, SynapticRAG significantly improves the identification of relevant conversational history.<br>
          • Experimental results show that the framework achieves improvements of up to 14.66% across multiple performance metrics and demonstrates clear advantages in dynamic memory management.
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
          • MEM1 is an innovative end-to-end reinforcement learning framework designed to enhance the efficiency of large language models (LLMs) in long-term multi-round interactions.<br>
          • MEM1 effectively solves the problem of memory dilation in context processing of traditional models by constructing a compact shared internal state.<br>
          • The experimental results show that MEM1 significantly improves performance in multiple tasks while reducing memory usage, demonstrating its wide applicability and optimization potential in dynamic environments.
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
          • MemAgent is a long text processing method that uses reinforcement learning (RL) to dynamically update memory, aiming to address the performance degradation and high computational complexity issues of large language models (LLMS) when dealing with long texts.<br>
          • The model can maintain a linear time complexity while handling inputs of infinite length by treating memory as a latent variable and introducing stream processing and multi-session strategies.<br>
          • The experimental results show that MemAgent performs outstandingly with high accuracy in ultra-long text tasks, especially having obvious advantages in complex multi-hop reasoning tasks.
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
        • The paper proposes HippoRAG 2, a “long-term memory–inspired” structured RAG system. It builds a knowledge graph from text and retrieves evidence via graph-based propagation (PPR) to support multi-hop association, while improving basic factual recall that earlier structured RAGs often hurt.<br>
        • Offline, an LLM performs OpenIE to extract triples and form a KG, and adds passages as nodes linked to phrase nodes to fuse concept-level structure with context-rich passages. Online, it first retrieves top-k triples with embeddings, then uses an LLM for triple filtering to remove irrelevant triples; the remaining nodes seed a PPR run to rank the most relevant passages for the generator.<br>
        • It evaluates factual QA, multi-hop reasoning, and narrative understanding, reporting Recall@5 for retrieval and F1 for QA. Compared with BM25, dense retrievers, and multiple structured-RAG baselines, HippoRAG 2 generally improves retrieval and end-to-end QA, and ablations plus “growing-corpus” settings support the contribution of its components.    
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
        • Introduces G-Memory, a hierarchical memory system designed to address the lack of self-evolution capabilities in Large Language Model (LLM)-based Multi-Agent Systems (MAS).<br>
        • Implements a three-tier graph architecture—Insight Graph, Query Graph, and Interaction Graph—to manage lengthy interaction histories by abstracting generalizable insights and condensing specific collaborative trajectories.<br>
        • Experimental results across embodied action and knowledge QA benchmarks demonstrate that G-Memory significantly enhances agent team performance, improving success rates by up to 20.89% without modifying the original frameworks.
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
          • M+ is a memory-augmented model designed to improve long-term information retention in large language models (LLMs).<br>
          • Built upon MemoryLLM, M+ integrates long-term memory mechanisms with a jointly trained retriever, substantially enhancing the model’s ability to handle knowledge spanning over 20,000 tokens while maintaining comparable GPU memory overhead.<br>
          • M+ achieves strong performance across multiple benchmarks, outperforming MemoryLLM and other competitive baselines, and demonstrates efficient information compression and end-to-end training, exhibiting mechanisms that closely resemble human memory.
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
        • MemGuide is a two-stage framework designed to enhance multi-session task-oriented dialogue (TOD) by incorporating task intent and slot-level guidance into memory selection.<br>
        • It employs Intent-Aligned Retrieval to match current context with stored intent descriptions and Missing-Slot Guided Filtering to prioritize memory units that fill information gaps using a Chain-of-Thought reasoner.<br>
        • The authors also introduce MS-TOD, a multi-session TOD benchmark. Evaluations show MemGuide significantly improves task success rates and reduces dialogue turns compared to strong baselines.
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
          • CoMEM addresses the token overload and performance degradation issues in traditional Retrieval-Augmented Generation (RAG) for Vision-Language Models (VLMs) by introducing a general continuous memory mechanism.<br>
          • The method innovatively utilizes the VLM itself as a memory encoder combined with a lightweight Q-Former, efficiently compressing diverse multimodal and multilingual knowledge into a compact set of continuous embeddings.<br>
          • CoMEM is data- and parameter-efficient (requiring only 1.2% trainable parameters) and plug-and-play, significantly enhancing performance on complex multimodal reasoning tasks while keeping the inference model frozen.
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
        • Introduces Limited Memory Language Models (LMLM), a new class of models that externalizes factual knowledge to an external database during pre-training rather than encoding it in parameters.<br>
        • The approach uses a modified pre-training objective that masks retrieved factual values from the loss, encouraging the model to perform targeted lookups for facts instead of memorizing them.<br>
        • Experiments demonstrate that LMLMs match the factual precision of significantly larger models while enabling instant, verifiable knowledge updates and effective machine unlearning through simple database operations.
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
          • Proposes Reflective Memory Management (RMM), a novel framework for long-term dialogue agents that addresses the limitations of rigid memory granularity and fixed retrieval mechanisms.<br>
          • Integrates Prospective Reflection to dynamically organize dialogue history into topic-based memories, and Retrospective Reflection to iteratively refine retrieval using online reinforcement learning guided by LLM attribution signals.<br>
          • Experimental results on MSC and LongMemEval benchmarks demonstrate that RMM significantly outperforms strong baselines, achieving over 10% improvement in accuracy and enhancing response personalization.
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
          • MemoRAG aims to enhance the ability of large language models (LLMs) in handling long contexts by improving the information retrieval and generation process through a global memory-enhanced retrieval mechanism.<br>
          • This framework adopts a lightweight global memory module and a complex generation system, which can effectively manage long contexts and generate useful clues to assist in answer generation.<br>
          • This model is applicable to a variety of tasks, including long document question answering and summarization, demonstrating its potential in handling complex long text scenarios.
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
        • SAGE addresses the long-term memory and multitasking challenges of large language models (LLMs) in dynamic environments through three collaborative agents. SAGE integrates a reflection mechanism and memory optimization based on the Ebbinghaus forgetting curve, helping the model effectively filter and store important information while reducing cognitive load.<br>
        • SAGE continuously optimizes the Assistant’s decisions through an iterative feedback mechanism and reflection functionality. Its MemorySyntax component simulates human memory decay, dynamically managing both short-term and long-term memory to ensure the retention of critical information while reducing unnecessary memory burden.<br>
        • Experiments show that SAGE significantly improves model performance on AgentBench and long-text tasks (e.g., HotpotQA), with performance improvements up to 2.26x in multi-hop question answering and code generation tasks, and it effectively resolves 73.6% of ambiguous references in dialog tasks, demonstrating its potential in real-world applications.
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
        • Introduces ComoRAG, a retrieval-augmented generation framework inspired by the human Prefrontal Cortex, designed to achieve stateful reasoning in long narrative contexts.<br>
        • The framework employs a dynamic memory workspace and a metacognitive regulation loop (including Self-Probe, Mem-Fuse, and Mem-Update) to iteratively fuse fragmented evidence into coherent context.<br>
        • Experimental results demonstrate that ComoRAG consistently outperforms strong baselines on challenging benchmarks like NarrativeQA and ∞BENCH, particularly excelling in complex narrative queries requiring global understanding.
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
        • The paper proposes Dynamic Cheatsheet (DC)—a continuously updated “sticky-note” external memory for black-box LLMs at inference time. It distills verified solving patterns and reuses them across problems, enabling test-time learning without training.<br>
        • DC consists of a Generator (Gen) and a Memory Curator (Cur): Gen produces an answer using the current memory, and Cur then refines/filters/compresses the information. A retrieval-based variant selects the most relevant past examples and solutions by similarity to assist generation, while preventing memory bloat.<br>
        • DC is evaluated across multiple tasks and models (e.g., AIME, GPQA-Diamond, Game of 24, MMLU-Pro; GPT-4o, Claude 3.5 Sonnet, etc.) using metrics such as Soft Match and Functionally Correct. Results show substantial gains; for example, the jump on Game of 24 is largely driven by reusable Python solver code being repeatedly “written and reused” in memory.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-03-27</td>
      <td style="width: 55%;"><strong>MemInsight: Autonomous Memory Augmentation for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Augmentation-purple" alt="Memory Augmentation">
        <img src="https://img.shields.io/badge/Autonomous%20Write-red" alt="Autonomous Write">
        <img src="https://img.shields.io/badge/Retrieval-success" alt="Retrieval">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2503.21760">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed an autonomous memory augmentation pipeline to improve how agents store and later retrieve historical interactions.<br>
        • Emphasized filtering/structuring memory to keep salient information and reduce irrelevant recall.<br>
        • Validated on multiple agent scenarios (e.g., QA / recommendation / summarization) to show improved contextual responses.
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
        • MemQ is proposed to decouple reasoning (natural-language steps) from query generation/execution (SPARQL): the LLM produces a clear reasoning plan, while the actual query is obtained via memory retrieval + rule-based reconstruction, reducing errors and hallucinations caused by entangling tool calls with reasoning.<br>
        • During training, gold SPARQL queries are decomposed into query fragments, and a natural-language explanation is generated for each fragment to build a query memory bank of (explanation → fragment) pairs. At inference time, the LLM generates step-by-step plans; reconstruction uses semantic retrieval (Sentence-BERT) to fetch an adaptive Top-N set of fragments, then assembles them with rules and fills entity slots to produce the final executable query.<br>
        • Experiments on WebQSP and CWQ use Hits@1 and F1, where MemQ achieves the best overall performance. Additional analyses with structural consistency / edge hit rate show the reconstructed queries are closer to the gold graphs, and ablation studies confirm that the main gains come from the memory bank + decoupling design.
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
          • The paper examines machine unlearning in large language models (LLMs) and the importance of its evaluation, with a particular focus on removing undesirable or unnecessary data memories.<br>
          • It introduces Unlearning with Calibration (UWC) to calibrate model performance and strengthen the evaluation of different unlearning methods.<br>
          • The study emphasizes the importance of selecting appropriate evaluation metrics and recommends Extraction Strength (ES) as a primary evaluation tool to ensure accuracy and robustness in assessment.
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
          • LM2 aims to overcome the limitations of traditional Transformers in multi-step reasoning, relational argumentation, and long context processing.<br>
          • The LM2 integrates an auxiliary memory module, which utilizes cross-attention mechanisms and gating technology to enhance information storage and update capabilities.<br>
          • In multiple benchmark tests, LM2 has demonstrated significantly superior performance, particularly excelling in long context reasoning tasks, effectively enhancing the ability to process and remember complex information.
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-03</td>
      <td style="width: 55%;"><strong>TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Temporal%20Reasoning-purple" alt="Temporal Reasoning">
        <img src="https://img.shields.io/badge/Multi--Session%20Dialogue-red" alt="Multi-Session Dialogue">
        <img src="https://img.shields.io/badge/Benchmark-success" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.01630">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Introduced an evaluation task/benchmark targeting temporal reasoning over noisy, multi-session dialogues with memory.<br>
        • Proposed a neuro-symbolic framework (TReMu) to improve temporal reasoning using memory-aware representations.<br>
        • Constructed multi-choice QA style evaluations (augmented from existing dialogue sources) and reported improved performance.
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
          • Introduces SECOM, a memory management method that constructs memory banks at the segment level to address limitations of turn-level and session-level approaches in long-term conversations.<br>
          • SECOM partitions conversations into topically coherent segments and employs prompt compression (LLMLingua-2) as a denoising mechanism to enhance retrieval accuracy.<br>
          • Experimental results demonstrate that SECOM significantly outperforms existing baselines on long-term conversation benchmarks like LOCOMO and Long-MT-Bench+.
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
          • Proposes Alternate Preference Optimization (AltPO), a method designed to effectively address the challenges of machine unlearning in large language models (LLMs).<br>
          • AltPO enhances unlearning by combining negative feedback from the forget set with positive feedback from the same domain to generate multiple alternative responses, thereby improving forgetting capability while preserving overall model performance.<br>
          • Experimental results demonstrate that AltPO outperforms existing methods in terms of both unlearning quality and model utility.
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
          • "Titans" aims to enhance the model's memory capacity when dealing with long sequences and complex contexts.<br>
          • The Titans architecture combines short-term memory and long-term memory modules, overcomes the limitations of traditional recursive models and attention mechanisms, and is capable of handling larger context Windows.<br>
          • The experimental results show that Titans exhibit superior performance and flexibility, especially in handling long dependency relationships and diverse tasks.
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
          • The paper investigates how the structure and retrieval methods of memory modules in large language models (LLMs) affect model performance, with a focus on different memory architectures and their roles in information extraction and generation.<br>
          • The study finds that hybrid memory structures outperform others in complex tasks, demonstrating greater robustness in noisy environments.<br>
          • Through hyperparameter sensitivity analysis, the research identifies memory retrieval strategies that are best suited to different task settings.
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
          • Proposes SELF-PARAM, a method to integrate contexts directly into LLM parameters without requiring extra storage modules, ensuring both high efficacy and long-term retention.<br>
          • Employs a training objective that minimizes the KL divergence between an original model (with context access) and a target model (without context), utilizing diverse generated QA pairs.<br>
          • Experiments demonstrate that SELF-PARAM significantly outperforms existing continual learning and RAG methods in question-answering and conversational recommendation tasks, achieving near-optimal performance with zero storage complexity.
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
          • This study introduces the Sequence Order Recall Task (SORT), designed to evaluate the episodic memory capabilities of large language models (LLMs).<br>
          • The task highlights the importance of episodic memory—linking memories with relevant context such as time and location—particularly in everyday cognitive tasks.<br>
          • Preliminary results indicate that LLMs exhibit strong memory performance when contextual information is provided, but their performance degrades significantly when relying solely on training data.
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
          • ELDER proposes a novel lifelong model editing method using a Mixture-of-LoRA structure to establish continuous associations between data and adapters, enhancing robustness against rephrased inputs.<br>
          • The framework integrates a router network with a guided loss function to align LoRA allocations with edit knowledge and utilizes a deferral mechanism to preserve the model's general capabilities.<br>
          • Extensive experiments on GPT-2 XL and LLaMA2-7B demonstrate that ELDER outperforms existing baselines in reliability, generalization, and scalability while maintaining performance on downstream tasks.
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
        <img src="https://img.shields.io/badge/OpenReview-Paper-1f6feb?logo=openreview" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed MemLong, a memory-augmented retrieval approach for long-context language modeling by fetching historical chunks externally.<br>
        • Combined a retrieval/memory module with a partially trainable decoder-only LM, plus controllable retrieval attention over retrieved chunks.<br>
        • Evaluated on long-context language modeling benchmarks to show improved generation quality and longer effective context.
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
          • This paper introduces the Selective Knowledge Unlearning (SKU) framework, aimed at improving the safety of large language models (LLMs).<br>
          • The SKU framework consists of two main stages: harmful knowledge acquisition, followed by knowledge negation, which focuses on removing undesirable knowledge without degrading model utility under benign prompts.<br>
          • SKU successfully reduces harmful outputs while preserving response quality, and demonstrates a strong balance between unlearning effectiveness and model utility across multiple LLM architectures, such as OPT and LLaMA2.
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
          • RULER is designed for the comprehensive evaluation of long-context language models (LMs) across a wide range of tasks.<br>
          • It extends the traditional Needle-in-a-Haystack (NIAH) test by incorporating tasks such as multi-hop tracking and aggregation, enabling a more thorough assessment of models’ understanding under long-context settings.<br>
          • RULER demonstrates strong performance in multi-hop reasoning and information retrieval tasks.
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
          • ReadAgent is a reading comprehension system designed to improve the performance of large language models (LLMs) when processing long-form text.<br>
          • Through three steps—episodic pagination, memory summarization, and interactive lookup—ReadAgent significantly extends the effective context length by up to 20×.<br>
          • ReadAgent outperforms traditional approaches on long-document reading comprehension benchmarks such as QuALITY, NarrativeQA, and QMSum.
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
          • Introduces E2URec, a recommendation data unlearning method specifically designed for LLM-based recommender systems (LLMRec).<br>
          • E2URec significantly improves unlearning efficiency while preserving recommendation performance by updating only Low-Rank Adaptation (LoRA) parameters.<br>
          • Experimental results show that E2URec outperforms existing baseline methods on real-world datasets.
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
          • Proposes Knowledge Graph Tuning (KGT), a novel approach that personalizes large language models (LLMs) by optimizing external knowledge graphs based on user feedback, without modifying model parameters.<br>
          • KGT extracts personalized factual knowledge triples from user interactions and employs a heuristic optimization algorithm, avoiding the high computational costs and low interpretability of back-propagation methods.<br>
          • Experiments with models like Llama2 and Llama3 demonstrate that KGT significantly enhances personalization performance while reducing latency by up to 84% and GPU memory costs by up to 77%.
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
          • MEMORYLLM is a self-updating large language model designed to effectively integrate new knowledge while maintaining long-term information retention.<br>
          • By embedding a fixed-size memory pool in the latent space of the transformer, MEMORYLLM achieves a seamless combination of model self-updating and knowledge preservation.<br>
          • Key design features include memory tokens that store compressed knowledge, an intelligent self-updating mechanism, and comprehensive evaluations of knowledge integration, retention capability, and robustness.
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
          • HippoRAG is a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory, designed to enable deeper and more efficient knowledge integration for LLMs.<br>
          • By orchestrating LLMs, knowledge graphs, and Personalized PageRank (PPR) to mimic the neocortex and hippocampus, it enables effective single-step multi-hop retrieval.<br>
          • The method outperforms state-of-the-art retrieval-augmented generation (RAG) methods on multi-hop QA tasks by up to 20% and is significantly faster and cheaper than iterative retrieval approaches.
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
          • Identifies an "impossible triangle" in lifelong model editing—reliability, generalization, and locality cannot be simultaneously achieved—attributing this to the gap between long-term and working memory mechanisms.<br>
          • Proposes WISE, a dual parametric memory framework that utilizes a side memory for edits and a router to bridge it with the pretrained main memory, employing knowledge sharding and merging to handle continuous updates.<br>
          • Extensive experiments show that WISE outperforms existing methods in question answering, hallucination correction, and out-of-distribution generalization settings across multiple LLM architectures.
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
          • Proposes the Self-Controlled Memory (SCM) framework to unleash infinite-length input capacity for Large Language Models (LLMs) without requiring modification or fine-tuning.<br>
          • The framework comprises an LLM-based agent, a memory stream for storing historical information, and a memory controller that dynamically manages "Activation Memory" (long-term) and "Flash Memory" (short-term).<br>
          • The authors also contribute a dataset covering long-term dialogues, book summarization, and meeting summarization, demonstrating that SCM achieves superior retrieval recall and response generation compared to baselines.
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
          • Introduces GraphRAG, a graph-based retrieval-augmented generation approach designed to address the limitations of conventional vector RAG in answering global questions about an entire text corpus.<br>
          • The method constructs an entity knowledge graph from source documents, partitions it into hierarchical communities using the Leiden algorithm, and pre-generates summaries to facilitate global sensemaking.<br>
          • By utilizing a map-reduce mechanism over community summaries, GraphRAG significantly outperforms baseline RAG systems in comprehensiveness and diversity for large-scale datasets.
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
          • Introduces the Memory Sharing (MS) framework, which enables multiple LLM-based agents to share Prompt-Answer (PA) pairs as memories in a dynamic, real-time pool.<br>
          • The framework employs a dual-purpose mechanism where newly generated high-quality memories are used to enhance In-Context Learning for agents and simultaneously train the retriever to improve future retrieval relevance.<br>
          • Experimental results across domains like Literary Creation and Logic Problem-solving demonstrate that the MS framework effectively evolves individual intelligence into collective intelligence, significantly improving performance on open-ended questions without explicit fine-tuning.
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
          • Investigates the information recall capabilities of large language models (LLMs), with particular emphasis on their dependence on prompt content and formatting.<br>
          • Using the Needle-in-a-Haystack (NIAH) evaluation, the study finds that recall performance is strongly influenced by training data bias, as well as the content and structure of prompts.<br>
          • The results show that architectural improvements, training strategy adjustments, and fine-tuning can all effectively enhance recall performance.
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
          • Introduces Memory of Amortized Contexts (MAC), an efficient online adaptation framework for large language models (LLMs) designed to address catastrophic forgetting and high computational costs in keeping models up-to-date.<br>
          • MAC utilizes a meta-learned amortization network to compress new documents into compact parameter-efficient finetuning (PEFT) modulations stored in a memory bank, using an aggregation network to retrieve and combine relevant knowledge for specific queries.<br>
          • Experimental results on StreamingQA and SQuAD-Seq demonstrate that MAC significantly outperforms existing online finetuning methods in both adaptation performance and knowledge retention, while offering superior time and memory efficiency.
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
          • MemoryBank is a long-term memory mechanism designed for large language models (LLMs) to address memory limitations in continuous interactions.<br>
          • By enabling models to effectively recall, update, and adapt user memories, MemoryBank enhances contextual understanding and user experience.<br>
          • Experimental results and analyses demonstrate MemoryBank’s effectiveness in improving emotional support and personalized interactions.
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
          • Explores methods for implementing “forgetting” or “unlearning” in large language models (LLMs) to eliminate undesired or misaligned behaviors.<br>
          • By applying a gradient ascent (GA) strategy and introducing a random-output loss, the study demonstrates that unlearning can effectively prevent models from generating harmful responses.<br>
          • Experimental results show that the GA and GA + Mismatch approaches perform particularly well in reducing content leakage rates.
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
          • Proposes a compressed contextual memory approach to improve the memory efficiency and computational performance of online language models when handling extended contexts.<br>
          • By leveraging conditional LoRA integration and parallel computation, the method significantly reduces memory requirements and enables support for effectively unlimited context lengths, surpassing traditional sliding-window strategies.<br>
          • Experimental results demonstrate that, across applications such as multi-task learning and dialogue generation, the approach reduces memory usage by up to 5× while effectively preserving generation quality and accuracy.
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
          • Introduces the Efficient Unlearning (EUL) framework, designed to address the challenges of handling user privacy data in large language models (LLMs).<br>
          • As LLMs are widely deployed, models may inadvertently memorize sensitive information during pretraining, raising significant privacy concerns.<br>
          • EUL enables the effective removal of specific sensitive data from LLMs without full retraining, while preserving overall predictive performance.
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
        • JARVIS-1 is an open-world multi-task agent for Minecraft that generates plans and executes tasks using a multimodal language model (MLM). It can perceive visual information and human instructions, and, by combining multimodal memory, it leverages past experiences to improve future task performance.<br>
        • JARVIS-1 integrates MLM and multimodal memory to generate action plans using visual observations and instructions, which are executed by goal-conditioned controllers. It features a self-improvement mechanism, where it autonomously generates tasks through self-instruction, explores the environment, and accumulates experiences to enhance decision-making abilities.<br>
        • JARVIS-1 excels in over 200 Minecraft tasks, especially in long-term tasks (such as obtaining a diamond pickaxe), outperforming current state-of-the-art models by five times in success rate. As the game progresses, its performance improves through continuous learning and experience accumulation.
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
          • Introduces a novel memory mechanism, Think-in-Memory (TiM), designed to enhance the performance of large language models (LLMs) in long-term human–AI interactions.<br>
          • TiM incorporates an efficient retrieval mechanism based on locality-sensitive hashing, enabling effective memory storage and management over extended interactions.<br>
          • Experimental results show that TiM significantly improves response accuracy and coherence in multi-turn dialogues.
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
          • Introduces <strong>Character-LLM</strong>, a trainable agent framework that teaches LLMs to act as specific characters (e.g., Beethoven) by learning from reconstructed experiences rather than relying solely on prompts.<br>
          • Proposes an <strong>Experience Upload</strong> process involving profile collection, scene extraction, and experience completion to generate high-quality, character-specific training data.<br>
          • Implements <strong>Protective Experiences</strong> to mitigate hallucinations, enabling agents to effectively "forget" or refuse knowledge inconsistent with their character's era or identity.
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
          • Introduces a new framework, LONGMEM, designed to enhance the ability of large language models (LLMs) to process long-form text.<br>
          • LONGMEM employs a decoupled network architecture that combines a frozen LLM memory encoder with an adaptive residual side network, enabling efficient caching and updating of long-term contextual information.<br>
          • By incorporating specialized memory-augmentation layers, a token-based memory retrieval module, and a joint attention mechanism, LONGMEM improves memory retrieval and context utilization, and demonstrates effectiveness across a variety of tasks.
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
        • Proposes MemoChat, an instruction tuning pipeline designed to enable Large Language Models (LLMs) to employ self-composed memos for maintaining consistency in long-range open-domain conversations.<br>
        • The approach utilizes a "memorization-retrieval-response" cycle, teaching LLMs to restructure dialogue history into memos and retrieve relevant evidence for answering current queries.<br>
        • Experiments show that MemoChat outperforms strong baselines on a newly curated, expert-annotated consistency benchmark (MT-Bench+), verifying the efficacy of the memo-equipped inner thinking process.
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
        • RET-LLM is a framework that equips large language models (LLMs) with a dedicated read-write memory unit, enabling them to explicitly extract, store, and recall knowledge from text.<br>
        • Inspired by Davidsonian semantics, the system extracts knowledge in the form of triplets (concept, relationship, concept) and uses a controller to manage interactions between the LLM and the memory module using a text-based API.<br>
        • The memory unit is designed to be scalable, updatable, and interpretable, effectively handling temporal-based question answering tasks where static models often fail.
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
        • Introduces RECURRENTGPT, a language-based simulacrum of the LSTM recurrence mechanism built upon LLMs to generate arbitrarily long texts without forgetting.<br>
        • Utilizes a dual-memory system: a short-term memory updated in the prompt and a long-term memory stored on hard drives retrieved via semantic search.<br>
        • Enables interpretable and interactive text generation ("AI as Contents"), allowing human users to observe and edit natural language memories and plans during the generation process.
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
        • Proposes MPC (Modular Prompted Chatbot), a novel approach using pre-trained LLMs as individual modules (clarifier, memory processor, utterance generator, summarizer) to create high-quality conversational agents without fine-tuning.<br>
        • Utilizes techniques like few-shot prompting, chain-of-thought (CoT), and external memory (using DPR) to achieve long-term consistency and flexibility in open-domain dialogue.<br>
        • Human evaluation results demonstrate that MPC is on par with or superior to fine-tuned models like Blenderbot3 in terms of sensibleness, consistency, and engagingness, particularly in maintaining long-term persona consistency.
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
            • Evaluates the blind spots of large language models in consistently following diverse user preferences under realistic and extremely long-horizon interaction settings.<br>
            • Introduces the RealPref benchmark, covering 100 user profiles and large-scale interaction data, specifically designed to assess generalized understanding of preference expressions ranging from explicit to implicit.<br>
            • Quantitatively demonstrates that increasingly implicit preference expression and excessively long contexts can cause cliff-like drops in LLM preference-following performance, thereby identifying a key bottleneck in the development of personalized perceptive assistants.
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
            • The evolution of long-term personal assistants requires models to perform complex reasoning based on non-declarative memory, such as inferring habits from digital traces, yet existing benchmarks offer virtually no coverage of this capability.<br>
            • Introduces the LifeBench benchmark, which leverages real-world priors and hierarchical structures from cognitive science to simulate densely distributed multi-source events spanning long time horizons, in order to evaluate agents' integrative reasoning abilities.<br>
            • Even state-of-the-art memory systems achieve only slightly above 50% accuracy (55.2%) on this benchmark, highlighting the extreme difficulty of long-horizon reasoning over fragmented digital traces.
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
            • Static offline evaluation data cannot faithfully capture the scalability and reliability of memory management strategies in dynamic, long-horizon interactions.<br>
            • Builds AMemGym, an interactive environment that supports online policy evaluation, using structured sampling to generate high-fidelity user profiles and state-evolution trajectories at low cost.<br>
            • The dynamic environment objectively reveals the long-horizon performance degradation of existing systems such as RAG, and validates the framework’s effectiveness in driving self-evolution of memory strategies.
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
            • Traditional benchmarks are mostly based on single-text dialogue histories and therefore cannot effectively evaluate agents' personalized referential reasoning ability in real-life, multimodal, and long-horizon settings.<br>
            • Introduces ATM-Bench, a multimodal and multi-source benchmark built from four years of private data, and proposes schema-guided memory for structured representation of heterogeneous data.<br>
            • Reveals the performance limitations of existing systems on complex real-world experience collections, and shows that structured SGM outperforms traditional descriptive methods in multi-source scenarios.
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
            • Existing evaluations of memory systems focus primarily on factual recall, while lacking measurement of how effectively emotional information is handled in long-horizon interactions.<br>
            • Introduces the first emotion-enhanced evaluation benchmark and the HLME dataset, covering three dimensions: emotional information extraction, emotional memory updating, and emotion-aware question answering.<br>
            • Experiments reveal significant instability across current state-of-the-art memory systems on emotion-related tasks, pointing the way toward future optimization of emotional coherence.
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
            • Introduces MemoryArena, a unified evaluation platform for benchmarking agent memory in multi-session tasks.<br>
            • The benchmark covers tasks such as web navigation, planning, information search, and reasoning, requiring agents to continuously learn and utilize memory during execution.<br>
            • The study reveals limitations of existing long-context memory benchmarks in evaluating real-world interactive scenarios and emphasizes the necessity of jointly evaluating memory and action.
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
            • Introduces AgentLAB, the first benchmark specifically designed to evaluate the vulnerability of LLM agents to adaptive long-horizon attacks.<br>
            • Supports five novel attack types, including memory poisoning, spanning 28 real-world agent environments and 644 security test cases.<br>
            • Experimental findings reveal that LLM agents are extremely vulnerable under long-term attacks, and that existing single-interaction defense mechanisms are insufficient to effectively address such complex security threats.
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
        • It introduces the LoCoMo-Plus benchmark to evaluate "cognitive memory" in LLM agents, focusing on their ability to retain and apply implicit constraints like user goals and values across long conversational contexts.<br>
        • It constructs scenarios with "cue–trigger semantic disconnect," requiring models to apply latent information even when downstream queries lack surface-level similarity to the original memory cues.<br>
        • It establishes an evaluation framework based on "constraint consistency," revealing through extensive experiments that current LLMs and memory systems struggle significantly with complex cognitive memory tasks.
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
        • Proposed AgentLongBench, evaluating long-context agents via simulated environment rollouts with context lengths ranging from 32K to 4M tokens.<br>
        • Constructed dynamic interaction trajectories based on Lateral Thinking Puzzles, featuring both Knowledge-Intensive and Knowledge-Free settings.<br>
        • Revealed that high information density in tool responses poses a greater challenge than memory fragmentation, identifying "minimum token requirement" as a key factor.
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
        • Proposed MemoryRewardBench, the first benchmark to systematically evaluate the ability of Reward Models (RMs) to assess long-term memory management.<br>
        • Covers 10 settings across reasoning, dialogue, and generation tasks with contexts from 8K to 128K tokens.<br>
        • Designed Outcome-based and Process-based evaluation criteria, revealing a generational advantage in newer models for evaluating memory capabilities.
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
        • Proposed the problem of Rational Personalization and introduced the RPEval benchmark to evaluate appropriate user preference utilization.<br>
        • Included a dataset for intent reasoning and a multi-granularity evaluation protocol, revealing widespread "irrational personalization" (e.g., Filter Bubbles).<br>
        • Proposed RP-Reasoner, a pragmatics-based mechanism to infer latent user intent and selectively integrate personalized information, reducing errors significantly.
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
        • Proposed Mem2ActBench to evaluate agents' ability to actively leverage long-term memory for executing tool-based tasks, beyond passive retrieval.<br>
        • Constructed a dataset of 2,029 sessions via automation and reverse-generated 400 memory-dependent tool-use tasks.<br>
        • Experiments revealed that existing systems struggle with "Parameter Grounding," failing to extract correct parameters from memory for tool execution.
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
        • Introduces CLONEMEM, a benchmark designed to evaluate long-term memory in AI Clones by utilizing non-conversational digital traces (e.g., diaries, social media, emails) spanning 1–3 years, rather than traditional conversational history.<br>
        • Proposes a hierarchical data construction framework that generates coherent longitudinal life trajectories, capturing the evolution of an individual's experiences, emotions, and opinions over time.<br>
        • Experimental results reveal that existing memory systems (such as A-Mem and Mem0) struggle with this setting, often underperforming compared to flat retrieval and failing to accurately track internal state changes due to lossy compression and reliance on narrative templates.
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
          • RealMem is a benchmark designed to evaluate LLMs in "long-term project-oriented" interactions, distinguishing itself from casual or task-oriented dialogue benchmarks by focusing on evolving goals and dynamic states.<br>
          • The framework employs a three-stage synthesis pipeline (Project Foundation, Multi-Agent Generation, Memory Management) to create over 2,000 cross-session dialogues across 11 realistic scenarios.<br>
          • Evaluations indicate that current state-of-the-art memory systems struggle with managing long-term project states, temporal reasoning, and proactive alignment, highlighting a critical gap in autonomous agent capabilities.
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
          • <strong>Introduction:</strong> Introduces KnowMe-Bench, a benchmark derived from long-form autobiographical narratives (4.7M tokens) designed to evaluate "person understanding"—inferring stable motivations and principles—in lifelong digital companions, moving beyond simple fact retrieval.<br>
          • <strong>Methodology:</strong> Utilizes a "Cognitive-Stream Reconstruction" pipeline to transform raw narratives into flashback-aware, time-anchored streams rich in inner thoughts and sensory details. It employs a 3-tier hierarchical evaluation suite ranging from factual extraction to psychoanalytic depth.<br>
          • <strong>Findings:</strong> Experiments with various memory architectures (RAG, Mem0, MemOS) reveal that while retrieval systems improve factual accuracy, they struggle with temporal grounding and deep reasoning (e.g., the "Update Paradox"), highlighting a critical gap in modeling the complex, non-linear nature of human memory.
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
          • <strong>Introduction:</strong> Introduces <strong>Mem-Gallery</strong>, a benchmark designed to evaluate multimodal long-term conversational memory in MLLM agents, bridging the gap between text-only long-context benchmarks and single-session multimodal tasks.<br>
          • <strong>Methodology:</strong> Constructs a dataset of high-quality multi-session conversations grounded in both visual and textual information. It establishes an evaluation framework covering three functional dimensions: Memory Extraction & Adaptation, Memory Reasoning, and Memory Knowledge Management.<br>
          • <strong>Findings:</strong> Extensive benchmarking across thirteen memory systems reveals that explicit multimodal information retention is crucial. However, current models struggle with memory reasoning, handling knowledge conflicts, and face significant efficiency bottlenecks.
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
          • <strong>Introduction:</strong> Introduces EvolMem, a cognitive-driven benchmark designed to evaluate the multi-session memory capabilities of LLMs and agent systems, addressing the gap in assessing non-declarative memory and long-term consistency.<br>
          • <strong>Methodology:</strong> Grounded in cognitive psychology, it categorizes memory into declarative (e.g., Retrieval, Inference) and non-declarative (e.g., Habituation) types. The benchmark uses a hybrid data synthesis framework—combining topic-initiated generation and narrative-inspired transformations—to create diverse, controllable multi-session dialogues.<br>
          • <strong>Findings:</strong> Evaluations reveal that no LLM consistently excels across all memory dimensions, with significant weaknesses in non-declarative tasks. Furthermore, existing agent memory mechanisms often fail to outperform strong base models and suffer from high latency.
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
          • Introduction: Introduces PersonaMem-v2, a state-of-the-art dataset featuring 1,000 realistic personas, 300+ scenarios, and 20,000+ implicit user preferences embedded in long-context interactions (up to 128k tokens).<br>
          • Gap & Findings: Benchmarking reveals that frontier LLMs (including GPT-5) struggle with implicit personalization, achieving only 37-48% accuracy. However, Reinforcement Fine-Tuning (RFT) significantly improves reasoning capabilities for user understanding.<br>
          • Methodology: Proposes an "Agentic Memory" framework that maintains a single, human-readable, and evolving memory. This approach outperforms GPT-5 with 55% accuracy while being 16× more token-efficient (using 2k memory vs. 32k history).
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
          • Introduces the IMPLEXCONV dataset and the TACITREE framework for studying implicit reasoning in personalized dialogue.<br>
          • IMPLEXCONV consists of 2,500 examples focused on implicit reasoning scenarios, capturing subtle syntactic and semantic relationships within conversations.<br>
          • TACITREE enhances large language models (LLMs)’ ability to perform implicit contextual reasoning in long dialogues by hierarchically organizing dialogue history.
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
          • Introduces the PERSONAMEM benchmark, designed to evaluate the performance of large language models (LLMs) in dynamic user profiling and personalized response generation.<br>
          • Although existing models achieve some success in recalling user preferences, they still exhibit significant performance gaps when handling novel scenarios.<br>
          • The paper provides a detailed description of the benchmark’s structure, the process for generating user dialogues, the methods for evaluating model performance, and related work, highlighting the importance of personalized dialogue generation in enhancing user experience.
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
        • EM-LLM (Event Memory Large Language Model) is a novel large language model designed to address the limitations of existing models in handling long contexts.<br>
        • EM-LLM achieves near-unlimited context processing without fine-tuning, delivering significant improvements over existing models across multiple benchmarks.<br>
        • The model integrates surprise-based event segmentation, graph-theoretic boundary refinement, and a two-stage memory retrieval mechanism, substantially enhancing performance on information retrieval and question-answering tasks.
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
          • MemoryAgentBench is a benchmark designed to evaluate four core capabilities of language models with memory mechanisms (Memory Agents): accurate retrieval, test-time learning, long-range understanding, and conflict resolution.<br>
          • By integrating existing datasets with newly constructed data, MemoryAgentBench enables a systematic evaluation of these capabilities.<br>
          • The benchmark reveals limitations of current approaches in memory updating and long-horizon dialogue processing, highlighting key challenges for future research.
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
        • MiniLongBench is a low-cost long-text understanding benchmark designed to improve the efficiency and affordability of evaluating large language models (LLMs) on long-context understanding (LCU).<br>
        • By applying data compression techniques, MiniLongBench significantly reduces the number of evaluation samples while maintaining evaluation consistency, and shows a high correlation with results from the original LongBench benchmark.<br>
        • Evaluations across multiple task categories demonstrate MiniLongBench’s effectiveness, although further improvements are still needed for summarization and synthesis tasks.
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
          • PersonaBench is a benchmark designed to evaluate AI models’ ability to understand personal information.<br>
          • The paper highlights the importance of personalization in AI assistants and emphasizes the challenge posed by the lack of publicly available datasets for assessing such capabilities.<br>
          • The evaluation primarily focuses on retrieval-augmented generation (RAG) models, with results indicating that current models still struggle to effectively handle personal queries.
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
          • MemBench is designed to comprehensively evaluate the memory capabilities of LLM-based agents.<br>
          • By constructing datasets that cover both factual memory and reflective memory, the study addresses limitations of existing evaluation approaches.<br>
          • The paper provides a detailed description of memory mechanism construction—including user relationship graphs and multi-layer memory designs—and emphasizes the importance of evaluation metrics such as accuracy, efficiency, and capacity.
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
          • This paper investigates the memory capabilities of large language models (LLMs) in long-term tasks, with a particular focus on dialogue systems.<br>
          • By constructing the Long-Order Chronological Conversation (LOCCO) dataset, the study provides a quantitative evaluation of LLMs’ long-term memory performance.<br>
          • Experimental results show that while LLMs can retain historical conversational information to some extent, their memory gradually degrades over time.
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
          • Introduces a user simulation framework, the Implicit User Profile User Simulator (USP), designed to enhance interactions between dialogue systems and human users by inferring implicit user attributes.<br>
          • USP extracts implicit features from user dialogues and combines conditionally supervised fine-tuning with reinforcement learning under cycle consistency, improving the realism and coherence of generated conversations.<br>
          • Experimental results show that USP achieves significant advantages across multiple metrics, particularly when compared with other dialogue generation models such as GPT-4o and PlatoLM.
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
          • Investigates privacy vulnerabilities in LLM agent memory, specifically the risk of extracting private user-agent interactions stored in long-term memory.<br>
          • Proposes the Memory EXTRaction Attack (MEXTRA), a black-box attack leveraging a novel prompt design (Locator + Aligner) and automated prompt generation to extract sensitive user queries.<br>
          • Experiments on representative agents (EHRAgent and RAP) demonstrate significant vulnerability, analyzing key factors like similarity scoring functions and memory configurations that influence leakage.
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
          • Proposes the PersonaFeedback benchmark for evaluating large language models (LLMs) in personalized response generation.<br>
          • The study shows that while LLMs have made progress in producing personalized content, they still face limitations in complex scenarios.<br>
          • By leveraging dynamic user attribute inference, personalized profiles, and reward models, the researchers aim to improve the effectiveness of personalized question answering.
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
          • Minerva is a programmable memory testing benchmark designed to evaluate large language models (LLMs) across diverse memory tasks.<br>
          • It quantitatively assesses models’ ability to use memory, with a particular focus on tasks such as information retrieval, reasoning, and state tracking.<br>
          • Experimental results indicate that while some models perform well on simple tasks, there remain substantial gaps on more complex tasks.
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
        • The Agentic Long-Context Understanding (AgenticLU) framework is designed to enhance large language models (LLMs) in long-text understanding and reasoning.<br>
        • AgenticLU introduces a Chain-of-Clarifications (CoC) mechanism that optimizes the model’s self-clarification process and employs tree-structured search paths to generate clarification questions, thereby significantly improving the accuracy and effectiveness of multi-step reasoning.<br>
        • Evaluation results show that the framework outperforms existing prompting techniques on long-context question answering, while keeping computational overhead well controlled.
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
        • The paper investigates the challenges LLM-powered embodied agents face in personalized assistance, specifically focusing on memory utilization for object semantics and user behavioral patterns.<br>
        • It introduces MEMENTO, a two-stage evaluation framework, which reveals that current agents struggle with sequential user patterns and coordinating multiple memories due to information overload.<br>
        • The study proposes a hierarchical knowledge graph-based user-profile memory module that separates personalized knowledge from episodic history, achieving substantial improvements in both single and joint-memory tasks.
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
        • SCBENCH (Shared Context BENCH) is a benchmark specifically designed to evaluate long-context large language models (LLMs).<br>
        • SCBENCH focuses on the lifecycle of key–value (KV) caches, covering generation, compression, retrieval, and loading, and aims to fill a gap in existing benchmarks regarding KV cache evaluation in multi-turn interactions.<br>
        • Experimental results reveal substantial differences across methods on different tasks, and show that dynamic sparse attention and cache optimization strategies deliver superior performance in complex scenarios.
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
        • The paper introduces LONGMEMEVAL, a comprehensive benchmark for evaluating the long-term memory capabilities of chat assistants.<br>
        • The benchmark assesses five core memory abilities, capturing key challenges faced by existing systems.<br>
        • LONGMEMEVAL adopts a unified three-stage framework—indexing, retrieval, and reading—and proposes several design optimizations to improve memory recall and question-answering accuracy.
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
        • Explores machine unlearning in large language models (LLMs) and the importance of its evaluation, with a particular focus on eliminating unnecessary data memorization.<br>
        • The study addresses two key challenges: the robustness of evaluation metrics and the trade-off between removing target knowledge and preserving other knowledge.<br>
        • It recommends Extraction Strength (ES) as a primary evaluation metric to ensure accuracy and robustness in unlearning assessment.
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
        • PREFEVAL is a benchmark designed to evaluate large language models (LLMs) in their ability to infer, remember, and follow user preferences over long conversations.<br>
        • The benchmark includes 3,000 user preference–query pairs spanning 20 topics, revealing significant challenges for current LLMs in adhering to user preferences.<br>
        • The study shows that explicit preferences are easier for models to infer than implicit preferences, and that task types and preference expression styles have a substantial impact on model performance.
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
        • Explores the importance of episodic memory in large language models (LLMs) and proposes the construction of new benchmarks to evaluate models’ reasoning capabilities.<br>
        • The authors develop a comprehensive framework with newly designed tasks and evaluation protocols, emphasizing the need for novel training strategies to effectively integrate episodic memory.<br>
        • The framework provides a promising solution for evaluating episodic memory in LLMs.
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
        • LongGenBench is a benchmark designed to evaluate large language models (LLMs) in generating high-quality long-form text, with a particular emphasis on following complex instructions.<br>
        • Unlike existing benchmarks, LongGenBench focuses specifically on long-text generation scenarios, covering tasks such as diary writing and menu design.<br>
        • Despite strong performance on other evaluations, LLMs face significant challenges on the LongGenBench benchmark.
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
        • LongBench v2 is a multi-task benchmark for evaluating large language models (LLMs) in long-context understanding and reasoning.<br>
        • It consists of 503 multiple-choice questions spanning diverse task types, with a focus on comprehending and answering long-form text.<br>
        • The study finds that the best-performing models surpass human experts in long-context tasks, highlighting the importance of enhanced reasoning and increased test-time computation.
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
        • MT-Eval is a benchmark designed to evaluate the performance of large language models (LLMs) in multi-turn conversations.<br>
        • While existing evaluations primarily focus on single-turn dialogue, MT-Eval fills this gap by constructing 1,170 multi-turn queries.<br>
        • The benchmark categorizes interaction patterns into recall, expansion, refinement, and follow-up, revealing that most models perform consistently worse in multi-turn settings than in single-turn scenarios.
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
        • LongGenBench is a newly proposed long-context generation benchmark designed to evaluate the performance of large language models (LLMs) on long-form text generation tasks.<br>
        • It complements existing benchmarks that primarily focus on retrieval skills by emphasizing coherence and logical consistency across multiple sub-questions.<br>
        • The study shows that different models exhibit substantial performance disparities in long-text generation.
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
        • MADial-Bench is a benchmark for evaluating memory-augmented dialogue generation, targeting the limitations of current dialogue systems in long-term memory.<br>
        • MADial-Bench incorporates concepts from cognitive science to assess memory retrieval and recognition, and introduces multi-dimensional evaluation metrics.<br>
        • The study shows that while large language models (LLMs) perform well in emotional support, their memory recognition and injection capabilities still require improvement.
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
        • L-CiteEval is a multi-task evaluation benchmark for long-context models (LCMs), designed to measure their abilities in understanding and citation.<br>
        • The benchmark covers 11 tasks, supports context lengths ranging from 8K to 48K, and provides a comprehensive evaluation framework.<br>
        • The study shows that closed-source models outperform open-source models in citation quality and generation accuracy, while retrieval-augmented generation (RAG) techniques effectively improve citation quality.
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
        • PerLTQA is a question-answering dataset designed to enhance long-term memory integration in dialogue systems.<br>
        • PerLTQA combines semantic memory and episodic memory, containing 8,593 questions across 30 personas, with the goal of improving memory classification, retrieval, and synthesis.<br>
        • Experiments show that BERT-based models outperform other large language models in memory classification tasks.
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
        • Explores the capabilities and limitations of large language models (LLMs) in long-text processing, and introduces the GLE benchmark for evaluating LLMs’ performance in long-context understanding.<br>
        • The paper describes the construction process and evaluation criteria of long-dependency question-answering tasks, and compares the performance of different models.<br>
        • Experimental results show that the GLE benchmark effectively assesses LLMs’ ability to process long-form text.
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
        • Evaluates the memory capabilities of large language models (LLMs) in long-duration conversations, with a particular focus on multimodal dialogue scenarios.<br>
        • By developing the LOCOMO dataset, the researchers establish a comprehensive evaluation benchmark covering tasks such as question answering, event summarization, and multimodal dialogue generation.<br>
        • Experimental results indicate that while some LLMs perform strongly, they still lag significantly behind humans in memory and reasoning, and the study outlines an evaluation framework and directions for future improvements.
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
        • Explores the importance of large language models (LLMs) in personalized response generation and introduces LaMP, a new benchmark specifically designed for training and evaluating personalized text generation and classification tasks.<br>
        • LaMP comprises seven personalized subtasks, highlighting the effectiveness of leveraging user-specific inputs (e.g., historical data) and retrieval-augmented strategies to enhance language model performance.<br>
        • Experimental results demonstrate that personalization methods significantly improve model performance, with the best results achieved through fine-tuning and the use of appropriate retrieval strategies.
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
        • LongBench is a bilingual, multi-task benchmark designed to evaluate large language models (LLMs) on long-context understanding.<br>
        • The benchmark comprises 21 datasets spanning six task categories: single-document QA, multi-document QA, summarization, few-shot learning, synthetic tasks, and code completion, with an average length of 6,711 words and 13,386 characters.<br>
        • Experimental results show that commercial models (e.g., GPT-3.5-Turbo-16k) generally outperform open-source models on long-context tasks.
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
        • HOMER (Hierarchical cOntext MERging) is an algorithm designed to address the limitations of large language models (LLMs) in handling long contexts.<br>
        • By splitting long inputs into smaller chunks and hierarchically merging them, HOMER improves both memory efficiency and reasoning capability when processing long-form text.<br>
        • Experimental results show that HOMER delivers strong performance with 32K and 64K context inputs, maintaining low perplexity and reduced memory consumption.
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
              • Critiques the limitations of treating memory as a short-term utility module, aiming to address the crisis of identity continuity across successive generations of AI models.<br>
              • Establishes the philosophical and system-level paradigm of memory as ontology, and designs a constitutional memory architecture featuring four layers of governance hierarchy and multi-layer semantic storage.<br>
              • This architecture demotes the underlying computational model to a replaceable substrate, prioritizing the persistence of identity and governance for digital entities, and providing a foundational infrastructure for the next generation of digital citizens.
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
              • Existing approaches that handle long-context window limitations through truncation or summarization are prone to losing critical interaction evidence.<br>
              • Proposes Memex, an indexed experience memory mechanism for lossless compression, and introduces the MemexRL reinforcement learning framework to optimize agents' read-write archiving strategies.<br>
              • The system enables agents to autonomously decide when to archive and retrieve information, substantially improving long-horizon task success rates while significantly compressing the working context.
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
            • Proposes the MPA agent, which leverages episodic memory of past reasoning trajectories to guide decision-making against both recurring and novel phishing threats.<br>
            • Achieves a 13.6% improvement in recall over state-of-the-art baselines on public datasets, with gains of up to 20% in real-world scenarios.<br>
            • Analysis shows that episodic memory contributes approximately 27% of the recall improvement without introducing additional computational overhead.
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
            • Proposes the Multimodal Memory Agent (MMA), which addresses overconfidence errors in RAG by assigning dynamic reliability scores to retrieved items, incorporating source credibility, temporal decay, and conflict awareness.<br>
            • Introduces the MMA-Bench benchmark to control speaker reliability and evaluate belief dynamics under text–vision contradictions.<br>
            • Reveals the “visual reassurance effect,” where agents tend to inherit latent visual biases from the underlying models.
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
        • It proposes the M2A framework, which utilizes collaborative agents (ChatAgent and MemoryManager) to transform static multimodal personalization into a co-evolving memory mechanism that updates during interactions.<br>
        • It introduces a dual-layer hybrid memory architecture linking raw message logs with high-level semantic observations via evidence IDs, employing tri-path retrieval to ensure precise and efficient context recall.<br>
        • It develops a scalable multimodal data synthesis pipeline for long conversations, with experiments demonstrating that M2A significantly outperforms existing RAG and text-only memory baselines in personalized reasoning.
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
        • Investigated memory mechanisms in Transformer attention layers drawing on the "Encoding Specificity Principle" from psychology.<br>
        • Proposed that Q encodes retrieval context, K indexes memory traces, and V stores content, identifying that contextual cues are encoded as keywords.<br>
        • Identified specific attention neurons whose activations facilitate keyword retrieval, providing a theoretical basis and extraction method for downstream tasks like unlearning.
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
        • Proposed S3-Attention (Sparse & Semantic Streaming Attention), achieving O(1) GPU memory for long-context inference.<br>
        • Uses Sparse Autoencoders (SAE) to decode attention states into sparse features, building a CPU-based inverted index and discarding the KV cache.<br>
        • Retained near-full-context performance (e.g., 99.4% on Llama-3-8B) on LongBench via endogenous retrieval based on feature co-activation.
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
        • Proposed LLM-as-RNN, an inference-only framework converting frozen LLMs into recurrent predictors to address immutable context history.<br>
        • Represents the hidden state as a natural language memory (structured system prompt) updated via feedback-driven text rewriting at each step.<br>
        • Significantly outperformed Zero-shot and MemPrompt baselines in healthcare, meteorology, and finance time-series tasks under fixed token budgets.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Introduced a continuum-style memory architecture to support long-horizon agent behavior beyond a single context window.<br>
        • Described how different memory stores (e.g., working/episodic/semantic) interact over time for planning and recall.<br>
        • Provided empirical evidence that architectural choices improve long-horizon task stability and retrieval quality.
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
        • Memory Bear constructs a human-like memory architecture grounded in cognitive science (ACT-R, Ebbinghaus), distinguishing between explicit and implicit memory to achieve a leap from "memory" to "cognition."<br>
        • It features a three-layer architecture with an Intelligent Semantic Pruning Algorithm and a Self-Reflection Engine, significantly reducing token consumption (~90%) while actively suppressing hallucinations.<br>
        • Experiments demonstrate it outperforms Mem0 and MemGPT in accuracy and latency, with validated effectiveness in healthcare (chronic disease management), enterprise operations, and personalized education.
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
        • O-Mem is a novel memory framework based on active user profiling that dynamically extracts and updates user characteristics and event records from proactive interactions.<br>
        • Unlike systems relying on semantic grouping, O-Mem supports hierarchical retrieval of persona attributes and topic-related context to enable adaptive and coherent personalized responses.<br>
        • The system achieves state-of-the-art performance on LoCoMo and PERSONAMEM benchmarks while significantly improving token efficiency and interaction response time compared to previous frameworks like LangMem and MemoryOS.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-21</td>
      <td style="width: 55%;"><strong>Episodic Memory in Agentic Frameworks: Suggesting Next Steps in Workflow Creation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Workflow%20Memory-purple" alt="Workflow Memory">
        <img src="https://img.shields.io/badge/Next--Step%20Suggestion-red" alt="Next-Step Suggestion">
        <img src="https://img.shields.io/badge/Episodic-success" alt="Episodic">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.17775">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Proposed an episodic memory store for workflow traces, enabling retrieval of similar historical workflows.<br>
        • Used retrieved workflow episodes to suggest plausible “next steps” during workflow creation, reducing hallucination pressure on the LLM.<br>
        • Evaluated next-step recommendation quality in agentic workflow settings.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-11</td>
      <td style="width: 55%;"><strong>From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Graph%20Memory-purple" alt="Graph Memory">
        <img src="https://img.shields.io/badge/Trainable%20Module-red" alt="Trainable Module">
        <img src="https://img.shields.io/badge/Strategy%20Learning-success" alt="Strategy Learning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.07800">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Introduced a trainable graph-structured memory to store experiences and support strategy formation over time.<br>
        • Learned how to weight/route experiences in the memory graph to inform future decisions and planning.<br>
        • Reported improvements on agent tasks requiring multi-step reuse of prior experience.
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
        • LightMem is a lightweight memory architecture inspired by the Atkinson-Shiffrin human memory model, designed to balance performance and efficiency in LLMs.<br>
        • It features a three-stage process: cognition-inspired sensory memory for filtering redundancy, topic-aware short-term memory for structured access, and long-term memory with sleep-time updates to decouple maintenance from inference.<br>
        • Experimental results on LongMemEval and LoCoMo show LightMem outperforms strong baselines in accuracy while reducing token usage by up to 100× and API calls significantly.
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
        • Introduces M3-Agent, a novel multimodal agent framework that mimics human memory by processing continuous visual and auditory inputs to build entity-centric episodic and semantic long-term memories.<br>
        • Proposes M3-Bench, a comprehensive long-video question answering benchmark comprising 1,020 videos from robot and web perspectives, designed to evaluate capabilities like person understanding and cross-modal reasoning.<br>
        • Experimental results demonstrate that M3-Agent, trained via reinforcement learning, significantly outperforms strong baselines such as Gemini-1.5-Pro and GPT-4o in memory retention and reasoning tasks.
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
        • A-Mem introduces a Zettelkasten-inspired dynamic memory organization that equips LLM agents with genuine long-term memory.<br>
        • Beyond simple storage, A-Mem enables self-linking and self-evolution, allowing agents to achieve significant advantages in complex reasoning tasks.<br>
        • Experimental results demonstrate that A-Mem outperforms existing methods in performance, efficiency, and scalability, laying a strong foundation for building more intelligent and autonomous LLM agents.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-01</td>
      <td style="width: 55%;"><strong>Improving Code Localization with Repository Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Repository%20Memory-purple" alt="Repository Memory">
        <img src="https://img.shields.io/badge/Code%20Localization-red" alt="Code Localization">
        <img src="https://img.shields.io/badge/SWE--bench-success" alt="SWE-bench">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2510.01003">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Modeled long-term “repository memory” from commit history, linked issues, and evolving code regions.<br>
        • Added tools to retrieve historical changes and summarize active code areas to support localization decisions.<br>
        • Demonstrated improved localization performance for software engineering agents on SWE-bench-style benchmarks.
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
        • Livia is an emotion-aware AR companion designed to combat loneliness through a modular multi-agent architecture and immersive augmented reality interactions.<br>
        • It introduces two novel memory compression algorithms—Temporal Binary Compression (TBC) and Dynamic Importance Memory Filter (DIMF)—to efficiently manage long-term memory while retaining emotionally significant context.<br>
        • The system integrates multimodal emotion recognition (text and voice) and an adaptive personality model, demonstrating high accuracy and fostering deeper emotional bonds with users.
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
        • Nemori is a self-organizing memory architecture inspired by cognitive science, designed to address the limitations of Large Language Models in long-term interactions by enabling persistent, adaptive memory.<br>
        • It introduces the Two-Step Alignment Principle for autonomous episode segmentation and the Predict-Calibrate Principle for proactive knowledge distillation, moving beyond passive storage to active learning.<br>
        • Experimental results on LoCoMo and LongMemEval benchmarks show that Nemori significantly outperforms state-of-the-art systems while using 88% fewer tokens than full-context baselines.
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
        • Proposes H-MEM, a hierarchical memory architecture that organizes memory into four semantic levels with positional index encoding, enabling efficient layer-by-layer retrieval without exhaustive similarity computation.<br>
        • Introduces a dynamic memory update mechanism that adjusts memory weights based on user feedback to reflect changing user interests and psychological states.<br>
        • Experimental results on the LoCoMo dataset demonstrate that H-MEM consistently outperforms baselines in long-term dialogue tasks while significantly reducing computational cost and retrieval latency.
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
        • MIRIX is a modular, multi-agent memory system that addresses the limitations of flat memory architectures by integrating six specialized memory components—including Episodic, Semantic, and Procedural memory—managed by dedicated agents.<br>
        • The framework introduces an "Active Retrieval" mechanism and a Meta Memory Manager to dynamically coordinate memory updates and retrieval, and validates these capabilities on a newly introduced multimodal benchmark, ScreenshotVQA, consisting of high-resolution user activity logs.<br>
        • Experimental results show that MIRIX outperforms RAG baselines by 35% in accuracy on ScreenshotVQA while reducing storage by 99.9%, and achieves state-of-the-art performance on the LOCOMO long-form conversation benchmark.
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
        • Introduces Ella, an embodied social agent equipped with a structured long-term multimodal memory system comprising name-centric semantic memory and spatiotemporal episodic memory.<br>
        • By integrating this lifelong memory system with foundation models, Ella can retrieve relevant information for decision-making, plan daily activities, and build social relationships in a 3D open world.<br>
        • Experimental results in a dynamic environment demonstrate Ella's ability to influence, lead, and cooperate with other agents, highlighting the potential of combining structured memory with foundation models.
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
        • MemoryOS aims to provide comprehensive and efficient memory management for AI agents.<br>
        • Inspired by memory management principles in computer operating systems and the hierarchical structure of human memory, MemoryOS adopts a unique segment–page hierarchical storage architecture and comprises four core functional modules: memory storage, memory updating, memory retrieval, and response generation.<br>
        • Experimental results show that MemoryOS significantly improves contextual coherence and personalized memory retention in long conversations across mainstream benchmarks; for example, on the LoCoMo benchmark, average F1 and BLEU-1 scores increase by 49.11% and 46.18%, respectively.
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
        • MemOS (Memory Operating System) is a memory operating system designed for AI systems that treats memory as a manageable system resource, unifying the representation, scheduling, and evolution of explicit, activation-based, and parameter-level memory to enable cost-efficient storage and retrieval.<br>
        • MemOS adopts a three-layer architecture consisting of an interface layer, an operation layer, and an infrastructure layer. The interface layer interacts with users or upstream systems and provides standardized memory APIs; the operation layer organizes and schedules memory resources; and the infrastructure layer handles storage, security, migration, and data flow of memory.<br>
        • MemOS provides operating-system-level support for cross-task adaptation, cross-modality evolution, and cross-platform migration. Its introduction marks a key transition for large models from “perception and generation only” to “memory-enabled and evolutionary” intelligence.
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
        • Mem0 is a memory architecture that dynamically extracts and integrates key information from conversations, enabling AI systems to remember important content and sustain cross-session dialogue.<br>
        • The authors further propose Mem0g, which extends Mem0 by incorporating graph-structured memory (i.e., knowledge graphs), allowing AI systems to handle complex relational reasoning more effectively.<br>
        • NLI tasks enhance constituency grammar induction ability, whereas SMS tasks reduce it in the upper layers.
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-22</td>
      <td style="width: 55%;"><strong>Echo: A Large Language Model with Temporal Episodic Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Episodic%20Memory-purple" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Temporal-red" alt="Temporal">
        <img src="https://img.shields.io/badge/LLM%20Model-success" alt="LLM Model">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.16090">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Introduced an LLM design that explicitly incorporates temporal episodic memory to store time-indexed events.<br>
        • Targeted improved recall of event sequences and time-sensitive dependencies for downstream reasoning.<br>
        • Evaluated on episodic-memory-focused tests to demonstrate gains over baselines without explicit episodic memory.
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
        • Introduces Zep, a memory layer service for AI agents powered by Graphiti, a dynamic and temporally-aware knowledge graph engine.<br>
        • Zep synthesizes unstructured conversational data and structured business data while maintaining historical relationships, enabling agents to handle complex, evolving contexts.<br>
        • Experimental results demonstrate that Zep outperforms MemGPT on the Deep Memory Retrieval (DMR) benchmark and achieves significant improvements in accuracy and latency on the more challenging LongMemEval benchmark.
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
        • Proposes Embodied VideoAgent, a multimodal agent that constructs persistent scene memory by fusing egocentric video with embodied sensory inputs like depth and pose to address dynamic scene understanding.<br>
        • Features a VLM-driven memory update mechanism that dynamically tracks object state changes and relations during actions, ensuring the memory remains accurate over long-form interactions.<br>
        • The agent achieves state-of-the-art performance on benchmarks such as Ego4D-VQ3D and OpenEQA, and demonstrates practical utility in generating synthetic embodied user-assistant interaction data.
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
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Studied trainable key–value “memory layers” as a sparse lookup module to add capacity without proportionally increasing FLOPs.<br>
        • Presented a fully parallelizable implementation and explored scaling behavior with very large memory parameter counts.<br>
        • Reported downstream improvements (notably on factual tasks) compared to dense and MoE baselines under matched budgets.
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
        • Proposes THEANINE, a framework for lifelong dialogue agents that utilizes a relation-aware memory graph to store memories without deletion, preserving temporal and cause-effect connections.<br>
        • Introduces a timeline-augmented response generation approach that retrieves and refines entire memory timelines, ensuring rich contextual cues are maintained for long-term interaction.<br>
        • Presents TeaFarm, a counterfactual-driven evaluation pipeline designed to stress-test dialogue agents' ability to correctly reference past conversations, where THEANINE demonstrates superior performance over existing baselines.
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
          • Memoro is a wearable audio-based memory assistant designed to minimize disruption during social interactions by utilizing Large Language Models (LLMs) for concise memory retrieval.<br>
          • The system introduces a "Queryless Mode" that proactively infers user memory needs based on real-time conversational context, alongside a traditional "Query Mode" for explicit natural language requests.<br>
          • User studies indicate that Memoro increases recall confidence and reduces device interaction time while effectively preserving the quality of ongoing conversations.
        </td>
    </tr>
    <!-- <tr>
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
        • Memory3 is a novel large language model that introduces explicit memory to reduce training and inference costs.<br>
        • The study proposes a memory circuit theory that describes the process of memory externalization, clarifies the definition of knowledge, and highlights the model’s advantages in handling long contexts.<br>
        • Memory3 effectively manages the costs of knowledge writing and reading, and employs compression techniques to significantly reduce the storage requirements of explicit memory.
      </td>
    </tr> -->

  </table>

</details>

## 🧰 Resources

### 📊 Benchmarks and Tasks

|     Task Type      | Benchmarks \& Datasets                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **Personalized Task Evaluation**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745)  |
|  **Comprehensive Evaluation**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **Memory Mechanism Evaluation**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **Long-Term Memory Evaluation**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144), [Mem-Gallery](https://arxiv.org/pdf/2601.03515), [RealMem](https://arxiv.org/pdf/2601.06966), [CloneMem](https://arxiv.org/pdf/2601.07023) |
|  **Long-Dialogue Reasoning**   | [PREFEVAL](https://arxiv.org/pdf/2502.09597),  [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf)|
|  **Long-Context Understanding**   | [LongBench V2](https://arxiv.org/pdf/2412.15204), [LongBench](https://arxiv.org/abs/2308.14508), [BABILong](https://arxiv.org/pdf/2406.10149), [HotpotQA](https://aclanthology.org/D18-1259.pdf) |
|  **Long-Context Evaluation** |[SCBENCH](https://arxiv.org/abs/2412.10319), [L-CiteEval](https://arxiv.org/pdf/2410.02115), [GLE](https://aclanthology.org/2024.acl-long.859/), [HOMER](https://arxiv.org/pdf/2404.10308), [RULER](https://arxiv.org/pdf/2404.06654), [MM-Needle](https://aclanthology.org/2025.naacl-long.166.pdf) |
|  **Long-Form Text Generation**   | [LongGenBench](https://arxiv.org/pdf/2409.02076) |
|  **Episodic Memory Evaluation**   | [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf)|
|  **Memory Hallucination Evaluation**   | [HaluMem](https://arxiv.org/pdf/2511.03506) |
|  **Web Interaction & Navigation** | [WebChoreArena](https://arxiv.org/pdf/2506.01952), [MT-Mind2Web](https://arxiv.org/pdf/2402.15057), [WebShop](https://arxiv.org/pdf/2207.01206), [WebArena](https://arxiv.org/pdf/2307.13854) |


### 💻 Systems and Open Sources
Systems below are ordered by **publication date**:

| System      | Time       | Stars | GitHub & Website |
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
| OMEGA  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/omega-memory/omega-memory?style=social) | https://github.com/omega-memory/omega-memory<br>https://omegamax.co/ |

### 🎥 Multi-media resource

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Website Link</th>
      <th>Video Introduction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6"><strong>Basic Theory of Memory</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>Short-Term Memory with LangGraph</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=WsGVXiWzTpI</td>
      <td>OpenAI: Agent Memory Patterns
</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=fsENEq4F55Q</td>
      <td>Long-Term Memory with LangGraph</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=L-au0tvDJbI</td>
      <td>LLMs Do Not Have Human-Like Working Memories</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=RkWor1BZOn0</td>
      <td> long-term memory and personalization for LLM applications</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=CFih0_6tn2w</td>
      <td>A Paradigm Shift to Memory as a First Class Citizen for LLMs</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>Memory-Related Tools</strong></td>
      <td>https://www.bilibili.com/video/BV1hom8YAEhX</td>
      <td>LLMs as Operating Systems: Agent Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1CU421o7DL</td>
      <td>Langchain Agent with memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1arJazVEaX</td>
      <td>Open Memory MCP</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV11HxXzuExk</td>
      <td> Agentic Memory for LLM Agents</td>
    </tr>
    <tr>
      <td rowspan="10"><strong>Memory-Related Papers</strong></td>
      <td>https://www.bilibili.com/video/BV1XT8ez6E46</td>
      <td>AI agent Survey Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1f12wBpEXX</td>
      <td>MemGen: Weaving Generative Latent Memory for Self-Evolving Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1deyFBKEFh</td>
      <td>MLP Memory: A Retriever-Pretrained Memory for Large Language Models</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV18FnVzpE6S</td>
      <td>How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1mpbrzSEH9</td>
      <td>Agent Workflow Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1qEtozyEoh</td>
      <td>Introduction to the Memory Mechanism of Large Language Model Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1FGrhYhEZK</td>
      <td>Memory Layers at Scale</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1aQ1xBkE45</td>
      <td>Agentic Memory for LLM Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1Yz421f7uH</td>
      <td>Evaluating Very Long-Term Conversational Memory of LLM Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV19RWdzxEsR</td>
      <td>Lightweight plug-in memory system</td>
    </tr>
  </tbody>
</table>


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

## 💬 Community & Support

Join our community to ask questions, share your projects, and connect with other developers.

- **GitHub Issues**: Report bugs or request features in our <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/issues" target="_blank">GitHub Issues</a>.
- **GitHub Pull Requests**: Contribute code improvements via <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/pulls" target="_blank">Pull Requests</a>.
- **GitHub Discussions**: Participate in our <a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory/discussions" target="_blank">GitHub Discussions</a> to ask questions or share ideas.
- **WeChat**: Scan the QR code below to join our discussion group, get the latest research information related to Memory, or promote your related research results.

<!-- <div style="text-align: center;">
  <img src="assets/wechat-qr-code.png" alt="QR Code" width="255">
</div> -->

<!-- <center>
  <img src="assets/wechat-qr-code.png" alt="QR Code" width="255">
</center> -->

<table style="width:100%">
  <tr>
    <td align="center">
      <img src="assets/wechat-qr-code.png" alt="QR Code" width="255">
    </td>
  </tr>
</table>

## 🌟 Star Trends

<a href="https://www.star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
 </picture>
</a>


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
[![Papers](https://img.shields.io/badge/Papers-501-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-107-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)


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
+ 2026-06-14 - 🎉 Updated 24 papers, including 2 on Survey, 4 on Systems & Models, 2 on Datasets & Benchmark, and 16 on Framework & Methods
+ 2026-06-06 - 🎉 Updated 45 papers, including 1 on Survey, 6 on Systems & Models, 12 on Datasets & Benchmark, and 26 on Framework & Methods
+ 2026-05-10 - 🎉 Updated 16 papers, including 3 on systems and models, 1 on benchmarks, and 12 on methods; also added 1 new project under systems and open sources
+ 2026-05-06 - 🎉 Updated 16 papers, including 2 on systems and models, 2 on benchmarks, and 12 on methods
+ 2026-04-27 - 🎉 Updated 15 papers, including 2 on survey, 3 on systems and models, and 10 on methods
+ 2026-04-17 - 🎉 Updated 46 papers, including 1 on survey, 5 on systems and models, 3 on benchmarks, and 37 on methods
+ 2026-04-07 - 🎉 Updated 16 papers, including 15 on methods, and 1 on benchmarks
+ 2026-03-15 - 🎉 Updated 14 papers, including 14 on methods
+ 2026-03-08 - 🎉 Updated 15 papers, including 3 on survey, 2 on systems and models, 5 on benchmarks, and 5 on methods
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
- [Awesome-AI-Memory](#awesome-ai-memory)
  - [👋 Introduction](#-introduction)
  - [🎯 Goal of Repository](#-goal-of-repository)
  - [📏 Project Scope](#-project-scope)
  - [🔔 Recent hot research and news](#-recent-hot-research-and-news)
  - [🧠 Core Concepts](#-core-concepts)
  - [📚 Paper List](#-paper-list)
  - [🧰 Resources](#-resources)
    - [📊 Benchmarks and Tasks](#-benchmarks-and-tasks)
    - [💻 Systems and Open Sources](#-systems-and-open-sources)
    - [🎥 Multi-media resource](#-multi-media-resource)
    - [🧠 Adam Framework](#-adam-framework)
  - [🤝  Make a Contribution](#--make-a-contribution)
  - [💬 Community \& Support](#-community--support)
  - [🌟 Star Trends](#-star-trends)

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
          • This survey systematically frames LLM agent environments across a full lifecycle, including environment modeling, synthesis, evaluation, and application. <br>
          • It introduces symbolic and neural paradigms for environment synthesis and analyzes environment design through structural properties and capability evolution. <br>
          • The work highlights co-evolution between agents and environments (memory, workflows, trajectories, and exploration) and points toward future directions such as environment-as-a-service and multi-agent ecosystems.
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
          • This paper analyzes security risks of LLM agents from a lifecycle perspective and formalizes key interactions including information flow, delegated authority, and persistent state. <br>
          • Based on a review of 247 studies, it organizes attack surfaces, defense mechanisms, and evaluation methods, showing that current defenses remain weak and incomplete. <br>
          • It emphasizes the need for clearly defined trust boundaries, principled permission control, and realistic long-horizon security evaluation frameworks aligned with real-world environments.
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
          • Characterizes agent memory as a stateful long-horizon systems workload rather than only a retrieval add-on.<br>
          • Introduces a system-oriented taxonomy and a phase-aware profiler for construction, retrieval, and generation cost.<br>
          • Analyzes ten representative systems and distills practical recommendations for scalable, freshness-aware memory deployment.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-23</td>
        <td style="width: 55%;"><strong>MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multimodal%20Memory-blue" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/Visual%20Benchmark-red" alt="Visual Benchmark">
          <img src="https://img.shields.io/badge/Evaluation%20Framework-green" alt="Evaluation Framework">
          <img src="https://img.shields.io/badge/Long--term%20Memory-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.15128">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Proposes MemEye, a visual-centric benchmark evaluating multimodal agents' long-term memory beyond text-dominated shortcuts.<br>
          • Designs a 2D evaluation matrix (X-axis: Scene/Region/Instance/Pixel granularity; Y-axis: Atomic/Relational/Evolutionary reasoning depth).<br>
          • Introduces three-stage validation gates ensuring questions cannot be solved via textual context, captions, or beyond VLM capabilities.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Long--term%20Memory-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20OS-orange" alt="Memory OS">
          <img src="https://img.shields.io/badge/Self--Organizing-green" alt="Self-Organizing">
          <img src="https://img.shields.io/badge/Semantic%20Consolidation-red" alt="Semantic Consolidation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.02163">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • Proposes EverMemOS, a three-stage memory lifecycle (Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection) that organizes fragmented conversations into structured, evolving memory units (MemCell/MemScene).<br>
          • Introduces MemCell as atomic memory unit containing Episode + Atomic Facts + Foresight + Metadata, and MemScene for scene-level consolidation enabling long-term user profile evolution.<br>
          • Designs a reconstructive retrieval paradigm with MemScene-guided retrieval, foresight validity filtering, and sufficiency verification to achieve "necessary and sufficient" context for long-horizon reasoning.
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
          • Identifies three engineering problems in pipeline-based retrieval: non-reusable strategy logic, non-observable routing decisions, and non-evolvable workflow coupling.<br>
          • Proposes Experience-RAG Skill with six modules (interface, scene analyzer, experience memory, strategy router, retriever pool, result packer) to encapsulate retrieval strategy selection as a pluggable agent skill.<br>
          • Shows rule-based routing outperforms learned routing (0.8924 vs 0.8778/0.8627) under limited experience memory; experience memory records (scene_features, score_vector, best_margin) enable future upgrade to learning-based routing.
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
          • Surveys memory, perception, language, reasoning, imagination, motivation, and metacognition in world models from a unified cognitive-architecture perspective.<br>
          • Introduces Epistemic World Models for structured knowledge agents in scientific discovery, with taxonomy and future directions across video, embodied, and cognitive world models.
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
          • Evaluates 22 common agentic frameworks on BBH, GSM8K, and ARC, comparing accuracy, latency, cost, and cross-benchmark consistency.<br>
          • Finds that performance differences mainly come from orchestration quality, especially memory control, context growth, and failure-retry mechanisms.
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
            • Surveys LLM agent externalization from the perspective of memory, skills, protocols, and harness engineering.<br>
            • Argues that memory externalizes cross-time state, skills externalize procedural capability, protocols externalize interaction structure, and harnesses orchestrate these components together.<br>
            • Maps the evolution from model parameters to context and then to external infrastructure, while discussing the key trade-offs and open challenges across these layers.
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
            • This paper introduces Multi-Agent Transactive Memory (MATM), which organizes action–observation trajectories generated by heterogeneous agents into group-level shared memory. Producer agents contribute execution experience, while consumer agents retrieve prior trajectories, enabling the reuse of procedural knowledge that would otherwise be discarded after a single task.<br>
            • MATM employs a state-conditioned key–value index, using the current task and recent interaction history as retrieval keys and subsequent trajectory segments as values. It further applies a learning-to-rank model that integrates producer reliability, consumer characteristics, retrieval scores, and trajectory attributes to perform personalized reranking.<br>
            • Experiments in ALFWorld and WebArena demonstrate that retrieving shared trajectories improves task performance and reduces interaction steps without requiring direct inter-agent coordination or joint training, with benefits extending across agents of varying capability levels. The work thereby extends individual experiential memory into a collective knowledge infrastructure for open agent ecosystems.
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
            • This paper formally investigates the information that generalist agents must retain to sustain near-optimal behavior across multiple environments and objectives. It defines states with identical observations but conflicting optimal actions as observational bottlenecks that reveal the necessity of memory.<br>
            • The separation theorem establishes that when different domains require mutually incompatible optimal actions at such a bottleneck, any unified near-optimal policy must induce distinct memory distributions. Consequently, a memoryless policy that relies solely on the current observation cannot simultaneously maintain a high success rate and cross-domain robustness.<br>
            • The paper further proves that if memory is sufficient to estimate the value functions of a set of relevant objectives, local transition dynamics can be approximately reconstructed from it. Memory therefore serves simultaneously as a mechanism for domain disambiguation, environment-model reconstruction, and a substrate for planning. These findings establish theoretical necessity but do not directly prescribe a specific engineering architecture for memory.
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
            • This paper decomposes personalized memory into user-specific content and reasoning skills shared across users. It proposes storing user facts through localized row edits in the hash-keyed memory table of the Engram model, while a single shared adapter provides fact interpretation and indirect reasoning capabilities.<br>
            • Unlike per-user LoRA modules, which exert dense effects on global weights, localized Engram edits operate only at precisely triggered positions and leave all other positions unchanged. Facts belonging to different users are written into non-overlapping hash slots, enabling additive and lossless multi-user composition within a shared table.<br>
            • The paper reports that the proposed design matches per-user LoRA in direct recall, improves indirect-reasoning accuracy by an average factor of 5.6, and reduces memory consumption by approximately 33,000 times. After roughly 100 facts, it also outperforms retrieval pipelines using larger models. Its applicability, however, depends on the underlying model possessing an editable Engram memory architecture.
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
            • This paper identifies a retention–forgetting dilemma faced by parameter-free verbal reinforcement learning in non-stationary environments: retaining obsolete rules indefinitely induces negative transfer, whereas permanently deleting prior knowledge causes catastrophic forgetting when similar conditions recur.<br>
            • The authors propose a three-layer memory architecture comprising rules, evidence, and skills, connected through a feedback-driven curation loop. Rules distill experience, evidence records the cross-episode reliability of rules, and skills govern rule selection, conflict resolution, and abstention when necessary.<br>
            • A financial forecasting case study shows that the same accumulated experience can produce performance below a zero-shot baseline when governance is absent, whereas incorporating the curation loop improves both predictive accuracy and risk-adjusted returns. This finding suggests that the central bottleneck in continual agent learning is not merely experience extraction, but also the governance of knowledge lifecycles and application permissions.
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
            • This paper models the finite program/erase endurance of robotic flash storage as non-renewable depreciating capital. It introduces an endurance shadow price η and uses it to construct a wear-augmented per-byte index for optimizing memory placement across RAM, onboard non-volatile storage, and cloud infrastructure.<br>
            • Theoretical analysis shows that threshold-based placement policies can achieve cost optimality under different value–write correlation levels χ. Only when χ is positive can the optimal policy become non-monotonic, moving frequently written, high-value memories away from local flash storage. Real-world logs show that χ is positive for cyclic long-horizon operations, near zero for short-horizon tasks, and negative for non-cyclic teleoperation.<br>
            • Endurance constraints are generally inactive for high-end TLC devices rated for approximately 3,000 P/E cycles, but may become binding for QLC or eMMC devices rated for approximately 1,000 P/E cycles. The paper also explicitly notes that wear-aware management primarily improves device longevity and cost efficiency; it has not yet been shown to increase task value or task success rates.
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
            • This paper introduces Posterior Twins, extending the output of enterprise digital twins from a single most likely behavior to a posterior distribution over behaviors conditioned on a specific decision context. This formulation captures states such as adoption, churn, hesitation, and risk migration across different population segments.<br>
            • The system uses governed historical memory as its evidence base and integrates behavioral-model routing, scenario orchestration, distribution aggregation, and auditing mechanisms. Evaluation employs both modal accuracy and Wasserstein-1 distance to distinguish point-prediction correctness from overall distributional fidelity.<br>
            • On 226 held-out samples, TL-Twin Alpha achieves the lowest Wasserstein-1 distance in the reported results, at 1.16, while Gamma and Delta exhibit more balanced operating points. The study demonstrates the need for distributional evaluation in enterprise simulation, although its conclusions remain constrained by the scale of a single benchmark and the particular system configurations examined.
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
            • This paper addresses error propagation in multi-agent software-engineering pipelines by employing a shared knowledge graph as both centralized semantic memory and a coordination interface. This enables downstream agents to evaluate and inherit upstream artifacts according to calibrated confidence estimates.<br>
            • The method comprises two-stage traceability-link prediction combining embedding-based retrieval with LLM-based multi-criteria analysis, a trace-seed mechanism for comparing confidence at generation and verification time, and protocols for threshold gating, confidence-disagreement detection, and conflict resolution.<br>
            • An automotive software-engineering case study and ablation experiments indicate that confidence calibration is essential to the effective operation of the coordination protocol. However, because the evidence is derived primarily from a domain-specific case, the work is better understood as an architectural validation of trustworthy multi-agent artifact governance than as a universally applicable conclusion across all collaborative settings.
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
            • This paper focuses on entangled causal credit assignment in memory-writing operations for long-horizon agents. A final failure may originate from tool invocation, noisy observations, or subsequent reasoning, yet trajectory-level rewards can mistakenly penalize an earlier memory update that was itself correct.<br>
            • HiMPO first compares the task-relevant information recoverable from the new and previous memories under the same pre-write state to estimate the local utility of a memory update. It then calibrates this utility using a bounded hindsight-relevance filter and applies the resulting memory-specific advantage exclusively to memory tokens.<br>
            • Across open-domain evaluations and compressed-memory question-answering tasks, the method outperforms multiple memory and reinforcement-learning baselines. Controlled interventions further demonstrate that HiMPO reduces responsibility leakage caused by tool errors and improves the accuracy and interpretability of credit attribution for memory writes.
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
            • This paper proposes the “User as Code” paradigm, implementing the user model of a personalized agent as a continuously evolving software project. Typed Python objects store user state, while ordinary functions encode constraints, aggregation logic, and response rules, allowing memory representation and memory reasoning to share the same executable medium.<br>
            • The system employs a two-stage pipeline comprising an append-only fact log and periodic code checkpoints. This preserves the original history while organizing it into verifiable structured state, thereby supporting contradiction resolution, cross-record aggregation, and safety rules that are proactively triggered by state changes.<br>
            • UaC achieves a conventional factual recall rate of 78.8% on LOCOMO and approximately 99% on historical aggregation questions, substantially exceeding the 6%–43% performance of retrieval-based memory. Its central contribution extends beyond improved recall: it transforms user memory from a passive query database into a proactively serving system capable of deterministic execution.
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
            • This paper observes that although conventional context pruning and dynamic memory eviction reduce input-token counts, they also alter sequence boundaries and prompt layouts, resulting in prefix mismatches and KV-cache invalidation. Context sparsity and cache continuity therefore exhibit a systematic tension.<br>
            • TokenPilot adopts a dual-granularity management strategy. At the global level, Ingestion-Aware Compaction compresses environmental noise as information enters the context and stabilizes the prompt prefix. At the local level, Lifecycle-Aware Eviction performs conservative batched offloading according to the remaining task utility of individual context segments.<br>
            • In both independent and continuous operation modes on PinchBench and Claw-Eval, the paper reports cost reductions of 56%–61% and 61%–87%, respectively, while maintaining task performance comparable to existing systems. These findings establish cache-compatible stable layout as an independent design objective for cost optimization in long-horizon agents.
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
            • This paper reveals that long-term memory introduces a cross-turn temporal channel into agent access control. A prohibited request that would ordinarily trigger refusal can be decomposed into superficially benign fragments, written separately into memory, and subsequently recombined during retrieval.<br>
            • FragFuse comprises three stages: refusal-sensitive fragment identification, memory injection using marker-based carriers, and fusion-oriented retrieval attacks. It further uses surrogate models to optimize fusion instructions and marker design, enabling automated attack generation under a black-box threat model.<br>
            • The paper reports an average access-control bypass rate of 86.3% and an end-to-end harmful-task success rate of 41.1%. Prompt-injection detectors and perplexity-based detectors provide limited defensive effectiveness. These results demonstrate that security review must encompass the complete lifecycle of memory writing, storage, retrieval, and fusion rather than inspecting only the current user query.
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
            • This paper introduces DYNA, which uses a frozen large language model as its reasoning core and constructs a continuously updatable external episodic memory by representing events as nodes and temporal relations such as “before,” “after,” and “co-occurs with” as timestamped directed edges.<br>
            • During querying, the system uses random walks, node centrality, and graph-structural information to identify relevant events, then combines the retrieved results with the model’s internal knowledge to generate answers. This avoids the training costs and parameter-level knowledge interference associated with continual fine-tuning.<br>
            • Across three categories of temporal-memory tasks, the paper reports that DYNA reduces catastrophic forgetting by approximately 7% relative to fine-tuning and improves temporal-ordering accuracy by approximately 5% relative to standard RAG. The positive correlation between graph clustering coefficients and retrieval performance further indicates that memory topology itself is an important determinant of performance.
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
          • This paper introduces AgentSpec, formalizing embodied agents as typed compositions of perception, memory, reasoning, reflection, action, and optional learning modules. Standardized interfaces support the independent replacement, ablation, and controlled recombination of these components.<br>
          • The study systematically compares different reasoning, memory, reflection, and reinforcement-learning components across DeliveryBench, ALFRED, MiniGrid, and RoboTHOR. The results show that agent performance is not determined by the strength of any single module, but is significantly influenced by module compatibility, task environment, and component interactions.<br>
          • The experiments specifically demonstrate that structured, multi-granularity memory provides more stable support for long-horizon state tracking, although its benefits depend on alignment between the memory representation and the downstream reasoning strategy. The work thus transforms agent scaffolding from an empirically configured engineering artifact into an analyzable compositional design space.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dynamic-Environments-4A90E2" alt="Dynamic Environments">
          <img src="https://img.shields.io/badge/Memory-Evolution-F5A623" alt="Memory Evolution">
          <img src="https://img.shields.io/badge/Benchmark-Evaluation-7ED321" alt="Benchmark">
          <img src="https://img.shields.io/badge/EvoMem-System-D0021B" alt="EvoMem">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13681">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • Introduces EvoArena, a benchmark suite for simulating dynamic environment changes to evaluate memory robustness in LLM agents.<br>
          • Proposes EvoMem, a patch-based memory paradigm that explicitly tracks structured memory evolution over time.<br>
          • Results show that current agents perform poorly under evolving environments, while EvoMem significantly improves performance.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>MemRefine: LLM-Guided Compression for Long-Term Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Memory-Compression-4A90E2" alt="Memory Compression">
          <img src="https://img.shields.io/badge/Long-Term-Memory-F5A623" alt="Long-Term Memory">
          <img src="https://img.shields.io/badge/LLM-Optimization-7ED321" alt="LLM Optimization">
          <img src="https://img.shields.io/badge/Budget-Constraint-D0021B" alt="Budget Constraint">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.13177">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • Proposes MemRefine, an LLM-driven memory compression framework under fixed storage budgets.<br>
          • Uses semantic and factual consistency evaluation to iteratively delete, merge, or retain memory entries.<br>
          • Maintains or exceeds baseline performance under strict memory constraints.
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
          • Introduces TRACE, which compiles user corrections into runtime constraints for LLM agents.<br>
          • Converts feedback into executable rules for continuous behavior correction.<br>
          • Significantly reduces preference violations in interactive tasks.
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
          • Proposes G-Long, a graph-based memory system using structured triples for long-term dialogue management.<br>
          • Employs lightweight LMs for structured extraction and attention-aware importance scoring.<br>
          • Achieves efficient and high-quality memory retrieval with reduced computational cost.
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
          • Addresses multi-turn reasoning failures caused by fragmented context input in dialogue systems.<br>
          • Introduces a compact rolling memory mechanism replacing full history tracking.<br>
          • Improves zero-shot reasoning and generalization across long-context tasks.
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
          • Introduces Arbor, a multi-agent framework using tree search as a shared cognitive layer.<br>
          • Maintains an explicit evolving search tree as shared working memory for coordination.<br>
          • Improves scalability, reproducibility, and reasoning efficiency in large state spaces.
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
          • Decomposes user-side memory into orthogonal axes rather than treating personalization as a single capability.<br>
          • Identifies three key dimensions: behavioral consistency, factual presence, and factual absence.<br>
          • Reveals asymmetries across models and highlights alignment and routing trade-offs.
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
          • Proposes HORMA, a hierarchical memory organization framework for efficient navigation and retrieval.<br>
          • Structures experience into layered representations to reduce loss and latency in unstructured retrieval.<br>
          • Improves performance and efficiency in long-horizon dialogue tasks.
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
          • Argues that explicit hippocampal-like memory is fundamental for achieving AGI-level capabilities.<br>
          • Claims implicit statistical learning alone is insufficient for planning, reasoning, and meta-cognition.<br>
          • Outlines computational requirements for implementing explicit memory systems in AI.
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
          • Introduces DocTrace, a multi-agent RAG framework with structure-aware hypergraph memory.<br>
          • Builds document structure trees and on-demand shared memory graphs for reasoning reuse.<br>
          • Achieves strong improvements over structured RAG baselines on long-document QA tasks.
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
          • Proposes REAL, a time- and confidence-aware directed graph for long-term memory management.<br>
          • Supports non-destructive updates with multi-version factual memory retention.<br>
          • Achieves +22.72% average improvement in long-term memory tasks.
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
          • Proposes Infini Memory, which organizes agent memory into maintainable topic-centric documents.<br>
          • Uses buffer-and-consolidation updates to continuously refine semantic memory over time.<br>
          • Enables iterative retrieval via tool-based memory reading rather than single-pass lookup.
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
          • Introduces ActiveMem, decoupling planning and memory systems for long-horizon reasoning tasks.<br>
          • Uses lightweight planners with distributed memory modules running in parallel.<br>
          • Improves efficiency while achieving state-of-the-art performance on complex benchmarks.
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
          • Proposes DCPM, a dual-process memory system separating explicit and implicit cognitive memory layers.<br>
          • Uses day-time writing and night-time consolidation mechanisms for long-term evolution.<br>
          • Demonstrates strong performance in cross-session reasoning and personalization tasks.
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
          • Proposes MemToolAgent, which enhances tool-using agents via structured memory extraction and retrieval.<br>
          • Converts past interactions into reusable memory entries for continuous improvement.<br>
          • Improves personalization and task accuracy through memory-augmented reasoning.
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
          • Proposes AdMem, a unified memory framework integrating semantic, episodic, and procedural memory.<br>
          • Uses multi-agent coordination for memory generation, reward annotation, and adaptive retrieval.<br>
          • Improves robustness and success rate in long-horizon task-solving scenarios.
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
          • Addresses the difficulty of using past experience when language agents face dynamic test-time conditions.<br>
          • Combines offline long-term trajectory memory with online short-term policy memory to guide decisions.<br>
          • Shows consistent gains over static memory baselines, highlighting test-time adaptation as a practical memory direction.
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
          • Studies when a lifelong agent should consult prior experience rather than always retrieving memory.<br>
          • Organizes experience into factual, episodic, and skill memory, and learns retrieval as an explicit policy action.<br>
          • Improves task success while reducing unnecessary interactions, showing the value of proactive memory control.
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
          • Argues that semantic similarity alone fragments decision trajectories in long-horizon agent tasks.<br>
          • Proposes MAGE, a hierarchical execution-state tree with grow, compress, maintain, and revise operations.<br>
          • Improves task success and reduces token use by preserving valid state paths and isolating erroneous branches.
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
          • Identifies semantic-similarity memory search as a trust boundary for personal AI agents.<br>
          • Introduces MemGate, a lightweight query-conditioned gate that decides whether retrieved memories should enter context.<br>
          • Reduces cross-domain leakage, sycophancy, tool drift, and memory-induced jailbreak risks while preserving utility.
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
          • Focuses on which evidence should survive when long-horizon agents have fixed retained-memory budgets.<br>
          • Learns to store source-backed evidence capsules with retrieval keys and update metadata during ingestion.<br>
          • Improves retained-evidence recall and answer quality, showing that memory quality depends on budgeted evidence survival.
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
          • Targets evolving jailbreak attacks where static safety classifiers and naive memory guardrails are insufficient.<br>
          • Builds contrastive safety memory cells pairing harmful queries with superficially similar benign requests.<br>
          • Improves agent-level defense while reducing over-refusal and maintaining robustness under memory poisoning.
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
          • Challenges the static retrieve-then-reason pipeline used by many memory-augmented agents.<br>
          • Represents memory as a Cue-Tag-Content graph and lets the agent actively reconstruct relevant paths during reasoning.<br>
          • Outperforms strong baselines on long-memory benchmarks while reducing token and runtime cost.
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
          • Treats contradiction resolution in persistent agent memory as a write-time consistency problem.<br>
          • Defines bitemporal operators with explicit isolation assumptions, provenance annotations, and audit rows.<br>
          • Clarifies the correctness contract needed by production memory systems when beliefs evolve or conflict.
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
          • Addresses the cost of keeping full interaction histories in long sequential decision tasks.<br>
          • Learns recursively updated natural-language belief states and directly supervises their information content.<br>
          • Reduces summary errors and memory footprint, narrowing the gap with full-context agents.
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
          • Focuses on building durable person understanding from long-term interactions.<br>
          • Organizes evidence, claims, confidence, and query-conditioned paths into a structured persona tree.<br>
          • Improves personalization by returning only the evidence depth needed for each query.
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
          • Addresses runtime context assembly for LLM agents with explicit memory policies.<br>
          • Defines a registry-based memory model with primitives such as promote, gate, write, evict, and rollback.<br>
          • Shows that grouping and priority management of memory blocks can improve task success across models.
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
          • Addresses the limitation that retrieval memories influence prompts but rarely change future agent behavior.<br>
          • Compresses historical experience into explicit memory and uses lightweight online updates as parametric memory.<br>
          • Establishes a scaling direction for agents that continuously improve after deployment.
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
          • Argues that event order is central to long-horizon memory but often lost in similarity-based organization.<br>
          • Introduces SegTreeMem, an online segment-tree structure that preserves temporal order while forming hierarchical memory.<br>
          • Improves long-memory answering and shows performance depends on keeping order during memory construction.
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
          • Studies how graph topology affects leakage of private information across multi-agent LLM systems.<br>
          • Introduces MAMA with Engram seeding and Resonance extraction phases over controlled synthetic PII documents.<br>
          • Finds denser connectivity, shorter distance, and higher target centrality increase leakage risk.
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
          • Targets nondeterminism and token cost in LLM-summary-based conversational memory pipelines.<br>
          • Uses classical NLP, vector geometry, mathematical scoring, survival scores, and decay rules.<br>
          • Achieves competitive accuracy while reducing token usage and improving reproducibility.
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
          • Addresses sparse rewards in training chunk-wise memory agents for long-context tasks.<br>
          • Uses answer-conditioned information gain to evaluate whether final memory supports the ground-truth answer.<br>
          • Provides a more targeted training signal for deciding what information should be retained.
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
          • Targets the lack of high-quality labeled data for training memory agents.<br>
          • Uses self-supervised masked reconstruction and intermediate memory recall objectives on unlabeled corpora.<br>
          • Improves memory-intensive reasoning on long-text and search-based QA tasks.
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
          • Targets long-term user-state modeling under evolving and potentially conflicting conversational evidence.<br>
          • Uses a renormalization-group-inspired multi-scale process with hierarchical coarse-graining and thresholded updates.<br>
          • Improves cross-session continuity and adaptation to changing user preferences over flat retrieval or static summaries.
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
          • Addresses memory-related failures in conversational agents by supervising memory operations more explicitly.<br>
          • Uses hierarchical staged rewards and contrastive refinement to train filtering, consolidation, and recall behavior.<br>
          • Improves end-to-end accuracy and personalization while reducing memory-operation errors.
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
          • Studies retrieval over multi-session conversational history where lexical and semantic cues have complementary strengths.<br>
          • Combines BM25 with dense late-interaction scoring without additional training.<br>
          • Improves controllable, reproducible retrieval for multi-hop, temporal, and adversarial memory questions.
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
          • Targets redundancy and retrieval conflict when agents accumulate many task experiences.<br>
          • Organizes goal-conditioned experience and scene-level knowledge into residual trees with self-organization.<br>
          • Enables compact experience reconstruction and improves performance across interactive environments.
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
          • Addresses personalization when user preferences change and older memories may conflict with newer evidence.<br>
          • Formulates retrieval as selecting historical turns that provide evidence about the latent preference state.<br>
          • Outperforms embedding-only retrieval in preference-dense long-context dialogue tasks.
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
          • Shows that LLM-based judgment is unreliable for resolving freshness conflicts in evolving memory.<br>
          • Replaces direct LLM tracking with candidate extraction and version-aware deterministic aggregation.<br>
          • Improves conflict resolution and clarifies that aggregation, not storage, is the main bottleneck.
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
          • Studies how reflexive agents may store false self-explanations as persistent memory.<br>
          • Introduces diagnostic signals for reflection dependence and replaces open-ended self-diagnosis with trajectory-level failure extraction.<br>
          • Reduces confabulated memory use across environments and improves the reliability of reflective agents.
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
          • Explores the mutual dependence between memory and exploration in open-ended agent environments.<br>
          • Uses novelty-driven interaction to jointly train memory and exploration policies.<br>
          • Improves generalization in unseen environments while reducing token consumption.
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
          • Challenges fixed memory construction-retrieval pipelines that stop improving after deployment.<br>
          • Treats the entire memory system as an evolvable program with version trees and failure-driven edits.<br>
          • Shows memory pipelines can continuously improve across benchmarks through iterative diagnosis and debugging.
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
          • Proposes BeliefMem, a memory framework that shifts the memory paradigm from storing deterministic conclusions to maintaining an attribute-level belief representation to combat self-reinforcing errors in partially observable environments.<br>
          • Maintains multiple candidate conclusions with probabilities updated via Noisy-OR evidence merge, and features a belief-aware retrieval mechanism to preserve uncertainty for agent decision-making.<br>
          • Demonstrates superior average performance on the LoCoMo and ALFWorld benchmarks over existing deterministic memory methods, showing strong memory correction capabilities and data efficiency.
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
          • Proposes MemReranker (0.6B/4B), a family of reasoning-aware reranking models for agent memory systems that moves beyond simple semantic matching by leveraging a multi-stage LLM knowledge distillation pipeline.<br>
          • Combines Elo/Bradley-Terry calibrated scoring, BCE pointwise distillation, and InfoNCE contrastive fine-tuning to achieve well-calibrated relevance scores and hard-sample discrimination.<br>
          • Demonstrates state-of-the-art performance on memory retrieval benchmarks (LOCOMO, LongMemEval), matching the ranking quality of larger closed-source models (e.g., GPT-4o-mini) with significantly lower inference latency.
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
          • Proposes Event-Causal RAG (EC-RAG), a lightweight framework for infinite long-video reasoning that asynchronously segments video streams into semantically complete events and abstracts them into State-Event-State (SES) graph memory, replacing traditional fixed-length clip memory.<br>
          • Designs a Dual-Store Memory system integrating a vector database for semantic matching and a graph database for causal-topological retrieval, achieving low-overhead storage and efficient spatiotemporal memory merging in streaming environments.<br>
          • Introduces a bidirectional graph retrieval strategy to efficiently identify relevant event causal chains, significantly improving causal reasoning accuracy and preventing out-of-memory issues without requiring expensive long-sequence fine-tuning of backbone video foundation models.
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
          • Proposes TreeMem, a tree-based reinforcement learning framework for multi-agent memory systems that derives agent-specific credit directly from final downstream rewards without task-specific annotations.<br>
          • Expands each memory agent's (builder, summarizer, retrieval) outputs into multiple subsequent branches, estimating the contributions of intermediate actions via Monte Carlo averaging.<br>
          • Converts coarse final rewards into granular optimization signals, enabling heterogeneous memory agents to specialize effectively and outperforming strong baselines on long-horizon benchmarks.
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
        • Proposes MemFlow, a training-free memory orchestration framework for Small Language Models (SLMs) that replaces open-ended reasoning loops with intent-driven memory routing to handle long-horizon memory tasks.<br>
        • Features a specialized multi-agent pipeline (Router, Memory, Answer, and Validator) with dynamic context packing to ensure deterministic evidence preparation and grounded responses under strict token budgets.
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
          • Proposes governed collaborative memory as an artificial selection regime for LLM-based multi-agent systems, determining which candidate memories persist as durable, shared institutional state.<br>
          • Introduces a layered architecture separating agent-local, shared institutional, archive, and project-continuity memory, emphasizing memory evaluation for provenance fidelity, selection traceability, and role preservation.
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
          • Proposes H²-EMV, a hierarchical episodic memory framework for lifelong robot deployment that uses LLM-based relevance judgment and selective forgetting to manage memory scale.<br>
          • Integrates user feedback to update natural-language forgetting rules, achieving personalized memory management while maintaining QA accuracy and reducing query overhead.
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
          • Formalizes multiple attack scenarios for persistent external memory poisoning in retrieval-augmented agents and proposes MEMSAD, a semantic anomaly detection defense.<br>
          • Proves via gradient-coupling theorem that anomaly score gradients align with retrieval objective gradients, enabling certifiable detection radii and optimal calibration sample complexity.
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
          • Introduces ScrapMem, a bio-inspired on-device agent memory framework that uses optical forgetting to progressively reduce old memory resolution for storage efficiency.<br>
          • Constructs an Episodic Memory Graph with causal-temporal event links to maintain semantic consistency, achieving superior retrieval performance on ATM-Bench with significantly lower storage cost.
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
          • Proposes the Semantic Autonomy Stack (SAS), a six-layer framework for VLM-integrated indoor robots, featuring a hybrid reasoning mechanism that resolves routine instructions deterministically to bypass VLM inference latency.<br>
          • Introduces a five-category semantic memory framework that compiles learned preferences into a shared digest, enabling cross-session learning and cross-robot knowledge transfer without retraining.
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
        • Proposes the Dynamic Gist-Based Memory Model (DGMM), a memory-centric architectural framework that represents experience as an explicit, persistent, and graph-structured episodic-semantic memory.<br>
        • Formally characterizes memory operations into four distinct regimes (ingestion, consolidation, recall, and analysis), decoupling memory storage from downstream interpretation.<br>
        • Defines architectural invariants such as episodic persistence and locality of cue-conditioned surprise, enabling stable memory structures to support evolving interpretation over time without retraining.
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
          • Proposes MAGE, inspired by shadow stack in system security, maintaining an independent safety memory that distills and preserves critical security context across long task trajectories.<br>
          • Evaluates pending actions against the safety memory before execution, enabling earlier detection of long-horizon attacks with minimal impact on agent utility.
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
          • Proves that group-orbit tangent directions in equivariant recurrent networks produce symmetry-protected zero Lyapunov exponents, forming long-lived neutral memory modes.<br>
          • Demonstrates through S¹, T^q, SO(n), U(m) systems and equivariant RNN experiments that strict equivariance enhances long-range memory retention, generalization, and stability.
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
          • Proposes an unbalanced multi-agent collaboration framework with planner, actor, and memory manager roles, showing that planning contributes most to task performance.<br>
          • Introduces planner-only RL optimization with trajectory-level rewards, validated on web navigation, system control, and tool-use benchmarks for efficient long-horizon automation.
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
          • Proposes MemORAI, a memory organization and retrieval framework that utilizes selective memory filtering with dual-layer compression to retain user-persona-relevant content and preserve global context.<br>
          • Constructs a provenance-enriched multi-relational knowledge graph to track factual origins at the turn level, enabling fine-grained and transparent memory auditing.<br>
          • Introduces Dynamic Weighted PageRank for query-adaptive subgraph retrieval, applying query-conditioned edge weighting to significantly improve context-sensitive retrieval precision and personalized response generation.
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
          • Argues AI memory should be schema-constrained rather than retrieval-based recall, proposing an iterative schema-aware write pipeline with object detection, field detection, and value extraction.<br>
          • Adds verification, retry, and state control to the ingestion process, outperforming baselines on structured extraction and end-to-end memory tasks requiring stable facts and state updates.
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
          • Proposes MemCoE, a cognition-inspired two-stage optimization framework: stage one induces global memory criteria via contrastive feedback, stage two uses multi-round RL to learn criteria-compliant memory evolution strategies.<br>
          • Validates on three personalized memory benchmarks, demonstrating improvements in preference memory, robustness, transferability, and efficiency.
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
          • Proposes AHE, an observability-driven closed-loop mechanism that automatically evolves coding-agent harnesses across component, experience, and decision layers.<br>
          • Compresses large trajectory volumes into usable evidence via self-prediction and outcome verification, significantly improving coding-agent performance with cross-model transferability.
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
          • Introduces EviMem with IRIS closed-loop iterative retrieval that detects evidence gaps via sufficiency assessment and rewrites queries directionally for scattered multi-turn evidence.<br>
          • Proposes LaceMem hierarchical memory architecture for coarse-to-fine evidence diagnosis, significantly improving temporal and multi-hop accuracy on LoCoMo while reducing retrieval latency.
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
          • Proposes MemRouter, replacing per-turn LLM-based memory management with embedding routing to decide which turns should be written to external memory, training only ~12M parameters.<br>
          • Outperforms LLM-style memory managers on LoCoMo while significantly reducing memory management latency, with retrieval pipeline, prompts, and QA backbone held constant.
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
          • Proposes a dual-stream memory architecture for health coaching LLM agents that separates patient self-reports from structured EHR/FHIR records with a reconciliation engine.<br>
          • Quantifies error cascades from memory extraction and identifies discrepancy types and severity, emphasizing the necessity of memory verification in clinical longitudinal agents.
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
          • Studies belief inertia in embodied agents, where agents ignore new observations and remain anchored to prior beliefs.<br>
          • Proposes Estimate-Verify-Update, which predicts, verifies, and evidence-updates textual belief states to actively manage beliefs and improve success rates across embodied benchmarks.
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
          • Proposes Memanto with 13-class typed semantic memory schema, achieving 89.8% on LongMemEval and 87.1% on LoCoMo without knowledge graphs.<br>
          • Introduces Moorcheh Information-Theoretic Search for index-free, deterministic retrieval under 90ms with zero write latency.<br>
          • Addresses constraint drift through built-in conflict resolution and temporal versioning with supersede mechanism.
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
          • Proposes MIA, a Memory Intelligence Agent framework featuring a Manager-Planner-Executor architecture that addresses storage and retrieval bottlenecks by compressing historical search trajectories into structured non-parametric memory.<br>
          • Introduces a two-stage alternating reinforcement learning paradigm to align high-level planning with low-level execution, alongside a continual test-time learning mechanism for on-the-fly parametric memory updates.<br>
          • Incorporates reflection and unsupervised evaluation mechanisms, achieving state-of-the-art performance in deep research tasks and demonstrating strong self-evolution capabilities across diverse benchmarks.
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
          • Introduces HeLa-Mem, modeling long-term LLM-agent memory as a dynamic graph inspired by association, consolidation, and spreading activation.<br>
          • Combines an episodic memory graph with semantic knowledge distilled through Hebbian Distillation, improving LoCoMo performance while saving context tokens.
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
          • Proposes Freshness-Aware Prioritized Experience Replay, adding exponential age decay to priority sampling.<br>
          • Mitigates stale priorities as LLM/VLM policies change quickly, outperforming standard on-policy methods and ordinary PER on multi-step reasoning, agent, and math tasks.
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
          • Introduces MEMRES, a memory-augmented agentic Python dependency resolver that uses a multi-level confidence cascade and treats the LLM as a last resort.<br>
          • Combines self-evolving memory, an error-pattern knowledge base, semantic import analysis, and Python 2 heuristics to improve dependency resolution success.
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
          • Introduces Visual Inception, an attack that embeds triggers in user-uploaded images to poison long-term memory in agentic recommender systems and hijack future planning chains.<br>
          • Proposes CognitiveGuard, a dual-process defense combining perceptual sanitization and counterfactual consistency checks to detect abnormal memory-driven planning and reduce risk.
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
          • Studies safety risks in experience-driven self-evolving LLM agents across web and embodied environments, showing that even benign-task experience can reinforce action-taking over refusal.<br>
          • In mixed benign/malicious tasks, refusal-related experience mitigates safety degradation but causes over-refusal, exposing a safety-utility trade-off in evolving experience memory.
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
          • Introduces OASIS, an on-demand hierarchical event memory framework for streaming video reasoning that organizes long histories into event hierarchies.<br>
          • Performs short-context reasoning first and triggers semantic retrieval under uncertainty, using high-level intent to guide memory access while reducing noise and token cost.
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
          • Introduces AdaExplore, which distills repeated execution failures into reusable validity-rule memories for future Triton kernel generation.<br>
          • Uses tree-structured candidate organization, local repair, and structural regeneration for diversity-preserving search, improving both correctness and performance optimization.
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
          • Introduces StageMem, treating language-model memory as a stateful lifecycle process rather than static storage.<br>
          • Separates memory into transient, working, and persistent layers, using confidence and strength to support low-cost writing, promotion, updating, and eviction while reducing deep-memory pollution.
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
          • Proposes Federation over Text, where agents upload reasoning traces after independent work and a central server semantically aggregates them.<br>
          • Builds a shared insight repository across tasks and domains, improving downstream accuracy and reducing reasoning cost without gradient updates or supervision.
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
        • Proposes MEDS, a memory-enhanced dynamic reward shaping framework that incorporates historical behavioral signals into reward design to mitigate error collapse during LLM reinforcement learning.<br>
        • Constructs an error memory by reusing layer-wise logits as lightweight representations of reasoning trajectories, applying HDBSCAN clustering to dynamically penalize frequently recurring failure patterns.<br>
        • Demonstrates consistent improvements in both reasoning performance and exploration diversity across multiple math reasoning benchmarks and base models.
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
              • Proposes MemCoT, a test-time memory scaling framework that recasts long-context reasoning as iterative, stateful information search.<br>
              • Uses multi-view long-term memory perception to surface evidence and a task-conditioned short-term memory module to track search history and refine subsequent queries.<br>
              • Achieves state-of-the-art results across several long-memory reasoning benchmarks.
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
              • Introduces SinkTrack, a training-free context anchoring method that exploits the model's attention sink at &lt;BOS&gt; to preserve critical context.<br>
              • Injects key information into the &lt;BOS&gt; representation so the model can retain initial context throughout generation instead of gradually forgetting it.<br>
              • Delivers consistent gains on text and multimodal tasks while reducing hallucination and context forgetting.
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
              • Proposes CoARS, a self-distilled reinforcement learning framework for co-evolving agentic recommender systems.<br>
              • Replaces reliance on external text memory with interaction rewards and self-distilled credit assignment that convert multi-turn supervision into parameter updates.<br>
              • Improves recommendation quality and user alignment over memory-only baselines.
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
              • Introduces CodeComp, a structural KV-cache compression method for agentic coding tasks.<br>
              • Combines static program analysis with code property graphs to preserve structurally critical tokens that attention-only pruning often removes.<br>
              • Outperforms attention-based compression under the same memory budget and integrates into the SGLang pipeline without changing the model.
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
              • Proposes ClawVM, a harness-managed virtual memory layer for stateful tool-using LLM agents.<br>
              • Organizes agent state as typed pages with multi-resolution representations and validates writeback at lifecycle boundaries to avoid stale or destructive state updates.<br>
              • Significantly reduces controllable failures while adding very little policy-engine overhead.
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
              • Presents CodaRAG, an associative retrieval framework inspired by complementary learning for RAG systems.<br>
              • Consolidates fragmented knowledge, navigates semantic and functional links to recover evidence chains, and suppresses distractors during retrieval.<br>
              • Improves both retrieval recall and generation accuracy over prior methods.
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
              • Introduces Astrolabe, a content-addressable hypergraph for semantic knowledge management.<br>
              • Uses content hashes and ordered reference lists to store structured knowledge, while a plugin system interprets records and decomposes structures by width or depth.<br>
              • Demonstrates the extensibility of the design through plugins that bridge informal and formal mathematics.
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
              • Proposes the MemReader family for long-term agent memory extraction, covering both passive structured extraction and active write decisions.<br>
              • MemReader-4B uses GRPO and a ReAct-style process to decide whether information should be written, deferred, retrieved, or discarded.<br>
              • Outperforms prior methods on knowledge updating, temporal reasoning, and hallucination reduction, and has been integrated into MemOS.
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
              • Introduces HyperMem, a hypergraph-based memory architecture for long-term conversation.<br>
              • Models higher-order relations through hyperedges, organizes memory into topic, event, and fact layers, and couples lexical-semantic indexing with coarse-to-fine retrieval.<br>
              • Improves recall and consistency on long-conversation tasks and achieves the best results on LoCoMo.
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
              • Proposes StreamMeCo for long-term memory compression in streaming video understanding.<br>
              • Compresses memory graphs through edge-aware pruning and isolated-node sampling, and adds time-decayed retrieval to offset compression loss.<br>
              • Delivers large memory savings and faster retrieval while maintaining or improving accuracy on multiple benchmarks.
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
              • Introduces a geometric memory management framework for continual visual place recognition in dynamic environments.<br>
              • Decomposes knowledge into static satellite anchors and a dynamic replay buffer, then allocates limited storage with spatially constrained sampling.<br>
              • Improves long-term retention and spatial generalization, and establishes a 21-task benchmark for evaluation.
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
              • Proposes SPASM, a stable persona-driven framework for multi-turn dialogue generation.<br>
              • Uses persona creation, client-responder simulation, and an ECP representation that stores dialogue history in a viewpoint-invariant form before projecting it back to each agent.<br>
              • Reduces persona drift, role confusion, and echoing across long conversations and releases a large-scale dialogue dataset.
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
              • Introduces SkillMOO, a multi-objective optimization framework for software engineering agent skills.<br>
              • Combines LLM-generated edits with NSGA-II selection to evolve skill bundles based on task failures and cost-performance trade-offs.<br>
              • Improves pass rates while lowering cost, and shows that replacing or pruning instructions can outperform simply accumulating them.
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
              • Proposes RecaLLM, which interleaves explicit in-context retrieval with reasoning to address the lost-in-thought problem.<br>
              • Uses constrained decoding to copy evidence spans and trains on both lexical and semantic retrieval tasks.<br>
              • Outperforms baselines on long-context benchmarks such as RULER and HELMET and scales to 128K contexts with relatively modest training data.
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
              • Introduces a constraint-aware corrective memory framework for language-based drug discovery agents.<br>
              • Audits protocols and diagnoses constraint violations, then writes compact corrective feedback into static, dynamic, and correction memory channels.<br>
              • Significantly improves task success rates by keeping planning context compact and actionable.
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
              • Presents ADAM, a systematic data extraction attack on agent memory via adaptive querying.<br>
              • Estimates the memory distribution of the victim and uses entropy-guided queries to maximize leakage.<br>
              • Achieves much higher attack success than prior methods, reaching up to 100% in some settings and highlighting major privacy risks in agent memory.
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
              • Proposes EE-MCP, a self-evolving framework for MCP-GUI agents.<br>
              • Builds a closed loop of environment generation, trajectory collection, task synthesis, and quality filtering, then stores distilled rules in an experience bank for inference-time improvement.<br>
              • Shows that experience-enhanced agents outperform pure distillation in GUI-intensive settings without requiring model fine-tuning.
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
              • Introduces MEMENTO, which teaches LLMs to manage their own context by summarizing long reasoning traces into dense intermediate mementos.<br>
              • Splits reasoning into blocks, generates compact summaries for each block, and continues reasoning from the summaries instead of the full trace.<br>
              • Reduces context length, KV cache usage, and compute cost while preserving reasoning quality, and releases the OpenMementos dataset.
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
              • Studies formal architecture descriptors as navigation primitives for AI coding agents.<br>
              • Shows that structured architecture context can reduce aimless repository exploration and improve behavioral consistency across agent runs.<br>
              • Compares JSON, YAML, and S-expression formats, and introduces <code>intent.lisp</code> and the Forge toolchain.
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
              • Introduces ACGM, a learned graph memory retriever for task-adaptive retrieval over long multimodal web histories.<br>
              • Optimizes sparse relevance graphs with policy gradients and models different temporal decay patterns across visual and textual observations.<br>
              • Outperforms multiple baselines on WebShop, VisualWebArena, and Mind2Web.
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
              • Proposes TSUBASA for long-horizon personalization with evolving memory and self-learning.<br>
              • Improves memory writing through dynamic memory evolution and strengthens memory reading through context-distilled self-learning that internalizes user experience.<br>
              • Outperforms systems such as Mem0 on long-horizon personalization benchmarks while achieving a better quality-efficiency trade-off.
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
              • Introduces DACS, a dynamic attentional context scoping mechanism for multi-agent LLM orchestration.<br>
              • Keeps only lightweight state summaries in registry mode and switches into a focus mode that injects full context for the selected agent while compressing others.<br>
              • Improves steering accuracy and reduces interference from irrelevant agents.
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
              • Proposes LogAct, a shared-log execution framework that turns agents into state machines over an explicit log.<br>
              • Makes planned actions visible before execution, enabling intervention, recovery, semantic replay, and LLM-based introspection from historical traces.<br>
              • Improves reliability, fault recovery, and debugging for agentic systems.
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
              • Introduces the DD-MM-PAS paradigm and the Pask system for intent-aware proactive agents with long-term memory.<br>
              • Combines IntentFlow for latent-need detection, a hybrid workspace-user-global memory design, and a full perception-memory-action infrastructure.<br>
              • Achieves deeper user-intent recognition under low-latency constraints and releases LatentNeeds-Bench.
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
              • Proposes HiExp, a framework that extracts reusable experience knowledge from raw agentic search trajectories.<br>
              • Uses comparative analysis and hierarchical clustering to organize trajectories into layered experience representations and trains agents with experience alignment.<br>
              • Turns stochastic exploration into more strategic search and improves stability, task performance, and cross-task generalization.
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
              • Introduces Global Workspace Agents, a cognitive architecture for LLM agents inspired by global workspace theory.<br>
              • Combines a central broadcast hub with heterogeneous agents, plus entropy-driven intrinsic motivation and a two-tier memory branching strategy.<br>
              • Improves semantic diversity and long-term cognitive continuity in multi-agent execution.
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
              • Proposes ACF, a collaborative framework for covert communication among memory-augmented agents under cognitive asymmetry.<br>
              • Decouples covert signaling from semantic reasoning and uses prefix-independent decoding with shared steganographic configurations to avoid symmetry assumptions.<br>
              • Maintains semantic consistency and covert communication quality even under severe asymmetry, with theoretical error and capacity guarantees.
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
              • Studies rule-level knowledge editing in LLMs and shows that rule knowledge is distributed across layers rather than concentrated locally.<br>
              • Extends the RuleEdit benchmark and uses causal tracing to distinguish how formulas, descriptions, and instances are represented in different layers.<br>
              • Proposes DMLE, which improves rule transfer and understanding while remaining competitive on standard editing metrics.
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
              • Proposes SkillClaw for collective skill evolution in multi-user LLM agent environments.<br>
              • Continuously aggregates user trajectories, detects repeated behaviors and failure modes, and converts them into skill revisions or new skills for a shared repository.<br>
              • Enables cross-user experience transfer and improves performance in real agent settings.
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
              • Introduces SAVeR, a self-auditing framework for faithful reasoning in LLM agents.<br>
              • Generates diverse candidate beliefs, audits them adversarially to locate violations, and applies minimal constrained edits before the agent commits to action.<br>
              • Reduces behavior drift caused by unfaithful reasoning while preserving task performance.
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
              • Proposes SkillForge, a framework for building and self-evolving domain-specific agent skills in cloud technical support.<br>
              • Combines domain-context skill creation with a closed loop of failure analysis, skill diagnosis, and skill rewriting driven by deployment feedback.<br>
              • Improves initial skill quality and continues to raise performance over repeated deployment cycles.
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
              • Revisits experience replay for LLM post-training and questions the assumption that only fresh on-policy data is useful.<br>
              • Analyzes the trade-off between staleness, diversity, and generation cost in replay buffer design.<br>
              • Shows that well-designed replay buffers can cut inference cost substantially without hurting and sometimes even improving performance.
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
              • Formalizes the idea that the environment itself can serve as external memory for an agent.<br>
              • Introduces artifacts as observations that reduce the information needed to represent history and connects the idea to reinforcement learning theory.<br>
              • Shows that observing spatial paths can lower the internal memory needed to learn strong policies and motivates future environment-backed memory designs.
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
              • Proposes MT-OSC, a framework that condenses multi-turn chat history in the background to preserve salient information.<br>
              • Uses a few-shot condenser and a lightweight decision module to retain key facts while compressing irrelevant content.<br>
              • Cuts token usage by up to 72% while maintaining or improving multi-turn dialogue accuracy and latency.
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
              • Proposes M^\star, which represents agent memory as executable Python memory programs rather than fixed schemas.<br>
              • Evolves task-specific memory data structures, storage logic, and interaction workflows through reflective code evolution guided by population search and failure analysis.<br>
              • Outperforms fixed memory baselines across dialogue, embodied planning, and expert reasoning benchmarks while discovering markedly different memory designs per task.
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
              • Proposes LOM-action, an ontology-governed graph simulation framework for auditable enterprise AI decisions.<br>
              • Triggers scenario conditions from business events, performs deterministic graph transformations in isolated sandboxes, and bases decisions only on the resulting scenario-valid graph.<br>
              • Improves accuracy and tool-chain F1 over baselines while generating fully traceable audit logs.
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
              • Proposes LAST, a tool-as-hints framework for improving multimodal spatial reasoning.<br>
              • Packages heterogeneous tool invocations into reusable spatial skills through LAST-Box and returns multimodal prompts that can be consumed directly by the model.<br>
              • Uses a three-stage curriculum to teach adaptive tool use and significantly improves performance on four spatial reasoning datasets.
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
              • The paper introduces LightThinker, a method that achieves efficiency through representation-level thought compression by condensing lengthy reasoning chains into compact hidden states via gist tokens. <br>
              • It proposes LightThinker++, an Explicit Adaptive Memory Management framework that utilizes behavioral primitives such as commit, expand, and fold to dynamically regulate context resolution and mitigate information loss in complex scenarios. <br>
              • The work establishes a specialized trajectory synthesis pipeline to train purposeful memory scheduling, enabling significant reductions in peak token usage and performance gains in both standard reasoning and long-horizon agentic tasks.
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
              • Unifies agent memory, skill discovery, and rule learning as different levels of experience compression, defining a compression function C_L mapping traces to knowledge at levels L0-L3 (raw trace → episodic memory → procedural skill → declarative rule). <br>
              • Reveals that the memory and skill communities are deeply fragmented with only <1% cross-citation rate among 22 core papers (1136 citations), and proposes a full-spectrum agent learning system that adaptively selects compression granularity across levels. <br>
              • Optimization targets include reducing context consumption, lowering retrieval latency, and improving cross-task/model/scenario migration ability; the workflow follows a cyclic pattern where new problems go to memory, repeated patterns compress to skills, and cross-scenario principles become rules.
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
              • The paper introduces Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session and cross-site compromise of web agents through environmental observations without requiring direct memory access. <br>
              • It discovers Frustration Exploitation, a phenomenon where environmental stress and task failures significantly amplify an agent's susceptibility to malicious instructions by up to eight times. <br>
              • The work introduces Chaos Monkey, a methodology inspired by chaos engineering, to systematically evaluate the robustness of LLM-based web agents under realistic deployment conditions such as network latency and input errors.
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
              • Identifying long-horizon agent failures as arising from two coupled but distinct objectives: global progress alignment and local feasibility alignment. <br>
              • Proposing the Neuro-Symbolic Dual Memory Framework that instantiates a neural Progress Memory for stage-aware semantic guidance and a symbolic Feasibility Memory for executable action verification. <br>
              • Demonstrating superior performance across diverse benchmarks including ALFWorld, WebShop, and TextCraft while significantly reducing invalid action rates and trajectory lengths.
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
              • Proposes an agent-native memory architecture where the LLM itself curates, structures, and retrieves knowledge, eliminating the architectural separation and subsequent semantic drift between reasoning agents and external storage pipelines. <br>
              • Introduces the Context Tree, a hierarchical file-based knowledge graph managed by an Adaptive Knowledge Lifecycle (AKL) that employs importance scoring, maturity tiers, and recency decay to evolve knowledge over time. <br>
              • Designs a 5-tier progressive retrieval strategy that minimizes latency by resolving queries through multi-level caching and indexing before escalating to agentic reasoning for novel questions.
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
              • MemFactory presents the first comprehensive framework that unifies the training, evaluation, and inference pipelines for memory-augmented AI agents. <br>
              • The framework features a highly modular architecture that decouples the memory lifecycle into atomic, plug-and-play components such as Extractors, Updaters, and Retrievers. <br>
              • It natively incorporates Group Relative Policy Optimization (GRPO) to facilitate efficient fine-tuning of internal memory management policies driven by multi-dimensional environmental rewards.
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
              • Introduction of a new benchmark for personalized product reranking that incorporates user purchase histories, candidate sets, and human-annotated relevance labels. <br>
              • Development of the MEMRERANK framework that distills long purchase histories into structured, query-independent within-category and cross-category preference memory. <br>
              • Implementation of a reinforcement learning post-training objective to optimize the preference memory extractor for downstream reranking utility.
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
              • OMNI-SIMPLEMEM is proposed as a unified multimodal memory framework for lifelong AI agents that utilizes selective ingestion , progressive pyramid retrieval , and structured knowledge graph augmentation. <br>
              • The system architecture and configurations were autonomously discovered and optimized through AUTORESEARCHCLAW , an autonomous research pipeline capable of code modification, bug diagnosis, and architectural redesign fundamentally beyond the reach of traditional AutoML. <br>
              • The framework achieves state-of-the-art results on LoCoMo and Mem-Gallery benchmarks , demonstrating that autonomously identified bug fixes and architectural changes contribute more significantly to performance gains than cumulative hyperparameter tuning.
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
              • Introduction of SelRoute, a selective routing framework that assigns queries to specialized retrieval pipelines based on their specific query types to optimize long-term conversational memory retrieval. <br>
              • Identification of the enrichment-embedding asymmetry, demonstrating that storage-time vocabulary expansion improves lexical search performance while simultaneously degrading embedding search quality. <br>
              • Achievement of state-of-the-art results on LongMemEval_M using a CPU-only architecture that requires no LLM inference at query time and generalizes across multiple benchmarks.
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
              • Proposes a Multi-Layer Memory Framework (MLMF) that decomposes dialogue history into working, episodic, and semantic layers to separate short-term interaction from long-term abstraction. <br>
              • Introduces an adaptive retrieval gating mechanism and a retention stability objective to regulate semantic drift and preserve persona consistency across extended sessions. <br>
              • Validates the framework through experiments on long-horizon benchmarks, achieving superior retention stability and multi-hop reasoning while reducing context usage and false memory rates.
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
      </tr>
      <tr>
          <td colspan="3">
              • OBLIVION introduces a read/write decoupled memory control paradigm that separates the decision of when to retrieve information from the selection of what to reinforce. <br>
              • The framework implements a hierarchical memory structure consisting of L1 procedural, L2 semantic, and L3 episodic layers integrated with Ebbinghaus-inspired decay-driven activation to manage accessibility without explicit deletion. <br>
              • Empirical evaluations on static and dynamic benchmarks demonstrate that self-adaptive memory control effectively balances learning and forgetting while significantly reducing interference and computational costs in long-horizon interactions.
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
              • GEMS is proposed as an agent-native multimodal generation framework that utilizes a structured multi-agent loop for iterative refinement and closed-loop optimization. <br>
              • A persistent Agent Memory mechanism is introduced to manage historical context through hierarchical compression, preserving factual artifacts while distilling high-level strategic experiences. <br>
              • An extensible Agent Skill module is developed to provide domain-specific expertise via an on-demand loading mechanism, effectively addressing specialized downstream applications.
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
              • Diverse long-context large language model (LLM) inference optimizations are unified into a common four-step memory processing pipeline, which is identified as a primary performance bottleneck through systematic profiling. <br>
              • This research characterizes the quantitative and qualitative computational heterogeneity across pipeline stages, distinguishing between compute-bound regular operations and memory-bound irregular tasks. <br>
              • A GPU-FPGA heterogeneous system is developed to accelerate inference by offloading irregular and memory-bounded operations to FPGAs while retaining compute-intensive tasks on GPUs, achieving significant speedups and energy savings.
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
              • CODEBASE-MEMORY provides a persistent, Tree-Sitter-based knowledge graph architecture supporting 66 languages through a multi-phase parallel build pipeline and incremental synchronization. <br>
              • The system introduces an MCP-based tool interface exposing 14 structural query tools, such as call-path tracing and impact analysis, with sub-millisecond query latency. <br>
              • Empirical evaluation across 31 repositories demonstrates that the approach achieves competitive answer quality while reducing token consumption by ten times and tool calls by 2.1 times compared to traditional file-exploration agents.
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
              • A joint scaling perspective is introduced for LLM multi-agent systems that connects team size and lifelong learning as an interacting scaling space rather than isolated dimensions. <br>
              • LLMA-Mem is proposed as a lifelong memory framework that integrates episodic, procedural, and transactive memory modules to enable cross-task transfer and coordination modeling under flexible memory topologies. <br>
              • Systematic empirical evaluations reveal a non-monotonic scaling landscape where effective memory design enables smaller teams to achieve superior long-horizon performance and token efficiency compared to larger collectives.
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
              • Proposes MemBoost, a memory-boosted LLM serving framework that integrates an Associative Memory Engine, a Meta Controller, and a Large-LLM Oracle to optimize the cost-quality trade-off. <br>
              • Introduces a retrieve-or-escalate decision loop combined with a continuous write-back mechanism to enable efficient semantic answer reuse and memory growth. <br>
              • Demonstrates through experiments on the MMLU-Pro dataset that the framework significantly reduces inference costs and latency while achieving accuracy comparable to or exceeding the oracle model.
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
          • Proposes PersonaVLM, an innovative personalized multimodal agent framework that transforms a general-purpose MLLM (e.g., Qwen2.5-VL) into a personalized assistant via proactive memory management and self-evolving personality alignment.<br>
          • Implements a multi-type memory architecture (core, semantic, episodic, procedural) for complex multi-turn reasoning, with proactive remembering that automatically extracts and summarizes multimodal interaction fragments into a persistent personalized database.<br>
          • Introduces Momentum-based Personality Evolving (PEM) mechanism for consistent response generation, and releases Persona-MME benchmark (2,000+ cases across 14 fine-grained tasks, CVPR 2026) along with full model weights, 80k+ training samples, and evaluation code.
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
          • Proposes MEMMA, a plug-and-play multi-agent framework that coordinates the memory cycle along both the forward and backward paths to address strategic blindness and delayed feedback.<br>
          • Introduces a Meta-Thinker for strategic reasoning during construction and iterative retrieval, and designs an in-situ self-evolving memory mechanism to convert downstream probe failures into direct memory repairs.
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
              • The memory systems of large-model agents are shifting from static retrieval to dynamic autonomous updating, which enhances agent adaptability but also raises serious stability and security concerns. These include semantic drift, program drift that solidifies erroneous workflows, and memory poisoning caused by malicious external injections.<br>
              • It proposes the Stable and Secure Governance Memory (SSGM) framework. The core design principle of this framework is to completely decouple an agent’s “generative cognitive strategies” from the underlying memory storage medium. Between the two, it introduces an actively intercepting governance middleware, so that memory updates are no longer blindly written directly, but must instead pass through multiple gateway checks.<br>
              • Pre-merge validation performs logical consistency checks before writes, rejecting updates that contradict core facts to prevent hallucinations from being solidified. Temporal and permission filtering combines decay functions at read time to filter out outdated or invalid data and uses access control to prevent cross-user privacy leakage. Reversible periodic alignment adopts a dual-track storage structure of “mutable activity graph + immutable situational log,” whereby the system regularly aligns current memory with the immutable log and rolls back errors, thereby imposing a strict mathematical upper bound on long-term semantic drift.
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
              • The paper systematically analyzes the security threats faced by autonomous large language model agents such as OpenClaw across five lifecycle stages: initialization, input, reasoning, decision-making, and execution.<br>
              • A detailed case study on OpenClaw demonstrates the destructiveness of these threats. For example, an attacker can turn transient malicious inputs into long-term behavioral control through “memory poisoning”; and during the decision-making and execution stages, ambiguous instructions may trigger “intent drift,” causing the agent to escalate a simple safety-check task into destructive firewall modifications and high-risk command execution.<br>
              • Mitigation strategies include: plugin verification and signing in the initialization phase; semantic firewall isolation in the input phase; dynamic memory integrity checks and state rollback in the reasoning phase; intent consistency verification in the decision-making phase; and kernel-level sandboxing and least-privilege control in the execution phase.
          </td>
      </tr>
            <tr>
        <td rowspan="2" style="width: 15%;">2026-03-12</td>
        <td style="width: 55%;"><strong>ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Dual--Level--Recurrent--Memory-indigo" alt="Dual-Level Recurrent Memory">
          <img src="https://img.shields.io/badge/Past--Prediction-indigo" alt="Past Observation Prediction">
          <img src="https://img.shields.io/badge/Multi-Modal-yellow" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.12942">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • ReMem-VLA introduces two sets of learnable recurrent memory queries: frame-level queries, which are updated frame by frame to capture short-term memory, and chunk-level queries, which are updated over longer temporal spans to stably maintain long-term memory.<br>
              • A visual prediction head is added, introducing past observation prediction as an auxiliary training objective, which forces the model to recall visual details by reconstructing historical RGB frames. To address the batching challenge of recurrent training on variable-length sequences, a slot-based streaming training paradigm is proposed, which preserves temporal continuity while preventing state leakage across episodes.<br>
              • To overcome the bottleneck of traditional truncated backpropagation through time on long-sequence optimization, the model creatively adopts a gradient-free recurrent update path that combines a frozen VLM with a fixed exponential moving average, allowing the queries to focus solely on learning “what task-relevant information to extract” rather than “how to propagate it.”
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Segment--Level--Memory-indigo" alt="Segment-Level-Memory">
          <img src="https://img.shields.io/badge/Multi--turn-indigo" alt="Multi-turn">
          <img src="https://img.shields.io/badge/Multi--Modal-yellow" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11896">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • Existing streaming multimodal large models typically adopt a serial “perception–generation alternation” paradigm, where text decoding blocks the continuous intake of video, and as long videos progress, the model is prone to forgetting key information from earlier segments. To address this, this paper proposes a novel streaming inference framework that “thinks while watching.”<br>
              • The framework divides a video into multiple segments and, during system operation, dynamically generates and maintains persistent segment-level memory notes online, which support multi-turn question answering via implicit retrieval.<br>
              • Constructs a dedicated three-stage streaming chain-of-thought (CoT) dataset—covering single-turn adaptation, multi-turn interaction, and long-range capability training—and pairs it with segment-level streaming causal masks to ensure strict temporal causality.
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi--turn-indigo" alt="Multi-turn">
          <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/Context%20Mgmt-blue" alt="Context-Optimization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09022">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • In long-horizon multi-agent games, early mistakes are easily amplified, and fixed prompts can lead to rigid strategies and highly variable evaluation results. To address this, this paper proposes MEMO, a self-play framework that requires no updates to model weights.<br>
              • MEMO cleverly decouples and combines the mechanisms of “retention” and “exploration.” It builds a persistent memory bank that uses CRUD (create, read, update, delete) operations to extract structured strategic insights from self-play trajectories and injects them as prior knowledge for subsequent reasoning; meanwhile, it employs tournament-style prompt evolution based on TrueSkill ratings and a prioritized experience replay mechanism to efficiently explore strategies and revisit critical decision states.<br>
              • In five text-based game benchmarks, MEMO demonstrates remarkable learning efficiency: with just 2,000 self-play episodes, it boosts GPT-4o-mini’s average win rate from 25.1% to 49.5%, while simultaneously causing a substantial reduction in the variance of its performance.
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
              • Existing personalized large-model memory systems are typically composed of multiple agents, but most prior methods optimize them independently and locally, neglecting cross-agent collaboration, which means that locally optimal performance cannot guarantee the best global question-answering performance of the overall system.<br>
              • To address the optimization challenges caused by asynchronous execution of heterogeneous agents, the paper proposes the CoMAM framework, which models the execution pipelines of agents—such as fine-grained extraction, coarse-grained profiling, and memory retrieval—as a sequential Markov decision process.<br>
              • To align local task improvements with global system performance, CoMAM quantifies each agent’s contribution by computing the group-level ranking consistency between its local rewards and the global system reward.
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-13</td>
        <td style="width: 55%;"><strong>Structured Distillation for Personalized Agent Memory: 11× Token Reduction with Retrieval Preservation</strong></td>
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
              • It proposes extracting each conversational interaction into a structured composite object that includes core content, specific context, topic classification, and related files. This approach follows a “surviving vocabulary” principle, avoiding arbitrary rewriting of technical terms, and successfully compresses the average number of tokens per interaction from 371 to 38, achieving an 11× compression efficiency.<br>
              • In experiments covering 107 retrieval configurations, it was found that the best pure distilled-text setup can retain 96% of the retrieval quality (MRR) of the original verbatim text. Furthermore, retrieval performance is highly mechanism-dependent: vector search shows virtually no noticeable degradation even under 11× compression, whereas keyword search (BM25) degrades significantly.<br>
              • The agent carries only the compressed distilled text within the context as a “routing index” for efficient retrieval, while the original full conversation text is stored locally and is only brought up for display when the user needs to inspect it in detail.
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
              • Structured episodic memory extraction: TA-Mem introduces an episodic memory extraction agent that uses one-shot prompting to adaptively chunk long contexts based on semantic topic shifts, extracting them into structured memory notes containing summaries, keywords, entities, and events.<br>
              • Tool-driven autonomous memory exploration: It constructs a multi-indexed memory database supporting diverse query methods (e.g., string matching and vector similarity). A tool-augmented retrieval agent can autonomously select appropriate tools and run iterative agentic loops to explore the memory space.<br>
              • Enhanced reasoning and token efficiency: By leveraging precise tool calls and a per-session memory caching mechanism to filter out redundant context, the framework significantly outperforms existing baselines on complex long-range inference tasks (such as the LoCoMo benchmark) while maintaining high token efficiency.
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
              • It points out that current memory retrieval in personalized large models either feeds in the entire history, causing context overload, or relies only on a single similarity search, leading to shallow understanding. To address this, the research team draws inspiration from the dual-process theory of human memory (“recollection–familiarity”) and proposes an adaptive memory retrieval framework called RF-Mem.<br>
              • RF-Mem measures “familiarity” by probing the average similarity scores and entropy of the retrieval. When familiarity is high and uncertainty is low, the system takes a fast “familiarity route,” directly returning the single top-K result; when familiarity is low and uncertainty is high, it instead activates a deeper “recollection route.”<br>
              • When the “recollection route” is triggered, the system clusters the candidate memories and uses an α-mix strategy to update the original query by blending it with the cluster centroids.
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-10</td>
        <td style="width: 55%;"><strong>A Control-Theoretic Foundation for Agentic Systems</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Control--Theory-blue" alt="Control-Theory">
          <img src="https://img.shields.io/badge/Agentic%20Systems-orange" alt="Agentic Systems">
          <img src="https://img.shields.io/badge/Feedback%20Control-pink" alt="Feedback Control">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.10779">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • It proposes a control-theoretic framework that embeds AI agent systems into a feedback control loop for analysis. Rather than treating AI memory, learning, tool invocation, interaction signals, and goal specification as isolated, fragmented functions, this framework unifies and integrates them into a single closed-loop dynamical architecture.<br>
              • It creatively defines a five-level hierarchy of agents based on the extent of “decision authority” that AI holds within the control architecture.<br>
              • Applying this framework to both nonlinear and linear systems, the paper points out that as the agent hierarchy increases, the system will inevitably introduce more complex dynamical mechanisms, such as time-varying adaptation, endogenous switching, decision-induced delays, and structural reconfiguration of the control pipeline.
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-11</td>
        <td style="width: 55%;"><strong>When OpenClaw Meets Hospital: Toward an Agentic Operating System for Dynamic Clinical Workflows</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Multi--Agent-orange" alt="Multi-Agent">
          <img src="https://img.shields.io/badge/openclaw--red" alt="openclaw">
          <img src="https://img.shields.io/badge/healthcare--green" alt="healthcare">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11721">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • Constrain the agents to an isolated environment where they are only allowed to read and write specific files and invoke a pre-vetted “medical skill library,” cutting off arbitrary code execution and network access at the operating-system level to ensure data security and compliance.<br>
              • Instead of traditional vector retrieval, clinical documents are organized into a tree structure augmented with manifests. Relying on natural language understanding to read these manifests, the agents perform “progressive disclosure” navigation, thereby acquiring long-term medical record context in a precise and interpretable manner.<br>
              • Instead of communicating directly, multiple agents collaborate implicitly by append-only writes to shared clinical documents and event subscriptions. This allows the agents to perform on-the-fly task orchestration and flexibly handle complex, long-tail clinical needs that traditional systems cannot address.
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
              • To address the agents’ “amnesia” problem, it systematically and automatically extracts reusable practical experience from their historical execution traces, including clean successes, inefficient successes, failures, and error recoveries.<br>
              • It proposes a complete learning feedback loop that includes trajectory intelligence extraction, decision attribution analysis, contextual learning generation, and adaptive memory retrieval.<br>
              • It achieves comprehensive improvements in agent task performance on the AppWorld benchmark, with particularly pronounced gains on long-horizon tasks that require complex planning.
          </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-03-09</td>
        <td style="width: 55%;"><strong>AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Adaptive-orange" alt="Adaptive">
          <img src="https://img.shields.io/badge/Cognitive%20Evolution-brightgreen" alt="Cognitive Evolution">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.09716v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • It structures the agent’s cognition into “internal cognition” and “external cognition.” This cognition, treated as an updatable state of the agent, is continuously self-corrected and evolved based on the actual outcomes of task interactions, thereby providing a more accurate and less biased knowledge foundation for decision-making.<br>
              • It adopts a dynamic “select–execute–update” loop for problem solving. The action space is uniformly divided into “emic actions” (self-driven) and “etic actions” (collaborative), enabling the agent to adaptively plan its next step entirely based on the current context and real-time cognition.<br>
              • To tackle context redundancy and token consumption in long-sequence reasoning, the system designs an Elastic Memory Orchestrator (EMO) that dynamically compresses historical trajectories, filters redundant information, and extracts reusable episodic memories.
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
              • It compares the multi-agent memory system to a classic computer system, distinguishing between two basic architectural prototypes: shared memory and distributed memory.<br>
              • It proposes an architecture-inspired three-layer memory hierarchy (I/O layer, cache layer, and memory layer), and identifies two critical missing protocols: an agent cache sharing protocol, and an agent memory access protocol that regulates read/write permissions and granularity.<br>
              • In the future, the most pressing challenge in building multi-agent systems is ensuring memory consistency. This requires the system to properly handle read-time conflicts, the visibility and ordering of update operations when multiple agents concurrently read and write shared memory, and to establish clear versioning and conflict resolution rules in order to maintain coherence of the global context.
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
            • Proposes Hippocampus, an efficient and scalable memory module for agentic AI that replaces dense-vector or graph-heavy retrieval with compact binary signatures and lossless token-ID streams.<br>
            • Introduces a Dynamic Wavelet Matrix (DWM) to jointly compress and index semantic signatures and reconstructable content, enabling ultra-fast search directly in the compressed domain.<br>
            • Experiments on LoCoMo and LongMemEval show up to 31× lower end-to-end retrieval latency and up to 14× fewer per-query tokens while maintaining accuracy.
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
            • Proposes the Traversal-as-Policy paradigm, which distills execution logs into structured Gated Behavior Trees (GBT) and replaces unconstrained generation with deterministic tree traversal at runtime, achieving externalized and verifiable Agent policies.<br>
            • Introduces Spine Memory to record traversal paths, effectively solving the problems of implicit strategy and post-hoc safety in long-horizon tasks.<br>
            • Experiments validate that this method can simultaneously improve success rates and significantly reduce violation risks and token consumption across software engineering, Web Agent, and safety domains.
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
        <a href="https://ojs.aaai.org/index.php/AAAI/article/view/40644">
        <img src="https://img.shields.io/badge/AAAI-Paper-%23003087?logo=aaai" alt="Paper Badge">
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
          • This paper introduces LegalWorld, which models Chinese civil litigation as a five-stage causal state chain encompassing legal consultation, preparation of initiating pleadings, first-instance proceedings, appeal, and second-instance proceedings. This design enables early factual representations, evidence organization, and litigation strategies to impose realistic constraints on subsequent procedures and adjudicative outcomes.<br>
          • The environment is built on 75,309 paired first- and second-instance judgments and incorporates local in-scenario memory, global case memory, and modular libraries of skills and tools. Local memory maintains conversational continuity within an individual scenario, while global memory consolidates case facts, evidence, claims, and procedural status at the conclusion of each stage to ensure cross-stage consistency.<br>
          • LongJud-Bench, constructed on this environment, evaluates agent capabilities across the complete litigation lifecycle. A total of 217 evaluators with legal backgrounds provided 18,992 ratings, validating the procedural realism and role consistency of the generated trajectories. Cross-model experiments further demonstrate substantial specialization across legal consultation, document drafting, and courtroom argumentation, indicating that a single aggregate score cannot reveal these stage-specific capability differences.
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
          • This paper introduces GateMem, extending memory evaluation from single-user private memory to multi-principal shared-memory settings. Agents must enforce context-dependent controls over the reading and disclosure of information in a shared memory pool according to the requester’s identity, role relationships, authorization scope, and deletion status.<br>
          • The benchmark spans four domains—healthcare, workplace, education, and household settings—and comprises 91 long-form multiparty interaction scenarios with 2,218 hidden checkpoints. It jointly measures the practical utility of legitimate long-horizon requests, information leakage across authorization boundaries, and the reliability of active forgetting following explicit deletion requests.<br>
          • Experiments reveal a pronounced tension among utility, access control, and forgetting. Long-context methods generally achieve stronger overall governance performance but incur substantial token overhead. Although retrieval-augmented and external-memory methods reduce computational costs, they may still disclose unauthorized information or recover deleted content, indicating that current systems remain inadequate for reliable institution-scale shared-memory deployment.
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
          • This paper introduces MemTrace, advocating user “knowledge points” with explicit types and session provenance as the unit of long-term memory evaluation, rather than aggregating mutually independent question instances into a single accuracy score. This formulation enables the persistent availability of the same fact to be traced across varying conditions.<br>
          • The benchmark generates probes along three controlled dimensions: memory recency, question type, and evidence condition. These dimensions respectively assess the retention of facts as the number of sessions increases; the ability to answer questions about current states, historical states, and trajectories of change; and the capacity to respond safely when evidence is absent or a question contains a false premise.<br>
          • MemTrace covers 20 users, 835 knowledge points, 15,422 question instances, and 13 memory-system configurations. Experiments show that systems with similar aggregate accuracy may exhibit fundamentally different failure structures. Moreover, when failures occur, relevant evidence is retrievable approximately ten times as often as it is absent, indicating that the primary bottleneck lies in the effective use of accessible evidence during reasoning rather than solely in storage capacity or retrieval recall.
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
          • This paper distinguishes between the recall plane, which retrieves existing facts, and the control plane, which governs memory overwriting, release, deletion, and updating. It investigates how the placement of large language models within these two planes systematically alters modes of forgetting failure.<br>
          • The authors construct the ForgetEval evaluation suite, comprising 1,000 template-based test cases and 385 adversarial cases, and compare 13 system configurations across six architectural paradigms. The results show that deterministic rules, write-time LLM processing, knowledge-graph abstraction, and mutation-time hooks address distinct lexical, temporal, normalization-related, and intent-aware forgetting challenges, offering partially complementary capabilities.<br>
          • Mutation-time LLM hooks increase the pass rate on 345 non-primitive existence cases from approximately 70% to over 93% and restore intent-aware deletion under prefix collisions and compound-fact conditions. The study therefore demonstrates that forgetting capability depends on where intelligent control is situated within the memory lifecycle, rather than merely on whether the system employs a large language model.
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
          • This paper introduces StreamMemBench, extending the evaluation target of personal-agent memory from static factual recall to the complete streaming assistance pipeline. It examines whether an agent can identify and retain user-relevant evidence from continuous first-person observations and apply that evidence to both current and subsequent tasks.<br>
          • The benchmark is constructed from EgoLife egocentric life streams and uses evidence anchors to connect initial tasks with follow-up tasks. Four metrics—Fidelity, Initial Evidence Use, Feedback Incorporation, and Follow-up Reuse—respectively diagnose evidence preservation, initial application, feedback assimilation, and experiential reuse.<br>
          • The dataset comprises 8,107 evidence anchors and 16,214 task queries. Evaluation of eight classes of memory systems across two model backbones shows that storing information, or incorporating feedback within the current interaction, does not ensure that an agent can reliably invoke the relevant experience in future tasks. These findings indicate that memory evaluation should primarily assess its actual influence on subsequent behavior.
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
          • This paper shows that persistent memory systems in LLMs amplify sycophancy, causing models to prioritize user-aligned beliefs over factual correctness. <br>
          • It introduces the MIST benchmark and evaluates multiple state-of-the-art memory systems and model families, systematically measuring this effect. <br>
          • The authors propose lightweight mitigation strategies that significantly reduce sycophancy while maintaining or improving factual recall performance.
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
          • This paper introduces H2HMem, a multimodal benchmark designed to evaluate agent memory in complex human-human interaction settings beyond single-user text conversations. <br>
          • It includes dyadic and multi-party dialogues and evaluates memory across recall, reasoning, and application dimensions. <br>
          • Results show that current systems struggle with cross-modal, cross-participant, and long-horizon memory construction and utilization, highlighting key limitations of existing agents.
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
          • Addresses the fact that long-term memories may complement, diverge from, or contradict each other.<br>
          • Constructs relation-controlled memory variants and embeds them into realistic long user-agent histories.<br>
          • Reveals that current memory systems remain weak at fine-grained relational memory preservation and use.
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
          • Studies when available sensitive memories should not be used in the current conversational turn.<br>
          • Introduces RBI-Eval, a controlled probe set comparing model behavior with and without sensitive memory access.<br>
          • Shows retrieval alone cannot ensure safety, motivating memory-aware decisions at both retrieval and generation time.
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
          • Targets the lack of benchmarks for LLM systems learning from accumulated service-time user feedback.<br>
          • Builds a user-feedback simulation framework across multiple domains, languages, and task types.<br>
          • Shows current baselines remain far from satisfactory in both effectiveness and efficiency.
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
          • Combines two hard capabilities: navigating multi-session dialogue memory and reasoning over long documents.<br>
          • Creates synthetic microworlds with characters, event timelines, long documents, conversations, and mixed-source questions.<br>
          • Shows joint retrieval architectures better integrate conversational memory with document navigation.
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
          • Frames persistent memory as a long-lived attack surface where untrusted inputs can shape future behavior.<br>
          • Identifies write channels, structural vulnerabilities, and memory poisoning attack categories, and introduces MPBench.<br>
          • Shows active memory systems are especially vulnerable and that prompt-injection defenses are insufficient.
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
          • Studies safety risks introduced by persistent long-term memory in conversational assistants.<br>
          • Defines cross-domain leakage and memory-induced sycophancy as memory-specific failure modes.<br>
          • Evaluates many frontier and open-source LLMs and reveals high failure rates on both risks.
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
          • Addresses the static and homogeneous nature of many long-term dialogue memory benchmarks.<br>
          • Constructs evolving user profiles, heterogeneous interactions, and challenging questions across memory types.<br>
          • Reveals weaknesses in current systems under realistic, dynamic long-term memory settings.
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
          • Targets streaming episodic memory for egocentric vision, where agents must remember over continuous input.<br>
          • Builds diagnostic questions across multiple cognitive dimensions under a unified streaming MLLM framework.<br>
          • Exposes key weaknesses of current memory management mechanisms in visual-agent settings.
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
          • Argues that multimodal agent memory should be tested through interaction with dynamic worlds.<br>
          • Builds a four-stage action-world loop and multi-session tasks to evaluate writing, maintenance, retrieval, and use.<br>
          • Shows that better storage quality does not always translate into better downstream multimodal memory performance.
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
          • Targets reflective memory, where agents must synthesize fragmented cues rather than only recall explicit facts.<br>
          • Introduces RefMem-Bench with annotated QA instances across reflective-memory dimensions and task formats.<br>
          • Shows that question-guided evidence retrieval and abstraction-aware supervision improve reflective answering.
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
          • Addresses the gap between single-session agent benchmarks and realistic multi-session service interactions.<br>
          • Creates tool-mediated tasks with persistent memory, temporal dependencies, changing user goals, and consequential actions.<br>
          • Shows current agents often fail by misestimating user state across sessions.
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
          • Targets real-world long-horizon visual memory for AI assistants using egocentric daily activity video.<br>
          • Builds human-validated VQA pairs covering object, location, intention, and scene memory.<br>
          • Shows current systems remain unreliable for practical everyday visual memory needs.
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
          • Introduces RHELM, a benchmark that simulates one-year virtual life trajectories of 10 diverse personas (500K–1M tokens context per user) to evaluate LLMs' realistic, heterogeneous, and evolving long-term memory capabilities.<br>
          • Proposes the LOOP module (pLan-rOllout-evOlve-Prune) to dynamically generate life trajectories and integrates heterogeneous external sources (emails, diaries, reports) alongside 11,764 dialogue turns, enabling high-fidelity multi-source memory evaluation.<br>
          • Defines 7 question types and 27 challenge characteristics, including memory-conditioned misleading queries that test conflict-aware responses; shows that SOTA models like Claude Opus 4.5 only score ~38% on average, with cross-source aggregation and real-world contextual reasoning as the dominant bottlenecks.
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
          • Introduces STALE, a long-context benchmark of 400 expert-validated implicit conflict scenarios to evaluate LLM agents' ability to detect when earlier memories are invalidated by new observations without explicit negation.<br>
          • Proposes a three-dimensional probing framework that tests State Resolution, Premise Resistance, and Implicit Policy Adaptation, revealing that current models struggle to apply updated states in downstream behavior.<br>
          • Presents CUPMEM, a prototype framework that performs explicit write-time state adjudication and topology-triggered belief propagation, significantly improving robust memory updating.
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
          • Proposes MEMAUDIT, an exact evaluation protocol that fixes experience streams, candidate memory representations, storage costs, evidence units, future queries, and budgets as an auditable optimization problem solvable by branch-and-bound and MILP.<br>
          • Distinguishes memory representation quality, validity retention, and budget allocation effects, outperforming end-to-end QA accuracy as an evaluation approach.
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
          • Introduces StratMem-Bench with 657 dialogue instances and mandatory/auxiliary/irrelevant memory pools to evaluate strategic memory use beyond factual recall in virtual character conversations.<br>
          • Designs metrics for strict memory compliance, memory integration quality, proactive enrichment, and conditional irrelevance rate, systematically assessing memory decision-making in role-play.
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
            • Introduces MemHomeLife and MemHome, a benchmark suite for memory-driven smart home control grounded in long-term real interaction logs.<br>
            • Evaluates fine-grained memory operations including adding, updating, deleting, and using memories in device control.<br>
            • Addresses a major gap in prior benchmarks by measuring both long-term memory utilization and feedback on memory management quality.
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
            • Introduces OmniBehavior, the first benchmark built entirely from real-world data for long-horizon, cross-scenario, heterogeneous behavior simulation.<br>
            • Highlights that real user decisions depend on cross-scenario causal chains that are largely missing from prior datasets.<br>
            • Shows that current LLMs remain weak on complex behavior simulation even with longer contexts, and exhibit homogenized personalities and optimistic bias.
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
            • Introduces KnowU-Bench, an online benchmark for interactive, proactive, and personalized mobile agents in Android simulation.<br>
            • Hides user profiles and provides only behavioral traces, requiring agents to infer preferences through interaction and decide when to intervene, ask consent, or stay silent.<br>
            • Reveals large performance drops for frontier models when preference inference and intervention calibration are required.
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
              • Proposes a unified modular framework that decomposes LLM-based agent memory systems into four essential components: information extraction, memory management, memory storage, and information retrieval. <br>
              • Conducts a comprehensive experimental evaluation and robustness analysis of representative agent memory methods on long-term conversational benchmarks, examining token efficiency, context scalability, and evidence position sensitivity. <br>
              • Introduces a novel memory architecture that integrates tree-based organization with hierarchical storage to achieve state-of-the-art performance while maintaining low computational overhead.
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
          • This paper introduces FlashAdventure, a benchmark for evaluating GUI agents on long-horizon, narrative-driven tasks requiring memory, planning, and interaction across complete story arcs. <br>
          • It identifies the observation–behavior gap, where agents must recall earlier observations and apply them later when those memories become actionable. <br>
          • The authors propose COAST (Clue-Oriented Agent for Sequential Tasks), an agent framework using long-term clue memory with a Seek-Map-Solve cycle to improve sequential decision-making. <br>
          • The benchmark contains 34 Flash-based adventure games and evaluates agents through milestone-based automated scoring with CUA-as-a-Judge. <br>
          • FlashAdventure demonstrates that explicit long-term memory enables GUI agents to better store, retrieve, and utilize historical information in long-horizon interactive environments.
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
        • Introduces Muse, the first multimodal conversational recommendation dataset, containing 83,148 utterances across 7,000 conversations in the Clothing domain with scenario-grounded user profiles.<br>
        • Proposes a three-stage multi-agent generation pipeline (User Profile Generator → Simulated Dialogue Generator → Dialogue Optimizer) powered by multimodal LLMs, where user profiles are derived from real-world scenarios rather than manual design, improving scalability.<br>
        • Validates quality against four baselines (MMCONV, Redial, Inspired, PEARL) across five dimensions (naturalness, coherence, informativeness, product-context relevance, image-text consistency) and demonstrates utility by fine-tuning three MLLMs for recommendation and response generation.
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
          • This paper introduces AtomMem, which adopts high-value atomic facts as the fundamental representational units of long-term memory. It seeks to balance the redundancy and overhead associated with preserving complete conversations against the loss of detail caused by excessive summarization, while mitigating the content drift and instability introduced by unconstrained memory updates.<br>
          • The system first employs a Fact Executor to selectively extract independent, verifiable, and information-dense facts from extended interactions, subsequently organizing them into hierarchical event structures and temporal profiles. The former preserve event-level episodic relationships, while the latter track dynamic changes in user preferences, goals, and attributes over time.<br>
          • During retrieval, an associative memory graph connects facts distributed across different events and time points to support cross-session, multi-hop, and temporal reasoning. Experiments on LoCoMo show that AtomMem achieves leading results across multiple reasoning categories, demonstrating that atomic representations must be integrated with event hierarchies, temporal evolution, and associative retrieval; merely partitioning memory into shorter text segments is insufficient to establish stable long-term memory.
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
          • This paper introduces FinAcumen, which accumulates financial multimodal reasoning trajectories across tasks, distills successful cases into reusable strategies, and converts failed trajectories into risk-warning rules. The framework addresses the tendency of stateless tool-using agents to repeatedly explore the same strategies, invoke tools incorrectly, and generate financial hallucinations.<br>
          • During inference, the system employs a selective experience-activation mechanism that injects retrieved experience into the reasoning context only when its semantic relevance to the current problem exceeds a calibrated threshold. When an experience is unreliable or insufficiently relevant, a fallback pathway explicitly suppresses its influence. A deterministic financial tool environment is then used to perform numerical calculations, information retrieval, chart interpretation, and answer verification.<br>
          • Across four financial multimodal reasoning benchmarks, FinAcumen consistently improves a frozen 8B vision-language model and, under certain settings, outperforms finance-specialized models while approaching leading proprietary general-purpose models. Further analysis shows that these performance gains depend on the selective use of experience rather than the unconditional expansion of memory injection.
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
          • This paper observes that existing interactive video world models generally employ history-compression strategies biased toward recent frames, which may discard critical event-transition frames that determine subsequent object states. This produces an “action-forgetting” problem in which a model can navigate but fails to retain the consequences of actions such as opening doors, picking up objects, or triggering physical changes.<br>
          • ActWorld introduces hierarchical action-aware memory into a chunk-wise autoregressive generation framework. Historical segments are assigned different compression pathways according to their importance for object interactions and state changes, while a persistent memory bank retains event-update tokens and object-identity tokens over the long term to preserve causal continuity across extended rollouts.<br>
          • The authors also construct a dataset containing approximately 100,000 human–computer interaction videos with chunk-level reasoning annotations. Experiments show that the model supports both free-viewpoint navigation and intermediate object interaction within a unified system, improving interaction fidelity without compromising viewpoint controllability. These findings indicate that long-term history management in world models must be governed by action causality rather than temporal recency alone.
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
          • This paper introduces PreAct, which compiles the trajectory of a computer-using agent’s first successful task completion into a compact state-machine program. States verify current screen conditions, while transitions execute actions such as clicking and text entry, transforming repeated tasks from instances of renewed reasoning into executable procedural-memory replay.<br>
          • Replay is not performed unconditionally: before executing each step, the system verifies whether the screen matches the program’s expected state and returns control to the general-purpose agent upon detecting an interface deviation. A new program is written to the long-term program repository only after it has been replayed in a clean environment and an independent evaluator has confirmed complete task execution.<br>
          • Across mobile, desktop, and web benchmarks, direct program replay achieves an 8.5- to 13-fold speedup without requiring step-by-step LLM calls, while write-time validation prevents defective programs from accumulating. The experiments further show that the system’s gains arise primarily from reliable program validation and reuse rather than prompt adjustments, runtime safeguards, or more sophisticated program retrievers.
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
          • This paper introduces CoreMem, an edge–cloud long-term memory architecture unified through information geometry. It is designed to address simultaneously the hubness problem in high-dimensional vector retrieval, semantic loss during context compression, and the constraints on GPU memory and computational resources imposed by consumer-grade devices.<br>
          • At the retrieval stage, CoreMem replaces isotropic cosine similarity with a locally adaptive Fisher–Rao Riemannian metric and uses a low-rank Woodbury acceleration scheme to enable real-time search. At the compression stage, Fisher-guided discrete token distillation progressively selects content from the sentence level to the token level according to parameter sensitivity, while explicitly preserving grammatical and structural information.<br>
          • Experiments on LoCoMo and LongMemEval-S report improvements of 4.51 percentage points in open-domain reasoning and 4.17 percentage points in temporal reasoning, while operating within a strict 8 GB GPU-memory budget. The principal significance of this work lies in providing a unified theoretical foundation for retrieval and compression, although its efficiency claims remain dependent on the adopted low-rank approximations and edge–cloud deployment configuration.
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
          • This paper proposes a hierarchical memory architecture for personalized presentation generation that explicitly separates cross-task long-term memory from working memory within an individual editing session. It further divides long-term memory into user-profile memory and tool memory to accommodate distinct temporal scales and functional objectives.<br>
          • User-profile memory retrieves stable preferences according to task intent and provides personalized conditioning for initial generation. Working memory continuously maintains newly introduced constraints and revision requirements during the current session. Tool memory stores reusable execution experience for localized editing and is combined with a scope-constrained slide-modification mechanism to reduce unnecessary regeneration of unrelated slides and elements.<br>
          • Controlled experiments show that user-profile memory improves persona consistency across multiple roles and intents, while tool memory enhances the execution reliability of closed-loop revisions. Case analyses also validate the role of working memory in preserving preferences across turns. These findings indicate that effective personalized generation requires memory to be functionally stratified by persistence and responsibility rather than consolidated into a single unified memory pool.
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
          • To address the strong dependence of conventional learner simulation on extensive individual interaction histories, this paper proposes a cohort-aware “roll-call” simulation paradigm. It first constructs a cohort-level ability prior from the logs of similar learners and then calibrates an individual’s knowledge state through a small number of targeted diagnostic interactions.<br>
          • Edu-Theater employs a teacher agent to coordinate the overall simulation process and dynamically switches between cohort-level priors and individual-level evidence through retrospective roll-call probing of historical learning logs. This design transforms historical logs from complete per-user contexts into shared cohort memory and sparse individual states, alleviating cold-start challenges and reducing invocation costs in large-scale deployment.<br>
          • Experiments on two real-world educational datasets show that the framework achieves higher accuracy in simulating future behavior with substantially fewer LLM calls, while its generated data also improve downstream tasks such as adaptive testing. Its primary contribution lies in enhancing the efficiency of state reconstruction for educational agents rather than establishing a general-purpose personal long-term memory system.
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
          • This paper observes that mainstream long-term conversational memory systems generally rely on lexical or embedding similarity and can therefore handle only descriptive recall in which queries exhibit explicit surface-level overlap with historical content. Such systems struggle to identify associative memories connected through causal, narrative, or latent semantic relationships.<br>
          • Inspired by episodic future thinking, T-Mem proactively generates triggers such as Entity, Bridge, Scene, and Horizon during memory writing. It simultaneously establishes descriptive and associative access pathways at both the factual and full-conversation granularities, enabling historical information to be reactivated by potentially relevant future contexts rather than by its original wording.<br>
          • Experiments show that T-Mem achieves leading results on both LoCoMo and the cognitively associative LoCoMo-Plus, reducing the performance gap between the two benchmarks to 5.45 percentage points. Ablation studies further demonstrate that scene-level associative triggers are particularly important for LoCoMo-Plus, indicating that future-oriented write-time indexing is the principal mechanism for overcoming the limitations of similarity-based retrieval.
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
          • This paper introduces GitOfThoughts, which maps an agent’s reasoning tree onto a Git repository: scored reasoning nodes correspond to commits, parent–child reasoning relationships correspond to commit history, and scores and verification results are recorded through notes and tags, respectively. This design supports deterministic replay, line-by-line comparison, provenance tracing, and cross-agent merging.<br>
          • The study compares five memory substrates—no memory, Markdown, vector databases, graph databases, and Git—on GPQA-Diamond and MATH-500. A preregistered replication experiment finds that no memory format consistently improves accuracy on genuinely novel problems, and the positive trends observed initially fail to replicate after the sample size is expanded.<br>
          • Memory gains emerge primarily above a “copyability threshold,” where retrieved cases are highly similar to the current problem, and the resulting improvement more closely resembles answer reuse than methodological transfer. The central value of GitOfThoughts therefore lies not in improving generalization accuracy, but in providing auditability, reproducibility, and collaborative governance of reasoning processes while maintaining broadly comparable accuracy.
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
          • This paper proposes Maestro, a workload-aware cross-cluster scheduling system designed for LLM-based multi-agent systems in resource-constrained cloud environments. <br>
          • It predicts token output length and memory usage per stage to drive a hierarchical scheduler supporting dynamic multi-model co-location and elastic memory allocation. <br>
          • Experiments show that Maestro significantly reduces memory overhead while improving SLO fulfillment and overall system efficiency.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-11</td>
        <td style="width: 55%;"><strong>Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent-Memory-4A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Cognitive-Model-F5A623" alt="Cognitive Model">
          <img src="https://img.shields.io/badge/Memory-Policy-7ED321" alt="Memory Policy">
          <img src="https://img.shields.io/badge/Explainability-Concept-D0021B" alt="Explainability">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12945v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This work introduces a cognitively grounded multi-factor memory value model to guide storage, retention, and forgetting decisions under limited memory budgets for LLM agents. <br>
          • It integrates seven interpretable factors (e.g., emotional intensity and goal relevance) into a unified framework for encoding and retrieval policies. <br>
          • Results show improved memory efficiency and retention quality compared to baselines, along with strong interpretability and lightweight deployment.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-05</td>
        <td style="width: 55%;"><strong>Rosetta Memory: Adaptive Memory for Cross-LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Cross-LLM-4A90E2" alt="Cross-LLM">
          <img src="https://img.shields.io/badge/Memory-System-F5A623" alt="Memory System">
          <img src="https://img.shields.io/badge/Adaptation-7ED321" alt="Adaptation">
          <img src="https://img.shields.io/badge/Robustness-D0021B" alt="Robustness">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.07711">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • Rosetta Memory transforms stateless LLMs into persistent, cross-model memory systems that remain effective across different model switches and task distributions. <br>
          • It introduces conditional operators that optimize how memory is stored and presented, enabling compatibility across heterogeneous LLM architectures. <br>
          • Experiments demonstrate strong robustness across benchmarks, maintaining performance even under unseen model substitution scenarios.
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent-Memory-4A90E2" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Long-Horizon-F5A623" alt="Long Horizon">
          <img src="https://img.shields.io/badge/System-Analysis-7ED321" alt="System Analysis">
          <img src="https://img.shields.io/badge/Memory-Cost-D0021B" alt="Memory Cost">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/abs/2606.06448">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • This paper redefines agent memory as a stateful long-horizon workload rather than a simple retrieval-augmented component. <br>
          • It introduces a stage-aware analytical framework that decomposes memory system costs across build, retrieval, and generation phases. <br>
          • Through analysis of multiple systems, it derives system-level insights on scheduling design, latency trade-offs, and scalable deployment.
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
          • Addresses context-window loss in long productive LLM sessions where important decisions and files disappear.<br>
          • Models session history as a typed knowledge graph and serializes it into compact resume blocks.<br>
          • Improves decision and file recall at lower token cost, providing a practical context-management system.
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
          • Highlights that embodied agents need memory searchable by meaning, space, and time simultaneously.<br>
          • Builds a hybrid graph memory with multiple indexes and tool-facing retrieval functions.<br>
          • Adds eMEM-Bench around cognitive psychology paradigms to evaluate embodied memory behavior.
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
          • Examines whether agentic memory systems generalize beyond the single scenarios they are often designed for.<br>
          • Compares multiple memory systems across diverse scenarios and introduces AutoMEM as a self-managed baseline.<br>
          • Shows that active agent control over storage and retrieval is more robust than fixed passive pipelines.
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
          • Targets long-horizon agents running across resource-constrained edge models and stronger cloud models.<br>
          • Uses decentralized execution with centralized reflection to filter reusable experience and circulate insights.<br>
          • Improves progress and grounding without updating model parameters, showing a practical cloud-edge memory pattern.
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
          • Provides an independent evaluation of long-term memory backends in distributed multi-agent systems.<br>
          • Measures accuracy, latency, CPU time, RAM, disk I/O, network use, and total cost under cloud-edge scenarios.<br>
          • Finds large cost-accuracy differences across vector, graph, hybrid, RAG, and full-context approaches.
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
          • Describes a production long-term semantic memory system for LinkedIn's hiring agent.<br>
          • Extracts signals from noisy behavioral data, stores them hierarchically, and supports low-latency retrieval under privacy constraints.<br>
          • Reports improvements in correctness and personalization, offering a rare deployed memory-system case study.
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
          • Argues cross-session LLM memory is a state management problem, not a search problem, and introduces a typed belief schema with five belief types, epistemic status, versioned supersession, and a `why_it_matters` field that converts extracted facts into imperative instructions rather than declarative facts.<br>
          • Demonstrates that cosine similarity over dense embeddings achieves mean precision of 0.12 on a 72-case retrieval suite, while alias-weighted BM25 with hard scope isolation achieves 1.0, passing 72/72 cases; under multi-turn topic drift, vector search produces drift scores of 0.43–0.50 on noise-critical turns while BM25 maintains 0.0.<br>
          • Ships as a local-first OpenAI-compatible proxy that injects curated belief context into every LLM session transparently; includes a reusable 72-case benchmark covering alias resolution, scope disambiguation, supersession chain exclusion, and session-level noise isolation.
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
          • Proposes Memini, a directed associative memory system for LLMs that continually updates knowledge through multi-timescale memory dynamics driven directly by incoming document streams.<br>
          • Implements coupled fast and slow variables on graph edges based on the Benna-Fusi model, inherently enabling episodic sensitivity, gradual consolidation, and selective forgetting without explicit rules.<br>
          • Leverages spreading activation over experience-shaped, dynamic edge weights for retrieval, allowing the memory substrate to autonomously reorganize and adapt to evolving evidence.
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
          • Proposes True Memory, a six-layer agent memory architecture that shifts from extraction-based storage schemas to a multi-stage retrieval pipeline operating over verbatim conversational events.<br>
          • Introduces a three-signal encoding gate (novelty, salience, prediction error) and achieves strong performance across LoCoMo, LongMemEval, and BEAM-1M benchmarks using a single SQLite file on commodity CPUs.
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
          • Proposes MEMTIER, a tripartite memory architecture for long-running autonomous agents that addresses context collapse, compaction discontinuity, structural blindness, and missing attribution loops in existing flat-file systems.<br>
          • Features a structured episodic JSONL store, a five-signal weighted retrieval engine, an asynchronous consolidation daemon, and an attention-attributed cognitive weight update loop with a PPO-based policy framework.<br>
          • Achieves significant performance improvements on the LongMemEval-S benchmark, demonstrating that high-precision, structurally isolated memory (episodic vs. semantic) drives long-horizon success while highlighting legacy linear-combination retrieval as the current bottleneck.
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
          • Analyzes functional circuits inside LLM agent memory systems across Qwen-3 scales with mem0 and A-MEM frameworks, tracing write, manage, and read circuits.<br>
          • Discovers that routing-control circuits can emerge before content circuits in small models, and leverages feature-space separation for unsupervised stage-wise fault localization of silent memory failures.
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
          • Proposes Deco, a dual-embodiment framework extending personal physical objects into pervasive AI companions using multimodal LLMs and augmented reality with synchronized digital-physical interaction.<br>
          • Introduces Reciprocal Memory as a design principle for sustaining emotional bonds, with a 7-day deployment study showing improvements in companionship, emotional connection, and sustained engagement.
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
          • Introduces Skilldex, a package manager and registry for LLM-agent skill packages, using a format-consistency score to check compliance with Anthropic skill conventions.<br>
          • Adds the skillset abstraction to bundle related skills and shared resources, with three-level scope distribution, human-feedback suggestion loops, a metadata registry, and an MCP server.
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
          • Presents Bolzano, an open-source multi-agent LLM system that coordinates parallel proving and verification agents while maintaining a persistent knowledge base across turns.<br>
          • Solves six problems in mathematics and theoretical computer science, with four publishable-level results and three produced almost autonomously.
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
          • Introduces GenericAgent, a self-evolving LLM agent for long-horizon tasks that maximizes decision-relevant information density in limited context.<br>
          • Combines a minimal toolset, hierarchical on-demand memory, self-evolution, and context truncation/compression, converting verified trajectories into reusable SOPs and code.
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
              • Proposes Mosaic, a cross-modal clustering system for efficient long-video understanding.<br>
              • Finds implicit clustering structure in VLM KV caches and uses clusters as the unit for cache organization, maintenance, and retrieval.<br>
              • Reduces fragmented transfers and management cost, achieving up to 1.38x speedups in streaming video inference.
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
              • Proposes EpiAgent, an agent-centric system for ancient inscription restoration.<br>
              • Uses an Observe-Conceive-Execute-Reevaluate loop in which a central LLM planner coordinates multimodal analysis, historical experience, tools, and self-reflection.<br>
              • Outperforms prior methods on real restoration tasks and improves both quality and generalization.
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
              • Reports the lessons from taking Zup's internal coding agent CodeGen from prototype to production.<br>
              • Shows that reliability depends not just on the base model but also on tool design, safety guardrails, state management, and human oversight.<br>
              • Uses string-replacement editing, layered safety constraints, and progressive supervision to raise adoption and reliability while outlining open questions.
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
              • Proposes PSI, a shared-state architecture that connects separately generated personal AI modules into a coherent tool ecosystem.<br>
              • Exposes current state through a personal context bus and supports writeback so modules can reason across each other and stay synchronized.<br>
              • Demonstrates that the system can automatically integrate later-generated tools in a three-week personal AI deployment.
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
              • Proposes Omakase, a proactive research assistant for evolving scientific projects.<br>
              • Monitors project documents, identifies timely deep-research queries, and distills long reports into project-grounded actionable suggestions.<br>
              • User studies show that its suggestions are more timely and actionable than raw reports.
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
              • For persistent memory in enterprise-grade agents, it proposes a mathematically grounded framework that unifies retrieval, lifecycle management, and consistency verification, overcoming the heavy reliance of traditional memory systems on engineering heuristics. <br>
              • On the LoCoMo benchmark, it achieves an average improvement of 12.7% over engineering baselines, with gains of 19.9% on the most challenging samples, validating the effectiveness of information-geometric methods for complex memory retrieval.<br>
              • This work advances agent memory beyond the stacking of engineering components toward a system design paradigm that is provable, governable, and compliant, with particular significance for high-privacy and high-sovereignty scenarios.
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
              • Proposes a new Memory-as-Ontology paradigm for persistent digital agents, addressing the problem of identity continuity across successive generations of AI models.<br>
              • Establishes a constitutional memory architecture that supports the long-term existence and evolution of digital citizens through a four-layer governance hierarchy, multi-layer semantic storage, and full lifecycle design.<br>
              • Relegates the underlying computational model to a replaceable substrate, prioritizing the persistence of digital identity and governance over the optimization of short-term memory access and retrieval efficiency.
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
| widemem-ai | 2026-02-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/remete618/widemem-ai?style=social) | https://github.com/remete618/widemem-ai<br>https://widemem.ai |
| Riverse | 2026-02-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/wangjiake/JKRiver?style=social) | https://github.com/wangjiake/JKRiver<br>https://wangjiake.github.io/riverse-docs/ |
| SuperLocalMemory | 2026-03-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/qualixar/superlocalmemory?style=social) | https://github.com/qualixar/superlocalmemory<br>https://superlocalmemory.com/ |
| Cog | 2026-03-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/marciopuga/cog?style=social) | https://github.com/marciopuga/cog<br>No official website |
| NeverOnce | 2026-03-18 | ![GitHub Repo stars](https://img.shields.io/github/stars/WeberG619/neveronce?style=social) | https://github.com/WeberG619/neveronce<br>https://pypi.org/project/neveronce/ |
| MHN AI Agent Memory | 2026-03-21 | ![GitHub Repo stars](https://img.shields.io/github/stars/shahzebqazi/mhn-ai-agent-memory?style=social) | https://github.com/shahzebqazi/mhn-ai-agent-memory<br>No official website |
| LycheeMem | 2026-03-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social) | https://github.com/LycheeMem/LycheeMem<br>No official website |
| MemClaw | 2026-03-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/Felo-Inc/memclaw?style=social) | https://github.com/Felo-Inc/memclaw<br>https://memclaw.me |
| MemPalace | 2026-04-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social) | https://github.com/MemPalace/mempalace<br>http://mempalaceofficial.com/ |
| SwarmVault | 2026-04-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/swarmclawai/swarmvault?style=social) | https://github.com/swarmclawai/swarmvault<br>https://swarmvault.ai |
| PackRat | 2026-04-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/kevdogg102396-afk/packrat?style=social) | https://github.com/kevdogg102396-afk/packrat<br>https://www.npmjs.com/package/packrat-compress |
| SkillClaw | 2026-04-10 | ![GitHub Repo stars](https://img.shields.io/github/stars/AMAP-ML/SkillClaw?style=social) | https://github.com/AMAP-ML/SkillClaw<br>https://arxiv.org/abs/2604.08377 |
| Synap | 2026-04-10 | ![GitHub Repo stars](https://img.shields.io/github/stars/maximem-ai/maximem_synap_sdk?style=social) | https://github.com/maximem-ai/maximem_synap_sdk<br>https://maximem.ai |
| Formative Memory | 2026-04-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/jarimustonen/formative-memory?style=social) | https://github.com/jarimustonen/formative-memory<br>No official website |
| taOSmd | 2026-04-13 | ![GitHub Repo stars](https://img.shields.io/github/stars/jaylfc/taosmd?style=social) | https://github.com/jaylfc/taosmd<br>[Docs & benchmarks](https://github.com/jaylfc/taosmd/blob/master/docs/benchmarks.md) |
| ToolPipe | 2026-04-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/COSAI-Labs/toolpipe-mcp-server?style=social) | https://github.com/COSAI-Labs/toolpipe-mcp-server<br>https://toolpipe.dev |
| Origin | 2026-04-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/7xuanlu/origin?style=social) | https://github.com/7xuanlu/origin<br>https://useorigin.app |
| Omnigraph | 2026-04-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/ModernRelay/omnigraph?style=social) | https://github.com/ModernRelay/omnigraph<br>No official website |
| Mnemory | 2026-05-03 | ![GitHub Repo stars](https://img.shields.io/github/stars/fpytloun/mnemory?style=social) | https://github.com/fpytloun/mnemory<br>No official website |
| kaeru | 2026-05-08 | ![GitHub Repo stars](https://img.shields.io/github/stars/LamantinAI/kaeru?style=social) | https://github.com/LamantinAI/kaeru<br>No official website |
| Dakera | 2026-05-12 | ![GitHub Repo stars](https://img.shields.io/github/stars/dakera-ai/dakera-mcp?style=social) | https://github.com/dakera-ai/dakera-mcp<br>https://dakera.ai/ |
| Perseus | 2026-05-18 | ![GitHub Repo stars](https://img.shields.io/github/stars/tcconnally/perseus?style=social) | https://github.com/tcconnally/perseus<br>https://perseus.observer/ |
| Agentic Task System | 2026-05-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/renezander030/agentic-task-system?style=social) | https://github.com/renezander030/agentic-task-system<br>https://www.npmjs.com/package/@reneza/ats-cli |
| OWASP Agent Memory Guard | 2026-05-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/OWASP/www-project-agent-memory-guard?style=social) | https://github.com/OWASP/www-project-agent-memory-guard<br>https://pypi.org/project/agent-memory-guard/ |
| Mimir | 2026-06-06 | ![GitHub Repo stars](https://img.shields.io/github/stars/tcconnally/mimir?style=social) | https://github.com/tcconnally/mimir<br>https://perseus.observer/mimir |
| AccInt | 2026-06-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/maxbaluev/accreted-intelligence?style=social) | https://github.com/maxbaluev/accreted-intelligence<br>https://accint.xyz/ |

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

### 🧠 Adam Framework

- **Description:** 5-layer persistent memory and coherence architecture for local AI assistants built on OpenClaw. Solves AI amnesia (cross-session) and within-session coherence degradation.
- **Layers:** Vault injection, mid-session memory search, neural graph (7219+ neurons), nightly Gemini reconciliation, coherence monitor with scratchpad dropout detection.
- **Validated:** 353 sessions, 6619 message turns, 8 months production use on a live business by a non-developer.
- **Platform:** Windows/macOS/Linux, OpenClaw, local-first, model-agnostic.
- **Links:** [GitHub](https://github.com/strangeadvancedmarketing/Adam) | [Live Demo](https://strangeadvancedmarketing.github.io/Adam/) | [Interactive Proof](https://strangeadvancedmarketing.github.io/Adam/showcase/ai-amnesia-solved.html)

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

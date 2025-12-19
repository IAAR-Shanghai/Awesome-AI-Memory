# Awesome-AI-Memory

<div align="center">
    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) 
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
          • The paper investigates memory management in large language model (LLM) agents and its impact on long-term performance.<br>
          • It identifies issues such as error propagation and misaligned experience replay, highlighting the importance of high-quality memory.<br>
          • By comparing multiple memory insertion and deletion strategies, the study finds that selective insertion performs better for long-term learning, while historical deletion is particularly effective at reducing low-quality memory records.
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
        • EM-LLM (Event Memory Large Language Model) is a novel large language model designed to address the limitations of existing models in handling long contexts.<br>
        • EM-LLM achieves near-unlimited context processing without fine-tuning, delivering significant improvements over existing models across multiple benchmarks.<br>
        • The model integrates surprise-based event segmentation, graph-theoretic boundary refinement, and a two-stage memory retrieval mechanism, substantially enhancing performance on information retrieval and question-answering tasks.
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

|     Edit Type      | Benchmarks \& Datasets                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **Personalized Task Evaluation**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250)  |
|  **Comprehensive Evaluation**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [Evo-Memory](https://arxiv.org/pdf/2511.20857), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **Memory Mechanism Evaluation**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **Long-Term Memory Evaluation**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144) |
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
      <td rowspan="1"><strong>Memory-Related Concepts</strong></td>
      <td>https://www.youtube.com/watch?v=UF230UuclZM</td>
      <td>Introduce the basic concept of memory in machine learning and explore how AI systems store and utilize information</td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Basic Theory of Memory</strong></td>
      <td>https://www.youtube.com/watch?v=-sRvcGURDbQ</td>
      <td>The working principle of the human memory system and its implications for AI design</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=LdFou-SXB00</td>
      <td>A Comparative analysis of memory Mechanisms in Deep Learning and Traditional Memory Models</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>Memory-Related Papers</strong></td>
      <td>https://www.youtube.com/watch?v=-sRvcGURDbQ</td>
      <td>Analysis of the Core viewpoints of the paper: How to Build an artificial intelligence System with long-term memory Capability</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=LdFou-SXB00</td>
      <td>Paper Interpretation: Innovation and Performance Evaluation of Memory Network Architecture</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1RBbUzQEFr</td>
      <td>Review of top Conference Papers on memory and Analysis of Research Trends</td>
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

## 🌟 Star Trends

<a href="https://star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=Date" />
  </picture>
</a>


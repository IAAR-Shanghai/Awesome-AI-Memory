---

## ❓ FAQ

### What is Awesome-AI-Memory?

Awesome-AI-Memory is a curated collection of **399+ research papers** and **104+ open-source projects** focused on AI memory systems for Large Language Models (LLMs). It systematically organizes resources across memory mechanisms, architectures, and practical implementations.

### Why do LLMs need external memory systems?

LLMs have a fundamental limitation: **finite context window length**. This means:
- Information outside the context window is inaccessible during inference
- Extended conversations lose earlier context
- Personalization across sessions is impossible
- Complex multi-stage tasks require information persistence

External memory systems solve this by providing **persistent, controllable storage** beyond model parameters, enabling cross-session consistency and continuous reasoning.

### What memory types are covered?

| Memory Type | Description | Examples |
|-------------|-------------|----------|
| **Short-Term Memory** | Context window-based, temporary | Session-level information |
| **Long-Term Memory** | Persistent across sessions | User preferences, historical facts |
| **Episodic Memory** | Event-based interaction history | Conversation logs with temporal sequence |
| **Semantic Memory** | Abstracted facts and rules | Knowledge distilled from experiences |
| **Procedural Memory** | Action patterns and skills | Task execution strategies |

### What memory operations are discussed?

- **Writing**: Determining what information to store
- **Retrieval**: Selecting relevant memories for current tasks
- **Updating**: Correcting or merging existing memories
- **Forgetting**: Removing or weakening low-value information
- **Compression**: Summarizing to fit context windows

### Is RAG considered a memory mechanism?

Yes. **Retrieval-Augmented Generation (RAG)** is treated as a memory access mechanism in this repository. RAG enables LLMs to retrieve information from external sources, functioning as a form of semantic memory retrieval.

### What frameworks and tools are included?

The repository catalogs:
- Memory-enhanced LLM frameworks
- Multi-agent shared memory systems
- Vector databases for semantic retrieval
- Memory management tools
- Evaluation benchmarks and datasets

### How can I contribute?

Use the issue template:
```
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```

Submit via GitHub Issues or Pull Requests.

### What disciplines does this bridge?

- Natural Language Processing (NLP)
- Information Retrieval
- Intelligent Agent Systems
- Cognitive Science
- Database Systems

### How often is this updated?

The repository is actively maintained with **399+ papers** and **104+ projects** continuously curated. Check the Star History chart for recent activity.

### What license does this use?

MIT License — Free to use, modify, and distribute.

### Where can I get help?

- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions or share ideas
- **WeChat**: Scan QR code in README to join discussion group

---

**Related Repositories**: If you're interested in broader AI agent topics, check out [Awesome-AI-Agents](https://github.com/IAAR-Shanghai/Awesome-AI-Agents) for agent frameworks and tools.
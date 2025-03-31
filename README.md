# GSoC Proposal: Mesa-LLM: Integrating LLMs into Agent-Based Modeling

## Project Title

**Mesa-LLM: Integrating Large Language Models (LLMs) into Agent-Based Modeling (ABM)**

## Summary

Mesa-LLM aims to extend the Mesa agent-based modeling (ABM) framework by incorporating **Large Language Models (LLMs)** into the decision-making process of agents. This project will allow researchers to create sophisticated, language-driven agents capable of performing tasks like communication, negotiation, and reasoning. The goal is to make it easier to design, test, and experiment with **LLM-based agents** by offering modular components like memory systems, decision-making modules, and optional **Chain-of-Thought (CoT)** reasoning.

## Benefits to the Community

The integration of LLMs into ABM represents a significant step forward in the modeling of human-like decision-making processes. By building a **modular API**, researchers can quickly assemble agents with different behaviors and test their decision-making in various scenarios. This would allow experimentation in areas such as:

- **Collaborative problem-solving**
- **Simulation of human-like reasoning**
- **Dynamic decision-making under uncertainty**
- **Inter-agent communication via forums to share insights**

The development of Mesa-LLM will make it easier to incorporate **LLMs into agent-based models**, allowing researchers to explore scenarios involving communication and negotiation more naturally and efficiently.

## Deliverables

The following deliverables will be achieved over the course of the summer:

### **1. Modular Integration Layer & Decision-Making Module**
- Develop a unified API for integrating different LLMs seamlessly using **LangChain for LLM abstraction**.
- Ensure the API implements a common interface, enabling compatibility across various LLM providers (e.g., OpenAI, Hugging Face).
- Allow users to define agent actions, memory systems, and personality traits while ensuring smooth switching between models.
- Enable context-aware decision-making, allowing agents to select actions based on past behaviors, reasoning, and environmental stimuli.

### **2. Memory Module**
- Implement a memory system that stores the agent’s decisions, enabling reinforcement learning and allowing agents to learn from past actions.

### **3. Chain-of-Thought (CoT) Integration**
- Implement CoT reasoning to allow agents to break down complex decisions into step-by-step reasoning, enhancing decision-making.

### **4. Forum Feature for Agent Communication**
- Implement a forum system where agents can post about their actions, results, and insights.
- Enable inter-agent discussions to enhance collaborative decision-making.

### **5. Testing, Documentation, and Tutorials**
- Provide unit tests for each module.
- Develop comprehensive documentation for users and developers.
- Create tutorial notebooks demonstrating **sample smaller models** that can be used for running a large number of agents efficiently.

## Timeline

### **Week 1-2: Task Planning with Mentor and Agent Creation**
- Review project requirements and establish a timeline with your mentor.
- Integrate LLM APIs (e.g., OpenAI, Hugging Face) for basic decision-making.
- Implement a basic agent creation process, allowing users to define actions and context.

### **Week 3-6: Modular Integration Layer & Decision-Making Module**
- Develop the **Modular Integration Layer** to support switching between different LLMs using **LangChain for abstraction**.
- Implement the **Decision-Making Module**, allowing agents to make context-aware decisions based on memory, available actions, and reasoning.
- Integrate personality traits to introduce decision-making biases for multiple agents.

### **Week 7-8: CoT Reasoning Integration**
- Implement **CoT (Chain-of-Thought)** reasoning to help agents perform complex tasks through reasoning and justifying their choices step by step.
- Test and debug CoT functionality for various decision-making scenarios (e.g., negotiation, cooperation).

### **Week 9-10: Memory System Implementation**
- Develop and test the **Memory Module**, enabling agents to store past actions and learn from them.
- Integrate memory with decision-making logic for reinforcement learning.
- Test how the memory system interacts with agent behaviors and their decisions.

### **Week 11-12: Final Testing and Debugging**
- Conduct integration testing for all modules (API, memory, decision-making, CoT).
- Test the full agent pipeline: agent creation → memory management → decision-making → action selection.
- Fix any bugs and ensure the system is robust and flexible.

### **Week 13-14: Documentation and Final Submission**
- **Write comprehensive documentation** for the entire framework:
  - User guides for building LLM-powered agents.
  - Developer documentation for extending the framework.
  - Tutorials and example notebooks showcasing sample smaller models for running large-scale agent simulations.
- Set up **CI/CD pipelines** for continuous integration and testing.

## Code Exploration & Insights

My initial code experiments have been instrumental in shaping the Mesa-LLM proposal, and they illustrate several key points:

### **Practical Integration of Mesa and LLMs**
- **Agent-Based Modeling in Action**: The code leverages Mesa’s agent-based framework to create a dynamic simulation environment. By defining an **LLMAgent** class, I demonstrated how agents can be enriched with personality traits and LLM-powered decision-making. This practical implementation underscores the flexibility of Mesa, showing that it can serve as a robust foundation for integrating advanced AI components.

- **LLM-Driven Decision Making**: Using LangChain’s **OllamaLLM**, the agents are capable of invoking an LLM to guide their actions (e.g., buying, selling, or holding stocks). This integration showcases how LLMs can facilitate more nuanced and context-aware decision-making in simulated agents—a central theme of my proposal.

### **Insights Gained**
- **Understanding Mesa’s Extensibility**: Working with Mesa has revealed its highly modular structure, which allows for seamless integration of new components like a decision-making module or a memory system. This insight is crucial for the proposed project, where modularity is key to enabling rapid experimentation with different agent behaviors.

- **Harnessing the Power of LLMs**: The experiment provided hands-on experience in incorporating LLM APIs into agent-based models. By leveraging LLM responses to simulate realistic economic decisions (such as stock trading), I gained a deeper understanding of how language models can be used to replicate human-like reasoning and dynamic decision-making.

- **Bridging Theory with Practice**: The process of embedding LLMs into Mesa agents not only validated the concept but also highlighted potential challenges and opportunities—such as ensuring coherent personality-driven responses and managing the agent’s memory of past actions. These practical learnings will guide the development of more sophisticated modules, like the Memory and Chain-of-Thought reasoning systems outlined in the proposal.

![Alt text](screenshots/screenshot1.png?raw=true "LLM Agents thinking and making decisions of buying, selling or holding during each step")

LLM Agents thinking and making decisions of buying, selling or holding during each step

![Alt text](screenshots/screenshot2.png?raw=true "LLM Agents final holdings after 40 steps of trading")

LLM Agents final holdings after 40 steps of trading

## Expected Outcomes
- LLM-powered agents with customizable behavior and decision-making.
- A modular framework for creating agents, enabling rapid experimentation.
- Improved decision-making via Chain-of-Thought reasoning and memory integration.
- An interactive forum system for agents to share insights, enhancing collaboration.
- Comprehensive documentation for easy adoption and integration by the research community.
- **Scientific Contribution**: The project will contribute to the growing body of work on LLM-based agent modeling and may lead to a publication in relevant journals.

## Skills Required
- Strong Python programming skills.
- Familiarity with agent-based modeling frameworks like Mesa.
- Experience with LLM APIs (e.g., OpenAI, Hugging Face).

## About Me
I am a Data Analyst with a strong passion for Machine Learning and its potential to tackle complex, real-world problems. I hold an AWS Machine Learning Engineer certification and won an AI award during university. In my recent project, ComplaintBot, I implemented agentic AI using LangChain, RAG, and agents to create an AI-powered customer support assistant for handling food delivery complaints. I am currently enrolled in Perplexity AI Business Fellowship to learn more about AI and build my network. 

Learn more about me via my LinkedIn: [https://www.linkedin.com/in/mihir-chhiber/](https://www.linkedin.com/in/mihir-chhiber/)

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

The development of Mesa-LLM will make it easier to incorporate **LLMs into agent-based models**, allowing researchers to explore scenarios involving communication and negotiation more naturally and efficiently.

## Deliverables

The following deliverables will be achieved over the course of the summer:

1. **Modular API for LLM-Powered Agents**:
    - Allow users to define agent actions, memory systems, and personality traits.
    - Provide an easy-to-use API for connecting LLMs to agent behaviors.

2. **Memory Module**:
    - Implement a memory system that stores the agent’s decisions, enabling reinforcement learning and allowing agents to learn from past actions.

3. **Decision-Making Module**:
    - Develop a module that uses LLMs to make decisions based on context, available actions, and reasoning.

4. **Chain-of-Thought (CoT) Integration**:
    - Implement CoT reasoning to allow agents to break down complex decisions into step-by-step reasoning, enhancing decision-making.

5. **Testing and Documentation**:
    - Provide unit tests for each module.
    - Develop comprehensive documentation for users and developers.

## Timeline

### **Week 1-2: API Development and Agent Creation**

- Develop the foundational **API** for defining agents and their actions.
- Integrate LLM APIs (e.g., OpenAI, Hugging Face) for basic decision-making.
- Implement a basic agent creation process, allowing users to define actions and context.

### **Week 3-4: Decision-Making Module**

- Develop the **Decision-Making Module** to enable agents to make decisions based on context, available actions, and reasoning.
- Integrate personality traits which allows for biases to be present during the decision making for multiple agents.

### **Week 5-6: CoT Reasoning Integration**

- Implement **CoT (Chain-of-Thought)** reasoning to help agents perform complex tasks through reasoning and justifying their choices step by step.
- Test and debug CoT functionality for various decision-making scenarios (e.g., negotiation, cooperation).

### **Week 7-8: Memory System Implementation**

- Develop and test the **Memory Module**, enabling agents to store past actions and learn from them.
- Integrate memory with decision-making logic for reinforcement learning.
- Test how the memory system interacts with agent behaviors and their decisions.

### **Week 9-10: Final Testing and Debugging**

- Conduct integration testing for all modules (API, memory, decision-making, CoT).
- Test the full agent pipeline: agent creation → memory management → decision-making → action selection.
- Fix any bugs and ensure the system is robust and flexible.

### **Week 11-12: Documentation and Final Submission**

- **Write comprehensive documentation** for the entire framework:
  - User guides for building LLM-powered agents.
  - Developer documentation for extending the framework.
  - Tutorials and example notebooks.
- Set up **CI/CD pipelines** for continuous integration and testing.

## Technical Details

### **Memory Module**:
The **Memory Module** allows agents to store and recall past decisions. This enables agents to adjust their behaviors based on previous actions and outcomes, enabling **reinforced learning**. Agents will have access to a history of their decisions (n-step memory) and use this to inform their future actions.

### **Decision-Making Module**:
The **Decision-Making Module** uses an **LLM API** to select the most appropriate action for an agent. It takes into account the current context, past actions, and available choices. The module processes the input and prompts the LLM for a decision. The resulting decision will be influenced by the agent’s memory and reasoning.

### **Personality Module**:
The **Personality Module** introduces biases or preferences into the decision-making process by assigning traits like **aggressive**, **empathetic**, or **strategic** to the agent. These traits influence the likelihood of an agent choosing certain actions over others, aligning with its **defined personality**. This will provide more human-like behavior for the agents.

### **Chain-of-Thought (CoT) Reasoning**:
CoT reasoning allows agents to break down complex decisions into logical steps. This enables the agent to **reason through** its decision-making, improving transparency and explainability. The **CoT Module** will allow users to enable step-by-step reasoning for their agents.


## Expected Outcomes
- LLM-powered agents with customizable behavior and decision-making.
- A modular framework for creating agents, enabling rapid experimentation.
- Improved decision-making via Chain-of-Thought reasoning and memory integration.
- Comprehensive documentation for easy adoption and integration by the research community.
- Scientific Contribution: The project will contribute to the growing body of work on LLM-based agent modeling and may lead to a publication in relevant journals.


## Skills Required
- Strong Python programming skills.
- Familiarity with agent-based modeling frameworks like Mesa.
- Experience with LLM APIs (e.g., OpenAI, Hugging Face).


## About Me
I am a Data Analyst with a strong passion for Machine Learning and its potential to tackle complex, real-world problems. I hold an AWS Machine Learning Engineer certification and won an AI award during university. In my recent project, ComplaintBot, I implemented agentic AI using LangChain, RAG, and agents to create an AI-powered customer support assistant for handling food delivery complaints. The system offers empathetic, context-aware responses to customer queries. I am currently enrolled in Perplexity AI Business Fellowship to learn more about the AI field and build my network in the new AI ecosystem. I’m always excited about exploring innovative AI solutions and pushing the boundaries of what technology can achieve. Learn more about me via my LinkedIn (https://www.linkedin.com/in/mihir-chhiber/)

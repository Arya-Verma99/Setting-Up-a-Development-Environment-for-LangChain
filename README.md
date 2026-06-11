# LangChain Learning Journey

## Overview

This repository documents my hands-on learning journey with **LangChain** and **Generative AI**. It contains assignments, practical implementations, and code examples covering LangChain fundamentals, environment setup, model integration, prompt engineering, LCEL, and real-world AI applications.

The goal is to build a strong foundation in developing AI-powered applications using LangChain and Groq-hosted Large Language Models (LLMs).

---

### Assignments

* ✅ Assignment 1: LangChain Basics
* ✅ Assignment 2: Development Environment for LangChain
* ✅ Assignment 3: Your First AI Connection – Models, Parameters, and Direct Invocation
* ✅ Assignment 4: The Chain Architecture Blueprint – Building Intelligent AI Pipelines with LCEL
* ✅ Assignment 5: Prompt Engineering Mastery – Controlling AI Behavior with Roles, Examples, and Intent
* ✅ Assignment 6: Applied AI in Action – Building Real-World Language Transformation Tools with LangChain
* ✅ Assignment 7: Multi-Modal Content Intelligence – Generating Platform-Specific Marketing Copy with LangChain
* ✅ Assignment 8: Advanced Multi-Modal Content Generation

---

# Assignment 1: LangChain Basics

## Objective

Understand the fundamentals of LangChain, its importance in AI development, and how it overcomes the limitations of standalone Large Language Models (LLMs).

## Key Concepts Covered

### What is LangChain?

LangChain is an open-source framework used to build applications powered by Large Language Models (LLMs). It enables developers to connect language models with external tools, APIs, databases, memory systems, and documents.

### Why is LangChain Called the "Glue of AI"?

LangChain acts as a bridge between:

* Language Models
* APIs
* Databases
* Documents
* Memory Components
* External Tools

This allows developers to build intelligent AI systems such as chatbots, AI assistants, and Retrieval-Augmented Generation (RAG) applications.

### Limitations of Standalone LLMs

* Lack of memory
* Limited context access
* No direct access to external tools
* Unable to retrieve real-time information independently

### Benefits of LangChain

* Memory Management
* Context Retrieval
* Tool Integration
* Workflow Management
* Scalable AI Pipelines

### LCEL (LangChain Expression Language)

LCEL provides a simple pipeline-based approach for building AI workflows.

Example:

```python
chain = prompt | llm | output_parser
```

### Typical Workflow

```text
User Input
    ↓
Prompt Template
    ↓
Language Model (LLM)
    ↓
Output Parser
    ↓
Final Response
```

---

# Assignment 2: Development Environment for LangChain

## Objective

Set up a professional and secure development environment for building LangChain applications.

## Creating a Virtual Environment

Create an isolated Python environment:

```bash
python -m venv lang_env
```

Activate the environment:

```bash
lang_env\Scripts\activate
```

Expected Output:

```text
(lang_env)
```

Upgrade pip:

```bash
python.exe -m pip install --upgrade pip
```

## Installing Required Dependencies

```bash
pip install langchain langchain-groq langchain-community python-dotenv tiktoken
```

### Dependency Overview

| Package             | Purpose                                       |
| ------------------- | --------------------------------------------- |
| langchain           | Core framework for building AI applications   |
| langchain-groq      | Integration between LangChain and Groq models |
| langchain-community | Community-supported integrations and tools    |
| python-dotenv       | Environment variable management               |
| tiktoken            | Token counting and prompt management          |

## Secure API Key Management

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## Configure .gitignore

```text
.env
lang_env/
__pycache__/
*.pyc
```

## Environment Validation Script

```python
import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("[INFO] Inspecting Environment...")
print(f"Python Version: {sys.version.split()[0]}")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("[CRITICAL ERROR] GROQ_API_KEY not found.")
else:
    masked_key = f"{api_key[:5]}...{api_key[-3:]}"
    print(f"[SUCCESS] API Key Loaded: {masked_key}")
    print("[SYSTEM] Ready for Takeoff.")
```

### Learning Outcomes

* Created an isolated Python environment
* Installed LangChain dependencies
* Secured API keys using environment variables
* Configured `.gitignore`
* Validated the development environment

---

# Assignment 3: Your First AI Connection

## Objective

Learn how to connect LangChain with a Groq-hosted Large Language Model and generate responses using direct invocation.

## Project File

```text
hello_world.py
```

## Model Initialization

```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=100
)

print("[SYSTEM] Model Initialized.")
```

### Model Parameters

| Parameter   | Description                  |
| ----------- | ---------------------------- |
| model       | Specifies which LLM to use   |
| temperature | Controls response creativity |
| max_tokens  | Limits the response length   |

## Direct Invocation

```python
question = "Explain recursion to a 10-year-old."

response = llm.invoke(question)

print(type(response))
print(response.content)
```

## How It Works

1. User provides a prompt.
2. LangChain sends the prompt to Groq.
3. The selected LLM processes the request.
4. The response is returned as an `AIMessage` object.
5. The generated content is extracted using `response.content`.

## Expected Output

```text
[SYSTEM] model initialized successfully.
---Row Response Object---
<class 'langchain_core.messages.ai.AIMessage'>
Recursion is a pretty cool concept in computer science and mathematics. Imagine you have a big box of toys, and inside that box, there's another smaller box. And inside that smaller box, there's an even smaller box, and so on.

Now, let's say you have a task to put all the toys away in their boxes. If you just started with the big box, you'd have to put all the toys in the smaller box, and then all the toys in the even smaller

```

### Learning Outcomes

* Initialized a Groq-hosted LLM
* Understood model configuration parameters
* Used the `.invoke()` method
* Worked with `AIMessage` objects
* Extracted generated responses

---
# Assignment 4: Chain Architecture Using LCEL

## Objective
Learn how to build modular AI pipelines using LangChain Expression Language (LCEL) by combining Prompt Templates, LLMs, and Output Parsers into a single execution chain.

## Project File
chain_architecture.py

## How It Works
User provides input (user_query)
Prompt template formats the instruction
LLM processes the formatted prompt
Output parser converts response into clean text
LCEL chain executes everything in one pipeline

## Model Parameters
| Parameter   | Description |
|------------|-------------|
| model | Specifies which LLM to use |
| temperature | Controls randomness/creativity |
| max_tokens | Limits response length |

## Key Concepts Learned
- Prompt Templates for dynamic inputs
- Groq LLM integration with LangChain
- Output parsing using StrOutputParser
- LCEL pipe operator (|) for chaining components
- End-to-end AI pipeline execution

---

# Assignment 5: Advanced Prompt Engineering

## Objective

Learn advanced prompt engineering techniques in LangChain to improve response quality, consistency, and control over LLM outputs. This assignment covers Role-Based Prompting and Few-Shot Prompting.

## Project File

advanced_prompt_engineering.py

## Technique A: Role-Based Prompting

Role-Based Prompting assigns a specific persona or role to the AI before providing the user's question.

Example:

```python
SystemMessage(
    content="You are a senior Python Architect. You only answer with code snippets. No explanations."
)
```

The System Message controls the behavior of the model, while the Human Message contains the user's actual request.

Because the AI is instructed to behave like a Python Architect, it responds with code only and avoids explanations.

### Expected Output

```python
my_list = [1, 2, 3, 4]
reversed_list = my_list[::-1]
print(reversed_list)
```

## Technique B: Few-Shot Prompting

Few-Shot Prompting improves consistency by showing the model examples before asking the real question.

### Examples Provided

```text
2 + 2 = 4
2 + 3 = 5
```

These examples teach the model the expected pattern.

### Prompt Structure

```text
System: You are a math wizard.

Human: 2+2
AI: 4

Human: 2+3
AI: 5

Human: What is 10 + 10?
```

The model uses the examples to infer the correct answer.

### Expected Output

```text
20
```

## How It Works

1. The Groq LLM is initialized.
2. Role-Based Prompting assigns a persona to control model behavior.
3. Few-Shot Prompting provides examples to guide responses.
4. ChatPromptTemplate creates structured prompts.
5. FewShotChatMessagePromptTemplate inserts example conversations.
6. StrOutputParser converts the model response into plain text.
7. LCEL connects all components using the pipe (`|`) operator.
8. The chain processes input and returns the final output.

## Data Flow

```text
Input
  ↓
Prompt Template
  ↓
Few-Shot Examples
  ↓
LLM
  ↓
Output Parser
  ↓
Final Response
```

## Key Concepts Learned

- Role-Based Prompting
- System Messages and Human Messages
- Few-Shot Prompting
- ChatPromptTemplate
- FewShotChatMessagePromptTemplate
- StrOutputParser
- LCEL Chain Architecture
- Prompt Engineering Best Practices

## Learning Outcomes

- Controlled AI behavior using personas
- Improved response consistency using examples
- Built dynamic prompts with templates
- Created reusable AI workflows
- Combined prompts, models, and parsers using LCEL
- Understood how prompt engineering improves output quality

# Assignment 6: Hands-On Lab – The Corporate Translator

## Objective

Build an AI-powered Corporate Translator that converts rude, emotional, or unprofessional text into professional corporate email language while preserving the original meaning. This project combines Prompt Templates, LCEL Chains, Output Parsers, and Prompt Engineering techniques to create a practical business communication tool.

## Project File

Corporate_Translator.py


## How It Works

1. The user enters a rude, emotional, or unprofessional statement.
2. The prompt template inserts the text into a predefined corporate communication prompt.
3. The Groq LLM rewrites the message using a professional and diplomatic tone.
4. The StrOutputParser converts the response into clean text.
5. The LCEL chain executes the complete workflow.
6. The professional version is displayed to the user.
7. The loop continues until the user types `exit`.

## Prompt Structure

```text
You are a Corporate Communication Expert.

Rewrite the following rude text into professional,
diplomatic email language.

Do not change the underlying meaning.
Only improve the tone.

RUDE TEXT:
{text}

PROFESSIONAL EMAIL SNIPPET:
```

## Data Flow

```text
User Input
     ↓
ChatPromptTemplate
     ↓
Groq LLM
     ↓
StrOutputParser
     ↓
Professional Email Text
```

## Test Case 1

### Input

```text
This idea is stupid and you are dumb.
```

### Output

```text
Dear [Name],

I wanted to discuss the recent idea presented by the team. While I appreciate the effort and creativity put into it, I have some concerns about its feasibility and potential impact on our goals. Upon further review, I believe there may be some potential drawbacks that need to be considered. I would like to schedule a meeting to discuss these points in more detail and explore alternative solutions.

Best regards,
[Your Name]
```

## Test Case 2

### Input

```text
This project is a mess and nobody knows what they are doing.
```

### Output

```text
Subject: Project Review and Improvement Opportunities

Dear Team,

I wanted to take a moment to discuss the current status of our project. While we've made significant progress, I've noticed that there are some areas where our processes and communication could be clarified to ensure we're all aligned and working efficiently. I'd like to schedule a meeting with the team to review our project plan, discuss any challenges we're facing, and explore ways to improve our workflows and communication.

Your input and collaboration in this matter are invaluable, and I appreciate your dedication to delivering a high-quality outcome.

Best regards,
[Your Name]"

```

## Key Components Used

| Component | Purpose |
|------------|----------|
| ChatPromptTemplate | Creates a dynamic prompt with placeholders |
| ChatGroq | Processes the prompt using the LLM |
| StrOutputParser | Converts model output into plain text |
| LCEL Pipe Operator (`|`) | Connects all components into a chain |
| Function (`make_professional`) | Makes the translator reusable |
| While Loop | Allows continuous user interaction |

## Key Concepts Learned

- Prompt Engineering
- Role-Based Prompting
- Dynamic Prompt Templates
- LCEL Chain Architecture
- Output Parsing
- Function-Based Design
- Interactive AI Applications
- Business Communication Automation

## Learning Outcomes

- Built a real-world AI application using LangChain.
- Created reusable AI workflows using functions.
- Converted unprofessional language into professional corporate communication.
- Applied Prompt Templates and Output Parsers together.
- Used LCEL to connect prompts, models, and parsers.
- Learned how prompt design directly influences AI-generated responses.

```
# Repository Structure

```text
LangChain/
│
├── README.md
├── .gitignore
├── hello_world.py
├── validate_env.py
│
├── Assignment_01_LangChain_Basics/
├── Assignment_02_Development_Environment/
├── Assignment_03_First_AI_Connection/
│
├── Assignment_04_chain_architecture/
├── Assignment_05_Prompt_Engineering/
├── Assignment_06_Applied_AI/
├── Assignment_07_MultiModal_Content/
└── Assignment_08_Advanced_Content_Generation/


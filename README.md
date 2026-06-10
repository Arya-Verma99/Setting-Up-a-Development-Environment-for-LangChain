# LangChain Learning Journey

## Overview

This repository documents my hands-on learning journey with **LangChain** and **Generative AI**. It contains assignments, practical implementations, and code examples covering LangChain fundamentals, environment setup, model integration, prompt engineering, LCEL, and real-world AI applications.

The goal is to build a strong foundation in developing AI-powered applications using LangChain and Groq-hosted Large Language Models (LLMs).

---

### Completed Assignments

* ✅ Assignment 1: LangChain Basics
* ✅ Assignment 2: Development Environment for LangChain
* ✅ Assignment 3: Your First AI Connection – Models, Parameters, and Direct Invocation

### Upcoming Assignments

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
├── Assignment_04_LCEL/
├── Assignment_05_Prompt_Engineering/
├── Assignment_06_Applied_AI/
├── Assignment_07_MultiModal_Content/
└── Assignment_08_Advanced_Content_Generation/
```

---

# Technologies Used

* Python 3.10+
* LangChain
* Groq
* python-dotenv
* tiktoken
* Git
* GitHub

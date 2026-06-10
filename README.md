LangChain Learning Journey
Overview

This repository contains my hands-on learning journey with LangChain. Each assignment focuses on a specific concept and includes explanations, code examples, exercises, and practical implementations using Groq-hosted LLMs.

The goal is to build a strong foundation in LangChain, Prompt Engineering, LCEL, AI Pipelines, and Real-World AI Applications.

Course Roadmap
Completed Assignments
✅ Assignment 1: LangChain Basics
✅ Assignment 2: Development Environment for LangChain
✅ Assignment 3: Your First AI Connection – Models, Parameters, and Direct Invocation
✅ Assignment 4: The Chain Architecture Blueprint (LCEL)
✅ Assignment 5: Prompt Engineering Mastery
✅ Assignment 6: Applied AI in Action
✅ Assignment 7: Multi-Modal Content Intelligence
✅ Assignment 8: Advanced Marketing Content Generation
Assignment 1: LangChain Basics
Objective

Understand what LangChain is, why it is called the "Glue of AI," and how it overcomes the limitations of standalone Large Language Models (LLMs).

Key Concepts Covered
What is LangChain?

LangChain is an open-source framework used to build applications powered by Large Language Models (LLMs). It connects language models with external tools, APIs, databases, memory, and documents to create intelligent AI applications.

Why is LangChain Called the "Glue of AI"?

LangChain acts as a bridge between:

Language Models
APIs
Databases
Documents
Memory Systems
External Tools

This allows developers to build AI assistants, chatbots, and Retrieval-Augmented Generation (RAG) applications efficiently.

Limitations of Standalone LLMs
No long-term memory
Limited access to external data
Cannot directly use APIs or tools
Limited ability to retrieve real-time information
Benefits of LangChain
Memory Management
Context Retrieval
Tool Integration
Workflow Orchestration
Scalable AI Pipelines
Assignment 2: Development Environment for LangChain
Objective

Set up a professional and secure development environment for building LangChain applications.

Creating a Virtual Environment

Create an isolated Python environment:

python -m venv lang_env

Activate the environment:

lang_env\Scripts\activate

Upgrade pip:

python.exe -m pip install --upgrade pip
Installing Dependencies
pip install langchain langchain-groq langchain-community python-dotenv tiktoken
Dependency Overview
Package	Purpose
langchain	Core LangChain framework
langchain-groq	Groq integration
langchain-community	Community integrations
python-dotenv	Environment variable management
tiktoken	Token counting and management
Secure API Key Management

Create a .env file:

GROQ_API_KEY=your_api_key_here
.gitignore Configuration
.env
lang_env/
__pycache__/
*.pyc
Validation Script

The validation script ensures that:

Python is installed correctly
Environment variables are loaded
API keys are accessible
Dependencies are configured properly
Assignment 3: Your First AI Connection
Objective

Learn how to connect LangChain with a Groq-hosted Large Language Model and generate responses using direct invocation.

Model Initialization

Create a file named:

hello_world.py

Add the following code:

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=100
)

print("[SYSTEM] Model Initialized.")
Understanding Model Parameters
Parameter	Description
model	Specifies the language model
temperature	Controls creativity of responses
max_tokens	Limits the response length
Direct Invocation
question = "Explain recursion to a 10-year-old."

response = llm.invoke(question)

print(type(response))
print(response.content)
Behind the Scenes
User sends a prompt.
LangChain forwards the prompt to Groq.
The selected LLM processes the request.
The response is returned as an AIMessage object.
The generated text is extracted using response.content.
Expected Output
[SYSTEM] Model Initialized.

<class 'langchain_core.messages.ai.AIMessage'>

Recursion is like looking into a mirror that reflects another mirror until it reaches a stopping point.
Learning Outcomes

After completing this assignment, I learned:

How LangChain interacts with LLMs
How to configure model parameters
How direct invocation works
How AIMessage objects store responses
How to extract generated content from responses
Repository Structure
LangChain/
│
├── README.md
├── .gitignore
├── .env
│
├── Assignment_01_LangChain_Basics/
│
├── Assignment_02_Development_Environment/
│   ├── validate_env.py
│
├── Assignment_03_First_AI_Connection/
│   ├── hello_world.py

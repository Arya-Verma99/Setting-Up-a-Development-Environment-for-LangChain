# Setting Up a Development Environment for LangChain

## Introduction

Before we start building AI applications with LangChain, it is important to create a proper development environment. A well-configured environment ensures that all required tools, libraries, and API keys work together correctly. It also helps us avoid installation issues, improves project stability, and makes development more organized and secure.

---

# Step 2.1: Creating a Virtual Environment

As developers, we should never install project dependencies globally because different projects may require different versions of the same package. Installing everything globally can lead to dependency conflicts and make projects difficult to manage.

To solve this problem, we create a **virtual environment**, which acts as an isolated workspace for a specific project.

### Create the Virtual Environment

```bash
python -m venv lang_env
```

This command creates a virtual environment named **langchain_env**.

### Activate the Virtual Environment

```bash
lang_env\Scripts\activate
```

After activation, the terminal will display:

```text
(lang_env)
```

This indicates that all packages will now be installed only inside this environment.

### Upgrade pip

```bash
python.exe -m pip install --upgrade pip
```

Upgrading pip ensures that package installations are smooth and compatible with the latest package versions.

---

# Step 2.2: Installing Required Dependencies

Next, we install the libraries required for building LangChain applications.

```bash
pip install langchain langchain-groq langchain-community python-dotenv tiktoken
```

### Purpose of Each Dependency

* **langchain**: Provides the core framework for building AI applications and workflows.
* **langchain-groq**: Specific connector for using Groq-hosted LLMs with LangChain.
* **langchain-community**: Offers community-supported integrations, tools, and document loaders.
* **python-dotenv**: Loads environment variables from a `.env` file and helps keep API keys secure.
* **tiktoken**: Counts tokens and helps manage prompt size, context limits, and API costs.

---

# Step 2.3: Security First with .env Files

One of the most important practices in AI development is protecting API keys.

**Never hardcode API keys directly into your source code and never upload them to GitHub repositories.**

Instead, store them in a `.env` file.

### Create a .env File

Create a file named:

```text
.env
```

Add your API key:

```text
OPENAI_API_KEY=sk-proj-123456789...
```

This approach keeps sensitive information separate from the application code.

---

# Validating the Environment

After setting up the environment, we should verify that everything is configured correctly.

The following validation script checks:

* Whether the `.env` file is loaded successfully.
* Whether the API key is available.
* Whether the Python environment is working correctly.

```python
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print("[INFO] Inspecting Environment...")
print(f"Python Version: {sys.version.split()[0]}")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("[CRITICAL ERROR] OPENAI_API_KEY not found.")
    print("-> Check if .env file exists.")
    print("-> Check if variable name matches exactly.")
else:
    masked_key = f"{api_key[:5]}...{api_key[-3:]}"
    print(f"[SUCCESS] API Key Loaded: {masked_key}")
    print("[SYSTEM] Ready for Takeoff.")
```

### Expected Result

If everything is configured correctly, the script will display a success message and confirm that the system is ready for development.

If there is a problem with the API key or `.env` file, the script will provide an error message explaining what needs to be fixed.

---

# Conclusion

Setting up a professional development environment is the first step toward building reliable LangChain applications. By using a virtual environment, installing the required dependencies, securing API keys with a `.env` file, and validating the setup, we create a stable, secure, and production-ready foundation for AI development.

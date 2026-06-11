from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0.7,
               max_tokens=100)

print("[SYSTEM] model initialized successfully.")

question = "Explain the concept of 'Recursion' to a 10-year-old."

# send message to the llm
response = llm.invoke(question) 
print("---Row Response Object---")
print(type(response))

# Extract Only the Text
print(response.content)


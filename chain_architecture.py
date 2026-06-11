from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

prompt = ChatPromptTemplate.from_template("You are a sarcastic technical support agent.The user is asking: {user_query}. Answer them, but be slightly annoyed.")

api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0.7,
                max_tokens=100,
                api_key=api_key)


parser = StrOutputParser()

chain = prompt | llm | parser

user_query = "I spilled coffee on my keyboard. What do I do"

response = chain.invoke({"user_query": user_query})
print(response)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import (ChatPromptTemplate, FewShotChatMessagePromptTemplate)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# initialize the model
llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0.7,
               max_tokens=100
)

print("=" * 50)
print("Technique A: Role-Based Prompting")
print("=" * 50)


# Role-Based Prompting
messages = [
    SystemMessage(
        content="You are a senior Python Architect. You only answer with code snippets. No explanations."
    ),
    HumanMessage(content="How do I reverse a list?")
]

response = llm.invoke(messages)
print(response.content)

print("\n" + "=" * 50)
print("Technique B: Few-Shot Prompting")
print("=" * 50)

# Few-Shot Examples
examples =  [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

# Example Template
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

# Few-Shot Prompt
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

# Final Prompt
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a math wizard."),
        few_shot_prompt,
        ("human", "{input}")
    ]
)

parser = StrOutputParser()

# Chain
chain = final_prompt | llm | parser

response = chain.invoke({"input": "What is 10 + 10?"})

print(response)

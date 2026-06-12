from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# initialize the model
llm = ChatGroq(model="llama-3.1-8b-instant",
                temperature=0.5)

# prompt template
prompt = ChatPromptTemplate.from_template("""
You are a marketing content expert.

Generate the following content for the product: {product}

1. Tweet
   - Maximum 280 characters
   - Include relevant hashtags

2. LinkedIn Post
   - Professional tone
   - Use bullet points

3. Instagram Caption
   - Fun and enthusiastic tone
   - Include emojis

Generate exactly 3 sections for the product: {product}
""")

# output parser
parser = StrOutputParser()

# create the chain
chain = prompt | llm | parser

# user input
product_name = input("Enter the product name: ")

# invoke the chain
response = chain.invoke({"product": product_name})
print(response)

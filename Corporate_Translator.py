from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# initialize the model
llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0.7,
               max_tokens=150
)


# Function
def make_professional(rude_text):

    template = """
    You are a Corporate Communication Expert.

    Rewrite the following rude text into professional,
    diplomatic email language.

    Do not change the meaning.
    Only improve the tone.

    RUDE TEXT:
    {text}

    PROFESSIONAL EMAIL SNIPPET:
    """

    prompt = ChatPromptTemplate.from_template(template)

    email_chain = prompt | llm | StrOutputParser()

    return email_chain.invoke({"text": rude_text})

# Interactive Loop
print("Welcome to the Corporate Translator")
print("Type 'exit' to quit")

while True:

    user_input = input("\nEnter your rude thought: ")

    if user_input.lower() == "exit":
        break

    print("\nDrafting...\n")

    result = make_professional(user_input)

    print("Professional Version:")
    print(result)
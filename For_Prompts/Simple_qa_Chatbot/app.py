"""
🔰 Beginner Level Project: "Simple Q&A Chatbot"
Description:
Create a chatbot that simulates a polite assistant answering general knowledge questions. Use ChatPromptTemplate.from_messages() with a system and a human role to guide how the model responds.

What you'll practice:

Structuring prompts using roles like system, human, ai

Understanding how multi-message inputs affect model behavior

Creating a conversational flow
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0
)

chat_prompt = ChatPromptTemplate.from_messages(
    [
    ("system","you are an chatbot ai model which will answers the queries from the user AND YOU SHOULD GREET AND BE FRIENDLY"),
    ("human","Nice to meet you"),
    ("ai","How can assist you?"),
    ("user","{user_input}")
    ]
)

# Query = chat_prompt.format(user_input = "who is the president of  india on 2025")

# print(Query)


while True:
    u_input = input("Enter your question (or 'quit' to exit): ")
    if u_input.lower() in ['quit', 'exit']:  # Check multiple exit commands
        break
    
    chain = chat_prompt | llm
    result = chain.invoke({"user_input": u_input})
    print(result.content)
    print("\n")

"""⚙️ Intermediate Level Project: "Customer Support Agent Simulator"
Description:
Build a multi-turn customer support simulation where the assistant uses predefined behavior (system message) and responds to user questions about a fake product/service. Use from_messages() to stack several messages and simulate memory.

What you'll practice:

Constructing 3+ message chains (e.g., system → user → ai → user)

Adding context with earlier messages

Improving answer quality using system role conditioning
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0.5
)


chat_prompt_template = ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful support assistant."),
    ("human", "Hi, I’m having trouble with my laptop."),
    ("ai", "I'm sorry to hear that! Can you tell me what the issue is?"),
    ("human", "It's overheating a lot lately."),
    ]
)

result = chat_prompt_template | llm
print(result.content)
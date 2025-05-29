"""⚙️ Intermediate Level Project: "Code Comment Generator"
Description:
Design a prompt that takes code snippets and returns human-friendly comments. Feed it a few examples using FewShotPromptTemplate — the model learns the format and generates comments for new code.

What you'll practice:

Creating few-shot training examples for functional outputs

Mixing multi-line text inputs (code) and outputs (comments)

Applying templates for real coding contexts"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0.5
)

examples =[
    {
        "code" : "for i in range(100):\nprint(2)",
        "comment" : "#Prints the string inside the print statement fro 100 times"
    },
    {
        "code" : "def add(num1,num2):",
        "comment" : "#This is Function named as add used to add 2 number inputs"
    },
    {
        "code" : "pwhile n<=1:",
        "comment" : "#This is an while loop ,which will run until n is lesser than 1."
    }
]

prompt_template = PromptTemplate.from_template(
    template = "code:\n{code}\ncomment:\n{comment}"
    )

few_prompt = FewShotPromptTemplate(
    examples =examples,
    example_prompt = prompt_template,
    suffix = "code:\n{code}\ncomment:\n",
    input_variables = ["code"]
)

# final_prompt = few_prompt.format(code = "def sum(n,m)")

# print(final_prompt)

chain = few_prompt | llm
result = chain.invoke("def sub(n,m)")
print(result.content)


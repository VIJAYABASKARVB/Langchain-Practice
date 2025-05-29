"""
⚙️ Intermediate Level Project: "Resume Tailor Bot"
Description:
Build a tool that helps tailor a user's resume summary for specific job roles. You can use partial_variables to predefine a base user description (skills, experience), and leave {job_title} or {company} open for dynamic inputs.

What you'll practice:

Combining from_template() and PromptTemplate directly

Using partial_variables to make reusable templates

Modularizing prompt templates for different job positions

"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0
)

template = "Rewrite this professional summary for a {job_title} position at {company}. Focus on these key skills: {skills}. Make it compelling and concise."

prompt_template = PromptTemplate(
    template=template,
    input_variables=["job_title", "company"],
    partial_variables={
        "skills": "python,data analysis,Langchain"
    }
)

print(prompt_template)

chain = prompt_template | llm
print(chain.invoke({"job_title":"Data Scientist","company":"Deloite"}).content)
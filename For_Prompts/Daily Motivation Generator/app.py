'''
🔰 Beginner Level Project: "Daily Motivation Generator"
Description:
Create a simple app that generates daily motivational quotes tailored to the user's mood. Use PromptTemplate.from_template() to inject variables like {mood} and {time_of_day} into the prompt.

What you'll practice:

Understanding how PromptTemplate works

Using .format() with different variables

Creating templates using from_template

'''
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0.5
)

template = "generate a motivational quote based upon my {mood} mood and my time of the day and now its {time_of_day} "

prompt_template = PromptTemplate.from_template(template=template)

# final_prompt = prompt_template.format(time_of_day="morning",mood = "tired")

print("\n")
print("THE PROMPT THAT THE MODEL TAKES AS AN INPUT:\n")
# print(final_prompt)
print(prompt_template)

chain = prompt_template | llm
print(chain.invoke({"time_of_day": "Evening", "mood": "happy"}).content)
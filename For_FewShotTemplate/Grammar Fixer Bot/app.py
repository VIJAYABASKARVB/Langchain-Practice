"""🔰 Beginner Level Project: "Grammar Fixer Bot"
Description:
Create a small tool that corrects grammar in English sentences. Use a few example input-output pairs (incorrect → corrected) to guide the model's behavior.

What you'll practice:

Structuring few-shot examples

Using consistent formatting ("Input: ... \nOutput: ...")

Embedding the pattern into a prompt for generalization"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature = 0.5
)


examples = [
    {
        "Input" : "what this behaviour?",
        "Output" : "What is this behaviour",
        "Additional consideration" : "if the input's grammer is correct make the model to provide the output as its already in correct grammer!"
    },

    {
        "Input" : "where you are?",
        "Output" : "Where are you?",
        "Additional consideration" : "if the input's grammer is correct make the model to provide the output as its already in correct grammer!"
    },

    {
        "Input": "she go to school everyday.",
        "Output": "She goes to school every day.",
        "Additional consideration" : "if the input's grammar is correct make the model to provide the output as its already in correct grammer!"
    },

    {
        "Input": "he don't like play football.",
        "Output": "He doesn't like playing football.",
        "Additional consideration" : "if the input's grammar is correct make the model to provide the output as its already in correct grammer!"
    },

    {
        "Input" : "they is going to the market now.",
        "Output": "They are going to the market now.",
        "Additional consideration" : "if the input's grammar is correct make the model to provide the output as its already in correct grammer!"
    }
]

prompt_template = PromptTemplate.from_template(
    template = "Input:\n{Input}\nOutput:\n{Output}"
    )

# print(prompt_template.format(**examples[0]))

few_shot_template = FewShotPromptTemplate(
    examples = examples,
    example_prompt = prompt_template,
    suffix="Input:\n{Input}\nOutput:\n",
    input_variables = ["Input"]
)

# question = "who you are?"

# final_prompt = few_shot_template.format(Input=question)
# print(final_prompt)

chain = few_shot_template | llm
result = chain.invoke("How the are you?")
print(result.content)
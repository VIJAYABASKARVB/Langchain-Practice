import warnings
from langchain.chains import LLMChain, SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from my_key import api_key
import os

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set up the API token
os.environ["GROQ_API_KEY"] = api_key

# Define the LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.8,
)

def generate_restaurant_name_and_items(cuisine):
    restaurant_name = PromptTemplate(
        input_variables=["cuisine"],
        template="You are a creative branding expert specializing in restaurant names. Craft a unique, catchy, and memorable name for a {cuisine} restaurant that reflects its cultural essence and appeals to a modern audience. Ensure the name is short, easy to remember, and stands out. Output only the name without quotes, explanations, or any additional text.\n\nName:"

    )

    name_chain = LLMChain(
        llm=llm,
        prompt=restaurant_name,
        output_key="restaurant_name"
    )
    
    menu_items = PromptTemplate(
        input_variables=["restaurant_name", "cuisine"],
        template="List exactly 5 authentic {cuisine} dishes as a simple numbered menu for {restaurant_name}. Format: 1. [Dish name]\n2. [Dish name] etc. No descriptions or additional text."
    )

    menu_chain = LLMChain(
        llm=llm,
        prompt=menu_items,
        output_key="menu_items"
    )

    # Combine the chains sequentially
    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    # Run the chain and get output
    output = chain({"cuisine": cuisine})
    return output

# Entry point for the script
if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))

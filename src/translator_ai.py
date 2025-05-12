import os
import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# configure the open Api

working_dir = os.path.dirname(os.path.abspath(__file__))
configure_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = configure_data["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def translator_ai(input_langauge,output_langauge,input_text):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are helpful assistance translator {input_language} to {Output_language},"),
            ("human","{input}")
        ]
    )

    chain = prompt|llm

    response = chain.invoke(
        {
            "input_language":input_langauge,
            "Output_language":output_langauge,
            "input":input_text
        }
    )
    return response.content
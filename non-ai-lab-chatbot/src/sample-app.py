import os
import requests
import time

import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate


model_endpoint = os.getenv("MODEL_ENDPOINT", "http://localhost:8001")
model_service = f"{model_endpoint}/v1"

def checking_model_service():
    start = time.time()
    print("Checking Model Service Availability...")
    ready = False
    while not ready:
        try:
            request = requests.get(f'{model_service}/models')
            if request.status_code == 200:
                ready = True
        except:
            pass
        time.sleep(1) 
    print("Model Service Available")
    print(f"{time.time()-start} seconds")

checking_model_service()
model_name = os.getenv("MODEL_NAME", "")

llm = ChatOpenAI(base_url=model_service,
                 model=model_name,
                 api_key="no-key",
                 )

template = """You are the best advisor in the world.

A user has come to you and asks the following question:
{message}

If you need to ask clarifying questions you may do so.
"""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm

def handle_response(message, history):
    result = chain.invoke({
            "message": message
        }
    )
    output_resp = ""
    for char in result.content:
        output_resp += char
        time.sleep(0.03)
        yield output_resp


chatbot = gr.ChatInterface(
                fn=handle_response,
                title="Sample Chatbot",
)

chatbot.launch(server_port=8501)
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

def ask_bot(message, history):
    return llm.invoke(message).content

chat = gr.ChatInterface(
        ask_bot,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Pergunte algo sobre para o SuperBot!", container=False, scale=7),
        title="SuperBot",
        description="Nosso SuperBot está pronto para atender suas perguntas!",
        theme="soft",
        examples=["Quem é você?", "O que você sabe sobre futebol?", "O que é uma abelha?"],
        cache_examples=True,
        retry_btn=None,
        undo_btn=None,
        submit_btn="Enviar",
        clear_btn="Limpar",
    )

chat.launch(share=True, server_name="0.0.0.0", server_port=7860)
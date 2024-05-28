from retriever import retrieve
from embeddings import embed_doc
from model import get_response
import gradio as gr
from langchain_openai import ChatOpenAI

def ask_bot(user_prompt, history):
    sources_retrieved = retrieve(embed_doc(user_prompt))

    return get_response("llama", user_prompt, history, sources_retrieved)

chat = gr.ChatInterface(
        ask_bot,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Pergunte algo sobre para o BOTcamp!", container=False, scale=7),
        title="Botcamp LLM4Devs ",
        description="Nosso BOTcamp está pronto para atender suas perguntas!",
        theme="soft",
        retry_btn=None,
        undo_btn=None,
        submit_btn="Enviar",
    )

chat.launch(share=True, server_name="0.0.0.0", server_port=7860)
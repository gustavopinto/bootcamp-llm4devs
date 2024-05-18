from retriever import retrieve
from embeddings import embed_doc

import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

def ask_bot(message, history):

    print(history)

    query = embed_doc(message)
    sources_retrieved = retrieve(query)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um expert em turismo em Belém. Responda a pergunta do usuário em até 30 palavras"),
            ("human", "{user_input}"),
            ("system", "Para responder a pergunta do usuário, considere as seguintes referências: {sources_retrieved}"),
            ("system", "Considere também o histórico de conversa: {history}"),
        ]
    )

    chain = prompt | llm
    response = chain.invoke({"user_input": message, "sources_retrieved": sources_retrieved, "history": history})

    return response.content

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
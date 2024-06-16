import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from databaser import retrieve

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

def chat_llm(user_query, history):
    prompt = ChatPromptTemplate.from_messages([
                        ("system", "Eu quero que você atue como um expert em design de código."),
                        ("user", "{user_query}"),
                        ("system", "Para responder a pergunta, considere o historico de conversa: {history}"),
                        ("system", "Nao precisa começar a responder com 'Pelo histórico da nossa conversa'. Pode responder diretamente."),
                        ("system", "Em mensagens de apresentacao, se limite a responder em 100 palavras."),
                        ("system", "Considere essas informacoes sobre design de codigo: {cdd}"),
                    ])

    chain = prompt | llm

    chunks = retrieve(embeddings.embed_query(user_query))
    print(chunks)

    response = chain.invoke({"user_query" : user_query,
                             "history" : history,
                             "cdd" : chunks
                             })
    return response.content


def ask_bot(message, history):
    return chat_llm(message, history)

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
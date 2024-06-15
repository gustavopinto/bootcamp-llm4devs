from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# 1. quantidade de tokens é uma limitacao do modelo
# 2. os modelos sao stateless; nao guardam informacoes anteriores
# 3. podemos variar a resposta do modelo usando a `temperature`

# resposta = llm.invoke("Oi, meu nome é Gustavo e eu estou no meio de um bootcamp sobre llm.")
# print(resposta.content)
# print("\n")
# resposta = llm.invoke("qual é o meu nome?")
# print(resposta.content)


llm = ChatOpenAI(temperature=1)

def chat_llm(user_query, history):
    prompt = ChatPromptTemplate.from_messages([
                        ("system", "Eu quero que você atue como um expert em design de código atuando com criancas."),
                        ("user", "{user_query}"),
                        ("system", "Para responder a pergunta, considere o historico de conversa: {history}"),
                        ("system", "Nao precisa começar a responder com 'Pelo histórico da nossa conversa'. Pode responder diretamente."),
                        ("system", "Em mensagens de apresentacao, se limite a responder em 30 palavras."),
                        ("system", "Se a pergunta nao for sobre design de codigo, se limite a responder 'Eu não sei'."),
                    ])

    chain = prompt | llm
    response = chain.invoke({"user_query" : user_query,
                             "history" : history})
    return response.content

history = []

while True:
    user_query = input("> ")
    history.append(user_query)
    llm_response = chat_llm(user_query, history)

    history.append(llm_response)
    print("> ", llm_response)
    

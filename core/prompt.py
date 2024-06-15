from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=1)

# 1. quantidade de tokens é uma limitacao do modelo
# 2. os modelos sao stateless; nao guardam informacoes anteriores
# 3. podemos variar a resposta do modelo usando a `temperature`

resposta = llm.invoke("Oi, meu nome é Gustavo e eu estou no meio de um bootcamp sobre llm.")
print(resposta.content)
print("\n")
resposta = llm.invoke("qual é o meu nome?")
print(resposta.content)



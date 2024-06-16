from databaser import store, retrieve
from langchain_openai import OpenAIEmbeddings
from splitter import chunknizer

# chunks = chunknizer("https://arxiv.org/pdf/2210.07342")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
# chunks_emb = []

# print("criando embeddings...")

# for chunk in chunks:
#     emb = embeddings.embed_query(chunk) 
#     chunks_emb.append(emb)


# print("inserindo embeddings no banco...")

# store(chunks, chunks_emb)

user_quer = embeddings.embed_query("what are the limitations of CDD?") 

chunks = retrieve(user_quer)

for chunk in chunks:
    print(chunk)
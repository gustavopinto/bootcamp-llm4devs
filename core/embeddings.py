from langchain_openai import OpenAIEmbeddings
from splitter import chunknizer
from scipy import spatial

chunks = chunknizer("https://arxiv.org/pdf/2210.07342")
#print(len(chunks))

# vetores de alta dimensao
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
chunks_emb = []

for chunk in chunks[0:15]:
    # o vetor resultante dos embeddings vao ter sempre o mesmo tamanho
    # eles guardam a informacao, a semantica do conteudo, as relacoes de palavras

    emb = embeddings.embed_query(chunk) 
    chunks_emb.append(emb)

#print(len(chunks_emb))

user_query = "como fazer uma lasanha?"
user_query_emb = embeddings.embed_query(user_query)


for idx in range(0, len(chunks_emb)):
    distancia = 1 - spatial.distance.cosine(chunks_emb[idx], user_query_emb)
    if distancia > 0.5:
        print(distancia, chunks[idx][:15], user_query)
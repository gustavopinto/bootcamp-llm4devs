from loader import load
from transformer import transform
from embeddings import embed_docs, embed_doc
from retriever import store, retrieve

# source = "https://llmbootcamp.dev/"

# source_loaded = load(source)

# sources_transformed = transform(source_loaded[0].page_content)

# print(len(sources_transformed))

# sources_embedded = embed_docs(sources_transformed)

# print(len(sources_embedded))

# stored = store(sources_transformed, sources_embedded)

query = embed_doc("onde ir em Belém?")

sources_retrieved = retrieve(query)

print(sources_retrieved)
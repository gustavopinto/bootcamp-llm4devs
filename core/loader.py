from langchain_community.document_loaders import WebBaseLoader

def load(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    return data
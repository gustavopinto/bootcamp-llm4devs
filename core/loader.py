from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader


def load_url(url):
    loader = WebBaseLoader(url)
    return loader.load()


def load_pdf(url):
    loader = PyPDFLoader(url)
    return loader.load()

# content = load_pdf("https://arxiv.org/pdf/2210.07342")
# print(content)

# content = load_url("https://python.langchain.com/v0.1/docs/modules/data_connection/")
# print(content)
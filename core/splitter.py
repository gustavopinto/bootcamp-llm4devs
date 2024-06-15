from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_pdf

content = load_pdf("https://arxiv.org/pdf/2210.07342")

# chunks sao pedacos de conteudo que idealmente sao coesos.

# 1. processamento de dados -> antes de criar os chunks, eu colocaria _MUITO_ esforco nessa etapa
pages = [page.page_content for page in content]
content_str = "\n".join(pages)


# 2. tenho que estudar o conteudo final dos chunks
text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        ".",
        "!",
        "?",
        ";",
        ",",
        " ",
        "",
    ],
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

chunks = text_splitter.split_text(content_str)

print(chunks)
for idx, chunk in enumerate(chunks):
    print(idx, chunk)

print(len(chunks))
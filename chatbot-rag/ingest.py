# ingest.py — script complet pour indexer PDF, TXT et Markdown

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    DirectoryLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def load_documents(data_path="data"):

    pdf_loader = DirectoryLoader(
        data_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    txt_loader = DirectoryLoader(
        data_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    md_loader = DirectoryLoader(
        data_path,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = (
        pdf_loader.load()
        + txt_loader.load()
        + md_loader.load()
    )

    print(f"{len(documents)} document(s) chargé(s).")

    return documents



def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    print(f"{len(chunks)} chunk(s) créé(s).")

    return chunks



def create_vectorstore(chunks, save_path="faiss_index"):

    if len(chunks) == 0:
        print("Aucun document trouvé. Vérifier le dossier data/")
        return

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(save_path)

    print(f"Index FAISS sauvegardé dans '{save_path}'.")

    return vectorstore



if __name__ == "__main__":

    docs = load_documents("data")

    chunks = split_documents(docs)

    create_vectorstore(
        chunks,
        "faiss_index"
    )
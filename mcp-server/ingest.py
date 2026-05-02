import os
import chromadb
from chromadb.utils import embedding_functions
from typing import Any, cast

client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.get_or_create_collection(
    name="knowledge_base", embedding_function=cast(Any, ef)
)


def ingest_docs(docs_path: str = "./docs"):
    files = [f for f in os.listdir(docs_path) if f.endswith(".txt")]

    if not files:
        print("No .txt files found in /docs")
        return

    for filename in files:
        filepath = os.path.join(docs_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = [text[i : i + 500] for i in range(0, len(text), 500)]
        ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]

        collection.upsert(documents=chunks, ids=ids)
        print(f"Ingested {filename} — {len(chunks)} chunks")


if __name__ == "__main__":
    ingest_docs()

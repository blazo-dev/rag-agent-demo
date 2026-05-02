from fastmcp import FastMCP
import chromadb
from chromadb.utils import embedding_functions
from typing import Any, cast

mcp = FastMCP("rag-mcp-server")

client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.get_or_create_collection(
    name="knowledge_base", embedding_function=cast(Any, ef)
)


@mcp.tool()
def query_knowledge_base(query: str, n_results: int = 3) -> str:
    """Query the knowledge base and return relevant context."""
    results = collection.query(query_texts=[query], n_results=n_results)

    documents = results.get("documents")
    if not documents or not documents[0]:
        return "No relevant information found."

    chunks = documents[0]
    return "\n\n---\n\n".join(chunks)


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)

import os
import asyncio

from fastmcp import Client
from strands import Agent, tool
from strands.models.ollama import OllamaModel

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000/mcp")


@tool
def query_knowledge_base(query: str) -> str:
    """Query the RAG knowledge base via MCP and return relevant context."""

    async def _query():
        async with Client(MCP_SERVER_URL) as client:
            result = await client.call_tool("query_knowledge_base", {"query": query})
            return result.data

    return asyncio.run(_query())


def create_agent(use_tools: bool = True, system_prompt: str | None = None) -> Agent:
    model = OllamaModel(
        model_id="llama3.2",
        host="http://localhost:11434",
    )

    prompt = system_prompt or """You are a helpful assistant.
Use only the provided knowledge base context to answer questions.
If the context does not contain relevant information, say so clearly."""

    agent = Agent(
        model=model,
        tools=[query_knowledge_base] if use_tools else [],
        system_prompt=prompt,
    )
    return agent


def run_agent(query: str) -> str:
    context = query_knowledge_base(query)
    if not context or context.strip() == "No relevant information found.":
        return "No relevant information found in the knowledge base."

    agent = create_agent(use_tools=False)
    prompt = (
        "You are given context from a knowledge base.\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer using only the context. If the context is insufficient, say so clearly."
    )
    response = agent(prompt)
    return str(response).strip()

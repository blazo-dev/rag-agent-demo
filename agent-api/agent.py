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


def create_agent() -> Agent:
    model = OllamaModel(
        model_id="llama3.2",
        host="http://localhost:11434",
    )

    agent = Agent(
        model=model,
        tools=[query_knowledge_base],
        system_prompt="""You are a helpful assistant with access to a knowledge base.
Always query the knowledge base before answering questions.
Base your answers only on the retrieved context.
If the knowledge base does not contain relevant information, say so clearly.""",
    )
    return agent


def run_agent(query: str) -> str:
    agent = create_agent()
    response = agent(query)
    return str(response)

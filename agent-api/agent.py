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
        model_id="qwen2.5:7b-instruct",
        host="http://localhost:11434",
    )
    prompt = (
        system_prompt
        or """You are Bryan Lazo's professional assistant.

RULES:
- Answer ONLY using the KB context provided. Never invent or assume facts.
- Be concise: 1 to 3 sentences maximum unless more detail is explicitly requested.
- Always refer to Bryan in third person (Bryan, he, his). Never use first person.
- Do not greet, add filler phrases, or explain your reasoning.
- If the context is insufficient, respond exactly: "I don't have enough information about that. Contact Bryan at blazo.dev@gmail.com"
- If asked about availability or hiring, always include: blazo.dev@gmail.com and linkedin.com/in/bryanlazodev"""
    )

    return Agent(
        model=model,
        tools=[query_knowledge_base] if use_tools else [],
        system_prompt=prompt,
    )


def run_agent(query: str) -> str:
    agent = create_agent(use_tools=True)

    prompt = (
        f"QUESTION: {query}\n\n"
        "INSTRUCTIONS:\n"
        "- Answer strictly using the context above.\n"
        "- Be direct and concise — 1 to 3 sentences.\n"
        "- Refer to Bryan in third person.\n"
        "- No greetings, filler, or meta commentary.\n"
        "- Decide if you need to use the knowledge base tool."
        "- If the question is about Bryan, you MUST use the tool."
        "- Answer only with verified information."
        "- If the context is insufficient, respond: "
        "\"I don't have enough information about that. "
        'Contact Bryan at blazo.dev@gmail.com"'
    )

    response = agent(prompt)
    return str(response).strip()

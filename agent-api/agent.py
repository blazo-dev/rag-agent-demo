import os

from mcp.client.streamable_http import streamable_http_client
from strands import Agent
from strands.models.ollama import OllamaModel
from strands.tools.mcp.mcp_client import MCPClient

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000/mcp")


def _create_mcp_client() -> MCPClient:
    def create_transport():
        url = MCP_SERVER_URL
        if not url.endswith("/"):
            url = f"{url}/"
        return streamable_http_client(url)

    return MCPClient(create_transport)


def create_agent(
    system_prompt: str | None = None,
    tools: list | None = None,
) -> Agent:
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

    resolved_tools = tools if tools is not None else []

    return Agent(model=model, tools=resolved_tools, system_prompt=prompt)


def run_agent(query: str) -> str:
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

    mcp_client = _create_mcp_client()
    with mcp_client:
        tools = mcp_client.list_tools_sync()
        agent = create_agent(tools=tools)
        response = agent(prompt)

    return str(response).strip()

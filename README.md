# RAG Agent Demo

End-to-end RAG-powered AI agent using MCP protocol for tool integration — FastMCP server with ChromaDB + sentence-transformers as knowledge base, consumed by a Strands Agent powered by Google Gemini, with a React chat interface.

## Architecture

```plaintext
User (React UI)
    ↓ HTTP POST /chat
Agent API (FastAPI)
    ↓ MCP tool call
MCP Server (FastMCP)
    ↓ vector search
ChromaDB + sentence-transformers
    ↓ context returned
Gemini 2.0 Flash
    ↓
Response rendered in UI
```

## Services

- **mcp-server** — FastMCP server exposing a `query_knowledge_base` tool backed by ChromaDB
- **agent-api** — Strands Agent wrapped in a FastAPI REST layer
- **ui** — React chat interface

## Quick Start

```bash
cp .env.example .env
# Add your GEMINI_API_KEY to .env
docker-compose up --build
```

Then open <http://localhost:3000>

## Tech Stack

FastMCP · ChromaDB · sentence-transformers · Strands Agents · Google Gemini 2.0 Flash · FastAPI · React · Docker · Docker Compose · Python 3.12

# RAG Agent Demo

End-to-end RAG-powered AI agent using MCP protocol for tool integration — FastMCP server
with ChromaDB + sentence-transformers as knowledge base, consumed by a Strands Agent
powered by Ollama (qwen2.5:7b-instruct), with a React chat interface.

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
Ollama qwen2.5:7b-instruct (local)
    ↓
Response rendered in UI

```

## Services

- **mcp-server** — FastMCP server exposing a `query_knowledge_base` tool backed by ChromaDB
- **agent-api** — Strands Agent wrapped in a FastAPI REST layer
- **ui** — React chat interface

## Quick Start

```bash
# 1. Install dependencies
uv venv --python 3.12
uv pip install -r requirements.txt

# 2. Install and start Ollama
# Download from https://ollama.com
ollama pull qwen2.5:7b-instruct

# 3. Configure environment
cp agent-api/.env.example agent-api/.env

# 4. Ingest documents
cd mcp-server
uv run python ingest.py

# 5. Start MCP server (terminal 1)
uv run python server.py

# 6. Start Agent API (terminal 2)
cd agent-api
uv run uvicorn main:app --host 0.0.0.0 --port 8001 --reload

# 7. Start React UI (terminal 3)
cd ui
pnpm install
pnpm dev
```

## Tech Stack

FastMCP · ChromaDB · sentence-transformers · Strands Agents · Ollama qwen2.5:7b-instruct · FastAPI · React · Python 3.12+

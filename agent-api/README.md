# Agent API

Strands Agent wrapped in a FastAPI REST layer. Connects to the MCP server to retrieve
context and generates grounded responses using Ollama llama3.2 running locally.

## What it does

- Exposes POST /chat endpoint
- Strands Agent calls `query_knowledge_base` tool via MCP protocol
- Retrieves relevant context from ChromaDB through the MCP server
- Sends context to Ollama llama3.2 for grounded response generation
- Returns answer as JSON

## Files

- `main.py` — FastAPI app and endpoint definitions
- `agent.py` — Strands Agent setup with Ollama and MCP tool

## Setup

```bash
# Copy and configure environment
cp .env.example .env
```

## Environment Variables

```bash
MCP_SERVER_URL=http://localhost:8000/mcp
```

## Usage

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

## Endpoints

- `POST /chat` — Body: `{ "message": "your question" }` → Response: `{ "response": "answer" }`
- `GET /health` — Health check

## Tech Stack

- Strands Agents
- Ollama llama3.2 (local, no API key required)
- FastAPI
- FastMCP client
- Python 3.12+

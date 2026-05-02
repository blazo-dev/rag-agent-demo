# MCP Server

FastMCP server that wraps a local RAG pipeline and exposes a `query_knowledge_base`
tool for any MCP-compatible agent.

## What it does

- Ingests .txt documents from the /docs folder
- Generates embeddings using sentence-transformers (all-MiniLM-L6-v2)
- Stores vectors locally in ChromaDB
- Exposes a `query_knowledge_base` MCP tool on port 8000

## Files

- `server.py` — FastMCP server definition and tool exposure
- `ingest.py` — Document ingestion pipeline into ChromaDB
- `docs/` — Place your .txt documents here before ingesting
- `chroma_db/` — Auto-generated vector store (gitignored)

## Usage

```bash
# Ingest documents first
uv run python ingest.py

# Start the server
uv run python server.py
```

Server runs at <http://localhost:8000/mcp>

## Tech Stack

- FastMCP 3.2+
- ChromaDB
- sentence-transformers (all-MiniLM-L6-v2)
- Python 3.12+

## Inspired by

Production work integrating AWS AgentCore Gateway + Bedrock Knowledge Bases at
enterprise scale. This project replicates the core pattern using open-source tooling.

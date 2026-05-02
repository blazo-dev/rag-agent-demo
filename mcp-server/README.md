# MCP Server

FastMCP server that wraps a local RAG pipeline and exposes a `query_knowledge_base` 
tool for any MCP-compatible agent.

## What it does

- Ingests documents from the /docs folder
- Generates embeddings using sentence-transformers
- Stores vectors in ChromaDB
- Exposes a `query_knowledge_base` MCP tool on port 8000

## Tech Stack

- FastMCP
- ChromaDB
- sentence-transformers
- Python 3.12

## Inspired by

Production work integrating AWS AgentCore Gateway + Bedrock Knowledge Bases at 
enterprise scale. This project replicates the core pattern using open-source tooling.
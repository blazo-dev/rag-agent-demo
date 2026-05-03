# RAG Agent Demo — PRD

## Goal

Build an end-to-end RAG-powered AI agent using MCP as the tool integration protocol,
with a React chat UI for interaction. Fully local — no cloud APIs required.

## Components

- **mcp-server** — FastMCP server that wraps a local RAG pipeline and exposes a `query_knowledge_base` tool
- **agent-api** — Strands Agent connected to the MCP server, wrapped in a FastAPI REST layer
- **ui** — React chat interface that calls the agent-api

## Tech Stack

FastMCP, ChromaDB, sentence-transformers, Strands Agents, Ollama llama3.2, FastAPI, React, Python 3.12+

## Core Flow

1. User submits a query via React UI
2. UI calls POST /chat on agent-api
3. Strands Agent calls `query_knowledge_base` tool via MCP
4. MCP server retrieves relevant chunks from ChromaDB
5. Context returned to agent
6. Ollama llama3.2 generates grounded response locally
7. Response rendered in React UI

## Infrastructure

- Single shared venv at project root managed by uv
- mcp-server and agent-api run as separate processes
- agent-api exposes POST /chat endpoint via FastAPI
- UI communicates with agent-api via REST
- Ollama runs as a local service on port 11434
- Environment variables managed via .env file in agent-api/

## MVP Scope

- [x] Ingest .txt documents into ChromaDB
- [x] Expose retrieval as MCP tool via FastMCP
- [x] Wrap Strands Agent in FastAPI with POST /chat endpoint
- [x] Agent returns grounded answer using Ollama locally
- [x] Connect React UI to agent-api
- [x] Full stack documented and ready for demo

## Out of Scope

- Authentication
- Multi-user support
- Cloud deployment
- Streaming responses

## Success Criteria

- Agent answers accurately based only on ingested documents
- MCP tool call visible in agent reasoning trace
- Chat UI functional and clean
- Project runs fully local with no external API dependencies

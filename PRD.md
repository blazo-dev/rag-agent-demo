# RAG Agent Demo — PRD

## Goal

Build an end-to-end RAG-powered AI agent using MCP as the tool integration protocol, with a React chat UI for interaction.

## Components

- **mcp-server** — FastMCP server that wraps a local RAG pipeline and exposes a `query_knowledge_base` tool
- **agent-api** — Strands Agent connected to the MCP server, wrapped in a FastAPI REST layer
- **ui** — React chat interface that calls the agent-api

## Tech Stack

FastMCP, ChromaDB, sentence-transformers, Strands Agents, Google Gemini 2.0 Flash, FastAPI, React, Docker, Python 3.12

## Core Flow

1. User submits a query via React UI
2. UI calls POST /chat on agent-api
3. Strands Agent calls `query_knowledge_base` tool via MCP
4. MCP server retrieves relevant chunks from ChromaDB
5. Context returned to agent
6. Gemini 2.0 Flash generates grounded response
7. Response rendered in React UI

## Infrastructure

- Docker + Docker Compose
- mcp-server, agent-api, and ui run as separate containers
- agent-api exposes POST /chat endpoint via FastAPI
- UI communicates with agent-api via REST
- Internal Docker network between mcp-server and agent-api
- Environment variables managed via .env file

## MVP Scope

- [ ] Ingest .txt or .pdf documents into ChromaDB
- [ ] Expose retrieval as MCP tool via FastMCP
- [ ] Wrap Strands Agent in FastAPI with POST /chat endpoint
- [ ] Connect React UI to agent-api
- [ ] Full stack runs with docker-compose up

## Out of Scope

- Authentication
- Multi-user support
- Cloud deployment
- Streaming responses

## Success Criteria

- Agent answers accurately based only on ingested documents
- MCP tool call visible in agent reasoning trace
- Full stack spins up with docker-compose up
- Chat UI functional and clean
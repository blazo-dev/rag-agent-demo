# RAG Agent Demo — PRD

## Goal
Build an end-to-end RAG-powered AI agent using MCP as the tool integration protocol.

## Components
- **rag-mcp-server** — FastMCP server that wraps a local RAG pipeline and exposes a `query_knowledge_base` tool
- **strands-rag-agent** — Strands Agent that connects to the MCP server and generates grounded responses via Gemini 2.0 Flash

## Tech Stack
- FastMCP, ChromaDB, sentence-transformers, Strands Agents, Google Gemini 2.0 Flash, Python 3.13+

## Core Flow
1. User submits a query to the Strands Agent
2. Agent calls `query_knowledge_base` tool via MCP
3. MCP server retrieves relevant chunks from ChromaDB
4. Context returned to agent
5. Gemini generates grounded response

## MVP Scope
- [ ] Ingest a set of .txt or .pdf documents into ChromaDB
- [ ] Expose retrieval as MCP tool via FastMCP
- [ ] Connect Strands Agent to MCP server
- [ ] Agent returns grounded answer to user query
- [ ] Clean CLI interface for demo purposes

## Out of Scope (for now)
- Authentication
- Multi-user support
- Cloud deployment
- UI frontend

## Success Criteria
- Agent answers questions accurately based only on ingested documents
- MCP tool call visible in agent reasoning trace
- Project runs locally with a single setup command

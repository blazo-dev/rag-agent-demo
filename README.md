# RAG Agent with MCP Integration — End to End Demo

A full end-to-end demonstration of a RAG-powered AI agent using the
Model Context Protocol (MCP) for tool integration. Built entirely with
open-source tooling and free APIs.

## Overview
This project consists of two components working together:

1. **rag-mcp-server** — An MCP server that wraps a local RAG pipeline
   (ChromaDB + sentence-transformers) and exposes it as a callable tool.

2. **strands-rag-agent** — An AI agent built with Strands Agents that
   connects to the MCP server, retrieves relevant context, and generates
   grounded answers using Google Gemini 2.0 Flash.

## Why this matters
Modern enterprise AI systems separate knowledge retrieval from agent logic.
The MCP protocol is the emerging standard that makes this separation possible —
allowing any MCP-compatible agent (including Salesforce Agentforce and AWS Bedrock
Agents) to connect to any MCP-compatible knowledge source.

This project demonstrates that pattern end to end, from document ingestion
to agent response.

## Architecture
```
User Query
    ↓
Strands Agent (strands-rag-agent)
    ↓ MCP tool call
RAG MCP Server (rag-mcp-server)
    ↓ vector search
ChromaDB + sentence-transformers
    ↓ context returned
Strands Agent → Gemini 2.0 Flash
    ↓
Grounded Response
```

## Tech Stack
- Strands Agents · FastMCP · ChromaDB
- sentence-transformers · Google Gemini 2.0 Flash
- Python 3.13+

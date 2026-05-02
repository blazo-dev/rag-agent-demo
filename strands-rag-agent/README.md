# Strands RAG Agent

An AI agent built with the Strands Agents framework that uses an external MCP server
as its knowledge retrieval tool, powered by Google Gemini as the LLM backend.

## What it does
Connects to the rag-mcp-server via MCP protocol, uses the `query_knowledge_base` tool
to retrieve relevant context, and generates accurate, grounded responses using
Gemini 2.0 Flash. Demonstrates agentic tool use with external MCP integration.

## Tech Stack
- Strands Agents — agentic framework
- FastMCP client — MCP tool integration
- Google Gemini 2.0 Flash — LLM (free tier via Google AI Studio)
- Python 3.13+

## Architecture
user query → Strands Agent → MCP tool call → rag-mcp-server → ChromaDB
→ context retrieved → Gemini generates response → answer returned

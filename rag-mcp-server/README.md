# RAG MCP Server

A production-inspired MCP (Model Context Protocol) server built with FastMCP that exposes
a Retrieval-Augmented Generation (RAG) knowledge base as a callable tool for external AI agents.

## What it does
Ingests documents, generates embeddings using sentence-transformers, stores vectors in ChromaDB,
and exposes a `query_knowledge_base` tool via the MCP protocol. Any MCP-compatible agent can
connect to this server and retrieve semantically relevant context from the knowledge base.

## Tech Stack
- FastMCP — MCP server framework
- ChromaDB — local vector store
- sentence-transformers — open-source embeddings (no API key required)
- Python 3.11+

## Architecture
documents → embeddings → ChromaDB → FastMCP tool → MCP-compatible agents

## Inspired by
Production work integrating AWS AgentCore Gateway + Bedrock Knowledge Bases at enterprise scale.
This project replicates the core pattern using open-source tooling.

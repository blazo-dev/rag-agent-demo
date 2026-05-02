# Agent API

Strands Agent wrapped in a FastAPI REST layer. Connects to the MCP server to retrieve 
context and generates grounded responses using Google Gemini 2.0 Flash.

## What it does

- Exposes POST /chat endpoint
- Strands Agent calls `query_knowledge_base` tool via MCP protocol
- Sends retrieved context to Gemini 2.0 Flash for response generation
- Returns grounded answer as JSON

## Tech Stack

- Strands Agents
- FastAPI
- Google Gemini 2.0 Flash
- Python 3.12

## Endpoints

POST /chat

Body: { "message": "your question here" }

Response: { "response": "agent answer", "sources": [] }
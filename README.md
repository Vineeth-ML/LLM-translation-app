# 🌐 Simple LLM Translation App with LCEL

A simple LLM application built with **LangChain Expression Language (LCEL)**
and **FastAPI** that translates English text into any language using Groq AI.

## 🏗️ Architecture

User Input → Prompt Template → LLM (Groq) → Output Parser → Response

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/docs` | GET | Swagger UI |
| `/chain/invoke` | POST | Translate text |
| `/chain/stream` | POST | Stream translation |


### Using curl:
    curl -X POST http://localhost:8000/chain/invoke \
    -H "Content-Type: application/json" \
    -d '{"input": {"language": "French", "text": "Hello!"}}'

### Using Swagger UI:
    Open http://localhost:8000/docs in your browser

## 🛠️ Tech Stack

- **LangChain** — LLM framework
- **LCEL** — LangChain Expression Language for chaining
- **Groq** — LLM inference (llama-3.1-8b-instant)
- **FastAPI** — API framework
- **LangServe** — Deploy LangChain chains as REST APIs

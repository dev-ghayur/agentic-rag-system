# Agentic RAG System

This project implements a basic agentic Retrieval-Augmented Generation (RAG) system that autonomously decides whether to retrieve answers from internal documents or perform a web search when its confidence in document-based answers is low.

## Features

*   **Document Ingestion**: Loads and indexes text and PDF documents using embeddings and FAISS vector store.
*   **Retriever-based QA**: Implements a RAG pipeline for answering queries based on indexed documents, including confidence scoring.
*   **Agentic Decision Layer**: An intelligent agent evaluates the confidence of the RAG output. If confidence is below a predefined threshold, it triggers a web search.
*   **Web Search Agent**: Fetches and summarizes information from the web using DuckDuckGo.
*   **Structured Output**: Returns answers in a consistent JSON format, indicating the source (document or web), answer text, confidence score, and contextual snippets.
*   **User Interface**: A Streamlit frontend for easy interaction, backed by a FastAPI backend.
*   **Logging**: Logs generated in a log file and controlled by environment variable log level.

## Architecture

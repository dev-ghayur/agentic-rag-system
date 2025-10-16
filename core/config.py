import os

# LLM Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Web Search Configuration
# DUCKDUCKGO_API_KEY = os.getenv("DUCKDUCKGO_API_KEY")

# RAG Configuration
CONFIDENCE_THRESHOLD = 0.7
VECTOR_DB_PATH = "faiss_index" # Path to save/load FAISS index
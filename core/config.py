import os
from dotenv import load_dotenv
load_dotenv()

# LLM Configuration
GEMINI_CONFIG = {
    "model_name": "gemini-2.5-flash",
    "temperature": 0.7,
    "max_tokens": 1024,
    "streaming": True,
    "extras": {},
}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Web Search Configuration
# DUCKDUCKGO_API_KEY = os.getenv("DUCKDUCKGO_API_KEY")

# RAG Configuration
CONFIDENCE_THRESHOLD = 0.7
VECTOR_DB_PATH = "faiss_index" # Path to save/load FAISS index
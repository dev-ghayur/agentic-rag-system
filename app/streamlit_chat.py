# streamlit_app.py
import streamlit as st
import requests
import json
import os

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")

st.set_page_config(page_title="Agentic RAG Assistant", layout="wide")

st.title("🧠 Agentic RAG Assistant")
st.markdown("""
Welcome to the Agentic RAG Assistant! This system intelligently decides whether to retrieve answers
from its internal knowledge base or search the web based on its confidence level.
""")

st.sidebar.header("About")
st.sidebar.info(
    """
    This application demonstrates an Agentic RAG system.
    - Loads documents into a FAISS vector store.
    - Uses a RAG for answering questions from documents.
    - Determines if RAG output is good enough,
      otherwise triggers a web search.
    - Fetches and summarizes information from the web.
    """
)

st.write("---")

user_query = st.text_input("Ask me anything:", placeholder="e.g., What is the capital of France? or Latest news on climate change?")

if st.button("Get Answer"):
    if user_query:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(f"{FASTAPI_URL}/query", json={"query": user_query})
                response.raise_for_status() # Raise an exception for HTTP errors
                result = response.json()

                st.subheader("Answer:")
                st.write(result.get("answer", "No answer found."))

                st.markdown(f"**Source:** `{result.get('source', 'N/A')}`")
                st.markdown(f"**Confidence:** `{result.get('confidence', 0.0):.2f}`")

                if result.get("context_snippets"):
                    st.subheader("Context Snippets:")
                    for i, snippet in enumerate(result["context_snippets"]):
                        st.expander(f"Snippet {i+1} (Source: {result.get('source_metadata', [{}])[i].get('source', 'N/A')} - Title: {result.get('source_metadata', [{}])[i].get('title', 'N/A')})").write(snippet)

            except requests.exceptions.ConnectionError:
                st.error(f"Could not connect to FastAPI backend at {FASTAPI_URL}. Please ensure it's running.")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a query.")

st.write("---")
st.info("Remember to have your 'documents' directory populated for RAG to work effectively!")

from typing import List, Dict
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from .chunker_base import BaseChunker


class SemanticChunkerImpl(BaseChunker):
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.text_splitter = SemanticChunker(
            self.embedding_model,
            breakpoint_threshold_type="percentile"
        )

    def chunk_content(self, content: str) -> List[Dict]:
        """Split the text semantically into chunks. Returns a list of dicts with 'text' as chunk content."""
        docs = self.text_splitter.create_documents([content])
        return [{"text": doc.page_content} for doc in docs]

if __name__ == "__main__":
    text = """
    Artificial Intelligence (AI) is transforming industries across the world.
    From healthcare to finance, AI systems help automate decisions and improve outcomes.
    However, ethical concerns about bias, privacy, and transparency remain significant challenges.
    Organizations must adopt responsible AI frameworks to ensure fair and safe usage.
    """

    chunker = SemanticChunkerImpl()
    chunks = chunker.chunk_content(text)

    print(f"Total chunks created: {len(chunks)}\n")
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}:\n{chunk['text']}\n{'-' * 40}")

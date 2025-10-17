from typing import List, Dict
from abc import ABC, abstractmethod
 
class BaseChunker(ABC):
    def preprocess_content(self, content: str) -> str:
        """Preprocess the content before chunking."""

    def chunk_content(self, content: str) -> List[Dict]:
        """Chunking method to create chunks of document."""

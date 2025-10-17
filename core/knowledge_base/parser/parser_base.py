from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def process_file(self, file_path: str) -> str :
        """Process the file and return extracted text."""

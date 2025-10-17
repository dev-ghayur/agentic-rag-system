from pypdf import PdfReader
from core.rag.knowledge_base.parser.parser_base import BaseParser


class PyPDFParser(BaseParser):
    def process_file(self, file_path: str) -> list[str]:
        """Parse a PDF document from the given file path and return a list of text blocks (paragraphs)
        for chunking/embedding.Handles missing files, empty files, corrupted files, and format mismatches."""
        parsed_output = []

        try:
            # Read the PDF document
            reader = PdfReader(file_path)
            num_pages = len(reader.pages)

            if num_pages == 0:
                print(f"Warning: No pages found in file -> {file_path}")
                return []

            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    # Split the text into paragraphs based on double newlines
                    paragraphs = [para.strip() for para in text.split('\n\n') if para.strip()]
                    parsed_output.extend(paragraphs)

            if not parsed_output:
                print(f"Warning: File contains no usable text -> {file_path}")

        except FileNotFoundError:
            print(f"Error: File not found -> {file_path}")
        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")

        return parsed_output

if __name__ == "__main__":
    parser = PyPDFParser()

    # Provide a sample file path
    sample_file = "core/resource/sample_files/survery_qc.pdf"

    parsed_output = parser.process_file(sample_file)

    print("Parsed Output:")
    for i, paragraph in enumerate(parsed_output, start=1):
        print(f"--- Paragraph {i} ---")
        print(paragraph)
        if i == 5:
            break # Print only first 5 paragraphs
        print()

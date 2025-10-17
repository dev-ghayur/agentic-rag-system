import gc
from core.rag.knowledge_base.parser.parser_base import BaseParser
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream


class DoclingParser(BaseParser):
    def __init__(self):
        self.converter = DocumentConverter()

    def process_file(self, file_path: str) -> list[str]:
        """
        Parse a document from the given file path and return
        a list of text blocks (paragraphs) for chunking/embedding.
        Handles missing files, empty files, corrupted files, and format mismatches.
        """
        parsed_output = []

        try:
            # Convert the document into a DocumentStream
            doc_stream: DocumentStream = self.converter.convert(file_path)

            if not hasattr(doc_stream, "blocks") or not doc_stream.blocks:
                print(f"Warning: No text blocks found in file -> {file_path}")
                return []

            for block in doc_stream.blocks:
                text = getattr(block, "text", "").strip()
                if text:
                    parsed_output.append(text)

            if not parsed_output:
                print(f"Warning: File contains no usable text -> {file_path}")

        except FileNotFoundError:
            print(f"Error: File not found -> {file_path}")
        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")
        finally:
            # Cleanup to prevent memory leaks
            try:
                del doc_stream
            except NameError:
                pass
            gc.collect()

        return parsed_output


if __name__ == "__main__":
    parser = DoclingParser()

    # Provide a sample file path
    sample_file = "/workspaces/agentic-rag-system/resource/sample_files/survery_qc.pdf"

    parsed_output = parser.process_file(sample_file)

    print("Parsed Output:")
    for i, paragraph in enumerate(parsed_output, start=1):
        print(f"--- Paragraph {i} ---")
        print(paragraph)
        if i == 5:
            break # Print only first 5 paragraphs
        print()

from io import BytesIO
from core.knowledge_base.parser.parser_base import BaseParser
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream


class DoclingParser(BaseParser):
    def __init__(self):

    def process_file(self, file_path: str) -> tuple[str, dict]:
        try:
            # content = self.client.get_object(file_path)
            # if not isinstance(content, bytes):
            #     error_message = f"Error in {self.__class__.__name__}: File {file_path} fetched from s3 bucket '{self.bucket_name}' is not a binary object"
            #     logger.error(error_message)
            #     raise TypeError(error_message)
            # buf = BytesIO(content)
            source = DocumentStream(name=file_path, stream=buf)
            converter = DocumentConverter()
            result = converter.convert(source)

            # Extract document data in json format
            document_data = result.document.export_to_dict()
            file_name = document_data.get("name", "")
            text_blocks = document_data.get("texts", [])
            table_blocks = document_data.get("tables", [])

            # Transform text_blocks into the required output format
            pages_data = self.extract_text_data(text_blocks)

            # Extract table data and add to pages_data
            # tables_by_page = self.extract_table_data(table_blocks)
            # self.add_table_data(pages_data, table_blocks, tables_by_page)

            document_dict = {file_name: pages_data}
            # Extract document text
            document_text = result.document.export_to_text()
            return document_text, document_dict
        except Exception as e:
            logger.error(f"Error in {self.__class__.__name__} while processing {file_path}: {e}")
            return "", {}

    def extract_text_data(self, text_blocks):
        try:
            pages_data = {}
            for block in text_blocks:
                page_no = str(block["prov"][0]["page_no"])
                text = block["text"]
                if page_no not in pages_data:
                    pages_data[page_no] = {
                        "text-content": [text],
                        "tables": [],
                        "images": []
                    }
                else:
                    pages_data[page_no]["text-content"].append(text)
            
            for page_no, data in pages_data.items():
                data["text-content"] = " ".join(data["text-content"])
            
            return pages_data
        except Exception as e:
            logger.error(f"Error in {self.__class__.__name__} while extracting text data: {e}")
            return {}

if __name__ == "__main__":
    # Example code to check the working of the parser
    pass

 
class BaseChunking:
    def __init__(self, config: Dict):
        """
        Initialize the base chunking class with the provided configuration.
        
        :param config: Dictionary containing chunking configuration parameters
        """
        self.max_token_size = config.get("chunk_size", constants.DEFAULT_CHUNK_TOKEN_SIZE)
        self.overlap_token_size = config.get("chunk_overlap", constants.DEFAULT_CHUNK_OVERLAP_TOKEN_SIZE)

    def preprocess_content(self, content: str) -> str:
        """
        Preprocess the content before chunking.
        This method can be overridden in subclasses to implement specific preprocessing logic.
        
        :param content: The raw content to preprocess
        :return: The preprocessed content
        """
        return content.strip().replace('\r\n', '\n')
    
    @staticmethod
    def count_tokens(text: str) -> int:
        """
        Count the number of tokens in the text.
        
        :param text: The text to count tokens in
        :return: The number of tokens
        """
        return len(text.strip())

    def postprocess_chunks(self, chunks: List[str]) -> List[Dict]:
        """
        Postprocess the chunks after chunking.
        This method standardizes the chunk format.
        
        :param chunks: List of string chunks to postprocess
        :return: The postprocessed chunks
        """
        processed_chunks = []
        for index, chunk in enumerate(chunks, 1):
            chunk_content = chunk.strip()
            if not chunk_content:  # Skip empty chunks
                continue
            processed_chunk = {
                "content": chunk_content,
                "chunk_order_index": index,
                "tokens": BaseChunking.count_tokens(chunk_content)
            }
            processed_chunks.append(processed_chunk)
        
        return processed_chunks

    def chunker(self, content: str) -> List[Dict]:
        """
        Main chunking method that orchestrates the chunking process.
        
        :param content: The content to chunk
        :return: List of processed chunks
        """
        try:
            # Step 1: Preprocess the content
            preprocessed_content = self.preprocess_content(content)
            if not preprocessed_content:
                logger.warning("Empty content after preprocessing")
                return []
            
            # Step 2: Perform the actual chunking
            chunks = self._chunk_content(preprocessed_content)
            if not chunks:
                logger.warning("No chunks generated from _chunk_content")
                return []
            
            # Step 3: Postprocess the chunks
            processed_chunks = self.postprocess_chunks(chunks)
            
            return processed_chunks
        except Exception as e:
            logger.error(f"Error in chunking process: {str(e)}")
            raise

    def _chunk_content(self, content: str) -> List[str]:
        """
        This method should be implemented in the subclass to handle specific chunking logic.
        
        :param content: The preprocessed content to chunk
        :return: List of string chunks
        """
        raise NotImplementedError("The _chunk_content method must be implemented in subclasses.")

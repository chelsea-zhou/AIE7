import os
from typing import List
import pypdf


class PDFLoader:
    """Load and extract text from PDF files"""
    
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"PDF file not found: {path}")
    
    def load_documents(self) -> List[str]:
        """Load and extract text from PDF file"""
        try:
            with open(self.path, 'rb') as file:
                pdf_reader = pypdf.PdfReader(file)
                
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    
                    if text.strip():  # Only add non-empty pages
                        self.documents.append(text)
                
                return self.documents
                
        except Exception as e:
            raise Exception(f"Error reading PDF file: {e}")
    
    def load_file(self):
        """Legacy method for compatibility"""
        return self.load_documents()


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    with open(
                        os.path.join(root, file), "r", encoding=self.encoding
                    ) as f:
                        self.documents.append(f.read())

    def load_documents(self):
        self.load()
        return self.documents


class UniversalDocumentLoader:
    """Load documents from various file types (TXT, PDF)"""
    
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.path = path
        self.encoding = encoding
    
    def load_documents(self) -> List[str]:
        """Load documents based on file extension"""
        if self.path.endswith('.pdf'):
            loader = PDFLoader(self.path, self.encoding)
        elif self.path.endswith('.txt'):
            loader = TextFileLoader(self.path, self.encoding)
        else:
            raise ValueError(f"Unsupported file type: {self.path}")
        
        return loader.load_documents()


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks


if __name__ == "__main__":
    # Test with text file
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])

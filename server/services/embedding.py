
import os
import io
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from services.storage import save_embedding

load_dotenv()
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

async def embed_document(file_bytes: bytes, filename: str):
    reader = PdfReader(io.BytesIO(file_bytes))
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = splitter.split_text(full_text)

    for chunk in texts:
        vector = embeddings.embed_query(chunk)
        save_embedding(filename, chunk, vector)

def get_embedding_for_query(query: str):
    return embeddings.embed_query(query)

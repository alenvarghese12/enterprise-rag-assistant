import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

CHROMA_PATH = os.getenv("CHROMA_PATH")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
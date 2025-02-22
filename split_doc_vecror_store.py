from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
from extract_text import extract_document_text
load_dotenv()  # This loads variables from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")
def process_documents(file_list, chunk_size=1000, chunk_overlap=200):
    all_chunks = []
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    for file in file_list:
        try:
            text = extract_document_text(file)
            if text.strip():
                # Split each file's text into manageable chunks                chunks = splitter.split_text(text)
                all_chunks.extend(chunks)
        except Exception as e:
            print(f"Error processing {file.name}: {e}")
    if not all_chunks:
        raise ValueError("No text extracted from any files. Check your file extraction code.")
    return all_chunks
def create_vector_store(chunks, persist_directory="./vector_store"):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)  # Ensure your OpenAI API key is set
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(persist_directory)
    return vector_store
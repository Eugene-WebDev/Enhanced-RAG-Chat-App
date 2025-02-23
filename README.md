# Enhanced-RAG-Chat-App

A Streamlit-based Retrieval-Augmented Generation (RAG) Chat Application that allows users to upload documents (PDF, TXT, DOCX, CSV, MD), process and split them into manageable chunks, store their embeddings using FAISS, and answer user queries by retrieving relevant content from the documents—all while providing a modern, live-chat interface.

## Features

- **Document Upload:** Upload various document types (PDF, TXT, DOCX, CSV, MD) via the sidebar.
- **Text Extraction & Splitting:** Extract text from documents and split it into manageable chunks to avoid token limit issues.
- **Vector Store Creation:** Generate embeddings using OpenAI and store them locally using FAISS.
- **Modern RAG Chat Interface:** Ask questions based on your uploaded documents. The chat UI uses native Streamlit components (`st.chat_input` and `st.chat_message`) for a polished, live-chat experience with real-time response streaming.
- **Chat History:** Maintains conversation history in session state, with user questions rendered immediately.

## Project Structure

. ├── main.py # Streamlit app: handles file uploads, modern chat interface, and query processing ├── split_doc_vector_store.py # Processes documents, splits text, and creates the FAISS vector store ├── extract_text.py # Contains helper functions to extract text from various document types ├── .env # Environment file (must contain your OPENAI_API_KEY) └── README.md # This file


## Requirements

- Python 3.7+
- Streamlit (version 1.24+ recommended to support native chat components)
- Langchain
- FAISS
- PyPDF2
- python-docx
- pandas
- markdown
- python-dotenv

You can install the required packages using:
pip install streamlit langchain faiss-cpu PyPDF2 python-docx pandas markdown python-dotenv

### Setup

Clone the repository:
git clone https://github.com/Eugene-WebDev/Enhanced-RAG-Chat-App.git
cd Enhanced-RAG-Chat-App

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Configure your environment:

Create a .env file in the root directory and add your OpenAI API key in the following format:
OPENAI_API_KEY=your_openai_api_key_here

### Usage:

Start the Streamlit App:
streamlit run main.py

Upload Documents:

Use the sidebar to upload your documents (PDF, TXT, DOCX, CSV, MD).
Click Process Documents to extract text, split it into chunks, and build the vector store.

Chat Interface:

Enter your query in the chat input at the bottom of the page.

Your question will appear immediately in the chat history.
The app retrieves relevant chunks from your documents and streams the assistant's answer word-by-word.

### Code Overview

main.py:
Handles the UI using Streamlit. It manages file uploads, maintains chat history, and integrates the RAG chain to answer user queries. The new implementation uses native chat components (st.chat_input and st.chat_message) for a modern, live-chat experience with immediate rendering of user questions and streaming responses.

split_doc_vector_store.py:
Processes uploaded documents by extracting and splitting text and creates a FAISS vector store for efficient retrieval.

extract_text.py:
Provides functions for extracting text from different document types (PDF, TXT, DOCX, CSV, MD).


**Troubleshooting** 

Token Limit Issues:
If you experience token limit errors, ensure that the text is properly split into smaller chunks. You can also experiment with different chain types (e.g., map_reduce or refine) in the RetrievalQA chain.

API Key Errors:
Make sure that your .env file contains a valid OPENAI_API_KEY.

**Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.

**License**
This project is licensed under the MIT License.

**Acknowledgements**
Built with Streamlit and Langchain.
Inspired by the growing need for efficient Retrieval-Augmented Generation systems.

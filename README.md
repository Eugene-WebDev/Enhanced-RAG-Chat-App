# Enhanced-RAG-Chat-App

A Streamlit-based Retrieval-Augmented Generation (RAG) Chat Application that allows users to upload documents (PDF, TXT, DOCX, CSV, MD), processes and splits them into manageable chunks, stores their embeddings using FAISS, and answers user queries by retrieving relevant content from the documents.

## Features

- **Document Upload**: Upload a variety of document types (PDF, TXT, DOCX, CSV, MD).
- **Text Extraction & Splitting**: Extract text from documents and split them into manageable chunks to avoid token limit issues.
- **Vector Store Creation**: Generate embeddings using OpenAI and store them locally using FAISS.
- **RAG Chat Interface**: Ask questions based on the uploaded documents with responses streamed in real time.
- **Chat History**: Maintains conversation history for context.

## Project Structure

```
.
├── main.py                   # Streamlit app: handles file uploads, chat interface, and query processing
├── split_doc_vector_store.py  # Processes documents, splits text, and creates the FAISS vector store
├── extract_text.py            # Contains helper functions to extract text from various document types
├── .env                       # Environment file (must contain your OPENAI_API_KEY)
└── README.md                  # This file
```

## Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [Langchain](https://github.com/hwchase17/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [python-docx](https://pypi.org/project/python-docx/)
- [pandas](https://pandas.pydata.org/)
- [markdown](https://pypi.org/project/Markdown/)
- [dotenv](https://pypi.org/project/python-dotenv/)

You can install the required packages using:

```bash
pip install streamlit langchain faiss-cpu PyPDF2 python-docx pandas markdown python-dotenv
```

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *(Alternatively, install the packages manually as listed above.)*

4. **Configure your environment:**

   - Create a `.env` file in the root directory.
   - Add your OpenAI API key in the following format:

     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. **Start the Streamlit App:**

   ```bash
   streamlit run main1.py
   ```

2. **Upload Documents:**

   - Use the sidebar to upload your documents (PDF, TXT, DOCX, CSV, MD).
   - Click **Process Documents** to extract text, split it into chunks, and build the vector store.

3. **Chat Interface:**

   - Enter your query in the text input and click **Send**.
   - The app retrieves relevant chunks from your documents and streams the answer.

## Code Overview

- **main1.py**:  
  Handles the UI using Streamlit, manages file uploads, chat history, and integrates the RAG chain to answer user queries.

- **split_doc_vector_store.py**:  
  Processes uploaded documents by extracting and splitting text using `CharacterTextSplitter`, then creates a FAISS vector store for efficient retrieval.

- **extract_text.py**:  
  Provides functions for extracting text from different document types (PDF, TXT, DOCX, CSV, MD).

## Troubleshooting

- **Token Limit Issues**:  
  If you experience token limit errors, ensure that the text is properly split into smaller chunks. You can also experiment with different chain types (e.g., `map_reduce` or `refine`) in the RetrievalQA chain.

- **API Key Errors**:  
  Make sure that your `.env` file contains a valid `OPENAI_API_KEY`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/) and [Langchain](https://github.com/hwchase17/langchain).
- Inspired by the growing need for efficient Retrieval-Augmented Generation systems.

```

---

This README provides a clear project overview, setup instructions, usage guidelines, and more to help users and contributors understand and work with your project. Feel free to customize it further to suit your project’s specifics.

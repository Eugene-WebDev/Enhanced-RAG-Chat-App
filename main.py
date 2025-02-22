import streamlit as st
import time
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from extract_text import extract_text_pdf, extract_text_txt, extract_text_docx, extract_text_csv, extract_text_md, extract_document_text
from split_doc_vector_store import process_documents, create_vector_store
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")
def stream_response(response_text):
    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Upload PDF, TXT, DOCX, CSV, MD files", type=["pdf", "txt", "docx", "csv", "md"], accept_multiple_files=True)
    if st.button("Process Documents") and uploaded_files:
        text_chunks = process_documents(uploaded_files)
        if not text_chunks:
            st.error("No text extracted from documents. Please upload readable files.")        else:
            st.session_state.text_chunks = text_chunks
            create_vector_store(text_chunks)
            st.success("Documents processed and embeddings stored.")
st.title("Enhanced RAG Chat App")
st.markdown("Ask questions based on your uploaded documents. Your conversation history
will be maintained.")
user_input = st.text_input("Your message:")
if st.button("Send") and user_input:
    if len(user_input) > 500:
        st.warning("Your question is too long. Please shorten it.")
        user_input = user_input[:500]
    st.session_state.chat_history.append({"sender": "user", "message": user_input})
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    try:
        vector_store = FAISS.load_local("./vector_store", embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"Error loading vector store: {e}")
        st.stop()
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    llm = OpenAI(temperature=0, max_tokens=200)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    answer = qa_chain.run(user_input)
    st.session_state.chat_history.append({"sender": "assistant", "message": answer})
    response_placeholder = st.empty()
    streamed_answer = ""
    for word in stream_response(answer):
        streamed_answer += word
        response_placeholder.markdown(f"**Assistant:** {streamed_answer}")
st.markdown("### Conversation History")
for chat in st.session_state.chat_history:
    if chat["sender"] == "user":
        st.markdown(f"**User:** {chat['message']}")
    else:
        st.markdown(f"**Assistant:** {chat['message']}")
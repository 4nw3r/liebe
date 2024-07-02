import streamlit as st
import requests
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
import os
from groq import Groq

# Initialize components
folder_path = "db"

cached_llm = Ollama(model="llama3") #You can use LLaVa model as well for vision and add upload image functionality

embedding = FastEmbedEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=80, length_function=len, is_separator_regex=False
)

raw_prompt = PromptTemplate.from_template("""
 <s> [INST] You are a helpful technical assistant, expert at searching and articulating information from the documents. If you do not have an answer form the provided information context say so. [/INST] </s>
[INST] {input}
        Context: {context}
        Answer:               
[/INST]
""")

# Streamlit app
st.title("AI Assistant")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
st.header("Chatbot Interface")
for chat in st.session_state.chat_history:
    st.write(f"**You:** {chat['query']}")
    st.write(f"**AI:** {chat['response']}")

# User input
query = st.text_input("Enter your query:")
if st.button("Submit Query"):
    response = requests.post("http://localhost:11434/ai", json={"query": query}).json()
    st.write(f"**AI:** {response['answer']}")

    # Update chat history
    st.session_state.chat_history.append({"query": query, "response": response['answer']})

# RAG functionality for Custom Agents
st.header("Ask PDF")
pdf_query = st.text_input("Enter your query for the PDF:")
if st.button("Submit PDF Query"):
    response = requests.post("http://localhost:11434/ask_pdf", json={"query": pdf_query}).json()
    st.write(f"**AI:** {response['answer']}")

    st.write("Sources:")
    for source in response["sources"]:
        st.write(f"Source: {source['source']}, Content: {source['page_content']}")

# PDF operations functionality
st.header("Upload PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    save_file = f"pdf/{uploaded_file.name}"
    with open(save_file, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"PDF File {uploaded_file.name} saved")

    with open(save_file, "rb") as f:
        response = requests.post("http://localhost:11434/pdf", files={"file": f}).json()

    st.write(response)

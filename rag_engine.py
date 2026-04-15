import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

from scraper import fetch_article

@st.cache_resource(show_spinner=False)
def get_embeddings():
    """Load HuggingFace embeddings (cached across reruns)."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_vector_store(urls: list[str]):
    """Fetch articles, split into chunks, embed, and return a FAISS vector store."""
    docs = []
    errors = []
    for url in urls:
        url = url.strip()
        if not url:
            continue
        try:
            text = fetch_article(url)
            if not text or len(text) < 100:
                errors.append(f"⚠️ Too little content at: {url}")
                continue
            docs.append(Document(page_content=text, metadata={"source": url}))
        except Exception as e:
            errors.append(f"❌ {e}")

    if not docs:
        return None, errors, []

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store, errors, chunks

def get_answer(question: str, vector_store, api_key: str):
    """Retrieve context and generate an answer using LCEL."""
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        api_key=api_key,
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )

    # Retrieve relevant docs
    source_docs = retriever.invoke(question)

    # Build context string
    context = "\n\n".join(doc.page_content for doc in source_docs)

    # LCEL RAG chain
    prompt = ChatPromptTemplate.from_template(
        """You are a helpful assistant. Answer the question based ONLY on the following context.
        If the answer is not contained in the context, say \"I don't have enough information in the provided articles to answer this.\"\n\n"
        "Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"""
    )

    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke({"context": context, "question": question})

    # Build unique source list
    unique_sources = list(
        {doc.metadata.get("source", "") for doc in source_docs if doc.metadata.get("source")}
    )

    return answer, unique_sources, source_docs

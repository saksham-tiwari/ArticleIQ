# ArticleIQ — Retrieval-Augmented Generation (RAG) Article Q&A

ArticleIQ is a modular, AI-powered Retrieval-Augmented Generation (RAG) application built with **Streamlit**, **LangChain**, **FAISS**, and **Groq**. It allows users to feed article URLs, from which it scrapes the content, indexes it into a locally-hosted vector store, and answers user questions strictly based on the provided context.

## 🌟 Features

- **Seamless Web Scraping**: Automatically fetches and cleans content from up to 5 article URLs simultaneously using `requests` and `BeautifulSoup4`.
- **Intelligent Chunking**: Employs LangChain's `RecursiveCharacterTextSplitter` to optimally segment text into manageable units.
- **Local Embedding**: Uses free, fast, and local `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace for dense vector representation.
- **In-Memory Vector Store**: Fast caching and similarity search powered by FAISS.
- **Lightning-Fast LLM Inference**: Powered by the highly performant **Groq `llama-3.1-8b-instant`** model.
- **Citation and Sourcing**: Explicitly states the related chunks and links used to generate its answers.
- **Interactive UI**: A highly stylized, intuitive Streamlit frontend with modular components.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
|---|---|---|
| **Frontend Options** | Streamlit | Lightweight and interactive web interface |
| **Web Scraping** | `requests`, `BeautifulSoup4` | Removes HTML noise (nav, footer, ads) to extract raw article content |
| **Embeddings** | `HuggingFace` | `all-MiniLM-L6-v2` for chunk-level semantic search |
| **Vector Store** | FAISS | High-dimensionality similarity search (In-memory) |
| **LLM** | Groq | Cloud-based rapid LLM inferencing (`llama-3.1-8b-instant`) |
| **Orchestration** | LangChain | Custom LCEL pipelines for document retrieval and prompt injection |

---

## 🚀 Setup & Installation

### 1. Prerequisites
- **Python 3.9+** installed on your system.
- A free **Groq API Key**: Get it from the [Groq Cloud Console](https://console.groq.com/).

### 2. Clone the Repository
```bash
git clone https://github.com/saksham-tiwari/ArticleIQ.git
cd ArticleIQ
```

### 3. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Configuration
Create a `.env` file in the root directory and add your API key:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```
*(Alternatively, you can skip this step and enter your key directly into the Streamlit sidebar at runtime).*

---

## 🕹️ Usage Guide

1. **Launch the Application**
   ```bash
   streamlit run main.py
   ```
2. **Provide URLs**: In the sidebar, paste 1 to 5 URLs of articles you'd like the AI to analyze.
3. **Build the Knowledge Base**: Click the **⚡ Process URLs & Build Vector DB** button. The app will fetch the text and compute embeddings.
4. **Ask Questions**: Once processed, type any question related to the articles in the main chat area (e.g., *"What is the main finding of the article?"*).
5. **Verify Sources**: Click on the **Relevant chunks** or **Sources used** sections to trace exactly where the model sourced its information.

---

## 📂 Project Structure

```text
ArticleIQ/
├── .env                # Environment variables (API Keys) - Ignored in version control
├── main.py             # Streamlit application entry point and UI logic
├── rag_engine.py       # Core logic for embeddings, FAISS store, and LCEL LLM chain
├── scraper.py          # Web crawling utility to retrieve and sanitize text
├── styles.py           # Custom CSS styling and Streamlit UI component layouts
├── requirements.txt    # Project dependencies
└── README.md           # This document
```

## 🧠 Architecture Overview (How RAG Works)

1. **Extraction**: `requests` + `BeautifulSoup` retrieve and clean text from URLs.
2. **Chunking**: `RecursiveCharacterTextSplitter` cuts text into 1,000-character segments (with 200 overlap).
3. **Embedding**: `HuggingFaceEmbeddings` maps text into high-dimensional vector space.
4. **Indexing**: FAISS creates an in-memory search index of the vectors.
5. **Retrieval**: The User's question is embedded to perform similarity search, obtaining the top 5 relevant document chunks.
6. **Generation**: The context chunks + user question are parsed to Groq using a LangChain conversational LCEL workflow.

## 🐛 Troubleshooting

- **No module named 'langchain' / 'streamlit'**: Ensure you are running the app with the correct virtual environment activated where `requirements.txt` was installed.
- **Groq API Key Errors**: Double-check your `.env` file format and ensure there are no missing characters in your key.
- **Article not fetching**: Some sites use heavy JavaScript rendering or protections (like Cloudflare) which block simple request fetches. Try providing a standard news or blog article URL.

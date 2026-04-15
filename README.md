# ArticleIQ — RAG Article Q&A

A **Retrieval-Augmented Generation (RAG)** app built with LangChain, FAISS, and Groq.

Paste article URLs → the app scrapes, chunks, and indexes them → ask questions → the AI answers **only from your articles**.

---

## Tech Stack

| Layer | Tech |
|---|---|
| UI | Streamlit |
| Web scraping | `requests` + `BeautifulSoup4` |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` (local, free) |
| Vector store | FAISS (in-memory) |
| LLM | Groq `llama-3.1-8b-instant` |
| Orchestration | LangChain (`RetrievalQAWithSourcesChain`) |

---

## Setup

### 1. Configure your API key

Edit `.env` and replace the placeholder:

```
GROQ_API_KEY=your_actual_groq_api_key
```

Get a free key at [console.groq.com](https://console.groq.com).

### 2. Install dependencies (if using a fresh venv)

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
# From GenAI root (using shared .venv)
/Users/sakshamtiwari/GenAI/.venv/bin/streamlit run "Project 1/main.py"

# Or if inside the Project 1 folder with activated venv
streamlit run main.py
```

---

## Usage

1. **Paste URLs** — Enter 1–5 article URLs in the sidebar
2. **Process** — Click *"⚡ Process URLs & Build Vector DB"*
3. **Ask** — Type a question and click *"🤖 Get Answer"*
4. **Explore** — Expand *Relevant chunks* to see exactly what context was used

---

## How RAG Works Here

```
Article URLs
    │
    ▼
requests + BeautifulSoup → clean article text
    │
    ▼
RecursiveCharacterTextSplitter → chunks (1000 chars, 200 overlap)
    │
    ▼
HuggingFace all-MiniLM-L6-v2 → embeddings
    │
    ▼
FAISS vector store (in-memory)
    │
 Question ──► similarity search → top-5 chunks
                                       │
                                       ▼
                              Groq llama-3.1-8b-instant
                                       │
                                       ▼
                              Answer + Sources
```

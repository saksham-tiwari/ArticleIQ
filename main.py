import os
import streamlit as st
from dotenv import load_dotenv

# Import custom modules
from styles import (
    apply_custom_styles,
    render_sidebar_header,
    render_hero,
    render_how_it_works,
    render_step_badge,
    render_footer_card
)
from rag_engine import build_vector_store, get_answer

# ── Load environment variables ──────────────────────────────────────────────
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# ── Page configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="ArticleIQ — Modular RAG",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Apply Styling ───────────────────────────────────────────────────────────
apply_custom_styles()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    render_sidebar_header()

    render_step_badge(1, "Paste Article URLs")

    url_inputs = []
    for i in range(1, 6):
        url = st.text_input(
            f"URL {i}",
            key=f"url_{i}",
            placeholder=f"https://example.com/article-{i}",
            label_visibility="collapsed",
        )
        url_inputs.append(url)

    st.markdown("<br>", unsafe_allow_html=True)

    process_clicked = st.button("⚡ Process URLs & Build Vector DB", use_container_width=True)

    st.markdown("---")
    render_how_it_works()

    st.markdown("---")
    groq_key_sidebar = st.text_input(
        "🔑 Groq API Key (optional override)",
        type="password",
        placeholder="Leave blank to use .env",
        key="groq_key_input",
    )

# ── Main area ─────────────────────────────────────────────────────────────────
render_hero()

# ── Process URLs Logic ────────────────────────────────────────────────────────
if process_clicked:
    valid_urls = [u.strip() for u in url_inputs if u.strip()]
    if not valid_urls:
        st.error("Please enter at least one article URL in the sidebar.")
    else:
        with st.spinner("🔍 Fetching articles and building vector database…"):
            vector_store, errors, chunks = build_vector_store(valid_urls)

        # Show any errors from fetching
        if errors:
            for err in errors:
                st.warning(err)

        if vector_store is not None:
            st.session_state["vector_store"] = vector_store
            st.session_state["processed_urls"] = valid_urls
            st.session_state["chunks"] = chunks

            st.success(f"✅ Vector DB ready! Indexed **{len(chunks)} chunks** from **{len(valid_urls)} article(s)**.")

            # Show preview of top chunks
            with st.expander("📄 Preview indexed chunks (first 5)", expanded=False):
                for i, chunk in enumerate(chunks[:5]):
                    st.markdown(
                        f'<div class="chunk-box"><b>Chunk {i+1}</b> — {chunk.metadata.get("source","")}<br><br>{chunk.page_content[:400]}…</div>',
                        unsafe_allow_html=True,
                    )
        elif not errors: # No store and no errors yet means nothing was processed
            st.error("Could not index any articles. Please check the URLs and try again.")

# ── Q&A Section ───────────────────────────────────────────────────────────────
st.markdown("---")
render_step_badge(2, "Ask a Question")

question = st.text_input(
    "Your question",
    placeholder="e.g. What are the main findings of the article?",
    label_visibility="collapsed",
    key="question_input",
)

ask_clicked = st.button("🤖 Get Answer", key="ask_btn")

if ask_clicked:
    if "vector_store" not in st.session_state:
        st.warning("⚠️ Please process at least one article URL first (use the sidebar).")
    elif not question.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        # Resolve API key
        api_key = groq_key_sidebar.strip() or os.getenv("GROQ_API_KEY", "")

        if not api_key:
            st.error("❌ No Groq API key found. Add it to your `.env` file or paste it in the sidebar.")
        else:
            with st.spinner("🧠 Thinking…"):
                try:
                    answer, unique_sources, source_docs = get_answer(
                        question, 
                        st.session_state["vector_store"], 
                        api_key
                    )

                    # Display answer
                    st.markdown(
                        f"""
                        <div class="answer-box">
                            <div style="color:#a5b4fc; font-weight:600; font-size:0.85rem; letter-spacing:0.05em; margin-bottom:10px;">
                                ✦ ANSWER
                            </div>
                            <div style="color:rgba(230,230,245,0.95); line-height:1.7; font-size:1rem;">
                                {answer}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Sources
                    if unique_sources:
                        st.markdown(
                            '<div style="margin-top:16px; color:rgba(200,200,220,0.8); font-size:0.85rem; font-weight:600;">📎 Sources used:</div>',
                            unsafe_allow_html=True,
                        )
                        chips = "".join(
                            f'<a href="{s}" target="_blank" class="source-chip">🔗 {s}</a>'
                            for s in unique_sources
                        )
                        st.markdown(chips, unsafe_allow_html=True)

                    # Relevant chunks
                    if source_docs:
                        with st.expander("🔎 Relevant chunks used to generate this answer", expanded=False):
                            for i, doc in enumerate(source_docs):
                                st.markdown(
                                    f'<div class="chunk-box"><b>Chunk {i+1}</b> — {doc.metadata.get("source","")}<br><br>{doc.page_content}</div>',
                                    unsafe_allow_html=True,
                                )

                except Exception as e:
                    st.error(f"❌ Error generating answer: {e}")

# ── Empty state ───────────────────────────────────────────────────────────────
if "vector_store" not in st.session_state and not process_clicked:
    render_footer_card()

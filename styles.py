import streamlit as st

def apply_custom_styles():
    """Apply all custom CSS overrides to the Streamlit app."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        /* ── Global font ── */
        html, body, [class*="css"], * {
            font-family: 'Inter', sans-serif !important;
        }

        /* ── Main background ── */
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 55%, #24243e 100%) !important;
            min-height: 100vh;
        }

        /* ── Hide Streamlit chrome (toolbar, hamburger, footer) ── */
        #MainMenu, footer, header,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="manage-app-button"],
        .stDeployButton { display: none !important; }

        /* ── Sidebar ── */
        [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
            background: rgba(15, 12, 41, 0.85) !important;
            backdrop-filter: blur(16px) !important;
            border-right: 1px solid rgba(99, 102, 241, 0.3) !important;
        }

        /* ── ALL INPUT FIELDS — dark background, white text ── */
        input, textarea,
        [data-testid="stTextInput"] input,
        [data-testid="stTextInput"] textarea,
        .stTextInput input,
        .stTextInput textarea,
        div[data-baseweb="input"] input,
        div[data-baseweb="textarea"] textarea,
        div[data-baseweb="base-input"] input {
            background-color: rgba(255, 255, 255, 0.08) !important;
            background: rgba(255, 255, 255, 0.08) !important;
            color: #e2e8f0 !important;
            border: 1px solid rgba(99, 102, 241, 0.4) !important;
            border-radius: 10px !important;
            caret-color: #a5b4fc !important;
        }
        input:focus, textarea:focus,
        div[data-baseweb="input"]:focus-within input,
        div[data-baseweb="base-input"]:focus-within input {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.25) !important;
            outline: none !important;
        }
        input::placeholder, textarea::placeholder {
            color: rgba(160, 160, 200, 0.5) !important;
        }

        /* ── Input wrapper backgrounds (BaseWeb) ── */
        div[data-baseweb="input"],
        div[data-baseweb="base-input"],
        div[data-baseweb="textarea"],
        [data-testid="stTextInput"] > div > div,
        .stTextInput > div > div {
            background: rgba(255,255,255,0.08) !important;
            border-radius: 10px !important;
        }

        /* ── Password input eye button ── */
        [data-baseweb="input"] button {
            background: transparent !important;
            color: rgba(160,160,200,0.7) !important;
        }

        /* ── Labels ── */
        label, [data-testid="stWidgetLabel"] p,
        .stTextInput label, .stTextInput p {
            color: rgba(200, 210, 235, 0.9) !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
        }

        /* ── Markdown text ── */
        .stMarkdown p, .stMarkdown li, .stMarkdown span,
        [data-testid="stMarkdownContainer"] p {
            color: rgba(210, 215, 240, 0.9) !important;
        }

        /* ── Buttons ── */
        .stButton > button {
            background: linear-gradient(135deg, #6366f1, #a855f7) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            padding: 10px 24px !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
        }
        .stButton > button:hover {
            opacity: 0.88 !important;
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
            transform: translateY(-1px) !important;
        }
        .stButton > button:active {
            transform: translateY(0) !important;
        }

        /* ── Success / warning / error banners ── */
        [data-testid="stNotification"],
        .stSuccess, .stWarning, .stError, .stInfo,
        div[data-testid="stAlert"] {
            border-radius: 12px !important;
            border-left-width: 4px !important;
        }
        .stSuccess, div[data-testid="stAlert"][kind="success"] {
            background: rgba(16, 185, 129, 0.12) !important;
            border-left-color: #10b981 !important;
            color: #a7f3d0 !important;
        }
        .stWarning, div[data-testid="stAlert"][kind="warning"] {
            background: rgba(245, 158, 11, 0.12) !important;
            border-left-color: #f59e0b !important;
            color: #fde68a !important;
        }
        .stError, div[data-testid="stAlert"][kind="error"] {
            background: rgba(239, 68, 68, 0.12) !important;
            border-left-color: #ef4444 !important;
            color: #fca5a5 !important;
        }

        /* ── Spinner ── */
        [data-testid="stSpinner"] > div {
            border-top-color: #6366f1 !important;
        }

        /* ── Expander ── */
        details[data-testid="stExpander"] {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(99, 102, 241, 0.25) !important;
            border-radius: 12px !important;
        }
        details[data-testid="stExpander"] summary {
            color: rgba(200, 210, 240, 0.9) !important;
            font-weight: 500 !important;
        }
        details[data-testid="stExpander"] summary:hover {
            color: #a5b4fc !important;
        }

        /* ── Divider ── */
        hr { border-color: rgba(99, 102, 241, 0.2) !important; }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: rgba(0,0,0,0.2); }
        ::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.5); border-radius: 3px; }

        /* ── Custom component classes ── */
        .card {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }
        .answer-box {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.12));
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 16px;
            padding: 24px;
            margin-top: 16px;
        }
        .source-chip {
            display: inline-block;
            background: rgba(99, 102, 241, 0.18);
            border: 1px solid rgba(99, 102, 241, 0.45);
            color: #a5b4fc;
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 13px;
            margin: 4px 4px 4px 0;
            text-decoration: none !important;
            word-break: break-all;
            transition: background 0.15s ease;
        }
        .source-chip:hover { background: rgba(99, 102, 241, 0.35); }
        .hero-title {
            font-size: 2.6rem;
            font-weight: 700;
            background: linear-gradient(90deg, #c7d2fe, #f0abfc, #fbcfe8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
        }
        .hero-subtitle {
            color: rgba(196, 200, 230, 0.85);
            font-size: 1.05rem;
            margin-top: 10px;
            line-height: 1.6;
        }
        .step-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            border-radius: 50%;
            color: white;
            font-weight: 700;
            font-size: 13px;
            margin-right: 8px;
            flex-shrink: 0;
        }
        .chunk-box {
            background: rgba(0,0,0,0.3);
            border-left: 3px solid #6366f1;
            border-radius: 8px;
            padding: 14px 16px;
            font-size: 13px;
            line-height: 1.6;
            color: rgba(210, 215, 235, 0.88);
            margin-bottom: 12px;
            white-space: pre-wrap;
            word-break: break-word;
        }
        .sidebar-label {
            color: rgba(200, 210, 240, 0.9);
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }
        .how-it-works {
            background: rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 10px;
            padding: 14px 16px;
            color: rgba(200, 210, 235, 0.85) !important;
            font-size: 13px;
            line-height: 1.8;
        }
        .how-it-works b { color: #a5b4fc !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_sidebar_header():
    """Render the Sidebar logo and header."""
    st.markdown(
        """
        <div style="text-align:center; padding: 12px 0 24px 0;">
            <span style="font-size:2.5rem">📰</span>
            <h2 style="color:white; margin:8px 0 4px 0; font-size:1.4rem;">ArticleIQ</h2>
            <p style="color:rgba(200,200,220,0.7); font-size:0.85rem;">Your personal article intelligence layer</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_hero():
    """Render the Hero title and subtitle."""
    st.markdown(
        """
        <div class="hero-title">Article Intelligence Q&A</div>
        <div class="hero-subtitle">
            Paste article links → Build a vector knowledge base → Ask anything — powered by LangChain + Groq
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

def render_how_it_works():
    """Render the 'How it works' box in the sidebar."""
    st.markdown(
        """
        <div class="how-it-works">
            <b>How it works</b><br>
            1. Paste up to 5 article URLs<br>
            2. Click <em>Process URLs</em> to index them<br>
            3. Ask any question below<br>
            4. The AI only uses your articles to answer
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_step_badge(number, text):
    """Render a step badge with text."""
    st.markdown(
        f'<div style="color:rgba(200,200,220,0.9); font-weight:600; font-size:1.1rem; margin-bottom:12px;">'
        f'<span class="step-badge">{number}</span> {text}</div>',
        unsafe_allow_html=True,
    )

def render_footer_card():
    """Render the initial state rocket card."""
    st.markdown(
        """
        <div class="card" style="text-align:center; padding: 48px 24px;">
            <div style="font-size: 3rem; margin-bottom: 16px;">🚀</div>
            <div style="color: rgba(200,200,220,0.9); font-size: 1.1rem; font-weight: 500; margin-bottom: 8px;">
                Get started in 3 simple steps
            </div>
            <div style="color: rgba(160,160,180,0.7); font-size: 0.9rem; line-height: 1.8;">
                1. Paste article URLs in the sidebar<br>
                2. Click <strong>Process URLs</strong> to build the vector knowledge base<br>
                3. Ask any question — the AI will answer using only your articles
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

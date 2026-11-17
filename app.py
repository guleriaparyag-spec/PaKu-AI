import os
from urllib.parse import quote
import requests
import streamlit as st
from google import genai
from google.genai import types

from knowledge_base import MANUAL, ORIGINAL_ASSISTANT_GUIDELINES

# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="PaKuai – LLM Expert Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# API Key & Model Configuration (from .streamlit/secrets.toml or Env/Sidebar)
# ---------------------------------------------------------------------------
def get_configured_api_key() -> str:
    """Retrieve GEMINI_API_KEY from st.secrets or environment variables."""
    try:
        secret_key = st.secrets.get("GEMINI_API_KEY", "").strip()
        if secret_key and secret_key != "YOUR_GEMINI_API_KEY_HERE":
            return secret_key
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY", "").strip()


def get_configured_model() -> str:
    """Retrieve GEMINI_MODEL from st.secrets or environment variables."""
    try:
        secret_model = st.secrets.get("GEMINI_MODEL", "").strip()
        if secret_model:
            return secret_model
    except Exception:
        pass
    return os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite").strip()


# ---------------------------------------------------------------------------
# Wikipedia Search Helper
# ---------------------------------------------------------------------------
def search_wikipedia(query: str, limit: int = 3) -> list[dict]:
    """Search Wikipedia for background context and return titles, snippets, and URLs."""
    try:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": limit,
        }
        headers = {"User-Agent": "PaKuaiAssistant/1.0 (Streamlit Educational App)"}
        response = requests.get(url, params=params, headers=headers, timeout=6)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("query", {}).get("search", []):
            title = item.get("title", "")
            # Clean basic HTML tags from snippet
            snippet = (
                item.get("snippet", "")
                .replace('<span class="searchmatch">', "")
                .replace("</span>", "")
            )
            page_url = f"https://en.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}"
            results.append({"title": title, "snippet": snippet, "url": page_url})
        return results
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "custom_api_key" not in st.session_state:
    st.session_state.custom_api_key = ""


# ---------------------------------------------------------------------------
# Sidebar Controls & Configuration
# ---------------------------------------------------------------------------
with st.sidebar:
    st.title("🤖 PaKuai")
    st.caption("LLM Expert Assistant & Technical Mentor")

    st.divider()

    # API Key Status / Override
    configured_key = get_configured_api_key()
    active_api_key = configured_key or st.session_state.custom_api_key

    if configured_key:
        st.success("✅ API Key loaded from `.streamlit/secrets.toml`")
    else:
        st.warning("⚠️ No valid key found in `.streamlit/secrets.toml`")
        manual_key = st.text_input(
            "Enter Gemini API Key:",
            type="password",
            value=st.session_state.custom_api_key,
            help="Get a free API key from https://aistudio.google.com/apikey",
        )
        if manual_key:
            st.session_state.custom_api_key = manual_key.strip()
            active_api_key = st.session_state.custom_api_key

    # Model & Feature Settings
    default_model = get_configured_model()
    model_options = ["gemini-3.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro"]
    if default_model not in model_options:
        model_options.insert(0, default_model)

    selected_model = st.selectbox("Gemini Model", options=model_options, index=0)
    use_wikipedia = st.toggle("🔍 Search Wikipedia for context", value=True)
    temperature = st.slider("Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.4, step=0.1)

    st.divider()

    # Action Buttons (replaces /clear and /help CLI commands)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    with col2:
        show_help = st.button("❓ Help", use_container_width=True)

    if show_help:
        st.info(
            "**Commands & Tips:**\n"
            "- Ask any question about AI, LLMs, RAG, Fine-tuning, or general topics.\n"
            "- Supports **English, Hindi, and Hinglish**.\n"
            "- Type `/clear` in chat or click **Clear Chat** to reset conversation history.\n"
            "- Toggle **Wikipedia Search** to attach live background sources."
        )

    with st.expander("📚 Knowledge Base Topics (35 Sections)"):
        st.markdown(
            """
            1. Intro to AI & Generative AI
            2. Large Language Models & Transformers
            3. Tokens, Parameters & Context Windows
            4. Pretraining, SFT & Alignment (RLHF/DPO)
            5. Prompt Engineering & APIs (Gemini, Groq)
            6. RAG, Embeddings & Vector Databases
            7. Fine-Tuning (LoRA / QLoRA)
            8. AI Agents, Tool Calling & Multimodal AI
            9. Hallucinations, Quantization & Evaluation
            10. Learning Roadmap & Official Resources
            """
        )


# ---------------------------------------------------------------------------
# Main Chat Interface
# ---------------------------------------------------------------------------
st.header("PaKuai – LLM Expert Assistant")
st.markdown(
    "Ask me anything about **Large Language Models, AI architecture, Prompt Engineering, RAG, Python code**, or general topics!"
)

# Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("🌐 Wikipedia Sources"):
                for src in msg["sources"]:
                    st.markdown(f"- [{src['title']}]({src['url']}) — *{src['snippet']}...*")

# Chat input box
if prompt := st.chat_input("Ask a question (or type /clear)..."):
    # Handle CLI-style /clear command gracefully
    if prompt.strip().lower() == "/clear":
        st.session_state.messages = []
        st.rerun()

    if not active_api_key:
        st.error(
            "Missing Gemini API Key! Please add `GEMINI_API_KEY` to `.streamlit/secrets.toml` or enter it in the sidebar."
        )
        st.stop()

    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        wiki_results = []
        if use_wikipedia:
            with st.spinner("Searching Wikipedia for background context..."):
                wiki_results = search_wikipedia(prompt)

        # Build system instruction combining guidelines + 35-section knowledge base
        system_instruction = f"{ORIGINAL_ASSISTANT_GUIDELINES}\n\n{MANUAL}"

        # Build conversation history for Gemini
        contents = []
        # Include prior turns (excluding the latest user prompt just appended)
        for past_msg in st.session_state.messages[:-1]:
            role = "user" if past_msg["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=past_msg["content"])],
                )
            )

        # Augment current user prompt with Wikipedia snippets if found
        enriched_prompt = prompt
        if wiki_results:
            wiki_context = "\n".join(
                [f"- {r['title']}: {r['snippet']} ({r['url']})" for r in wiki_results]
            )
            enriched_prompt = (
                f"User Question: {prompt}\n\n"
                f"Relevant Wikipedia Background Information:\n{wiki_context}"
            )

        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=enriched_prompt)],
            )
        )

        try:
            client = genai.Client(api_key=active_api_key)
            with st.spinner("Thinking..."):
                response = client.models.generate_content(
                    model=selected_model,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=temperature,
                    ),
                )
                reply_text = response.text or "I could not generate a response. Please try again."

            st.markdown(reply_text)

            if wiki_results:
                with st.expander("🌐 Wikipedia Sources"):
                    for src in wiki_results:
                        st.markdown(f"- [{src['title']}]({src['url']}) — *{src['snippet']}...*")

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": reply_text,
                    "sources": wiki_results,
                }
            )

        except Exception as err:
            st.error(f"Error communicating with Gemini API: {err}")

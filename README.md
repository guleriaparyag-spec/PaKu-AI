# PaKuai – LLM Expert Assistant (Streamlit Edition)

An interactive Streamlit web application converted from the single-file CLI **PaKuai** chatbot, preserving the complete 35-section LLM Knowledge Base, conversation memory, and live Wikipedia context lookup.

## Project Structure

```text
pakuai_streamlit/
├── .streamlit/
│   └── secrets.toml      # API key & default model configuration
├── app.py                # Main Streamlit chat application
├── knowledge_base.py     # Complete 35-section LLM Manual & system guidelines
├── requirements.txt      # Python dependencies
├── .gitignore            # Prevents secrets.toml from being committed
└── README.md             # Setup and usage guide
```

## Setup & Installation

1. **Extract the ZIP archive** and navigate into the folder:
   ```bash
   cd pakuai_streamlit
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your Gemini API Key**:
   Open `.streamlit/secrets.toml` and replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual key from [Google AI Studio](https://aistudio.google.com/apikey):
   ```toml
   GEMINI_API_KEY = "AIzaSy..."
   GEMINI_MODEL = "gemini-3.5-flash-lite"
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

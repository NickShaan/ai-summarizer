import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
API_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")

# UI setup
st.set_page_config(page_title="Tiny AI Summarizer", layout="centered")
st.title("🧠 Tiny AI Text Summarizer")
st.write("Enter any long text or article below and get a concise summary (3 sentences by default).")

with st.form("summarize_form"):
    text = st.text_area("Input text", height=320)
    max_sentences = st.number_input("Max sentences", min_value=1, max_value=10, value=3)
    submitted = st.form_submit_button("Summarize")

if submitted:
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                resp = requests.post(
                    f"{API_URL}/summarize",
                    json={"text": text, "max_sentences": int(max_sentences)},
                    timeout=60,
                )
                if resp.status_code == 200:
                    data = resp.json()
                    st.success("Summary generated ✅")
                    st.write(data.get("summary", "No summary text found"))
                else:
                    st.error(f"Backend error: {resp.status_code}\n{resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")

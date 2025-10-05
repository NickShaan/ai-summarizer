# Tiny AI Summarizer

## 🧠 About Project
Tiny AI Summarizer is a lightweight AI-powered text summarization app built using:
- **Python 3.11**
- **FastAPI** for the backend
- **Streamlit** for the frontend
- **Google Gemini API** for text summarization

It shows how to build a simple, end-to-end AI app without any database or complex deployment. The app accepts long text, sends it to Gemini API, and returns a short 3-sentence summary.

---

## 🧪 Test Examples

**Example 1:**
```
Input:
Climate change is causing sea levels to rise and making extreme weather events like hurricanes and heatwaves more common. Scientists attribute the primary cause to rising greenhouse gas emissions from industry, transport, and deforestation. Many countries and organizations are investing in renewable energy, reforestation, and efficiency measures to limit warming.

Output:
Climate change leads to rising sea levels and frequent extreme weather. The main cause is increased greenhouse gas emissions from industry and deforestation. Efforts include renewable energy, reforestation, and efficiency measures to reduce warming.
```

**Example 2:**
```
Input: Python is a popular programming language often used for web and AI projects.
Output: Python is a widely used programming language for AI and web development.
```

---

## ⚙️ Tech Stack & Dependencies

| Library | Version | Purpose |
|----------|----------|----------|
| Python | 3.11 | Core language |
| FastAPI | 0.95.2 | Backend framework |
| Uvicorn | 0.22.0 | ASGI server |
| Pydantic | 1.10.11 | Data validation |
| Streamlit | 1.25.0 | Frontend web UI |
| Requests | 2.31.0 | API calls |
| Python-dotenv | 1.0.0 | Environment variable loader |
| Google-genai | 0.8.0 | Gemini API SDK |

---

## 📁 File Structure
```
tiny-ai-summarizer/
├─ backend.py
├─ streamlit_frontend.py
├─ requirements.txt
├─ .env.example
└─ README.md
```

---

## 🪜 Step-by-Step Setup

### POSIX (Linux / macOS)
```bash
cd tiny-ai-summarizer
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set GEMINI_API_KEY
```

### Windows PowerShell
```powershell
cd C:\path\to\tiny-ai-summarizer
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# Edit .env and set GEMINI_API_KEY
```

---

## 🚀 How to Run

### 1️⃣ Start Backend
```bash
uvicorn backend:app --reload --port 8000
```
Backend runs at: http://localhost:8000

### 2️⃣ Start Frontend
```bash
streamlit run streamlit_frontend.py
```
Frontend runs at: http://localhost:8501

---

## ⚙️ Environment Variables
```
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
BACKEND_URL=http://localhost:8000
```

---

## 📊 Logging
The backend prints detailed logs:
- .env loaded confirmation
- SDK import & client initialization
- Each incoming request info (text length, sentence count)
- Gemini API call start/finish
- Summary generation completion

---

## 🧰 Troubleshooting

| Issue | Fix |
|-------|-----|
| `RuntimeError: GEMINI_API_KEY not set` | Create `.env` with correct key |
| SDK import fails | Reinstall google-genai package |
| No summary output | Print raw response in backend for debugging |
| Streamlit not found | Activate `.venv` before running |

---

## 🏁 Summary
You now have a complete AI text summarizer with a FastAPI backend and Streamlit frontend running on one Python environment. It can be deployed to **Render**, **Hugging Face Spaces**, or **Streamlit Cloud** easily.

---

import os
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# --- Pretty print colors ---
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def log(msg, color=CYAN):
    print(f"{color}[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}{RESET}")

# Load environment
load_dotenv()
log(".env loaded successfully", GREEN)

# Import Gemini SDK
try:
    from google import genai
    log("Google GenAI SDK imported successfully", GREEN)
except Exception as e:
    log(f"Failed to import google.genai SDK: {e}", RED)
    genai = None

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing. Add it in .env")

if genai is None:
    raise RuntimeError("google-genai SDK not installed or importable")

# Initialize client
client = genai.Client(api_key=API_KEY)
log(f"Gemini client initialized | Model: {MODEL}", GREEN)

# FastAPI setup
app = FastAPI(title="Tiny AI Summarizer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True
)
log("FastAPI app initialized with CORS middleware", GREEN)

# Request / response schemas
class SummarizeRequest(BaseModel):
    text: str
    max_sentences: int = 3

class SummarizeResponse(BaseModel):
    summary: str

@app.get("/")
async def root():
    log("Root endpoint '/' called", CYAN)
    return {"status": "ok", "message": "Tiny AI Summarizer Backend Running"}

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(payload: SummarizeRequest):
    log("Received /summarize request", CYAN)
    if not payload.text.strip():
        log("No text provided", RED)
        raise HTTPException(status_code=400, detail="No text provided")

    prompt = (
        f"Summarize the following text in {payload.max_sentences} concise sentences. "
        "Keep the meaning intact and avoid adding new facts.\n\n"
        f"TEXT:\n{payload.text}"
    )
    log("Sending request to Gemini model...", YELLOW)
    try:
        response = client.models.generate_content(model=MODEL, contents=prompt)
        log("Gemini model responded successfully", GREEN)
    except Exception as e:
        log(f"Gemini API call failed: {e}", RED)
        raise HTTPException(status_code=500, detail=f"Gemini API error: {e}")

    # Extract text
    summary_text = getattr(response, "text", None) or getattr(response, "content", None)
    if not summary_text:
        summary_text = str(response)
        log("Response did not have .text/.content, using stringified response", YELLOW)

    log(f"Summary generated ({len(summary_text)} chars)", GREEN)
    return SummarizeResponse(summary=summary_text.strip())

# Run manually with:
# uvicorn backend:app --reload --port 8000

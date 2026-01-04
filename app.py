import os
from typing import List, Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

from prompts import build_system_prompt

# Load an environment variables from .env
load_dotenv("../constraint_engine/.env")

# Groq's OpenAI-compatible endpoint
GROQ_BASE_URL = "https://api.groq.com/openai/v1"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

if not GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY. Put it in your .env file.")

client = OpenAI(api_key=GROQ_API_KEY, base_url=GROQ_BASE_URL)

app = FastAPI(title="Constraint Chat")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ChatRequest(BaseModel):
    message: str
    audience: str
    length: str
    history: List[Dict[str, str]] = []


class ChatResponse(BaseModel):
    answer: str
    history: List[Dict[str, str]]


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    # Basic guard
    user_text = (req.message or "").strip()
    if not user_text:
        return ChatResponse(answer="Please type a message.", history=req.history or [])

    system_prompt = build_system_prompt(req.audience, req.length)
    
    # keeping only last 20 messages so prompts don't grow forever
    history = (req.history or [])[-20:]

    # Message which we are sending to the model
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_text})

    # Calling out model
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=0.7,
    )

    answer = (completion.choices[0].message.content or "").strip()

    # Save updated history 
    new_history = history + [
        {"role": "user", "content": user_text},
        {"role": "assistant", "content": answer},
    ]
    new_history = new_history[-20:]

    return ChatResponse(answer=answer, history=new_history)

# ContextLens

ContextLens is a lightweight web-based chatbot that answers any question while letting users
control how the answer is framed. By selecting the target audience and response depth, the
same AI output can be viewed through different contextual lenses.

The motivation behind this project was to build a single chatbot that works equally well for
beginners, engineers, and experts, without changing the underlying model.

---

## Features
- Ask any question
- Control **Audience**: Beginner / Intermediate / Expert
- Control **Answer Depth**: Quick / Balanced / Natural
- Small visual easter eggs for celebratory phrases (e.g., “happy new year”, “today is my birthday”)

---

## Tech Stack
- FastAPI (backend)
- Single-page HTML / CSS / JavaScript (frontend)
- Open LLM via Groq API

---

## Setup

Install dependencies:

pip install -r requirements.txt



## Create .env file in the project root with the following values:

GROQ_API_KEY=api_key_you_created
GROQ_MODEL=llama-3.1-8b-instant

- You can use config.env_example as a reference.



## How to run it?

uvicorn app:app --reload



## Where to see your CHATBOT?

After running the app locally, open your browser it will be available at http://127.0.0.1:8000 (If port 8000 is already in use, uvicorn will print the active port in the terminal.)



## Notes

- This application runs locally and is not deployed.

- No data is stored; conversation history is kept only for the current session.

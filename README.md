# ContextLens

ContextLens is a lightweight web-based chatbot that answers any question while letting users
control the audience and depth of the response, so the same AI output can be viewed through
different contextual lenses.


Includes small visual easter eggs (e.g., “happy new year”, “today is my birthday”).

The motivation was to build a chatbot that answers anything, but lets users control how the answer is framed, so the same model works equally well for beginners, engineers, and experts.


## Tech
- FastAPI backend
- Single-page HTML/CSS/JS frontend
- Open model via Groq API

## Setup

pip install -r requirements.txt


## Create .env file 
such as

GROQ_API_KEY=api_key_you_created
GROQ_MODEL=llama-3.1-8b-instant

## How to run it?

uvicorn app:app --reload

## Where to see your CHATBOT?

It will be available at http://127.0.0.1:8000
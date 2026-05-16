# Anime Recommendation Chatbot

A conversational anime recommendation system that understands natural language queries like "something dark like Death Note but shorter" and suggests what to watch next.

## Project Structure

This project was built in 3 stages:

- **Stage 1 (Done)** — Recommendation Engine using TF-IDF and Cosine Similarity on a 12,000+ anime dataset
- **Stage 2 (Done)** — Conversational Chatbot layer using Ollama (TinyLlama) and LangChain
- **Stage 3 (Done)** — Both stages merged into a single Streamlit chat interface

## File Structure

```
Anime_recommender_chatBot/
├── anime (1).csv                  # Kaggle dataset — 12,000+ anime entries
├── recommender.py                 # Stage 1: TF-IDF + cosine similarity engine
├── chatbot.py                     # Stage 2+3: TinyLlama + recommendation trigger logic
├── app.py                         # Streamlit chat UI
├── Anime-Recommendation-PIP.ipynb # Original exploration notebook
├── requirements.txt               # Python dependencies
└── README.md
```

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (TF-IDF, Cosine Similarity)
- LangChain
- Ollama (TinyLlama)
- Streamlit

## Dataset

Kaggle Anime Dataset — 12,000+ anime entries with genres, ratings, episode counts, and metadata.

## How It Works

1. User describes what they want to watch in plain English
2. If a recommendation trigger word is detected ("recommend", "suggest", "something like", etc.), TinyLlama extracts 2-5 genre/intent keywords from the message
3. The recommendation engine finds the top 5 matching anime using cosine similarity on TF-IDF genre vectors
4. Results are formatted directly in Python and returned — no LLM involved in the final output (prevents hallucination)
5. For casual conversation (no trigger word), TinyLlama responds normally

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/SurendraPrasadSH/AnimeRecommendation.git
cd AnimeRecommendation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and start Ollama

Download Ollama from https://ollama.com and run:

```bash
ollama pull tinyllama
ollama serve
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at http://localhost:8501

## Example Queries

- `"recommend something dark and psychological"`
- `"something like Attack on Titan but shorter"`
- `"show me a good romance anime"`
- `"I want a funny slice of life"`

## Status

✅ All 3 stages complete and working.

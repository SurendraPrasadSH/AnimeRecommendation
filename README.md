# Anime Recommendation Chatbot

A conversational anime recommendation system that understands natural language queries like "something dark like Death Note but shorter" and suggests what to watch next.

## Project Structure

This project is being built in 3 stages:

- **Stage 1 (Done)** — Recommendation Engine using TF-IDF and Cosine Similarity on a 12,000+ anime dataset
- **Stage 2 (In Progress)** — Conversational Chatbot layer using Ollama (LLaMA 3) and LangChain
- **Stage 3 (Planned)** — Merging both stages into a single chat interface

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (TF-IDF, Cosine Similarity)
- LangChain
- Ollama (LLaMA 3)
- Streamlit

## Dataset

Kaggle Anime Dataset — 12,000+ anime entries with genres, ratings, and metadata.

## How It Works

1. User describes what they want to watch in plain English
2. The chatbot understands the intent and extracts genre/mood preferences
3. The recommendation engine finds the top 5 matching anime using cosine similarity on TF-IDF genre vectors
4. The chatbot responds naturally with recommendations and reasoning

## Setup

```bash
git clone https://github.com/SurendraPrasadSH/AnimeRecommendation.git
cd AnimeRecommendation
pip install -r requirements.txt
jupyter notebook
```

## Status

Actively in development. Stage 1 complete.

import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from recommender import get_recommendations

EXTRACTOR_PROMPT = SystemMessage(content="""
You are an anime intent extractor.
Given a user message, extract the core anime/genre search query in 2-5 keywords.
Return ONLY the keywords — no explanation, no punctuation, no extra text.

Examples:
User: "something dark and psychological like Death Note but shorter"
Output: death note psychological short

User: "I want a funny slice of life"
Output: comedy slice of life

User: "action anime with supernatural powers"
Output: action supernatural
""")

CHAT_PROMPT = SystemMessage(content="""
You are a friendly anime recommendation assistant.
Understand what kind of anime the user is in the mood for.
Ask follow-up questions if the request is vague.
Keep responses short and conversational.
Do not make up anime titles.
""")

TRIGGER_WORDS = [
    "recommend", "suggest", "watch", "show me", "looking for",
    "something like", "similar to", "what should", "find me",
    "mood for", "in the mood", "want to watch", "give me"
]

def get_llm():
    ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    return ChatOllama(model="tinyllama", temperature=0.7)

def _wants_recommendation(text: str) -> bool:
    text_lower = text.lower()
    return any(trigger in text_lower for trigger in TRIGGER_WORDS)

def chat(llm, history: list, user_input: str):
    history.append(HumanMessage(content=user_input))

    if _wants_recommendation(user_input):
        # Step 1: TinyLlama extracts genre/intent keywords
        extract_response = llm.invoke([EXTRACTOR_PROMPT, HumanMessage(content=user_input)])
        query = extract_response.content.strip()

        # Step 2: get real results from the recommendation engine
        results = get_recommendations(query)

        # Step 3: format directly in Python — no LLM, no hallucination
        if results:
            rec_lines = "\n".join([
                f"**{i+1}. {r['name'].title()}** — {r['genre']} | ⭐ {r['rating']} | {r['type']}"
                for i, r in enumerate(results)
            ])
            response_text = f"Here are your top picks:\n\n{rec_lines}"
        else:
            response_text = "Hmm, I couldn't find a match. Could you describe the genre or mood differently?"

        history.append(AIMessage(content=response_text))
        return response_text, history

    else:
        # Normal conversation
        response = llm.invoke([CHAT_PROMPT] + history)
        history.append(AIMessage(content=response.content))
        return response.content, history
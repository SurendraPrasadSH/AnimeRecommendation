from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

SYSTEM_PROMPT = SystemMessage(content="""
You are a friendly anime recommendation assistant.
Your job is to understand what kind of anime the user is in the mood for.
Ask follow-up questions if their request is vague.
Keep your responses short and conversational.
Do not make up titles — just have a natural conversation for now.
""")

def get_llm():
    return ChatOllama(model="tinyllama", temperature=0.7)
    
def chat(llm, history: list, user_input: str):
    history.append(HumanMessage(content=user_input))
    response = llm.invoke([SYSTEM_PROMPT] + history)
    history.append(AIMessage(content=response.content))
    return response.content, history
import streamlit as st
from chatbot import get_llm, chat

st.set_page_config(page_title="Anime Chatbot", page_icon="🎌")
st.title("Anime Recommendation Chatbot")
st.caption("Tell me what you are in the mood for")

if "history" not in st.session_state:
    st.session_state.history = []

if "llm" not in st.session_state:
    st.session_state.llm = get_llm()

for msg in st.session_state.history:
    role = "assistant" if msg.__class__.__name__ == "AIMessage" else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

if prompt := st.chat_input("e.g. What's up G!"):
    with st.chat_message("user"):
        st.markdown(prompt)

    response, st.session_state.history = chat(
        st.session_state.llm,
        st.session_state.history,
        prompt
    )

    with st.chat_message("assistant"):
        st.markdown(response)
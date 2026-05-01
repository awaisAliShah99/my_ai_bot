import streamlit as st
from groq import Groq

st.title("Welcome to AWAIS ai bot 🤖")

# API Key setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Sawal pochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})

import streamlit as st
from langchain_groq import ChatGroq

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chatbot")
st.write("Your Premium AI Assistant powered by Groq")

# Initialize model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key="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",
    temperature=0.6,
    max_tokens=500
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # AI response
    response = llm.invoke(user_input)

    # Show AI message
    st.chat_message("assistant").write(response.content)

    # Save AI response
    st.session_state.messages.append({"role": "assistant", "content": response.content})
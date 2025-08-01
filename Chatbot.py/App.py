import streamlit as st
from prompt_templates import build_prompt
from llm_interface import ask_llm

st.title("🤖 QuantalAI Knowledge Assistant (Demo)")

user_input = st.text_input("Ask a question about QuantalAI")

if user_input:
    with open("context/quantal_site.txt", "r") as file:
        context = file.read()
    
    prompt = build_prompt(user_input, context)
    response = ask_llm(prompt)
    
    st.markdown("### 🧠 Answer:")
    st.write(response)

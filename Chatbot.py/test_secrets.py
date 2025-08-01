import streamlit as st

st.title("🔐 Testing secrets.toml")

# Correct way to access the secret
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.write("Your OpenAI API Key is:")
st.write(openai_api_key)

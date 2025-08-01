import requests
import streamlit as st

def ask_llm(prompt):
    api_key = st.secrets["TOGETHER_API_KEY"]
    url = "https://api.together.xyz/v1/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # or try 'meta-llama/Llama-2-70b-chat-hf'
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()




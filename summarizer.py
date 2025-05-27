from openai import OpenAI
import os
import streamlit as st


api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def summarize_content(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes text into key points and action items."},
            {"role": "user", "content": f"Summarize this content:\n\n{content}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

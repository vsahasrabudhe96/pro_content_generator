from openai import OpenAI
import os
import streamlit as st


api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
# client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY")))

def generate_technical_doc(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a technical writer who creates professional documentation."},
            {"role": "user", "content": f"Generate technical documentation from the following:\n\n{content}"}
        ],
        temperature=0.6
    )
    return response.choices[0].message.content

import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import streamlit as st

client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY"))

def fetch_web_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.stripped_strings
        visible_text = " ".join(texts)
        return visible_text[:5000]  # Limit to 5K characters to stay in token budget
    except Exception as e:
        return f"Error fetching URL: {e}"

def summarize_website(url):
    page_text = fetch_web_text(url)
    if page_text.startswith("Error"):
        return page_text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You summarize webpages into concise key points."},
            {"role": "user", "content": f"Summarize the content of this webpage:\n\n{page_text}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

# -*- coding: utf-8 -*-
"""Untitled62.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1masv9CaIHOnj5HujcujsWVEw2Vu2Ns_Z
"""

import streamlit as st
from gtts import gTTS
import tempfile
import re

# Streamlit app title
st.title("A Simple Hello World voice chatbot")

# Function to convert text to speech and save it to a temporary file
def text_to_speech(text):
    tts = gTTS(text)
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio_file.name)
    return temp_audio_file.name

# Function to handle user inputs and generate responses
def voice_bot(question):
    greetings = {
        r"hello": "Hello there!",
        r"how are you": "I'm doing well. How can I assist you?",
        r"what's your name": "I'm just a simple demo bot. You can call me VoiceBot!",
        r"good morning": "Good morning! How can I help you today?",
        r"good afternoon": "Good afternoon! What can I assist you with?",
        r"good evening": "Good evening! How may I assist you?",
        r"bye": "Goodbye! If you have more questions in the future, feel free to ask."
    }

    # Convert the question to lowercase for case-insensitive matching
    question = question.lower()

    for pattern, response in greetings.items():
        if re.search(pattern, question):
            return response

    return "I'm sorry, I don't understand that question."

# Text input for user's question
user_question = st.text_input("Ask me a question:")

# Respond to the user's question
if st.button("Ask"):
    response = voice_bot(user_question)
    # Generate and play the voice response directly
    audio_file_path = text_to_speech(response)
    audio = open(audio_file_path, 'rb').read()
    st.audio(audio, format="audio/mp3")

# Instructions
st.write("Ask a question, and the response will get generated.")

# Optional: Display the user's question
st.write("Your question:")
st.write(user_question)

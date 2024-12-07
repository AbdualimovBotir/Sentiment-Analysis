import streamlit as st
import requests

# Streamlit foydalanuvchidan matn olish
st.title('Sentiment Analysis')

text_input = st.text_area('Enter text to analyze sentiment')

if st.button('Analyze Sentiment'):
    if text_input:
        # Flask ilovasiga so'rov yuborish
        response = requests.post("http://127.0.0.1:5000/predict", json={'text': text_input})
        
        if response.status_code == 200:
            data = response.json()
            sentiment = data.get('sentiment')
            st.write(f"Sentiment: {sentiment}")
        else:
            st.write("Error in prediction.")
    else:
        st.write("Please enter some text.")

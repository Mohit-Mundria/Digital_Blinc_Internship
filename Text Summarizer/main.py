import requests
import streamlit as st





def get_response():
    
    response = requests.post(
         'http://localhost:11434/api/generate',
         json={
            'model': 'llama3.2:latest',
            'prompt': f"You are a Text Summarization tool. Make a summary of {User_input} in minimum 50 words and maximum 200 word.",
            'stream': False
        }
    )
    return response.json()['response']


st.set_page_config(page_title="Turn long reads into lightning-fast insights — your smart text shrinker is here!", page_icon="📝⚡",layout="centered",initial_sidebar_state='collapsed')
st.header('Text Summarisation Tool')

User_input=st.text_input("Enter your text here: ",height=200)
submit=st.button("Summary")

if submit and User_input.strip():
    with st.spinner("Processing..."):
        st.write(get_response())
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as sia 
def score(text):
    score=sia.polarity_scores(text)
    st.write(score) 
    st.title("***Sentiment Scores!!***")
    st.write(f" Your text {text}is Positive!! ")
    st.write(f"Your text {text}is  Negative!!")
    st.write(f"Your text{text} is  Neutral!!")
    st.write(f"Your text {text} is Compound!!")
    
score("good day")

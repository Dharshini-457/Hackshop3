import streamlit as st
import nltk 
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer= SentimentIntensityAnalyzer()
text=st.text_input("Enter a text to analysis...")
st.write(text)

sentiment_scores = analyzer.polarity_scores(text)
st.write(sentiment_scores)





import streamlit as st
import nltk 
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.header("***WELCOME TO OUR PROJECT!!!***")
st.subheader("***FEELING FINDER***")
 # Determine the sentiment
def result(text):
    analyzer= SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05: 
        st.write( "Positive" )
        st.balloons()
    elif sentiment_scores['compound'] <= -0.05:
        st.write( "Negative" )
        st.balloons()
   
        st.balloons()
text=st.text_input("Enter a text to analysis....")
if st.button("Apply"):
    result(text) 


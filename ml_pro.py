import streamlit as st
import nltk 
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.header("***WELCOME TO OUR PROJECT!!!***")
st.subheader("***FEELING FINDER***")
analyzer= SentimentIntensityAnalyzer()
text=st.text_input("Enter a text to analysis....")
text = word_tokenize(text)
text=str(text)
sentiment_scores = analyzer.polarity_scores(text) # Determine the sentiment
if st.button("Apply"):
    if sentiment_scores['compound'] >= 0.05: 
        st.write( "Positive" )
        st.balloons()
    elif sentiment_scores['compound'] <= -0.05:
        st.write( "Negative" )
        st.balloons()
    else: 
        st.write( "Neutral")
        st.balloons()
 


import streamlit as st
import nltk 
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer= SentimentIntensityAnalyzer()
text = word_tokenize("NLTK is a great library for text processing!")
text=(str(text))
print(text)
sentiment_scores = analyzer.polarity_scores(text)
print(sentiment_scores)




'''import 
st.title("Sentiment Anslyzer kit!!")
st.balloons()
st.subheader("***Here we test the Emotion of the text that you have entered get ready with me...*** ")
text= st.text_input("Enter the text....")
if st.button("Test the Text!!"): '''
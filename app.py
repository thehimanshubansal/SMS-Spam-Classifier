import streamlit as st
import nltk
from nltk.corpus import stopwords
import pickle
from nltk.stem.porter import PorterStemmer

model = pickle.load(open("esc-model.pkl","rb"))
tfidf = pickle.load(open("vectorizer.pkl","rb"))
ps = PorterStemmer()
stopword_list = stopwords.words('english')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    t = []
    for i in text:
        if i.isalnum() & (i not in stopword_list):
            t.append(ps.stem(i))

    return " ".join(t)

st.set_page_config(page_title="Spam Classifier",page_icon="🗑️",layout="centered")
st.title("📩Email / 💬SMS Spam Classifier Model")
st.info("This project is a text-based spam detection system designed to identify unwanted or malicious messages in SMS and email formats")

# Input the text
sms = st.text_area("Enter the message or text",placeholder="Try out some messages like: Congratulations! You've won a free vacation/gift card! To claim, reply with your full name, address, and date of birth")

if st.button("Predict"):

    # Transform it
    transformed_sms = transform_text(sms)

    # Vectorize it
    vectorized_sms = tfidf.transform([transformed_sms])

    # Prediction
    result = model.predict(vectorized_sms)

    # Display
    if result == 0:
        st.success("Not a spam ✔️")
    elif result == 1:
        st.warning("Spam 🗑️")
    else:
        st.error("Some error has occurred ❌")

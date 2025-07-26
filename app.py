import streamlit as st
import nltk
from nltk.corpus import stopwords
import pickle
from nltk.stem.porter import PorterStemmer
nltk.download("punkt_tab")
nltk.download("stopwords")

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

st.markdown("---")  # Adds a horizontal line

st.markdown("**Try some examples:**")
examples = [
    "I am free today, let's go out for a movie. What do you say?",
    "A [redacted] loan for £950 is approved for you if you receive this SMS. 1 min verification and cash in 1 hr at www.[redacted].co.uk to opt out reply stop.",
    "Did you see the match? It was insane.",
    "Accident compensation\nYou have still not claimed the compensation you are due for the accident you had. To start the process please reply YES. To opt out text STOP.",
    "I love you... Do you love me?",
    "Congratulations! You've won a free vacation/gift card! To claim, reply with your full name, address, and date of birth."
]

for item in examples:
    st.markdown(f"- {item}")

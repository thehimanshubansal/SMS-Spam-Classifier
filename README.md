# 📬 SMS/Email Spam Classifier

[![GitHub Repo](https://img.shields.io/badge/GitHub-SMS--SPAM--DETECTION-blue)](https://github.com/thehimanshubansal/SMS-Spam-Classifier)

A machine learning-powered text classification system designed to identify unwanted or malicious messages in SMS and email formats using **Multinomial Naïve Bayes** algorithm.

## 🎯 Overview

This project implements a robust spam detection system that analyzes message content and classifies it as either "Spam" or "Not Spam". After evaluating multiple classification algorithms, Multinomial Naïve Bayes was selected for its superior performance on textual data with discrete features.

## ✨ Key Features

- **Real-time Classification:** Instant spam detection for SMS and email messages
- **High Accuracy:** Achieves 97% accuracy with 1.0 precision on spam detection
- **User-friendly Interface:** Built with Streamlit for easy interaction
- **Efficient Processing:** Fast training and prediction times
- **Robust Preprocessing:** Comprehensive text cleaning and feature extraction pipeline

## 🔧 Technical Stack

- **Algorithm:** Multinomial Naïve Bayes
- **Frontend:** Streamlit
- **Text Processing:** NLTK (Natural Language Toolkit)
- **Feature Extraction:** TF-IDF Vectorization
- **Model Serialization:** Pickle

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 97% |
| Precision | 1.0 |
| Algorithm | Multinomial Naïve Bayes |

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd spam-classifier
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data:**
   ```python
   import nltk
   nltk.download('punkt_tab')
   nltk.download('stopwords')
   ```

### Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter a message** in the text area and click "Predict" to classify it

## 📁 Project Structure

```
spam-classifier/
│
├── app.py                 # Main Streamlit application
├── esc-model.pkl          # Trained Multinomial Naïve Bayes model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## 🔍 How It Works

### 1. Text Preprocessing Pipeline

The system processes input text through several stages:

- **Lowercasing:** Converts all text to lowercase
- **Tokenization:** Splits text into individual words using NLTK
- **Stopword Removal:** Removes common English stopwords
- **Stemming:** Reduces words to their root form using Porter Stemmer
- **Alphanumeric Filtering:** Keeps only alphanumeric tokens

### 2. Feature Extraction

- **TF-IDF Vectorization:** Converts preprocessed text into numerical features
- **Vocabulary Building:** Creates a feature space based on training data

### 3. Classification

- **Model Prediction:** Uses trained Multinomial Naïve Bayes classifier
- **Binary Output:** Returns 0 (Not Spam) or 1 (Spam)

## 🎨 User Interface

The Streamlit interface provides:

- **Clean Design:** Intuitive layout with emoji indicators
- **Text Input Area:** Large text field for message input
- **Sample Prompts:** Example spam messages for testing
- **Real-time Results:** Instant classification with visual feedback
- **Status Indicators:** 
  - ✔️ Green for "Not Spam"
  - 🗑️ Orange for "Spam"
  - ❌ Red for errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add some feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NLTK Team** for providing excellent text processing tools
- **Streamlit** for the user-friendly web framework
- **Scikit-learn** community for machine learning algorithms
- **Kaggle** used for dataset  ```spam.csv```


## 🔮 Future Enhancements

- [ ] Support for multiple languages
- [ ] Advanced deep learning models (LSTM, BERT)
- [ ] Real-time learning capabilities
- [ ] Enhanced visualization and analytics dashboard

---

**Made with ❤️ for spam-free communication**

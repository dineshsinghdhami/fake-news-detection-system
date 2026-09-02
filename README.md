# Fake News Detection System

![License](https://img.shields.io/badge/license-Proprietary-red)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)

**Fake News Detection System** is a bilingual machine learning web application built using **Python, Scikit-learn, TF-IDF, and Flask**.

It classifies news text as **REAL** or **FAKE** and supports both **English and Nepali (Devanagari)** input.

> This system uses NLP and Machine Learning to classify English and Nepali news text as REAL or FAKE based on learned text patterns. It is designed as a practical demonstration of fake news classification, not as a replacement for professional fact verification.

---

## Features

- English and Nepali news classification
- REAL / FAKE prediction
- TF-IDF character n-gram text processing
- Comparison of four ML models
- Model evaluation and confusion matrix
- Flask web interface
- Prediction dashboard
- Prediction history tracking

---

## Machine Learning Models

The project compares:

- Logistic Regression
- Multinomial Naive Bayes
- Linear SVM
- Random Forest

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The best-performing model is saved as:

```text
fake_news_model.pkl
```

---

## Machine Learning Workflow

```text
News Dataset
     ↓
Text Cleaning
     ↓
English + Nepali Processing
     ↓
TF-IDF Vectorization
     ↓
Train / Test Split
     ↓
Multiple ML Models
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Flask Web Application
```

---

## Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Joblib**
- **HTML / CSS / Jinja2**
- **Jupyter Notebook**

---

## Bilingual Support

The preprocessing pipeline preserves both English and Nepali characters.

Character-level TF-IDF is used:

```python
TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(3, 5),
    max_features=10000
)
```

This allows the system to process both English and Nepali text patterns.

---

## Flask Application

The application contains three pages:

```text
/              → News Checker
/dashboard     → Prediction Dashboard
/history       → Prediction History
```

The dashboard displays total predictions and REAL/FAKE prediction counts.

Prediction history stores:

- News text
- Prediction
- Date and time

---

## Project Structure

```text
fake-news-detection-system/
│
├── app.py
├── Fake_News_Detection.ipynb
├── fake_news_model.pkl
├── prediction_history.csv
├── fake_news_test_results.csv
│
├── screenshots/
│   ├── model_comparison.png
│   └── confusion_matrix.png
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── history.html
│
├── requirements.txt
├── README.md
└── LICENSE.md
```

---

## Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Example

### English

```text
Government announces a new scholarship program for engineering students.
```

Output:

```text
REAL NEWS
```

### Nepali

```text
सरकारले नयाँ शिक्षा नीति सार्वजनिक गरेको छ।
```

Output:

```text
REAL NEWS
```

Fake-style example:

```text
एउटा फल खाएपछि सबै रोग तुरुन्त निको हुन्छ।
```

Output:

```text
FAKE NEWS
```

---

## Limitations

- The training dataset is relatively small.
- Prediction quality depends on the training data.
- The system learns text patterns and does not independently verify facts.
- It is intended as an educational ML project.

---

## Future Improvements

- Larger English and Nepali datasets
- Source credibility checking
- Multilingual transformer models
- Cloud deployment

---

## Author

**Dinesh Singh Dhami**

- Website: https://dineshsinghdhami.com.np
- GitHub: https://github.com/dineshsinghdhami
- Email: dineshdhamidn@gmail.com

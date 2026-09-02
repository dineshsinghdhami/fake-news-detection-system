# Fake News Detection System

![License](https://img.shields.io/badge/license-Proprietary-red)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)

**Fake News Detection System** is a bilingual machine learning web application built using **Python**, **Scikit-learn**, **TF-IDF**, and **Flask**. It classifies news headlines or article text as **REAL** or **FAKE** and supports both **English and Nepali (Devanagari) text**.

The project includes text preprocessing, multiple machine learning model comparisons, prediction history, a Flask dashboard, and an interactive news-checking interface.

> **Note:** This project is developed for educational and internship demonstration purposes. It is **not a professional fact-checking service** and predictions should not be treated as verified factual judgments.

> **License Notice:** This project is **not open source**. All source code, designs, models, datasets prepared for the project, and other assets are proprietary and may not be copied, modified, or redistributed without permission.

---

## Features

- English and Nepali news text support
- REAL / FAKE news classification
- TF-IDF based NLP text processing
- Character n-gram support for bilingual classification
- Logistic Regression model
- Multinomial Naive Bayes model
- Linear SVM model
- Random Forest model
- Machine learning model comparison
- Accuracy evaluation
- Classification report
- Confusion matrix
- Automatic trained model selection
- Model persistence using Joblib
- Flask-based web interface
- Prediction history tracking
- Prediction dashboard
- REAL and FAKE prediction statistics
- Responsive user interface
- CSV-based prediction history storage

---

## Machine Learning Workflow

```text
News Dataset
     │
     ▼
Text Cleaning
     │
     ▼
English + Nepali Text Processing
     │
     ▼
TF-IDF Vectorization
(Character N-Grams)
     │
     ▼
Train / Test Split
     │
     ▼
┌─────────────────────────────┐
│ Machine Learning Models     │
├─────────────────────────────┤
│ Logistic Regression         │
│ Multinomial Naive Bayes     │
│ Linear SVM                  │
│ Random Forest               │
└─────────────────────────────┘
     │
     ▼
Model Evaluation
     │
     ▼
Best Model Selection
     │
     ▼
Saved ML Model
     │
     ▼
Flask Web Application
     │
     ├── News Checker
     ├── Dashboard
     └── Prediction History
```

---

## Tech Stack

- **Programming Language:** Python
- **Web Framework:** Flask
- **Machine Learning:** Scikit-learn
- **NLP:** TF-IDF Vectorization
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Model Storage:** Joblib
- **Frontend:** HTML, CSS, Jinja2
- **Prediction Storage:** CSV
- **Development Environment:** Jupyter Notebook, VS Code

---

## Machine Learning Models

The project compares four classification algorithms:

- **Logistic Regression**
- **Multinomial Naive Bayes**
- **Linear Support Vector Machine (Linear SVM)**
- **Random Forest Classifier**

The models are evaluated using metrics such as:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The best-performing model is selected and saved as:

```text
fake_news_model.pkl
```

---

## Bilingual Support

The system supports:

- English
- Nepali / Devanagari

Instead of removing Nepali characters during preprocessing, the text-cleaning pipeline preserves both English and Devanagari Unicode characters.

The project uses character-level TF-IDF features:

```python
TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(3, 5),
    max_features=10000
)
```

This allows the machine learning pipeline to process text patterns from both English and Nepali input.

---

## Flask Application

The Flask application contains three main pages:

```text
/              → Fake News Checker
/dashboard     → Prediction Dashboard
/history       → Prediction History
```

### News Checker

Users can enter a news headline or article and receive:

```text
REAL NEWS
```

or:

```text
FAKE NEWS
```

### Dashboard

The dashboard displays:

- Total predictions
- REAL news predictions
- FAKE news predictions
- Prediction summary

### Prediction History

Each prediction is stored with:

- News text
- Prediction result
- Prediction date and time

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
│   ├── confusion_matrix.png
│   └── ...
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

## Installation

Clone the repository:

```bash
git clone https://github.com/dineshsinghdhami/fake-news-detection-system.git
```

Move into the project directory:

```bash
cd fake-news-detection-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Example Prediction

### English Example

```text
Government announces a new scholarship program for engineering students.
```

Example output:

```text
REAL NEWS
```

### Nepali Example

```text
सरकारले नयाँ शिक्षा नीति सार्वजनिक गरेको छ।
```

Example output:

```text
REAL NEWS
```

Example fake-style Nepali input:

```text
एउटा फल खाएपछि सबै रोग तुरुन्त निको हुन्छ।
```

Example output:

```text
FAKE NEWS
```

---

## Model Evaluation

The project evaluates machine learning models using a held-out test dataset.

Generated evaluation outputs include:

```text
screenshots/model_comparison.png
screenshots/confusion_matrix.png
```

These visualizations are useful for comparing model performance and examining classification errors.

---

## Limitations

- The current dataset is relatively small compared with production-scale misinformation datasets.
- Prediction quality depends strongly on the quality and diversity of training data.
- The model identifies learned language patterns rather than independently verifying factual claims.
- Real-world misinformation detection requires source verification, external evidence, context analysis, and larger continuously updated datasets.
- The application should therefore be considered an educational machine learning system rather than a professional fact-checking platform.

---

## Future Improvements

Possible future enhancements include:

- Larger English and Nepali datasets
- Real news API integration
- Source credibility analysis
- URL-based article checking
- Transformer-based NLP models
- Multilingual BERT
- Confidence score visualization
- Database integration
- User authentication
- Admin dashboard
- REST API development
- Cloud deployment
- Automated fact-checking against trusted sources

---

## License

This project is **proprietary** and **all rights are reserved**.

You may **not**:

- Copy or redistribute the source code
- Modify or reuse any part of the project
- Publish or mirror the project
- Use the project or its assets for personal, academic, or commercial purposes without written permission
- Reverse engineer, decompile, or create derivative works
- Repackage the trained model or application as another project

Unauthorized copying, modification, distribution, or reuse of this project may constitute copyright infringement and may result in legal action.

See the [LICENSE](LICENSE.md) file for complete terms.

---

## Contributions

Public contributions are not accepted.

For collaboration or licensing inquiries, please contact the author.

---

## Author

**Dinesh Singh Dhami**

- Website: https://dineshsinghdhami.com.np
- GitHub: https://github.com/dineshsinghdhami
- Email: dineshdhamidn@gmail.com

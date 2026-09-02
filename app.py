import os
import re
from datetime import datetime

import joblib
import pandas as pd

from flask import (
    Flask,
    render_template,
    request
)


# =========================================================
# FLASK APP
# =========================================================
app = Flask(__name__)


# =========================================================
# LOAD TRAINED BILINGUAL MODEL
# =========================================================
model = joblib.load("fake_news_model.pkl")


# =========================================================
# TEXT CLEANING
# Supports:
# - English
# - Nepali / Devanagari
# =========================================================
def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(
        r"http\S+|www\S+",
        "",
        text
    )

    # Keep English + Nepali / Devanagari characters
    text = re.sub(
        r"[^a-zA-Z\u0900-\u097F\s]",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# =========================================================
# HOME / NEWS CHECKER
# =========================================================
@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    message = None
    news_text = ""

    if request.method == "POST":

        news_text = request.form.get(
            "news_text",
            ""
        )

        # ---------------------------------------------
        # EMPTY INPUT CHECK
        # ---------------------------------------------
        if not news_text.strip():

            message = (
                "Please enter a news headline or article."
            )

        else:

            # -----------------------------------------
            # CLEAN TEXT
            # -----------------------------------------
            cleaned_news = clean_text(
                news_text
            )

            # -----------------------------------------
            # INVALID TEXT CHECK
            # -----------------------------------------
            if not cleaned_news:

                message = (
                    "The entered text could not be processed. "
                    "Please enter valid English or Nepali news text."
                )

            else:

                # -------------------------------------
                # PREDICT
                # -------------------------------------
                prediction = model.predict(
                    [cleaned_news]
                )[0]


                # =====================================
                # SAVE PREDICTION HISTORY
                # =====================================
                history_data = pd.DataFrame({
                    "News": [
                        news_text
                    ],

                    "Prediction": [
                        prediction
                    ],

                    "PredictionTime": [
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    ]
                })

                history_file = (
                    "prediction_history.csv"
                )

                if os.path.exists(
                    history_file
                ):

                    history_data.to_csv(
                        history_file,
                        mode="a",
                        header=False,
                        index=False
                    )

                else:

                    history_data.to_csv(
                        history_file,
                        index=False
                    )


    return render_template(
        "index.html",
        prediction=prediction,
        message=message,
        news_text=news_text
    )


# =========================================================
# DASHBOARD PAGE
# =========================================================
@app.route("/dashboard")
def dashboard():

    history_file = (
        "prediction_history.csv"
    )

    total_predictions = 0
    real_count = 0
    fake_count = 0

    real_percentage = 0
    fake_percentage = 0


    # ---------------------------------------------
    # READ PREDICTION HISTORY
    # ---------------------------------------------
    if os.path.exists(
        history_file
    ):

        df = pd.read_csv(
            history_file
        )

        total_predictions = len(
            df
        )

        real_count = int(
            (
                df["Prediction"] == "REAL"
            ).sum()
        )

        fake_count = int(
            (
                df["Prediction"] == "FAKE"
            ).sum()
        )


        # -----------------------------------------
        # PERCENTAGES
        # -----------------------------------------
        if total_predictions > 0:

            real_percentage = round(
                (
                    real_count /
                    total_predictions
                ) * 100,
                2
            )

            fake_percentage = round(
                (
                    fake_count /
                    total_predictions
                ) * 100,
                2
            )


    return render_template(
        "dashboard.html",

        total_predictions=total_predictions,

        real_count=real_count,

        fake_count=fake_count,

        real_percentage=real_percentage,

        fake_percentage=fake_percentage
    )


# =========================================================
# HISTORY PAGE
# =========================================================
@app.route("/history")
def history():

    history_file = (
        "prediction_history.csv"
    )

    records = []


    if os.path.exists(
        history_file
    ):

        df = pd.read_csv(
            history_file
        )


        # Show newest predictions first
        df = df.iloc[
            ::-1
        ]


        records = df.to_dict(
            orient="records"
        )


    return render_template(
        "history.html",
        records=records
    )


# =========================================================
# RUN FLASK APPLICATION
# =========================================================
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
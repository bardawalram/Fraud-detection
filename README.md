# 💳 Fraud Detection System Using Machine Learning

A machine learning-based web application that detects fraudulent financial transactions in real-time using user input features. The model is trained and integrated into a Streamlit web interface for ease of use and deployment.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Model Details](#model-details)
- [Dataset](#dataset)
---

## 📖 Overview

Fraudulent transactions are a major challenge in the financial sector. This project aims to provide an intelligent system to flag suspicious or fraudulent transactions using machine learning techniques.

The web application takes user input for transaction details and predicts whether the transaction is fraudulent or not using a trained classification model.

---

## 🌟 Features

- 🚀 Real-time fraud detection
- 🧠 ML model integrated using `joblib`
- 🧾 Simple and intuitive web interface built using Streamlit
- 📊 Takes transaction features as input
- ✅ Predicts if a transaction is safe or fraudulent
- 📁 Includes model training and analysis notebook (`analysis_model.ipynb`)

---
##🛠️ Tech Stack
- Language: Python 3.8+
-Libraries: - pandas
            - scikit-learn
            - joblib
            - Streamlit
Model: Machine learning classification model (e.g., RandomForest, XGBoost – depending on training in notebook)

---
##🧠 Model Details
The machine learning model (fraud_detection_pipeline.pkl) was trained using features such as:

type – Type of transaction (PAYMENT, TRANSFER, CASH_OUT, DEPOSIT)

- amount – Amount of money transferred
- oldbalanceOrg – Sender's balance before transaction
- newbalanceOrig – Sender's balance after transaction
- oldbalanceDest – Receiver's balance before transaction
- newbalanceDest – Receiver's balance after transaction

--
## 📂 Dataset
The model was trained using the PaySim Fraud Detection Dataset from Kaggle.
Dataset Info:
Simulated mobile money transactions dataset
6 million+ transactions
Used for anomaly and fraud detection research

import streamlit as st  # type: ignore
import pandas as pd     # type: ignore
import joblib           # type: ignore

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

# App title and description
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and use the predict button")
st.divider()

# Input fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0, step=100.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0, step=100.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0, step=100.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0, step=100.0)

# Centered Predict button using layout columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_trigger = st.button("🚀 Predict", use_container_width=True)

# Prediction logic
if predict_trigger:
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("🚨 This transaction can be fraud")
    else:
        st.success("✅ This transaction looks like it is not a fraud")

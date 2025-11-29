import streamlit as st
import joblib
import pandas as pd

st.title("Price Prediction App")

# Load the pre-trained model
model = joblib.load("price_prediction_model.pkl")

# Define input features
st.header("Input Features")
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
if st.button("Predict Price"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'feature1': [feature1],
        'feature2': [feature2],
        'feature3': [feature3]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"The predicted price is: ${prediction[0]:.2f}")

import streamlit as st
import joblib
import pandas as pd

st.title("Price Prediction App")

# Load the pre-trained model
model = joblib.load("stock_price_model.pkl")

# Define input features
st.header("Please input Features")
Open_close = st.number_input("Feature 1", value=0.0)
Low_high = st.number_input("Feature 2", value=0.0)
Is_quarter_end3 = st.number_input("Feature 3", value=0.0)
if st.button("Predict Price"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'Open_close': [feature1],
        'Low_high': [feature2],
        'Is_quarter_end': [feature3]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"The predicted price is: ${prediction[0]:.2f}")

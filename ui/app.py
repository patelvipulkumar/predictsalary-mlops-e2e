import streamlit as st
import requests

# ⚠️ When running locally
API_URL = "http://localhost:8000/predict"

st.title("MLOps Salary predictor based on Years of Exp")

exp = st.number_input("YrsofExp") 

if st.button("Predict"):

    if exp.strip() == "":
        st.warning("Please enter some value")   

    else: 
        response = requests.post(API_URL, params={"exp": exp})

        if response.status_code == 200:
            result = response.json()

            Salary = result["Salary"]
        

            st.markdown(
                f"""
                ### 🧠 Prediction Result
                **Salary:** `{Salary}`
                """
            )
        else:
            st.error("Failed to get prediction from API")
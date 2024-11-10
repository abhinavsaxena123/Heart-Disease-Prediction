import streamlit as st
import pandas as pd
import time
import numpy as np
import pickle
#from xgboost import XGBClassifier
#from lightgbm import LGBMClassifier
#import lightgbm as lgb
#from sklearn.linear_model import LogisticRegression


# Loading Pre-Trained Pipeline (Model + Scalers)
with open(r'Saved_Models\best_lr_model_pipeline.pkl', 'rb') as model_file:
    lr_pipeline = pickle.load(model_file)

with open(r'Saved_Models\best_xgb_model_pipeline.pkl', 'rb') as model_file:
    xgb_pipeline = pickle.load(model_file)

with open(r'Saved_Models\best_lgbm_model_pipeline.pkl', 'rb') as model_file:
    lgbm_pipeline = pickle.load(model_file)


# Streamlit app
st.title("*** Predict the likelihood of heart disease ❤️")

# Model selection
model_choice = st.selectbox("Choose a model for prediction:", ["XGBoost", "LightGBM", "Logistic Regression"])

# User Input
age = st.number_input("Age (0-120)", min_value=0, max_value=120, help="Enter your age in years.")
sex = st.selectbox("Sex (0: Female, 1: Male)", [0, 1], help="Select your gender.")
cp = st.selectbox("Chest Pain Type (1-4)", [1, 2, 3, 4], help="Type of chest pain: 1 - Typical angina, 2 - Atypical angina, 3 - Non-anginal pain, 4 - Asymptomatic.")
bp = st.number_input("Blood Pressure (in mm Hg)", min_value=0, max_value=200, help="Enter Blood Pressure in mm Hg.")
chol = st.number_input("Serum Cholesterol (in mg/dl)", min_value=0, max_value=600, help="Enter serum Cholesterol in mg/dl.")
ecg = st.selectbox("Electrocardiographic Results (0-2)", [0, 1, 2], help="Select the results of Electrocardiography: 0 - Normal, 1 - Having ST-T wave abnormality, 2 - Showing probable or definite left ventricular hypertrophy.")
maxHR = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=220, help="Enter the Maximum Heart Rate achieved.")
exang = st.selectbox("Exercise Induced Angina (0: No, 1: Yes)", [0, 1], help="Did exercise induce angina?")
stdep = st.number_input("Oldpeak (depression induced by exercise relative to rest)", min_value=0.0, max_value=10.0, help="Enter the oldpeak value.")
slope = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", [0, 1, 2], help="Select the slope: 0 - Upsloping, 1 - Flat, 2 - Downsloping.")
vessels_fluro = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, help="Enter the number of major vessels (0-3) colored by fluoroscopy.")
thal = st.selectbox("Thallium Stress Test Results", [3, 6 ,7], help="Select thalassemia: 3 - Normal, 6 - Fixed defect, 7 - Reversible defect.")


# Predict button
if st.button("Predict"):
    # Validate input data
    if age < 0 or age > 110:
        st.error("Please enter a valid age between 0 and 110.")
    elif bp < 0 or bp > 200:
        st.error("Please enter a valid blood pressure between 0 and 200 mm Hg.")
    elif chol < 0 or chol > 600:
        st.error("Please enter a valid serum cholesterol level between 0 and 600 mg/dl.")
    elif maxHR < 0 or maxHR > 220:
        st.error("Please enter a valid maximum heart rate achieved.")
    elif stdep < 0.0 or stdep > 10.0:
        st.error("Please enter a valid oldpeak value.")
    else:
        # Prepare input data for the prediction
        input_data = pd.DataFrame([[age, sex, cp, bp, chol, ecg, maxHR, exang, stdep, slope, vessels_fluro, thal]],
                              columns=['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol', 'EKG results', 
                                       'Max HR', 'Exercise angina', 'ST depression', 'Slope of ST', 
                                       'Number of vessels fluro', 'Thallium'])
        
        #input_data = np.array([[Sex, CP, bp, chol, ecg, maxHR, exang, stdep, slope, vessels_fluro, thal]])

        # Choose model and make prediction
        if model_choice == "LightGBM":
            with st.spinner('Model is predicting...'):
                time.sleep(2)
                prediction = lgbm_pipeline.predict(input_data)
        elif model_choice == "XGBoost":
            with st.spinner('Model is predicting...'):
                time.sleep(2)
                prediction = xgb_pipeline.predict(input_data)
        else:
            with st.spinner('Model is predicting...'):
                time.sleep(2)
                prediction = lr_pipeline.predict(input_data)

        # Display result
        if prediction[0] == 1:
            st.image('Data\heart_disease.png', width=100)
            st.success("The model predicts that may have heart disease. Please consult a doctor")
        else:
            st.image("Data/no_heart_disease.png", width=100)
            st.success("The model predicts that you do not have heart disease.")



st.markdown("""
---
❤️ Heart Disease Prediction App ❤️
    Created by- Abhinav Saxena
""" )

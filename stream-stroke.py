import pickle
import numpy as np
import streamlit as st

# load save classifier
classifier = pickle.load(open('stroke.sav', 'rb'))

# Judul web
st.title ('Prediction of Stroke Disease')

col1, col2 =st.columns(2)
with col1:
    gender = st.text_input('Gender')
with col2:
    age = st.text_input('Age')
with col1:
    hypertension = st.text_input('Hypertension')
with col2:
    heart_disease = st.text_input('Heart Disease')
with col1:
    ever_married = st.text_input('Has the patient ever been married?')
with col2:
    work_type = st.text_input('Work Type of the Patient')
with col1:
    Residence_type = st.text_input('Residence type of the Patient')
with col2:
    avg_glucose_level = st.text_input('Average Glucose Level in Blood')
with col1:
    bmi = st.text_input('Body Mass Index')
with col2:
    smoking_status = st.text_input('Smoking Status of The Patient')

# code for prediction
stroke_diagnosis = ''

# membuat tombol prediksi
if st.button('Prediction Results'):
    stroke_prediction = classifier.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])

    if (stroke_prediction[0]==1):
        stroke_diagnosis = 'Patient Affected by Stroke Disease'
    else:
        stroke_diagnosis = 'Patient Not Affected by Stroke Disease'
    st.success(stroke_diagnosis)







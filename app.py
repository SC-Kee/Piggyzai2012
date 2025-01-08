# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WWBWyHVmJZT1CY0FIqequaBYXPFycL_6
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model (make sure the model file is in the same directory)
# model = joblib.load('model.pkl')

# Define the app layout
st.title('Diabetes Prediction')

st.write('Input Your Details')

# Create two columns
col1, col2 = st.columns(2)

# Create user input fields (modify these based on your model's features)
input1 = st.selectbox('Do you have high blood pressure?', ['No', 'Yes'])
input2 = st.selectbox('Do you have high cholesterol?', ['No', 'Yes'])
input3 = st.selectbox('Cholesterol check within past five years?', ['No', 'Yes'])
with col1:
    input19 = st.text_input('Age', '')
    input4 = st.text_input('Height (cm)', '')
    input20 = st.selectbox('Education', ['Never attended school or only kindergarten', 'Grades 1 through 8 (Elementary)','Grades 9 through 11 (Some high school)','Grade 12 or GED (High school graduate)',
                                         'College 1 year to 3 years (Some college or technical school)','College 4 years or more (College graduate)'])
with col2:
    input18 = st.selectbox('Gender', ['Male', 'Female'])
    input21 = st.text_input('Weight (kg)', '')
    input22 = st.selectbox('Income', ['Less than $10,000', '$10,000 to less than $15,000','$15,000 to less than $20,000','$20,000 to less than $25,000','$25,000 to less than $35,000',
                                      '$35,000 to less than $50,000','$50,000 to less than $75,000','$75,000 or more'])
    
input5 = st.selectbox('Have you smoked at least 100 cigarettes in your entire life?', ['No', 'Yes'])
input6 = st.selectbox('Do you have stroke', ['No', 'Yes'])
input7 = st.selectbox('Do you have coronary heart disease (CHD) or myocardial infarction (MI)', ['No', 'Yes'])
input8 = st.selectbox('Did you engage in physical activity or exercise during the past 30 days', ['No', 'Yes'])
input9 = st.selectbox('Do you consume fruit 1 or more times per day?', ['No', 'Yes'])
input10 = st.selectbox('Do you consume vegetables 1 or more times per day?', ['No', 'Yes'])
input11 = st.selectbox('Are you heavy drinkers?', ['No', 'Yes'])
input12 = st.selectbox('Do you have any kind of health care coverage?', ['No', 'Yes'])
input13 = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?', ['No', 'Yes'])
input14 = st.radio('Would you say that in general your health is', options=['Excellent','Very good','Good','Fair','Poor'])
input15 = st.slider('How many days during the past 30 days was your mental health not good?', min_value=0, max_value=30, value=15)
input16 = st.slider('How many days during the past 30 days was your physical health not good?', min_value=0, max_value=30, value=15)
input17 = st.selectbox('Do you have serious difficulty walking or climbing stairs?', ['No', 'Yes'])

if input4:
    # Try to convert input to integer
    try:
        Height = int(input4)/ 100
        # Check if height is within the range 90 to 250
        if not(0.90 <= Height <= 2.44):
            st.write('Please enter a value between 90 and 244 cm.')
    except ValueError:
        st.write('Please enter a valid number.')

if input21:
    # Try to convert input to integer
    try:
        Weight = int(input21)
        # Check if weight is within the range 23 to 295
        if not(23 <= Weight <= 295):
            st.write('Please enter a value between 23 and 295 kg.')
    except ValueError:
        st.write('Please enter a valid number.')

health_mapping = {
    'Excellent': 5,
    'Very good': 4,
    'Good': 3,
    'Fair': 2,
    'Poor': 1
}

income_mapping = {
    'Less than $10,000': 1,
    '$10,000 to less than $15,000': 2,
    '$15,000 to less than $20,000': 3,
    '$20,000 to less than $25,000': 4,
    '$25,000 to less than $35,000': 5,
    '$35,000 to less than $50,000': 6,
    '$50,000 to less than $75,000': 7,
    '$75,000 or more': 8
}
education_mapping = {
    'Never attended school or only kindergarten': 1,
    'Grades 1 through 8 (Elementary)': 2,
    'Grades 9 through 11 (Some high school)': 3,
    'Grade 12 or GED (High school graduate)': 4,
    'College 1 year to 3 years (Some college or technical school)': 5,
    'College 4 years or more (College graduate)': 6
}
Height = int(input4)/ 100
Weight = int(input21)

HighBP = 1 if input1 == 'Yes' else 0 
HighChol = 1 if input2 == 'Yes' else 0 
CholCheck = 1 if input3 == 'Yes' else 0 
BMI = Weight /(Height * Height)
Smoker = input5
Stroke = input6
HeartDiseaseorAttack = input7
PhysActivity = input8
Fruits = input9
Veggies = input10
HvyAlcoholConsump = input11
AnyHealthcare = input12
NoDocbcCost = input13
GenHlth = health_mapping.get(input14)
MentHlth = input15
PhysHlth = input16
DiffWalk = input17
Sex = input18
Age = input19
Education = education_mapping.get(input20)
Income = income_mapping.get(input22)

st.write(f'Your BMI is {BMI:.2f}')
st.write(f'Your BMI is {GenHlth:.2f}')
st.write(f'Your BMI is {MentHlth:.2f}')
st.write(f'Your BMI is {DiffWalk:.2f}')
st.write(f'Your BMI is {Education:.2f}')

# Combine inputs into a single array for prediction
inputs = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]])

# Button to trigger prediction
# if st.button('Predict'):
    # prediction = model.predict(inputs)  # Replace with your model's prediction method
    # st.write('Predicted Value:', prediction[0])

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

# Create user input fields (modify these based on your model's features)
input1 = st.selectbox('Do you have high blood pressure?', ['No', 'Yes'])
input2 = st.number_input('High Cholesterol', min_value=0.0, max_value=100.0, value=30.0)
input3 = st.number_input('Cholesterol Check', min_value=0.0, max_value=100.0, value=30.0)
input4 = st.text_input('Height (cm)', '')
input21 = st.text_input('Weight (kg)', '')
input5 = st.number_input('Smoker', min_value=0.0, max_value=100.0, value=30.0)
input6 = st.number_input('Stroke', min_value=0.0, max_value=100.0, value=30.0)
input7 = st.number_input('Heart Disease or Attack', min_value=0.0, max_value=100.0, value=30.0)
input8 = st.number_input('PhysActivity', min_value=0.0, max_value=100.0, value=30.0)
input9 = st.number_input('Fruits', min_value=0.0, max_value=100.0, value=30.0)
input10 = st.number_input('Veggies', min_value=0.0, max_value=100.0, value=30.0)
input11 = st.number_input('Heavy Alcohol Consumption', min_value=0.0, max_value=100.0, value=30.0)
input12 = st.number_input('Any Health care', min_value=0.0, max_value=100.0, value=30.0)
input13 = st.number_input('No Doctor because Cost', min_value=0.0, max_value=100.0, value=30.0)
input14 = st.number_input('General Health', min_value=0.0, max_value=100.0, value=30.0)
input15 = st.number_input('Mental Health', min_value=0.0, max_value=100.0, value=30.0)
input16 = st.number_input('Physical Health', min_value=0.0, max_value=100.0, value=30.0)
input17 = st.number_input('Diff Walk', min_value=0.0, max_value=100.0, value=30.0)
input18 = st.number_input('Gender', min_value=0.0, max_value=100.0, value=30.0)
input19 = st.number_input('Age', min_value=0.0, max_value=100.0, value=30.0)
input20 = st.number_input('Education', min_value=0.0, max_value=100.0, value=30.0)
input22 = st.number_input('Income', min_value=0.0, max_value=100.0, value=30.0)

if input4:
    # Try to convert input to integer
    try:
        Height = int(input4)/ 100
        # Check if height is within the range 90 to 250
        if 0.90 <= Height <= 2.44:
            st.write(f'Your height is {Height} m')
        else:
            st.write('Please enter a value between 90 and 244 cm.')
    except ValueError:
        st.write('Please enter a valid number.')

if input21:
    # Try to convert input to integer
    try:
        input21 = int(input21)
        # Check if height is within the range 23 to 295
        if 23 <= input21 <= 295:
            st.write(f'Your weight is {height} kg')
        else:
            st.write('Please enter a value between 23 and 295 kg.')
    except ValueError:
        st.write('Please enter a valid number.')
        

HighBP = 1 if input1 == 'Yes' else 0 
HighChol = input2
CholCheck = input3
BMI = input21 /(Height * Height)
Smoker = input5
Stroke = input6
HeartDiseaseorAttack = input7
PhysActivity = input8
Fruits = input9
Veggies = input10
HvyAlcoholConsump = input11
AnyHealthcare = input12
NoDocbcCost = input13
GenHlth = input14
MentHlth = input15
PhysHlth = input16
DiffWalk = input17
Sex = input18
Age = input19
Education = input20
Income = input22

st.write(f'Your BMI is {BMI:.2f}')

# Combine inputs into a single array for prediction
inputs = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]])

# Button to trigger prediction
# if st.button('Predict'):
    # prediction = model.predict(inputs)  # Replace with your model's prediction method
    # st.write('Predicted Value:', prediction[0])

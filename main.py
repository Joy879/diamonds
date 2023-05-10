import streamlit as st
import requests
import pandas as pd
from pycaret.regression import load_model, predict_model

st.title('Diamond App')


# Define predict function
#  defining a function called predict which will take the input and internally uses PyCaret’s predict_model function to generate predictions and return the value as a dictionary

def get_predictions(carat_weight, cut, color, clarity, polish, symmetry, report):
    url = 'https://diamonds-ktsy.onrender.com/predict?carat_weight={carat_weight}&cut={cut}&color={color}&clarity={clarity}&polish={polish}&symmetry={symmetry}&report={report}' \
        .format(carat_weight=carat_weight, cut=cut, \
                color=color, clarity=clarity, polish=polish, symmetry=symmetry, report=report)
    response = requests.post(url)
    json_response = response.json()
    price=json_response['prediction']
    return price


carat_weight = st.number_input("Enter carat weight ")
cut= st.text_input("cut")
color= st.text_input("color")
clarity= st.text_input("clarity")
polish= st.text_input("polish")
symmetry= st.text_input("symmetry")
report= st.text_input("report")





result = ""

# when 'Predict' is clicked, make the prediction and store it
if st.button("Predict"):
    result= get_predictions(carat_weight=carat_weight, cut=cut, color=color, clarity=clarity, polish=polish,symmetry=symmetry, report=report)
    st.success(f'Price of Diamond  {result}')


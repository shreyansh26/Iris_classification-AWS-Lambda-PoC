import requests
import streamlit as st
from src.train import Classifier
import math
import numpy as np

def predict_class_local(sepl, sepw, petl, petw):
    dt = list(map(float,[sepl, sepw, petl, petw]))

    req = {
        "data": [
            dt
        ]
    }

    cls = Classifier()
    return cls.load_and_test(req)

def predict_class_aws(sepl, sepw, petl, petw):
    API_URL = "https://ti53furxkb.execute-api.us-east-1.amazonaws.com/test/classify"

    dt = list(map(float,[sepl, sepw, petl, petw]))

    req = {
        "data": [
            dt
        ]
    }

    r = requests.post(API_URL, json=req)
    return r.json()

### Streamlit code (works as a straigtht-forward script) ###
st.title("Welcome to Iris Classifier")
st.header("Classify Iris type based on dimensions of the flower")

sepl = st.slider('Sepal Length (in cm)', 4.0, 8.0, 4.0)
sepw = st.slider('Sepal Width (in cm)', 2.0, 5.0, 2.0)
petl = st.slider('Petal Length (in cm)', 1.0, 7.0, 1.0)
petw = st.slider('Petal Width (in cm)', 0.1, 2.8, 0.1)

left, right = st.beta_columns(2)
with left:
    if st.button("Predict Local"):
        ret = predict_class_local(sepl, sepw, petl, petw)
        conf_list = np.array(ret['log_proba'][0])
        conf = math.exp(conf_list.max())*100

        st.write(f"Prediction: {ret['prediction'][0]}")
        st.write(f"Confidence: {conf:.2f}%")

with right:
    if st.button("Predict AWS"):
        ret = predict_class_aws(sepl, sepw, petl, petw)
        conf_list = np.array(ret['log_proba'][0])
        conf = math.exp(conf_list.max())*100

        st.write(f"Prediction: {ret['prediction'][0]}")
        st.write(f"Confidence: {conf:.2f}%")


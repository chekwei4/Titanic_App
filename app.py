import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
from sklearn.ensemble import RandomForestClassifier


def predict(X):
    pickle_in = open("rf_clf.pkl","rb")
    classifier = pickle.load(pickle_in)
    pred = classifier.predict(X)
    return pred

def main():
    st.title("Will you survive the Titanic Disaster?")
    selected_sex = st.selectbox("Select Sex", ("Male", "Female"))
    selected_sex_enc = None
    if selected_sex=="Male":
        selected_sex_enc = 0
    else:
        selected_sex_enc = 1

    selected_age = st.slider("Select Age", min_value=0, max_value=85, value=30)

    selected_sibsp = st.slider("# of siblings / spouses with you", min_value=0, max_value=6, value=2)

    selected_parch = st.slider("# of siblings / spouses with you", min_value=0, max_value=6, value=3)

    selected_fare = st.slider("Price of ticket", min_value=0, max_value=100, value=32)

    selected_class = st.radio("Select Class", ("First", "Second", "Third"))
    selected_class_enc = None
    if selected_class=="Third":
        selected_class_enc = 3
    elif selected_class=="Second":
        selected_class_enc = 2
    else:
        selected_class_enc = 1


    st.write(f"You are {selected_sex}")
    st.write(f"You are {selected_age} years old")
    st.write(f"You have {selected_sibsp} siblings / spouses with you")
    st.write(f"You have {selected_parch} parents / children with you")
    st.write(f"Price of ticket is ${selected_fare}")
    st.write(f"You are sitting in {selected_class} class")
    st.button("Predict")
    X = [[selected_class_enc, selected_sibsp, selected_parch, selected_fare, selected_sex_enc, selected_age]]
    pred = predict(X)
    if pred == 1:
        st.write("YOU SURVIVED!")
    else:
        st.write("YOU DEAD!")

    if st.button("About Me:"):
        st.text("Chekwei. Someone starting out...")
        st.text("Built with Streamlit...")

if __name__=='__main__':
    main()
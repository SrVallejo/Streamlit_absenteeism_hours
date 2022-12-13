import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

@st.experimental_memo
def read_dataset():
    return pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")

data_set = read_dataset()


data_set_prediction = data_set

#data_set_prediction -> 
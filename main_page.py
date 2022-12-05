import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

@st.experimental_memo
def read_dataset():
    return pd.read_csv("titanic.csv")

data_set = read_dataset()
data_set = data_set.drop(["PassengerId"], axis = 1)
import streamlit as st
import pandas as pd


@st.cache
def read_dataset():
    return pd.read_csv("titanic.csv")


columns_list = []


def create_filter_columns(Column_Name):
    if st.sidebar.checkbox(Column_Name, value = True):
        columns_list.append(Column_Name)
    else:
        try:
            columns_list.remove(Column_Name)
        except:
            pass


df_titanic = read_dataset()
df_titanic = df_titanic.drop(["PassengerId"], axis = 1)

st.sidebar.write("Show Columns")
for column in df_titanic.columns:
    create_filter_columns(column)


st.write(df_titanic[columns_list])

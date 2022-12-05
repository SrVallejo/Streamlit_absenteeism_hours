import streamlit as st
import pandas as pd
from main_page import data_set

columns_list = []


def create_filter_columns(Column_Name):
    if st.sidebar.checkbox(Column_Name, value = True):
        columns_list.append(Column_Name)
    else:
        try:
            columns_list.remove(Column_Name)
        except:
            pass


st.sidebar.write("Show Columns")
for column in data_set.columns:
    create_filter_columns(column)


st.write(data_set[columns_list])

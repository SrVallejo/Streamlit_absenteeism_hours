import streamlit as st
from main_page import data_set
import seaborn as sns
import matplotlib.pyplot as plt



# List of columns to show

columns_list = []

# Function that creates a checkbox in the sidebar to select the columns
#If true, it adds the *column_name* to *columns_list*, if not, remove that name
def create_filter_columns(column_name):
    #columns hided as default
    hided_columns = [
        "ID","Month of absence",
        "Transportation expense","Distance from Residence to Work","Service time",
        "Hit target", "Work load Average",
        "Weight","Height","Education",
        "Social drinker","Social smoker"
    ]

    #Las que quité en la predicción "ID","Service time","Month of absence","Weight","Height"

    default = column_name not in hided_columns
    if st.sidebar.checkbox(column_name, value = default):
        columns_list.append(column_name)
    else:
        try:
            columns_list.remove(column_name)
        except:
            pass


#Loop to create a checkbox for each column in the dataset
st.sidebar.write("Show Columns")
for column in data_set.columns:
    create_filter_columns(column)

fig, ax = plt.subplots()
sns.heatmap(data_set[columns_list].corr(), ax=ax, annot=True)
st.write(fig)
import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

@st.experimental_memo
def read_dataset():
    return pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")

@st.experimental_memo
def prepare_dataset_prediction():

    #Drop columns that lower our prediction accuracy
    columnsToDrop = ["ID","Service time","Month of absence","Weight","Height"]
    dataset_pred = data_set.drop(columns=columnsToDrop,axis=1)

    #Categorize columns

    #The target column (Absenteeism time in hours) to clasification
    #   short: x <=2
    #   medium: 2 < x <=8
    #   long: 8 < x

    group_hours = []
    for index, row in dataset_pred.iterrows():
        if row["Absenteeism time in hours"] <= 2: group_hours.append("short")
        elif row["Absenteeism time in hours"] <= 8: group_hours.append("medium")
        else: group_hours.append("long")

    dataset_pred["Group Hours"] = group_hours
    dataset_pred.head()

    #Education column group the values in:
    #   Where it was a 1 -> Highschool
    #   Where it was a 2, 3 or 4 -> University
    education_col = []
    for i,r in dataset_pred.iterrows():
        if r["Education"] == 1: education_col.append("High School")
        else: education_col.append("University")

    dataset_pred["Education"] = education_col

    #Distance column
    #   close: x < 20
    #   mid: 20 <= x < 40
    #   far: 40 <= x

    distance_col = []
    for i,r in dataset_pred.iterrows():
        if r["Distance from Residence to Work"] < 20: distance_col.append("close")
        elif r["Distance from Residence to Work"] < 40: distance_col.append("mid")
        else: distance_col.append("far")
        
    dataset_pred["Distance from Residence to Work"] = distance_col

    #Age column
    #   young: x < 35
    #   adult: 35 <= x < 45
    #   old: 45<= x

    age_col = []
    for i,r in dataset_pred.iterrows():
        if r["Age"] < 35: age_col.append("young")
        elif r["Age"] < 45: age_col.append("adult")
        else: age_col.append("old")

    dataset_pred["Age"] = age_col


    #Pet column
    #   no: x == 0
    #   few: x <= 2
    #   a lot: 2 < x

    pet_col = []
    for i,r in dataset_pred.iterrows():
        if r["Pet"] <= 0: pet_col.append("no")
        elif r["Pet"] <= 2: pet_col.append("few")
        else: pet_col.append("a lot")
        
    dataset_pred["Pet"] = pet_col


    #Dummies for categorical columns

    dummies_cols = ["Age","Seasons","Distance from Residence to Work","Education","Son","Pet"]
    dataset_pred = pd.get_dummies(dataset_pred,columns= dummies_cols,drop_first=True)
    
    return dataset_pred



data_set = read_dataset()

dataset_pred = prepare_dataset_prediction()

#data_set_prediction -> 
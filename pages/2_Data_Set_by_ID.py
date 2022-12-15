import streamlit as st
import pandas as pd
import numpy as np
from main_page import data_set

st.markdown("# Data Set by Employee ID")
st.sidebar.markdown("# Data Set by ID")

############################   Creation of a Data Set grouped by ID #########################

#Function to create the mode of *column* grouped by ID in the dataset *df*
#If draw, it takes the first value
def create_groupby_column(df,column):
    return df.groupby(df["ID"])[column].agg(lambda x: pd.Series.mode(x)[0]).values

#Create a dataset_id that will cointain the mode of all columns by ID 
# and the mean, sum, and frequency of Absenteeism Hours
dataset_id = data_set.groupby(data_set["ID"])["Reason for absence"].agg(lambda x: pd.Series.mode(x)[0]).to_frame()

#We take the dataset without *columnsToDrop*
# and create a new column with the mode of the rest of fields grouped by ID
columnsToDrop = ["ID","Reason for absence","Absenteeism time in hours","Disciplinary failure"]
for column in data_set.drop(columnsToDrop,axis = 1).columns:
    dataset_id[column] = create_groupby_column(data_set,column)

dataset_id["Absenteeism hours mean"] = data_set.groupby(data_set["ID"])["Absenteeism time in hours"].mean()
dataset_id["Absenteeism hours total"] = data_set.groupby(data_set["ID"])["Absenteeism time in hours"].sum()
dataset_id["Total absences"] = data_set["ID"].value_counts()


############################# Creating a checkbox filter by column ###########################



# List of columns to show
columns_list = []

# Function that creates a checkbox in the sidebar to select the columns
#If true, it adds the *column_name* to *columns_list*, if not, remove that name
def create_filter_columns(column_name):
    if st.checkbox(column_name, value = True):
        columns_list.append(column_name)
    else:
        try:
            columns_list.remove(column_name)
        except:
            pass





######################################## Row filters ##############################################
col1, col2, col3,col4 = st.columns(4)

with col1:
    options = dataset_id["Reason for absence"].unique().tolist()
    options.sort()
    options.insert(0,"No filter")
    sb_reasons = st.selectbox("Reason",options)

    ssl_smoker = st.select_slider("Social smoker",options= ["No", "No filter", "Yes"], value = "No filter")
    
with col2:
    sb_sons = st.selectbox("Sons",["No Filter","Yes","No"])

    ssl_drinker= st.select_slider("Social drinker",options= ["No", "No filter", "Yes"], value = "No filter")
    
with col3:
    min = int(dataset_id["Body mass index"].min())
    max = int(dataset_id["Body mass index"].max())
    sl_min_mass, sl_max_mass = st.slider("Body Mass Index",min,max, value = (min,max))
    
with col4:
    #Loop to create a checkbox for each column in the dataset
    st.write("Show Columns")
    for column in dataset_id.columns:
        create_filter_columns(column)


ds_show = dataset_id
if sb_sons == "Yes": ds_show = ds_show[ds_show["Son"] != 0]
elif sb_sons == "No": ds_show = ds_show[ds_show["Son"] == 0]
if sb_reasons != "No filter":
    ds_show = ds_show[ds_show["Reason for absence"]== int(sb_reasons)]
ds_show = ds_show[(ds_show["Body mass index"]>=sl_min_mass) & (ds_show["Body mass index"]<=sl_max_mass)]

if ssl_drinker == "Yes":ds_show = ds_show[ds_show["Social drinker"] == 1]
elif ssl_drinker == "No": ds_show = ds_show[ds_show["Social drinker"] == 0]



st.write(ds_show[columns_list])
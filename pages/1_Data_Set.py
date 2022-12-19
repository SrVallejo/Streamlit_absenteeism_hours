import streamlit as st
import pandas as pd
from main_page import data_set


st.markdown("# Full Data Set")
st.sidebar.markdown("# Full Data Set")
st.write("Each row represents one work absence")

######################################## Column filter ###############################

columns_list = []

def create_filter_columns(column):
    hided_columns = [
        "Transportation expense","Distance from Residence to Work","Service time",
        "Hit target", "Work load Average/day ","Pet",
        "Weight","Height","Education",
        "Social drinker","Social smoker","Son",
        "Body mass index","Age"
    ]
    default = column not in hided_columns
    if st.sidebar.checkbox(column, value = default):
        columns_list.append(column)
    else:
        try:
            columns_list.remove(column)
        except:
            pass


st.sidebar.write("Show Columns")
for column in data_set.columns:
    create_filter_columns(column)

########################################### Row filters #####################################

#Position to put the rows displayed text
marg_left, text = st.columns((2,1))
with text:
    total_cont = st.container()
col1, col2, col3 = st.columns((1,1.75,1))

with col1:
    #Days of the week filter
    days = ["No filter","Monday","Tuesday","Wednesday","Thursday","Friday"]
    sb_day = st.selectbox("Day of the week",days)

    #Season filter
    seasons = ["No filter","Spring","Summer","Autumn","Winter"]
    sb_season = st.selectbox("Season",seasons)
    

with col2:

    #Reason for absence filter
    options = data_set["Reason for absence"].unique().tolist()
    options.sort()
    options.insert(0,"No filter")
    sb_reasons = st.selectbox("Reason for absence",options)

    #Absenteeism hours filter
    min = int(data_set["Absenteeism time in hours"].min())
    max = int(data_set["Absenteeism time in hours"].max())
    sl_min_hour, sl_max_hour = st.slider("Absenteeism time in hours",min,max, value = (min,max))
    
 
with col3:
    
    #Disciplinary failure filter
    ssl_df = st.radio("Disciplinary Failure",options= ["No Filter", "No", "Yes"], index = 0)
    


############################################### Apply Filters ########################################
ds_show = data_set
#Filter hours
ds_show = ds_show[(ds_show["Absenteeism time in hours"]>=sl_min_hour) & (ds_show["Absenteeism time in hours"]<=sl_max_hour)]

#Filter reasons
if sb_reasons != "No filter":
    ds_show = ds_show[ds_show["Reason for absence"]== sb_reasons]

#Filter Disciplinary failure
if ssl_df == "Yes":
    ds_show = ds_show[ds_show["Disciplinary failure"]==1]
elif ssl_df == "No":
    ds_show = ds_show[ds_show["Disciplinary failure"]==0]

#Filter day

if sb_day != "No filter":
    ds_show = ds_show[ds_show["Day of the week"] == sb_day]

#Filter season
if sb_season != "No filter":
    ds_show = ds_show[ds_show["Seasons"]== sb_season]

#Show dataset
st.write(ds_show[columns_list])

total_cont.write("Total rows displayed: "+ str(len(ds_show)))
import streamlit as st
import numpy as np
import pandas as pd
import cufflinks

# @st.cache
#def get_data(url):
 #   df = pd.read_csv(url)
  
    #return df


sidebar = st.sidebar

analysis_choice = sidebar.radio("Analysis Type", ["Single", "Multiple"])
st.markdown(f"Analysis Mode: {analysis_choice}")

if analysis_type=="Single":
   
   

    trend_level = sidebar.selectbox("Trend Level", ["month_of_absence','day_of_the_week',
       'seasons'])
    st.markdown(f"### Currently Selected {trend_level}")

    show_data = sidebar.checkbox("Show Data")

    trend_kwds = {"Daily": "1D", "Weekly": "1W", "Monthly": "1M", "Quarterly": "1Q", "Yearly": "1Y"}
    trend_data = data.query(f"location=='{location_selector}'").\
        groupby(pd.Grouper(key="date",
        freq=trend_kwds[trend_level])).aggregate(new_cases=("new_cases", "sum"),
        new_deaths = ("new_deaths", "sum"),
        new_vaccinations = ("new_vaccinations", "sum"),
        new_tests = ("new_tests", "sum")).reset_index()

    trend_data["date"] = trend_data.date.dt.date
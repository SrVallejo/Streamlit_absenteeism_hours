import streamlit as st
import numpy as np
import pandas as pd
import cufflinks

# @st.cache
#def get_data(url):
 #   df = pd.read_csv(url)
  
    #return df


sidebar = st.sidebar


trend_level = sidebar.selectbox("Trend Level", ["month_of_absence','day_of_the_week',
       'seasons'])
st.markdown(f"### Currently Selected {trend_level}")

fig = sns.lineplot(x = 'month_of_absence', y =  'absenteeism_time_in_hours', data = df,estimator=sum)
warnings.filterwarnings(action='once')

st.plotly_chart(fig)
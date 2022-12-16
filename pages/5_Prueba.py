import streamlit as st
from main_page import data_set as df
import matplotlib as plt
import plotly.express as px


def interactive_plot(dataframe):
    x_axis_val=st.selectbox('Select X-Axis Value',options = dataframe.columns)
    y_axis_val=st.selectbox('Select Y-Axis Value',options = dataframe.columns)
    plot=px.scatter(dataframe,  x=x_axis_val, y=y_axis_val)
    col=st.color_picker('Select a graph color')
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

interactive_plot(df)
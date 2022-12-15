
#------mainpage???---------
#------aqui una opción para páginas com opciones de variables y 2 tipos de producion de graficos----
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import plotly_express as px

def stast(dataframe):
    st.header('Data Statistic')
    st.writer(dataframe.describe())

def data_header (dataframe):
    st.header('Data Header')
    st.write('df.head'())

def plot(dataframe):
    fig, ax= plt.subplot(1,1)
    ax.scatter (x=df['Depth'], y= df['Magnitud'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitud')
    st.pyplot(fig)
def interactive_plot(Absenteeism_at_work):
    x_axis_val=st.selectbox('Select X-Axis Value'),
    options = df.columns
    y_axis_val=st.selectbox('Select Y-Axis Value'),
    options = df.columns
    plot.scatter(dataframe,  x=x_axis_val, y=y_axis_val)
    col=st.color_picker('Select a graph color')
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

options = st.radio ('Pages', options = 
                    Data Statistics,
                    Data Header, Plot, Interactive Plot)

if upload_file:
    df= pd.read_csv('Absenteeism_at_work.csv')
if options=='Data Statistics':
    (stats(df))
elif options=='Data Header':
    data_header(df)
elif options=='Plot':
    plot(df)
elif options=='Interactive Plot':

    plot(df)    



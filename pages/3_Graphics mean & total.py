import streamlit as st
from main_page import data_set

st.markdown("# Graphics mean & count")
st.sidebar.markdown("# Graphics mean & count")

import plotly.graph_objects as go
fig = go.Figure(
    data=data_set["Absenteeism time in hours"].value_counts(),
    layout_title_text="A Figure Displaying Itself"
)

st.plotly_chart(fig)
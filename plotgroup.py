#-------------------graficos con groupby----------------

# Absence sum by season (Bar chat)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import plotly.express as px

absenteeism_by_season= (def_selection.groupby(by=['absenteeism_time_in_hours']).sum().
['season'].sort_values(by='season')
)
Fig_absence_season = px.bar(
    absenteeism_by_season,
    x= 'season',
    y = 'absenteeism_by_season'
    orientation=h,
    title= <b> Absenteeism_by_season </b>,
    color_discrete_sequence=[#0083B8]* len[absenteeism_by_season],
    template= "plotly_white",
)
# To quit the grades from ploty

Fig_absence_season.update_layout
        (plot_bgcolors="rgba"(0,0,0,0)",
        xaxis=dict(showgrid)
)

st.ploty_chart(Fig_absence_season)
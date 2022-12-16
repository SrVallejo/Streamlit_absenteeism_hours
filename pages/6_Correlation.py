import streamlit as st
from main_page import data_set as df
import seaborn as sns
import matplotlib as plt


# fig = plt.figure(figsize=(10, 4))
# sns.heatmap(df.corr(), annot = True)
# st.pyplot(fig)

fig = plt.figure(figsize=(10, 4))
sns.countplot(x="Seasons", data=df)

st.pyplot(fig)
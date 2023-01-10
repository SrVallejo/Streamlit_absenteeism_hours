import streamlit as st
import pickle

st.markdown("# Classification")
st.sidebar.markdown("# Classification")


#pickled_model = pickle.load(open('model.pkl', 'rb'))
file_path = 'pickle\classifier_Gradient Boosting.pkl'
pickled_model = pickle.load(open(file_path, 'rb'))
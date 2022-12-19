import streamlit as st
from main_page import dataset_pred

st.markdown("# Classification")
st.sidebar.markdown("# Classification")

st.write(dataset_pred)

# picle.load(open(model.pkl))
# pickled_model = pickle.load(open('model.pkl', 'rb'))
# pickled_model.predict(X_test)
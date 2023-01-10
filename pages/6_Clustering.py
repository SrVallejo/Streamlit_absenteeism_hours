import streamlit as st
from PIL import Image
from io import StringIO, BytesIO
import base64
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as com
import streamlit as st
# com.html("""
# <div>
# <style>
# h1.heading{
#    background.color:+ blueviolet;
#    color:lightyellow;
#    border-radius:20px;
#    text-align:center;
# }
# </style>
# <h1.class="heading">
# <h1>

# </h1>
# <p>
# Despite the fact that there are still values ​​of inertia to go down before achieving stability, we consider the starting from 3 clusters one could consider the beginning of stability and, therefore, where would we find three different groups of employees features
# </div>
# """)
st.header("This is our clustering 3D result")
st.write("Despite the fact that there are still values ​​of inertia to go down before achieving stability, we consider the starting from 3 clusters one could consider the beginning of stability and, therefore, where would we find three different groups of employees features")
path_to_html = "./Imagenes/test.html" 

# Read file and keep in variable
with open(path_to_html, 'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Clustering 3d - k-means=3 ")
st.components.v1.html(html_data,height=600)


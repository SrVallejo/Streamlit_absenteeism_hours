import streamlit as st
from main_page import data_set
import plotly.express as px


GRAPHIC_OPTIONS = [
    "ID",
    "Day of the week",
    "Month of absence",
    "Reason for absence",
    "Seasons",
    "Education",
    "Body mass index",
    "Age",
    "Service time"
]

day_orders= {
            "Day of the week": ["Monday", "Tuesday", "Wednesday", "Thursday","Friday"]
        }
season_orders = {
    "Seasons": ["Spring","Summer","Autumn","Winter"]
}
education_orders = {
    "Education": ["High school","Graduate","Postgraduate","Master and doctor"]
}

reason_orders = {
    "Reason for absence": [
        "Not specified", "Infectious and parasits", "Neoplasms",
        "Blood and immune mechanism","Endocrine, nutritional and metabolic","Mental and behavioural",
        "Nervous system", "Eye and adnexa", "Ear and mastoid process",
        "Circulatory system","Respiratory system","Digestive system",
        "Skin and subcutaneous tissue", "Musculoskeletal system","Genitourinary system",
        "Pregnancy and childbirth","Perinatal period","Congenital malformations",
        "Syntoms not classified","Injury or poisoning","External causes",
        "Health status", "Patient follow-up","Medical consultation",
        "Blood donation", "Laboratory examination", "Unjustified absence", 
        "Physiotherapy", "Dental consultation" 
    ]
}

st.markdown("# Absenteeism time Graphics")
st.sidebar.markdown("# Absenteeism time Graphics")


def plot_graph(option,aggregation,color):
    category_orders={}
    if option == "Day of the week": 
        category_orders=  day_orders 

    elif option == "Seasons":
        category_orders = season_orders

    elif option == "Education":
        category_orders = education_orders

    elif option == "Reason for absence":
        category_orders = reason_orders

    if aggregation == "Mean": 
        data_plot = data_set.groupby([option]).mean().reset_index()
        label_y = "Mean absence time in hours"
    elif aggregation == "Count": 
        data_plot = data_set.groupby([option]).count().reset_index()
        label_y = "Number of absences"
    else: 
        data_plot = data_set.groupby([option]).sum().reset_index()
        label_y = "Total absence time in hours"


    if option == "ID": title = label_y + " by Employee ID"
    else: title = label_y + " by " + option
    
    plot = px.bar(
        data_plot, 
        x=option, 
        y="Absenteeism time in hours", 
        barmode='group', 
        category_orders= category_orders,
        labels = {"Absenteeism time in hours": label_y, option: ""},
        title = title
        )
    plot.update_traces(marker=dict(color=color))
    plot.update_layout(
        xaxis = dict(
            tickmode = "linear"
        )
    )

    st.plotly_chart(plot)



col1,col2,col3,col4 = st.columns((1,0.1,0.7,1))


with col3:
    
    r_agg = st.radio("Aggregation",["Mean","Sum","Count"])
    if r_agg == "Mean": default_color = '#1f77b4' #muted blue
    elif r_agg == "Sum": default_color = '#bcbd22' #curry yellow-green
    else: default_color = '#d62728' #brick red

with col4:
    col1_container = st.container()
    if st.checkbox("Use same color (resets to black)"): default_color = None

with col1:
    sb_xlabel = st.selectbox("X Axis",GRAPHIC_OPTIONS)
    

   
color_p = col1_container.color_picker("Select graph color", value= default_color)

        

plot_graph(sb_xlabel,r_agg,color_p)









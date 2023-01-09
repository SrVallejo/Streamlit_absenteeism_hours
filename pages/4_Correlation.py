import streamlit as st
import pandas as pd
from Main_Page import data_set
import plotly.express as px

st.markdown("# Correlation visuals")
st.sidebar.markdown("# Correlation")

#Return a dataframe with all the correlations that surpass the threshold
def correlation_list(dataset, threshold):
    corr_names_1 = []  # Lists of names of correlated columns
    corr_names_2 = []   
    corr_coef = [] #List of coeficient values
    corr_matrix = dataset.corr()

    #Iterate the corr_matrix
    for column in corr_matrix.columns:
        for index in corr_matrix.index:

            #Takes the coeficient of that cell
            coeficient = abs(corr_matrix[column][index])
            if  coeficient > threshold and coeficient < 1:  # Get absolut values bigger than treshold
                                                            # And not 1 (the field with themself)
                corr_names_1.append(column) # Saving field names
                corr_names_2.append(index) 
                corr_coef.append(corr_matrix[column][index])    #Saving coeficient (including negative)
    return pd.DataFrame({"Field 1":corr_names_1,"Field 2": corr_names_2,"Coeficient":corr_coef})

#Scatter plot between all columns of the data set
def interactive_plot(dataframe):
    x_axis_val=st.selectbox('Select X-Axis Value',options = dataframe.columns)
    y_axis_val=st.selectbox('Select Y-Axis Value',options = dataframe.columns)
    plot=px.scatter(dataframe,  x=x_axis_val, y=y_axis_val)
    col=st.color_picker('Select graph color', value = '#1f77b4') #muted blue
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)


columns_list = []
# Function that creates a checkbox in the sidebar to select the columns
#If true, it adds the *column_name* to *columns_list*, if not, remove that name
def create_filter_columns(column_name):
    #columns hided as default
    hided_columns = [
        "ID","Month of absence",
        "Transportation expense","Distance from Residence to Work","Service time",
        "Hit target", "Work load Average",
        "Weight","Height","Education",
        "Social drinker","Social smoker",
        "Seasons","Reason for absence","Disciplinary Failure"
    ]

    default = column_name not in hided_columns
    if st.sidebar.checkbox(column_name, value = default):
        columns_list.append(column_name)
    else:
        try:
            columns_list.remove(column_name)
        except:
            pass


def filter_columns():
    # List of columns to show

    #Loop to create a checkbox for each column in the dataset
    st.sidebar.write("Columns on heat map")
    for column in data_set.columns:
        create_filter_columns(column)


def heat_map():
    #Create filter columns
    filter_columns()

    #Show heatmap
    plot = px.imshow(data_set[columns_list].corr().round(3), text_auto=True, color_continuous_scale="blugrn_r")
    st.plotly_chart(plot)


def top_correlations():

    col1, col2 = st.columns((1,2))
    with col1:
        coef_threshold= st.slider("Correlation coeficient threshold",min_value=0.1,max_value=0.9,value=0.5)

    df_corr = correlation_list(data_set,coef_threshold)
    df_corr = df_corr.drop_duplicates(subset=["Coeficient"], keep='first')
    st.write(df_corr.sort_values("Coeficient",ascending=False))
    


#Radio to select page
r_page = st.radio("Select Visual",["Heat map","Correlation rank","Scatter Plots"])

#Calling of function: One for each option
if r_page == "Heat map": heat_map()

elif r_page == "Scatter Plots": interactive_plot(data_set)

else: top_correlations()
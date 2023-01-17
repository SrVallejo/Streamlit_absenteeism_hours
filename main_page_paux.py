import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import settings
#from create_database import clean_dataset

st.markdown("# Main page")
st.sidebar.markdown("# Main page")

st.write("This dashboard is a report for the data set Absenteeism at work that have a collection of sick\
     leaves, one in each row, for a Brazilian courier company from July 2007 to July 2010")
    
st.markdown("The objective is to predict how long will be each sick leave. In order to do that we categorize\
    the Absenteeism hours in 3 categories.\n\n\
    1. Short: Less than 2 hours\n\
    2. Medium: A day or less\n\
    3. Long: More than a day\n")

st.markdown("You will find the next pages:\n\n\
    - Data set: Shows full data set with filters\n\
    - Data set by id: Show the data set grouped by id with filters\n\
    - Graphics mean & total: Graphics of Absenteeism time crossed with some fields\n\
    - Correlation: Heatmap and other correlation visuals\n\
    - Prediction: Predicts how long a sick leave will take\n\
    - Clustering: Shows a cluster visualization")

st.write("This dashboard is created by")
st.write("Etty Guerra de Queiroz [linkedin](https://www.linkedin.com/in/etty-guerra-42590225b/)")
st.write("Luis Vallejo Carretero [linkedin](https://www.linkedin.com/in/luisvallejocarretero/)")




reasons_list = [
        "Not specified", "Infectious and parasites", "Neoplasms",
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
education_list = [
        "Not specified",
        "High school",
        "Graduate",
        "Postgraduate",
        "Master and doctor"
    ] 

@st.experimental_memo
#Function to prepare de dataset to visuals
def clean_dataset(data_set):
# Remove rows with wrong values

    data_set = data_set[data_set["Month of absence"]!= 0]

    

    # reasons = [
    #     "[0]Not specified", "[01]Infectious and parasitic diseases", "[02]Neoplasms",
    #     "[03]Diseases of the blood and immune mechanism","[04]Endocrine, nutritional and metabolic diseases","[05]Mental and behavioural disorders",
    #     "[06]Diseases of the nervous system", "[07]Diseases of the eye and adnexa", "[08]Diseases of the ear and mastoid process",
    #     "[09]Diseases of the circulatory system","[10]Diseases of the respiratory system","[11]Diseases of the digestive system",
    #     "[12]Diseases of the skin and subcutaneous tissue", "[13]Diseases of the musculoskeletal system and connective tissue","[14]Diseases of the genitourinary system",
    #     "[15]Pregnancy, childbirth and the puerperium","[16]Certain conditions from the perinatal period","[17]Congenital malformations and chromosomal abnormalities",
    #     "[18]Syntoms not elsewhere classified","[19]Injury, poisoning or other by external causes","[20]External causes of morbidity and mortality",
    #     "[21]Health status and contact with health services", "[22]Patient follow-up","[23]Medical consultation",
    #     "[24]Blood donation", "[25]Laboratory examination", "[26]Unjustified absence", 
    #     "[27]Physiotherapy", "[28]Dental consultation" 
    # ]



    day_of_the_week = [
        "Not specified","Sunday","Monday",
        "Tuesday","Wednesday","Thursday",
        "Friday","Saturday"
    ]

      

    # Loop for changing Season, day and reason Number to String
    seasons_list =[]
    day_col = []
    reason_col = []
    education_col = []
    for index,row in data_set.iterrows():
        if row["Seasons"] == 1: seasons_list.append("Winter")
        elif row["Seasons"] == 2: seasons_list.append("Summer")
        elif row["Seasons"] == 3: seasons_list.append("Autumn")
        elif row["Seasons"] == 4: seasons_list.append("Spring")

        reason_col.append(reasons_list[int(row["Reason for absence"])])
        day_col.append(day_of_the_week[int(row["Day of the week"])])
        education_col.append(education_list[int(row["Education"])])


    data_set["Seasons"] = seasons_list
    data_set["Reason for absence"] = reason_col
    data_set["Day of the week"] = day_col
    data_set["Education"]= education_col

    return data_set


#Function that prepares the dataset for prediction
#Create dummies and categorize columns
@st.experimental_memo
def prepare_dataset_prediction(data_set):

    #Drop columns that lower our prediction accuracy
    columnsToDrop = ["ID","Service time","Month of absence","Weight","Height"]
    dataset_pred = data_set.drop(columns=columnsToDrop,axis=1)

    #Categorize columns

    #The target column (Absenteeism time in hours) to clasification
    #   short: x <=2
    #   medium: 2 < x <=8
    #   long: 8 < x

    group_hours = []
    for index, row in dataset_pred.iterrows():
        if row["Absenteeism time in hours"] <= 2: group_hours.append("short")
        elif row["Absenteeism time in hours"] <= 8: group_hours.append("medium")
        else: group_hours.append("long")

    dataset_pred["Group Hours"] = group_hours
    dataset_pred.head()

    #Education column group the values in:
    #   Where it was a 1 -> Highschool
    #   Where it was a 2, 3 or 4 -> University
    education_col = []
    for i,r in dataset_pred.iterrows():
        if r["Education"] == 1: education_col.append("High School")
        else: education_col.append("University")

    dataset_pred["Education"] = education_col

    #Distance column
    #   close: x < 20
    #   mid: 20 <= x < 40
    #   far: 40 <= x

    distance_col = []
    for i,r in dataset_pred.iterrows():
        if r["Distance from Residence to Work"] < 20: distance_col.append("close")
        elif r["Distance from Residence to Work"] < 40: distance_col.append("mid")
        else: distance_col.append("far")

    dataset_pred["Distance from Residence to Work"] = distance_col

    #Age column
    #   young: x < 35
    #   adult: 35 <= x < 45
    #   old: 45<= x

    age_col = []
    for i,r in dataset_pred.iterrows():
        if r["Age"] < 35: age_col.append("young")
        elif r["Age"] < 45: age_col.append("adult")
        else: age_col.append("old")

    dataset_pred["Age"] = age_col


    #Pet column
    #   no: x == 0
    #   few: x <= 2
    #   a lot: 2 < x

    pet_col = []
    for i,r in dataset_pred.iterrows():
        if r["Pet"] <= 0: pet_col.append("no")
        elif r["Pet"] <= 2: pet_col.append("few")
        else: pet_col.append("a lot")

    dataset_pred["Pet"] = pet_col


    #Dummies for categorical columns

    dummies_cols = ["Age","Seasons","Distance from Residence to Work","Education","Son","Pet"]
    dataset_pred = pd.get_dummies(dataset_pred,columns= dummies_cols,drop_first=True)

    return dataset_pred

def connect():
    conn = psycopg2.connect(database="Absenteeism",
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

    cur = conn.cursor()
    return cur, conn

@st.experimental_memo
def read_dataset_raw():
    #Try to connect to the database and get the data set
    try:
        cur, conn = connect()
        sql = 'SELECT * FROM "Absenteeism at work"'
        data_set_raw = sqlio.read_sql_query(sql, conn)
        conn = None
        #if its loaded from postgress, erase index column
        data_set_raw = data_set_raw.drop(["index"], axis = 1)
        print("Dataset loaded from PostgreSQL")

    #Read from csv file instead
    except:
        print("Can't connect to BBDD\nReading Dataset from csv")
        data_set_raw = pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")
    return data_set_raw
    

#We have to data sets: data_set with the cleaned data, and
#data_set_raw with no processed data
data_set_raw = read_dataset_raw()
data_set = clean_dataset(data_set_raw)
data_set_prediction = prepare_dataset_prediction(data_set_raw)

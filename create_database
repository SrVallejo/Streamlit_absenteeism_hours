import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
import settings



def clean_dataset(data_set):
# Remove rows with wrong values

    data_set = data_set[data_set["Month of absence"]!= 0]

    reasons = [
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

    education = [
        "Not specified",
        "High school",
        "Graduate",
        "Postgraduate",
        "Master and doctor"
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

        reason_col.append(reasons[int(row["Reason for absence"])])
        day_col.append(day_of_the_week[int(row["Day of the week"])])
        education_col.append(education[int(row["Education"])])


    data_set["Seasons"] = seasons_list
    data_set["Reason for absence"] = reason_col
    data_set["Day of the week"] = day_col
    data_set["Education"]= education_col

    return data_set


############### Create dataframe from csv ###############

data_set = pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")
data_set = clean_dataset(data_set)
print(data_set.head())

############## Create database in postgress ###########


def createDatabase(db_name):
        conn = psycopg2.connect(user=settings.USER,
                                password=settings.PASSWORD,
                                host=settings.HOST,
                                port=settings.PORT)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = conn.cursor()

        try:
            cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(db_name)))
        except psycopg2.Error as e:
            return str(e)

        cur.close()
        conn.close()

user = settings.USER
password = settings.PASSWORD
port = settings.PORT
host = settings.HOST
db_name = "Absenteeism"

createDatabase(db_name)
url = "postgresql://" + user + ":" + password + "@"+ host + ":" + port + "/" + db_name
engine = create_engine(url)
data_set.to_sql('Absenteeism at work', engine)

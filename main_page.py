import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import settings
from create_database import clean_dataset

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")



def connect():
    conn = psycopg2.connect(database="Absenteeism",
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

    cur = conn.cursor()
    return cur, conn


try:
    cur, conn = connect()
    sql = 'SELECT * FROM "Absenteeism at work"'
    data_set = sqlio.read_sql_query(sql, conn)
    conn = None

except:
    print("Can't connect to BBDD\nReading Dataset from csv")
    data_set = pd.read_csv()
    data_set = pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")
    data_set = clean_dataset(data_set)
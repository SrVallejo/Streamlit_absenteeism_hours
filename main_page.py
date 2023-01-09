import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import settings

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

def connect():
    conn = psycopg2.connect(database="Absenteeism",
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

    #conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    return cur, conn

cur, conn = connect()
sql = 'SELECT * FROM "Absenteeism at work"'
data_set = sqlio.read_sql_query(sql, conn)
conn = None
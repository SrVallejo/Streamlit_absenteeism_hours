import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
import settings



############### Create dataframe from csv ###############

data_set = pd.read_csv("dataset/Absenteeism_at_work.csv",delimiter=";")

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

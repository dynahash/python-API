import psycopg2
from decouple import config


database_user, database_password = config("DATABASE_USER"), config("DATABASE_PASSWORD")

mydb = psycopg2.connect(
    database=database_user,
    user=database_user,
    password=database_password,
    host='motty.db.elephantsql.com',
    port='5432'
)

cursor = mydb.cursor()

# This file is currently in unitility
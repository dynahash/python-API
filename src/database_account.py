import psycopg2
import json

dados = json.load(open("../configs.json"))

mydb = psycopg2.connect(
    database=dados["database"]["user"],
    user=dados["database"]["user"],
    password=dados["database"]["password"],
    host='motty.db.elephantsql.com',
    port='5432'
)


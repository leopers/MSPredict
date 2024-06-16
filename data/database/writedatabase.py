import pandas as pd
import psycopg2
from config import  config

df = pd.read_csv('../processed/processed_test.csv')
params = config()

connection = psycopg2.connect(**params)
cur = connection.cursor()

# Insere o DataFrame no PostgreSQL
df_columns = list(df)
columns = ','.join(df_columns)
values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
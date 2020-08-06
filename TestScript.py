import os
import psycopg2
try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("Connected!")
except:
    print("Error connecting.")
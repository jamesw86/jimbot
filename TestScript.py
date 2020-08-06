import os
import psycopg2
try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("Connected!")
except:
    print("Error connecting.")

cur = conn.cursor()
def getBirthday(name):
    try:
        cur.execute("SELECT \"Birthday\" FROM \"Users\" WHERE \"Name\"='" + name + "';") 
        return cur.fetchone()
    except:
        print("Error occured trying to get birthday.")
        return "Error"

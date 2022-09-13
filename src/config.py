import os
import psycopg2

def heroku_db_init():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("!!!!!!!!!!!!!!! DB CONN SUXXX !!!!!!!!!!!!!!!")
    return conn

def local_db_init():
    conn = psycopg2.connect(database = "testdb", user = "postgres", password = "admin", host = "127.0.0.1", port = "5432")
    print("!!!!!!!!!!!!!!! DB CONN SUXXX !!!!!!!!!!!!!!!")
    return conn
import os
import sqlite3

TABLE_NAME = "../db/db.sqlite3"
def local_db_init():
    conn = sqlite3.connect(TABLE_NAME)
    print("!!!!!!!!!!!!!!! DB CONN SUXXX !!!!!!!!!!!!!!!")
    return conn
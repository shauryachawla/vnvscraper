def deleteAllRecords(cur):
    cur.execute("delete from brandtbl")
    cur.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'brandtbl'")

def insertNewRecords(cur, new_list):
    for brand in new_list:    
        cur.execute("insert into brandtbl (brand) values (?)", (brand,))
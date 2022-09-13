def deleteAllRecords(cur):
    cur.execute("delete from brandtbl")

def insertNewRecords(cur, new_list):
    for brand in new_list:
        cur.execute("insert into brandtbl (brand) values (%s);", (brand,))
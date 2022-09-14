def deleteAllRecords(cur):
    cur.execute("delete from brand_schema.brandtbl")

def insertNewRecords(cur, new_list):
    for brand in new_list:
        cur.execute("insert into brand_schema.brandtbl (brand_name) values (%s);", (brand,))
from distutils.command.config import config
import requests
from bs4 import BeautifulSoup
import random
import os
import psycopg2
import config
import queries


# db connex
def setup_db():
    global CONN 
    CONN = config.heroku_db_init()
    print("db opened succex")

# scrapin
def scrape_to_find_brands():
    url = "https://www.vegnonveg.com/footwear?size%5B%5D=7&size%5B%5D=7.5&gender%5B%5D=Unisex&gender%5B%5D=Men"
    # makes a request to the web page and gets its HTML
    r = requests.get(url)
    # stores the HTML page in 'soup', a BeautifulSoup object
    soup = BeautifulSoup(r.content)
    brand_list = []
    for brand in soup.find_all("div", {"class":"info mt-10"}):
        brand_name = brand.contents[1].contents[1].contents[0].strip()
        brand_list.append(brand_name)
    return brand_list

def getExisistingRecords():
    cur.execute("select * from brandtbl")
    rows = cur.fetchall()
    list = []
    for row in rows:
        # print(row[1])
        list.append(row[1])
    return list

setup_db();
with CONN:
    brand_list = scrape_to_find_brands();
    global cur 
    cur = CONN.cursor();
    existing_list = getExisistingRecords();
    new_list = scrape_to_find_brands()
    if((new_list == existing_list ) == False):
        print("lists are different")
        # sendNotif();
        queries.deleteAllRecords(cur);
        queries.insertNewRecords(cur, new_list);
        CONN.commit()
    else:
        print("No new records")

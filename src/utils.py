import requests
from bs4 import BeautifulSoup
import config
import notifs

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

def getExisistingRecords(cur):
    cur.execute("select * from brandtbl")
    rows = cur.fetchall()
    list = []
    for row in rows:
        # print(row[1])
        list.append(row[1])
    return list

def checkForNewBalance(list):
    for brand in list:
        if(brand.lower() == "new balance"):
            notifs.notifyNewBalance()

# db connex
def setup_db():
    CONN = config.local_db_init()
    print("db opened succex")
    return CONN
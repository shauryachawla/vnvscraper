# from distutils.command.config import config

import queries
import time
import notifs
import utils


# scrapin
utils.setup_db();
with utils.setup_db() as CONN:
    while(True):
        global cur 
        cur = CONN.cursor();
        existing_list = utils.getExisistingRecords(cur);
        new_list = utils.scrape_to_find_brands()
        if((new_list == existing_list ) == False):
            print("lists are different")
            notifs.sendNotif();
            queries.deleteAllRecords(cur);
            queries.insertNewRecords(cur, new_list);
            utils.checkForNewBalance(new_list)
            CONN.commit()
        else:
            print("No new records")
        time.sleep(60*60*5)

#===================================================================#
#                   _               _      | |               | |    #
#   ____ ___  ____ | |_  ____  ____| |_ ___| | _   ___   ___ | |  _ #
#  / ___/ _ \|  _ \|  _)/ _  |/ ___|  _(___| || \ / _ \ / _ \| | / )#
# ( (__| |_| | | | | |_( ( | ( (___| |__   | |_) | |_| | |_| | |< ( #
#  \____\___/|_| |_|\___\_||_|\____)\___)  |____/ \___/ \___/|_| \_)#
#===================================================================#

import sys
import sqlite3 

def ascii_start():
    print("                        __              __        ")
    print(".----.-----.-----.----|  |_.---.-.----|  |_.-----.")
    print("|  __|  _  |     |  __|   _|  _  |  __|   _|__ --|")
    print("|____|_____|__|__|____|____|___._|____|____|_____|")
    print("=== <>--------------------------------------<> ===")
    
ascii_start()


connected = sqlite3.connect('./contacts.db') # connecting to sqlite data base
cur = connected.cursor() # initizliazing cursor, needed to fetch date form .db

#sql commands
persoon = ()


# try for error catching
try:
    cur.execute("SELECT * FROM contacts")


# error catching
except sqlite3.Error as e:
    print("Error!:", e)

# clossing connection
finally:
    if (connected):
        connected.close()
        print("=== \\\===============|closed|===============// ===")


# connected.commit()
# #clossing the connection to data base
# connected.close()


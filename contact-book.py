#!/usr/bin/env python


#===================================================================#
#                   _               _      | |               | |    #
#   ____ ___  ____ | |_  ____  ____| |_ ___| | _   ___   ___ | |  _ #
#  / ___/ _ \|  _ \|  _)/ _  |/ ___|  _(___| || \ / _ \ / _ \| | / )#
# ( (__| |_| | | | | |_( ( | ( (___| |__   | |_) | |_| | |_| | |< ( #
#  \____\___/|_| |_|\___\_||_|\____)\___)  |____/ \___/ \___/|_| \_)#
#===================================================================#

import sys
import sqlite3 
import nerdfonts as nf


def ascii_start():
    print("                       |--|            |--|")
    print(" .----.-----.-----.----|  |_.---.-.----|  |_.-----.")
    print(" |  __|  _  |     |  __|   _|  _  |  __|   _|__ --|")
    print(" |____|_____|__|__|____|____|___._|____|____|_____|")
    print("||=== <>--------------------------------------<> ===")
    
ascii_start()


connected = sqlite3.connect('./contacts.db') # connecting to sqlite data base
cur = connected.cursor() # initizliazing cursor, needed to fetch date form .db

#variables



# funcitons
def print_all():
    cur.execute("SELECT * FROM people")
    rows = cur.fetchall()
    print(">-|people|--------------------------------------------------------<")
    for x in rows:
        # print(nf.icons['nf-cod-archive'])
        print(">-" +" | ".join(x))
        # print(">----------------------------------------------------------<")
    cur.execute("SELECT * FROM companies")
    rows = cur.fetchall()
    print(">-|companies|-----------------------------------------------------<")
    for x in rows:
        print(">-" + " | ".join(x))
        # print(">----------------------------------------------------------<")
def close_connection():
    # clossing connection
    if (connected):
        connected.close()
        print("=== \\\===============|closed|===============// ===")
        sys.exit()
        


# try for error catching

while True:
    try:
        usr_input = input("||>")
        match usr_input:
            case "close":
                close_connection()
            case "see all":
                print_all ()


    # error catching
    except sqlite3.Error as e:
        print("Error!:", e)




# connected.commit()
# #clossing the connection to data base
# connected.close()


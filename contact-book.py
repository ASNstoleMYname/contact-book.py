
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

# connecting to sqlite data base
connected = sqlite3.connect('./test.db')

# initizliazing cursor, needed to fetch date form .db
cursor = connected.cursor()

#sql commands
persoon = ()

# inserting data
cursor.execute("INSERT INTO contacts (contact_id,first_name,last_name,email,phone) VALUES (2,'Jarne','Guy','Jarne.Guy@gmail.com',666666)")

connected.commit()
#clossing the connection to data base
connected.close()


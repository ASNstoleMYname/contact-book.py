#!/usr/bin/env python


#===================================================================#
#                   _               _      | |               | |    #
#   ____ ___  ____ | |_  ____  ____| |_ ___| | _   ___   ___ | |  _ #
#  / ___/ _ \|  _ \|  _)/ _  |/ ___|  _(___| || \ / _ \ / _ \| | / )#
# ( (__| |_| | | | | |_( ( | ( (___| |__   | |_) | |_| | |_| | |< ( #
#  \____\___/|_| |_|\___\_||_|\____)\___)  |____/ \___/ \___/|_| \_)#
#===================================================================#
#https://github.com/ASNstoleMYname

import sys
import sqlite3 
# import nerdfonts as nf


def ascii_start():
    print("                        __              __")
    print(" .----.-----.-----.----|  |_.---.-.----|  |_.-----.")
    print(" |  __|  _  |     |  __|   _|  _  |  __|   _|__ --|")
    print(" |____|_____|__|__|____|____|___._|____|____|_____|")
    print("||=== <>--------------------------------------<> ===")
    
ascii_start()


connected = sqlite3.connect('./contacts.db') # connecting to sqlite data base
cur = connected.cursor() # initizliazing cursor, needed to fetch date form .db

#variables



# funcitons

def help():
    print(">=============================================<")
    print(" *   see all => see all entries")
    print(" *   search => search buy name(SQL key)")
    print(" *   add => add new entrie")
    print(" *   delete => remove item from list")

def add_contact():
    contact_type = input("(P)erson or (C)ompanie:")

    match contact_type.capitalize():
        case "P":
            contact_naam = input("name:")
            contact_a_naam = input("last name:")
            contact_nummer = input("nummer:")
            contact_email = input("email:")
            print(" * added " + contact_naam + '\n')
            cur.execute("""INSERT INTO people (naam,a_naam,nummer,email) VALUES (?,?,?,?)""", [contact_naam,contact_a_naam,contact_nummer,contact_email]) 
        case "C":
            contact_naam = input("name:")
            contact_nummer = input("nummer:")
            contact_email = input("email:")
            contact_addres = input("straat:")
            print(" * added " + contact_naam +'\n')
            cur.execute("""INSERT INTO companies (naam,nummer,email,addres) VALUES (?,?,?,?)""", [contact_naam,contact_email,contact_nummer,contact_addres])


def print_all(): #prints all contacts
    #----people 
    cur.execute("SELECT * FROM people")
    rows = cur.fetchall() #puts cursor elements in a tuplet
    print(">-|people|--------------------------------------------------------<" + '\n')
    for x in rows:
        # print(nf.icons['nf-cod-archive'])
        print("[*]  " +" | ".join(x)) #print the tuplet in a nicer way
        # print(">----------------------------------------------------------<")
    
    #----companies
    cur.execute("SELECT * FROM companies")
    rows = cur.fetchall()
    print(">-|companies|-----------------------------------------------------<" + '\n')
    for x in rows:
        print("[*]" + " | ".join(x))
        # print(">----------------------------------------------------------<")


def search_all(table, item):
    match table.capitalize():
        case "p": 
            rows = cur.execute("""Select * From people Where naam like ?""", [item] )
            for x in rows:
                print("[x]" + " | ".join(x) + '\n')

        case "c":
            rows = cur.execute("""SELECT * FROM companies WHERE naam LIKE ?""", [item])
            for x in rows:
                print("[x]" + " | ".join(x) + '\n')



def delete_item(table, item):
    match table.capitalize():
        case "P":
            cur.execute("""DELETE FROM people WHERE naam = (?)""", [item])
        case "C":
            cur.execute("""DELETE FROM companies WHERE naam = (?)""", [item])
     # cur.execute("""DELETE FROM ? where naam = ?""", [table, item])
    


def close_connection():
    # closing connection
    if (connected):
        connected.close() 
        print("=== \\\===============|closed|===============// ===")
        sys.exit()
        


# try for error catching
while True:
    try:
        usr_input = input("||>")
        match usr_input:
            case "close": #close program
                close_connection()

            case "see all": # see all entries
                print_all ()

            case "search": # search for specifiek entrie
                s_table = input("(P)erson or (C)ompanie:")
                s_item = input("name:")
                search_all(s_table, s_item)
                result = cur.fetchall()
                print(result, '\n')

            case "add": # add an entrie
                add_contact()
                connected.commit()

            case "delete":
                del_table = input("(P)erson or (C)ompanie:")
                del_name = input("name:")
                delete_item(del_table, del_name)
                connected.commit()
                print("Deleted =>", del_name, '\n')

            case "help":
                help()

    # error catching
    except sqlite3.Error as e:
        print("Error!:", e)




# connected.commit()
# #clossing the connection to data base
# connected.close()


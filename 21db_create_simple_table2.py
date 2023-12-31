#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db04.sqlite"
tableNameList = ["t01"]  # , "t02", "t03"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            print("OK: cursor created")
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            allTablesList = [item[0] for item in cur.execute(query).fetchall()]
            for tableName in tableNameList:
                if tableName not in allTablesList:
                    query = "CREATE TABLE {}(id, col01, col02, col03, col05)".format(tableName)
                    cur.execute(query)
                    print("Table created:", tableName)
                else:
                    print("Table {} already exists".format(tableName))
    except sqlite3.Error as error:
        print("Problem to create table:", error)
    cur.close()
    con.close()
    print("OK: cursor and connection closed")

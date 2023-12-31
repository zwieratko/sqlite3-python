#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
# tableNameList = ["t07", "t08", "t09"]

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            allTablesList = [item[0] for item in cur.execute(query).fetchall()]
            if len(allTablesList) == 0:
                print("There is no table")
            else:
                print("List of all tables in:", dbPath)
                print(allTablesList)
                userAnswer = input(
                    "Do you want to delete all of these tables? [y/n]: ")
                if userAnswer.lower() in ["y", "yes"]:
                    for tableName in allTablesList:
                        if tableName == "sqlite_sequence":
                            query = "UPDATE {} SET 'seq'=0".format(tableName)
                        else:
                            query = "DROP TABLE {}".format(tableName)
                        cur.execute(query)
                        print("Table dropped / cleared:", tableName)
                else:
                    print("No tables will be deleted")
    except sqlite3.Error as error:
        print("Problem to drop table, {}".format(error))

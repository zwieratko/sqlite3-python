#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableNameList = ["t07", "t08", "t09"]

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
            for tableName in tableNameList:
                if tableName in allTablesList:
                    query = "DROP TABLE {}".format(tableName)
                    cur.execute(query)
                    print("Table dropped:", tableName)
                else:
                    print("Table {} doesn't exists".format(tableName))
    except sqlite3.Error as error:
        print("Problem to drop table, {}".format(error))

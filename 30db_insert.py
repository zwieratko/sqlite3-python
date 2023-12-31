#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db03.sqlite"
tableNameList = ["t03"]  # , "t02", "t03"
columnName = "id"  # id / col01
startValue = 42.5
totalRecords = 1
values = "?"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            for tableName in tableNameList:
                query = "INSERT INTO {}({}) VALUES({})".format(
                    tableName, columnName, values)
                for iter in range(totalRecords):
                    newRecord = (startValue + iter, )
                    cur.execute(query, newRecord)
                    print("OK: simple record inserted")
                    print("Last rowid:", cur.lastrowid)
                    print("Modified rows:", cur.rowcount)
    except sqlite3.Error as error:
        print("Problem to insert:", error)

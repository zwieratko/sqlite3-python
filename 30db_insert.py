#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableNameList = ["t01", "t02", "t03"]
startValue = 42
totalRecords = 5

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
                query = "INSERT INTO {} VALUES(?)".format(tableName)
                for iter in range(totalRecords):
                    newRecord = (startValue + iter, )
                    cur.execute(query, newRecord)
                    print("OK: simple record inserted")
                    print("Last rowid:", cur.lastrowid)
                    print("Modified rows:", cur.rowcount)
    except sqlite3.Error as error:
        print("Problem to insert:", error)

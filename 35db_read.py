#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableName = "t01"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

try:
    with con:
        cur = con.cursor()
        query = "SELECT * FROM {} ORDER BY id DESC LIMIT 10".format(tableName)
        result = cur.execute(query).fetchall()
        for row in result:
            print(row)
except sqlite3.Error as error:
    print("Problem with simple query:", error)

#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db09.sqlite"
tableName = "t01"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

try:
    with con:
        cur = con.cursor()
        query = "DROP TABLE IF EXISTS {}".format(tableName)
        cur.execute(query)
        print("Table dropped:", tableName)
except sqlite3.Error as error:
    print("Problem to drop table:", error)

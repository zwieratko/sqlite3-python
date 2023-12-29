#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db02.sqlite"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

try:
    with con:
        cur = con.cursor()
        query = "UPDATE tabulka01 SET stlpec01 = ? WHERE id = ?"
        # query = "UPDATE sqlite_sequence SET seq = ? WHERE name = ?"
        newRecord = (41, 2)
        cur.execute(query, newRecord)
        print("OK: record updated")
except sqlite3.Error as error:
    print("Problem with simple query:", error)

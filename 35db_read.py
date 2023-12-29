#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

try:
    with con:
        cur = con.cursor()
        query = "SELECT * FROM tabulka01 ORDER BY id DESC LIMIT 10"
        result = cur.execute(query).fetchall()
        for row in result:
            print(row)
except sqlite3.Error as error:
    print("Problem with simple query:", error)

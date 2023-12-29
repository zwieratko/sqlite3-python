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
        query = "INSERT INTO tabulka01 VALUES(NULL, ?)"
        newRecord = (42,)
        cur.execute(query, newRecord)
        print("OK: simple record inserted")
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
except sqlite3.Error as error:
    print("Problem to insert:", error)

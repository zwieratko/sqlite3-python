#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableName = "t01"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)
else:
    try:
        with con:
            cur = con.cursor()
            query = "UPDATE {} SET col05 = ? WHERE id = ?".format(tableName)
            # query = "UPDATE sqlite_sequence SET seq = ? WHERE name = ?"
            newRecord = ("42", 7016)
            cur.execute(query, newRecord)
            print("OK: record updated")
    except sqlite3.Error as error:
        print("Problem with simple query:", error)

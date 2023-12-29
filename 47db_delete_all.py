#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db02.sqlite"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

# delete all record

try:
    with con:
        cur = con.cursor()
        tableNameStr = "tabulka01"
        query = "DELETE FROM {}".format(tableNameStr)
        cur.execute(query)
        print("OK: all records delted")
        query = "UPDATE sqlite_sequence SET seq = 0 WHERE name = ?"
        tableName = (tableNameStr,)
        cur.execute(query, tableName)
        print("OK: sqlite sequence updated")
except sqlite3.Error as error:
    print("Problem to delete all records!")

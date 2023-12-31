#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableName = "t01"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            query = """
                    CREATE TABLE {}(
                    id    INTEGER PRIMARY KEY AUTOINCREMENT,
                    col01 INTEGER NOT NULL,
                    col02 REAL,
                    col04 TEXT DEFAULT CURRENT_TIMESTAMP,
                    col05 BLOB
                    )""".format(tableName)
            cur.execute(query)
            print("Table created:", tableName)
    except sqlite3.Error as error:
        print("Problem to create table:", error)

#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"
tableName = "sqlite_sequence"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)
else:
    try:
        with con:
            cur = con.cursor()
            if (tableName == "sqlite_sequence"):
                query = "SELECT * FROM {} ".format(tableName)
            else:
                query = "SELECT * FROM {} ORDER BY id DESC LIMIT 20".format(
                    tableName)
            result = cur.execute(query).fetchall()
            print("Content of table {}:".format(tableName))
            for row in result:
                print(row)
    except sqlite3.Error as error:
        print("Problem with simple query:", error)
    else:
        cur.close()
        con.close()
        print("DB closed")

try:
    print(con.execute("PRAGMA database_list").fetchall())
except sqlite3.ProgrammingError as error:
    print(error)
except NameError as error:
    print("dbPath probably doesn't exists:", error)

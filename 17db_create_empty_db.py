#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db01.sqlite"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    con.close()
    print("OK: connection closed")

#!/usr/bin/env python

import os
import sqlite3

dbDir = "DBtesty/"
dbFile = "db01.sqlite"
dbPath = "{}{}".format(dbDir, dbFile)

try:
    os.makedirs(dbDir)
    print("DB directory created: {}".format(dbDir))
except FileExistsError:
    print("DB directory {} already exists".format(dbDir))

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    con.close()
    print("OK: connection closed")

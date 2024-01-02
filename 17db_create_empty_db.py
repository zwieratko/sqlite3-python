#!/usr/bin/env python

import os
import sqlite3

dbDir = "DBtesty/"
dbFile = "db01.sqlite"
dbPath = "{}{}".format(dbDir, dbFile)

try:
    os.makedirs(dbDir)
    print("OK: DB directory created - {}".format(dbDir))
except FileExistsError as error:
    print("NOK: {}".format(error))
except PermissionError as error:
    print("NOK: {}".format(error))
finally:
    try:
        con = sqlite3.connect(dbPath)
        print("OK: connected to {}".format(dbPath))
    except sqlite3.Error as error:
        print("NOK: {}".format(error))
    else:
        con.close()
        print("OK: connection closed")

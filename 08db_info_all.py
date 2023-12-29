#!/usr/bin/env python

import sqlite3
import os

# mem = sqlite3.connect(":memory:")
# db01 = "DBtesty/db01.sqlite"
# dbBk = "DBtesty/db01.bck"
# db02 = "DBtesty/db02.sqlite"
# db2B = "DBtesty/db02.bck"

dbDir = "DBtesty"


def complexInfo(dbPath):
    try:
        con = sqlite3.connect(dbPath)
        print("Connected to:", dbPath)
        with con:
            cur = con.cursor()
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            allTablesList = cur.execute(query).fetchall()
            print(allTablesList)
            for tableName in allTablesList:
                query = 'SELECT count(*) FROM {}'.format(tableName[0])
                recNum = cur.execute(query).fetchone()
                query = "SELECT * FROM PRAGMA_TABLE_INFO('{}');".format(
                    tableName[0])
                tableInfoList = cur.execute(query).fetchall()
                print("{}: totalColumn:{} / totalRows:{}".format(
                    tableName[0], len(tableInfoList), recNum[0]))
    except sqlite3.Error as error:
        print("Problem with DB: ", error)


# Information abou all DBs in 'dbDir'
# print("main:")
# print("---")
# complexInfo(db01)
# print("---")
# complexInfo(dbBk)
# print("---")
# complexInfo(db02)
# print("---")
# complexInfo(db2B)
# print("---")

if (not os.path.exists(dbDir)):
    print("Problem to find DB dir:", dbDir)
else:
    dbList = os.listdir(dbDir)
    for oneDB in dbList:
        dbFullPath = "{}/{}".format(dbDir, oneDB)
        complexInfo(dbPath=dbFullPath)
        print("---")

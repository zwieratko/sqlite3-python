#!/usr/bin/env python

import sqlite3
import random

dbPath = "DBtesty/db04.sqlite"
tableName = "t01"
totalRecords = 2


def generateRandomValues(tableInfo, totalRow):
    totalCol = len(tableInfo)
    return [tuple(random.random() for i in range(totalCol)) for x in range(totalRow)]


try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            query = "SELECT * FROM PRAGMA_TABLE_INFO('{}');".format(tableName)
            tableInfoList = cur.execute(query).fetchall()
            # for columnTuple in tableInfoList:
            #     print(columnTuple)
            questionMarksInQuery = ("?," * len(tableInfoList))[:-1]
            query = "INSERT INTO {} VALUES({})".format(
                tableName, questionMarksInQuery)
            cur.executemany(query, generateRandomValues(
                tableInfoList, totalRecords))
            print("Modified rows:", cur.rowcount)
    except sqlite3.Error as error:
        print("Problem to insert:", error)

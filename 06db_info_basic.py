#!/usr/bin/env python

import sqlite3
from prettytable import PrettyTable

dbPath = "DBtesty/db01.sqlite"
# tableName = "t01"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to", dbPath)
    print("---")
    print("")
except sqlite3.Error as error:
    print("Problem to connect to {}: {}".format(dbPath, error))
else:
    try:
        with con:
            cur = con.cursor()
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            allTablesList = cur.execute(query).fetchall()
            print("List of all tables in:", dbPath)
            print(allTablesList)
    except sqlite3.Error as error:
        print("Problem to gather list of tables:", error)
    else:
        if allTablesList:
            print("---")
            print("")

    try:
        with con:
            cur = con.cursor()
            for tableName in allTablesList:
                query = "SELECT * FROM PRAGMA_TABLE_INFO('{}');".format(
                    tableName[0])
                tableInfoList = cur.execute(query).fetchall()
                print("Information about each column in table:", tableName[0])
                columnInfoTable = PrettyTable()
                fieldNames = [
                    "Col.Nr", "Name", "Data type",
                    "NOT NULL", "Default val.", "Prim. key"
                ]
                columnInfoTable.field_names = fieldNames
                for columnInfo in tableInfoList:
                    # print(columnInfo)
                    columnInfoTable.add_row(columnInfo)
                print(columnInfoTable)
                print("")
    except sqlite3.Error as error:
        print("Problem to gather table info:", error)
    else:
        if allTablesList:
            print("---")
            print("")

    try:
        with con:
            cur = con.cursor()
            for tableName in allTablesList:
                query = "SELECT count(*) FROM {};".format(tableName[0])
                totalRecords = cur.execute(query).fetchall()
                print("Total records in table:", tableName[0])
                print(totalRecords)
    except sqlite3.Error as error:
        print("Problem to gather quantity of records in tables:", error)
    else:
        if allTablesList:
            print("---")
            print("")

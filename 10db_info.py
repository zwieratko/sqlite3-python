#!/usr/bin/env python

import sys
import sqlite3
from prettytable import PrettyTable

dbPath = "DBtesty/db01.sqlite"

print("Hello world!")
print(sys.version)
print("sqlite3.apilevel:", sqlite3.apilevel)
print("sqlite3.paramstyle:", sqlite3.paramstyle)
print("sqlite3.sqlite_version:", sqlite3.sqlite_version)
print("sqlite3.threadsafety:", sqlite3.threadsafety)
print("---")

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

# print(con.execute('SELECT SQLITE_VERSION()').fetchone())

try:
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        allTablesList = cur.execute(query).fetchall()
        print("OK")
        print("List of all tables in", dbPath, ":")
        print(allTablesList)
        for tableName in allTablesList:
            query = 'SELECT count(*) FROM {}'.format(tableName[0])
            recNum = cur.execute(query).fetchone()
            print(tableName[0], ":", recNum[0])
except sqlite3.Error as error:
    print("Problem to find all tables in DB")
# finally:
#     con.close()

# print(con.execute('SELECT SQLITE_VERSION()').fetchone())

if not allTablesList:
    print("DB has not any tables")
else:
    print("DB has some tables")
    try:
        with con:
            cur = con.cursor()
            for tableName in allTablesList:
                myTable = PrettyTable()
                print(tableName[0])
                if (tableName[0] == "sqlite_sequence"):
                    query = "SELECT * FROM {} LIMIT 8".format(tableName[0])
                else:
                    query = "SELECT * FROM {} ORDER BY id DESC LIMIT 3".format(
                        tableName[0])
                result = cur.execute(query).fetchall()
                fieldsNameResult = cur.description
                fieldsName = [item[0] for item in fieldsNameResult]
                myTable.field_names = fieldsName
                print(fieldsName)
                for row in result:
                    rowList = list(row)
                    myTable.add_row(rowList)
                    # for col in range(len(result[0])):
                    # print(fieldsName[col], ":", row[col])
                #         print(row[col], end=" ")
                #     print("")
                # print("")
                print(myTable)
    except sqlite3.Error as error:
        print("Problem with SQL query:", error)
    finally:
        con.close()

print("...end...")

#!/usr/bin/env python

import sqlite3

dbPath = "DBtesty/db02.sqlite"

try:
    con = sqlite3.connect(dbPath)
    print("OK: connected to:", dbPath)
except sqlite3.Error as error:
    print("Problem to connect to:", dbPath)

# delete last record

try:
    with con:
        cur = con.cursor()
        tableNameStr = "tabulka01"
        query = "SELECT * FROM {} ORDER BY id DESC LIMIT 1".format(
            tableNameStr)
        lastRecord = cur.execute(query).fetchone()
        if (lastRecord):
            lastRecordNum = lastRecord[0]
            print(lastRecord)
            query = "SELECT seq FROM sqlite_sequence WHERE name = ?"
            tableName = (tableNameStr,)
            maxRowId = cur.execute(query, tableName).fetchone()
            maxRowIdNum = maxRowId[0]
            print(maxRowId)
            query = "DELETE FROM {} WHERE id = ?".format(tableNameStr)
            cur.execute(query, maxRowId)
            print("OK: deleted last record")
            query = "UPDATE sqlite_sequence SET seq = ? WHERE name = ?"
            updateSequence = (maxRowIdNum - 1, tableNameStr)
            cur.execute(query, updateSequence)
            print("OK: sqlite sequence updated")
        else:
            print("there is no more records")
except sqlite3.Error as error:
    print("Problem with simple query:", error)

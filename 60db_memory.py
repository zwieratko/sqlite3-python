#!/usr/bin/env python

import sqlite3
import random
import time

start = time.time()

mem = sqlite3.connect(":memory:")
con = sqlite3.connect("DBtesty/db01.sqlite")
bck = sqlite3.connect("DBtesty/db01.bck")
tableName = "t01"

# Load real DB file to in-memory DB

try:
    with con:
        con.backup(mem)
        print("OK: db -> mem")
except sqlite3.Error as error:
    print("Problem with db -> mem: ", error)

# Update / change records in in-memory DB

try:
    with mem:
        cur = mem.cursor()
        query = "INSERT INTO {}(col01, col02) VALUES (?,?)".format(tableName)
        newRecords = []
        oneRecord = ()
        for iter in range(2):
            randomFloat = random.random()*100
            oneRecord = (iter + time.time_ns(), randomFloat,)
            newRecords.append(oneRecord)
        # print(type(newRecords))
        # print(type(newRecords[0]))
        cur.executemany(query, newRecords)
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
        mem.commit
except sqlite3.Error as error:
    print("Problem insert new records: ", error)

try:
    with mem:
        cur = mem.cursor()
        query = "SELECT * FROM {} ORDER BY id DESC LIMIT 1".format(tableName)
        result = cur.execute(query).fetchall()
        print(result)
except sqlite3.Error as error:
    print("Problem with simple query: ", error)

# In-memory DB backup to real DB file

try:
    with mem:
        mem.backup(con)
        print("OK: mem -> db")
except sqlite3.Error as error:
    print("Problem with mem -> db", error)

# Backup real DB file

try:
    with con:
        con.backup(bck)
        print("OK: db -> bck")
except sqlite3.Error as error:
    print("Problem with db -> bck: ", error)

end = time.time()
totalTime = end - start
print("---")
print(totalTime)

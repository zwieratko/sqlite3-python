#!/usr/bin/env python

import sqlite3
import time

totalRecords = 100000
totalTables = 4
mem = sqlite3.connect(":memory:")
print("OK: in-memory DB opened")

try:
    with mem:
        cur = mem.cursor()
        for tableNr in range(totalTables):
            query = """CREATE TABLE IF NOT EXISTS t{}(
                            id  INTEGER PRIMARY KEY,
                            num INTEGER
                        )""".format(tableNr)
            cur.execute(query)
        print("OK: {} tables created".format(totalTables))
except sqlite3.Error as error:
    print("Problem to create table:", error)
print("---")

# insertmany / no explicit transaction
start = time.time()
try:
    with mem:
        cur = mem.cursor()
        query = "INSERT INTO t0 VALUES(?, ?)"
        newRecords = [(x, x) for x in range(totalRecords)]
        cur.executemany(query, newRecords)
        print("OK: insertmany / no explicit transaction")
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
except sqlite3.Error as error:
    print("Problem to insert new records:", error)
end = time.time()
totalTime = end - start
print("Time:", round(totalTime, 5))
print("---")

# insertmany / with explicit transaction
start = time.time()
try:
    with mem:
        cur = mem.cursor()
        query = "INSERT INTO t1 VALUES(?, ?)"
        newRecords = [(x, x) for x in range(totalRecords)]
        cur.execute("BEGIN;")
        cur.executemany(query, newRecords)
        print("OK: insertmany / with explicit transaction")
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
        cur.execute("COMMIT;")
except sqlite3.Error as error:
    print("Problem to insert new records:", error)
end = time.time()
totalTime = end - start
print("Time:", round(totalTime, 5))
print("---")

# insertone / no explicit transaction
start = time.time()
try:
    with mem:
        cur = mem.cursor()
        query = "INSERT INTO t2 VALUES(?, ?)"
        # newRecords = [(x,x) for x in range(totalRecords)]
        for iteration in range(totalRecords):
            newRecord = (iteration, iteration)
            cur.execute(query, newRecord)
        print("OK: insertone / no explicit transaction")
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
except sqlite3.Error as error:
    print("Problem to insert new records:", error)
end = time.time()
totalTime = end - start
print("Time:", round(totalTime, 5))
print("---")

# insertone / with many explicit transaction
start = time.time()
try:
    with mem:
        cur = mem.cursor()
        query = "INSERT INTO t3 VALUES(?, ?)"
        # newRecords = [(x,x) for x in range(totalRecords)]
        for iteration in range(totalRecords):
            newRecord = (iteration, iteration)
            cur.execute("BEGIN;")
            cur.execute(query, newRecord)
            cur.execute("COMMIT;")
        print("OK: insertone / with many explicit transaction")
        print("Last rowid:", cur.lastrowid)
        print("Modified rows:", cur.rowcount)
except sqlite3.Error as error:
    print("Problem to insert new records:", error)
end = time.time()
totalTime = end - start
print("Time:", round(totalTime, 5))
print("---")

# show last records from all tables

try:
    with mem:
        cur = mem.cursor()
        for tableNr in range(totalTables):
            query = "SELECT * FROM t{} ORDER BY id DESC LIMIT 2".format(
                tableNr)
            result = cur.execute(query).fetchall()
            print(result)
except sqlite3.Error as error:
    print("Problem with simple query:", error)

print("...end...")

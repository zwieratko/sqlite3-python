#!/usr/bin/env python

import sqlite3
# import random
import time

mem = sqlite3.connect(":memory:")
print("OK: in-memory DB opened")

try:
    with mem:
        cur = mem.cursor()
        query = """CREATE TABLE IF NOT EXISTS t1(
                        num INTEGER UNIQUE,
                        id  INTEGER PRIMARY KEY AUTOINCREMENT
                    )"""
        cur.execute(query)
        print("OK: table created")
except sqlite3.Error as error:
    print("Problem to create table:", error)

start = time.time()

try:
    # mem = sqlite3.connect(":memory:")
    # print("OK: in-memory DB opened")
    with mem:
        cur = mem.cursor()
        query = """INSERT INTO t1 VALUES(?, NULL)"""
        newRecords = []
        for iter in range(100000):
            oneRecord = (iter, )
            newRecords.append(oneRecord)
        # cur.execute("BEGIN;")
        cur.executemany(query, newRecords)
        # cur.execute("COMMIT;")
        print("OK: records inserted")
        # cur.execute("BEGIN;")
        cur.execute(query, ("A",))
        # cur.execute("COMMIT;")
        print("OK: last records inserted")
except sqlite3.Error as error:
    print("Problem to insert records:", error)


end = time.time()
totalTime = end - start
print("---")
print(totalTime)
print("---")

try:
    with mem:
        cur = mem.cursor()
        query = """INSERT INTO t1 VALUES(?, NULL)"""
        cur.execute("BEGIN;")
        cur.execute(query, ("x",))
        cur.execute("COMMIT;")
        cur.execute(query, ("y",))
        cur.execute(query, ("z",))
        # if this line is uncommented, inserts 'y,z' will fail
        cur.execute(query, ("A",))
        print("OK: last records inserted")
except sqlite3.Error as error:
    print("Problem to insert records:", error)

print("---")

try:
    with mem:
        cur = mem.cursor()
        query = "SELECT * FROM t1 ORDER BY id DESC LIMIT 10"
        result = cur.execute(query).fetchall()
        for row in result:
            print(row)
except sqlite3.Error as error:
    print("Problem with simple query:", error)

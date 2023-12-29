#!/usr/bin/env python

import sqlite3

con = sqlite3.connect("DBtesty/db01.sqlite")
bck = sqlite3.connect("DBtesty/db01.bck")


def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')


try:
    with con:
        con.backup(bck, pages=1, progress=progress)
        print("OK: db -> bck")
except sqlite3.Error as error:
    print("Problem with db -> bck: ", error)

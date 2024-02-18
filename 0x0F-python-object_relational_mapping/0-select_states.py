#!/usr/bin/python3

import MySQLdb
from sys import argv
"""
a script that lists all states
from the database.
"""

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY ID ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

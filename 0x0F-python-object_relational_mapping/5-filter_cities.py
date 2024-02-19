#!/usr/bin/python3
'''
a script that lists all cities of a given state,
from the database 'hbtn_0e_4_usa'.
'''


import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''
    connect to db and get the states data.
    '''
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""
             SELECT cities.name
             FROM cities JOIN states
             ON cities.state_id = states.id
             WHERE states.name LIKE BINARY %s
             ORDER BY cities.id ASC
                """, (argv[4],))
    rows = cur.fetchall()
    ls = []
    if rows is not None:
        for row in rows:
            ls += row
        print(*ls, sep=", ")

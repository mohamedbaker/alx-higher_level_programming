#!/usr/bin/python3
'''
a script that lists all cities,
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
             SELECT cities.id, cities.name, states.name
             FROM cities JOIN states
             ON cities.state_id = states.id
             ORDER BY cities.id ASC
                """)
    rows = cur.fetchall()

    for row in rows:
        print(row)

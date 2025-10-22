#!/usr/bin/python3

"""This script lists all states from the database
that has been passed as a command line argument.

It imports the database using MySQLdb.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for item in cur.fetchall():
        print(item)

    cur.close()
    db.close()

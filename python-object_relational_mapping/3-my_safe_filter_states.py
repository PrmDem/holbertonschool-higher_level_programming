#!/usr/bin/python3

"""This script lists all states from the database
that fit the state name passed as a command line argument
And this time using 'format' is not mandatory,
and that makes our exe safe from injections!
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
    cur.execute("""SELECT * FROM states
                WHERE name = %s ORDER BY states.id ASC""", (sys.argv[4],))

    for item in cur.fetchall():
        print(item)

    cur.close()
    db.close()

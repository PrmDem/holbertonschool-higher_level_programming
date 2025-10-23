#!/usr/bin/python3

"""This script lists all cities from a given state
provided by the user via the command line.
Only the names are printed, and on a single line.
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
    cur.execute("SELECT cities.name FROM cities "
                "LEFT JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s", (sys.argv[4],))

    by_state = ", ".join(city[0] for city in cur.fetchall())
    print(by_state)

    cur.close()
    db.close()

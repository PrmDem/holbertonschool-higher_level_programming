#!/usr/bin/python3

"""This script lists all cities from db hbtn_0e_4_usa
with city id, city name, state name in that order
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
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities LEFT JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")

    for item in cur.fetchall():
        print(item)

    cur.close()
    db.close()

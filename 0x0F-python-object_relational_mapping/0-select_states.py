#!/usr/bin/python3
"""Lists states from database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)


def list_states(username, password, database):
    """lists states from database.
    Ags:
        username: mysql-username
        password: mysql-password
        database: mysql-database
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', \
            port=3306, \
            user=username, \
            passwd=password, \
            db=database)
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()


# Example usage
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

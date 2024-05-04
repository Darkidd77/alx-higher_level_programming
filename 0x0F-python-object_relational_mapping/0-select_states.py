#!/usr/bin/python3
"""Module lists states from mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """lists states from database.
    Ags:
        username: mysql-username
        password: mysql-password
        database: mysql-database
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = db.cursor()

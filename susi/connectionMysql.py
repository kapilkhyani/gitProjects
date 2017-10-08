#!/usr/bin/python
import pymysql

def getMysqlconnection():
    # Open database connection
    db = pymysql.connect("localhost", "root", "", "susi")

    # prepare a cursor object using cursor() method
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # cursor = db.cursor() # fetches as tuples
    return cursor

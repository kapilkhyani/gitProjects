#!/usr/bin/python
import os
import connectionMysql
import json
import start
from datetime import datetime
from time import mktime

def writeThought():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    x = input("Enter your thought \n")
    t = datetime.now()
    unix_secs = mktime(t.timetuple())
    unix_secs = int(unix_secs)
    query = "INSERT INTO thoughts(date, thought)  values("+str(unix_secs)+",'"+x+"')"
    newcursor.execute(query)
    start.clearSn()
    start.main()

def showThought():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    newcursor.execute("SELECT * from thoughts order by id desc limit 10 ")
    data = newcursor.fetchall()
    for tData in data:
        newStr = tData['thought'].replace('\n', '')
        print(str(tData['id'])+'\t'+newStr)
    print("\n")
    start.main()
#!/usr/bin/python
import os
import connectionMysql
import json
import start
from datetime import datetime
from time import mktime

def writeTask():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    x = raw_input("Enter your Task \n")
    tp = raw_input("Enter Task Priority \n")
    if tp=="":
        tp = 0
    t = datetime.now()
    unix_secs = mktime(t.timetuple())
    unix_secs = int(unix_secs)
    query = "INSERT INTO tasks(date, task,priority)  values("+str(unix_secs)+",'"+x+"',"+str(tp)+")"
    newcursor.execute(query)
    start.clearSn()
    start.main()

def showTask():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    newcursor.execute("SELECT * from tasks order by priority desc limit 10 ")
    data = newcursor.fetchall()
    for tData in data:
        newStr = tData['task'].replace('\n', '')
        print(str(tData['priority'])+'\t'+newStr)
    print("\n")
    start.main()
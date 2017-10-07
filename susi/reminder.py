#!/usr/bin/python
import os
import connectionMysql
import json
import start
from datetime import datetime
from time import mktime

def writeReminder():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    x = input("Enter your Reminder \n")
    tp = input("Enter Reminder Priority \n")
    if tp=="":
        tp = 0
    t = datetime.now()
    unix_secs = mktime(t.timetuple())
    unix_secs = int(unix_secs)
    query = "INSERT INTO reminders (date, reminder,priority)  values("+str(unix_secs)+",'"+x+"',"+str(tp)+")"
    newcursor.execute(query)
    start.clearSn()
    start.main()

def showReminder():
    start.clearSn()
    newcursor = connectionMysql.getMysqlconnection()
    newcursor.execute("SELECT * from reminders order by priority desc limit 10 ")
    data = newcursor.fetchall()
    for tData in data:
        newStr = tData['reminder'].replace('\n', '')
        print(str(tData['priority'])+'\t'+newStr)
    print("\n")
    start.main()
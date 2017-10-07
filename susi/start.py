#!/usr/bin/python
import os
import subprocess
import time
import datetime
from random import shuffle
import random
import sys
import connectionMysql
import json
import thought
import task
import reminder

def clearSn():
    os.system('clear')

def main():
    clearSn()
    newarr = ['Write thought',
              'Show Thoughts',
              'Write Task',
              'Show Task',
              'Write reminder',
              'Show Reminder'
              ]
    choiceStr = ''
    counterN = 0
    for i in newarr:
        counterN = counterN+1
        choiceStr = str(choiceStr)+"\n "+str(counterN)+' '+str(i)
    x = input("Enter your choice "+choiceStr+"\n")
    x = int(x)
    if x == 1:
        thought.writeThought()
    elif x == 2:
        thought.showThought()
    elif x == 3:
        task.writeTask()
    elif x == 4:
        task.showTask()
    elif x == 5:
        reminder.writeReminder()
    elif x == 6:
        reminder.showReminder()





if (__name__ == '__main__') : main()
#!/usr/bin/python
import os
import subprocess
import time
import datetime
from random import shuffle
import random


file = open("/home/pi/gitprojects/rebootScript/rebootOutput.txt","a")
y =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file.write("Executed at time"+y+"\n")
file.close()

x = input("Enter your choice")
print (x)


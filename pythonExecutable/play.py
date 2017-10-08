import os
import subprocess
import time
import datetime
from random import shuffle
import random
import play

dirNpath = "/home/pi/gitprojects/rasberryPiAlarm/";
dirpath = dirNpath+"/music"

def playMusic(newPair,ch):
    filename = newPair[ch]
    devnull = open(os.devnull, 'wb')
    # proc = subprocess.Popen("omxplayer " + dirpath + '/' + filename, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    filename = filename.replace(' ','\ ')
    # print("omxplayer " + dirpath + '/' + filename)
    os.system("omxplayer " + dirpath + '/' + filename +" &")
    time.sleep(2)
    os.system('clear')


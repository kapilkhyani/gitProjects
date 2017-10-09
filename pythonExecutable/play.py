import os
import subprocess
import time
import datetime
from random import shuffle
import random
import play
import argparse

dirNpath = "/home/pi/gitProjects/rasberryPiAlarm/";
dirpath = dirNpath+"/music"

def playMusic(newPair,ch):
    filenameOriginal = newPair[ch]
    devnull = open(os.devnull, 'wb')
    # proc = subprocess.Popen("omxplayer " + dirpath + '/' + filename, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    filename = filenameOriginal.replace(' ','\ ')
    # print("omxplayer " + dirpath + '/' + filename)
    os.system("omxplayer " + dirpath + '/' + filename +" &")
    time.sleep(2)
    os.system('clear')
    print ("Playing song "+str(filenameOriginal))

def getList():
    dirNpath = "/home/pi/gitProjects/rasberryPiAlarm";
    dirpath = dirNpath + "/music"
    alarmdir = os.listdir(dirpath)
    newPair = {k: v for k, v in enumerate(alarmdir)}
    return newPair

def playSelectedSong():
    # file = open("/home/pi/gitProjects/pythonExecutable/wwwOutput.txt", "a")
    # y = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # file.write("\n the time is " + y + "\n")

    newPair = getList()
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--number', help='user name', default='0')
    parser.add_argument('-k', '--killM', help='user name', default='0')
    results = parser.parse_args()
    number = int(results.number)
    killmusic =int(results.killM)
    if (number) :
        filenameOriginal = newPair[number]
        filename = filenameOriginal.replace(' ', '\ ')
        # os.system("/usr/bin/sudo /usr/bin/omxplayer --no-keys -o local " + dirpath + '/' + filename + " &")
        proc = subprocess.Popen("omxplayer " + dirpath + '/' + filename, shell=True)
    if (killmusic or 1):
        # file.write(" for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done")
        # file.close()
        proc = subprocess.Popen("for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done", shell=True)
        # os.system("")
        os.system("for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done")
        os.system("sudo ps -ef | grep omx | grep -v grep | awk '{print $2}' | xargs kill")
        os.system("/usr/bin/sudo /bin/ps -ef | /bin/grep omx | /bin/grep -v grep | /usr/bin/awk '{/usr/bin/print $2}' | /usr/bin/xargs /bin/kill")
        print("Came and executed New")



if __name__ == '__main__':
    playSelectedSong()

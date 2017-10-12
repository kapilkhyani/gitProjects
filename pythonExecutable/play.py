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
        xx = os.popen("sudo -S killall omxplayer.bin", 'w').write("sapna9889")
        os.system("kill -9 5127")
        print(xx)
        os.system("ps -ef | grep omxplayer.bin | grep -v grep | awk '{print $2}' > /home/pi/gitProjects/pythonExecutable/prid.txt")
        file = open("/home/pi/gitProjects/pythonExecutable/prid.txt", "r")
        for line in file:
            os.system("kill -9 "+str(line))

        exit()




if __name__ == '__main__':
    playSelectedSong()



# ----------------- FOR FUTURE HELP --------------------------------------------------------------









# proc = subprocess.Popen("for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done", shell=True)
# # os.system("")
# os.system('export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/pi/gitProjects/shellscripts:/home/pi/gitProjects/pythonExecutable:/home/pi/gitProjects/:/home/pi/gitProjects/susi"')
# os.system("for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done")
# os.system("sudo ps -ef | grep omxplayer.bin | grep -v grep | awk '{print $2}' | xargs kill")
# os.system("/usr/bin/sudo /bin/ps -ef | /bin/grep omx | /bin/grep -v grep | /usr/bin/awk '/usr/bin/print $2' | /usr/bin/xargs /bin/kill")
# os.system("sudo killall omxplayer.bin")
#
# os.system('''
# export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/pi/gitProjects/shellscripts:/home/pi/gitProjects/pythonExecutable:/home/pi/gitProjects/:/home/pi/gitProjects/susi"
# for pid in $(sudo ps -ef | grep omx | grep -v grep | awk '{print $2}'); do sudo kill -9 $pid; done
# sudo killall omxplayer.bin
# ''')
# print(xx)
# print("Came and executed New")
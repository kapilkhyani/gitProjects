#!/usr/bin/python
import os
import subprocess
import time
import datetime
from random import shuffle
import random


file = open("/home/pi/gitprojects/rasberryPiAlarm/cronOutput.txt","a")
y =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file.write("the time is "+y+"\n")


dirNpath = "/home/pi/gitprojects/rasberryPiAlarm/";
dirpath = dirNpath+"/music"
alarmdir = os.listdir(dirpath)
shuffle(alarmdir)
for files in alarmdir:
    if (files.endswith(".mp3") or files.endswith(".mp4")):
        command1 = 'omxplayer '+dirpath+'/'+files
        file.write("\t command executed : "+command1+"\n")
        # os.system('omxplayer '+dirpath+'/'+files)
        proc = subprocess.Popen("omxplayer " +dirpath+'/'+files, shell=True)
        ranNumber = random.randint(22, 28)*10
        time.sleep(ranNumber)
        os.system("sudo ps -ef | grep omx | grep -v grep | awk '{print $2}' | xargs kill")


file.close()
exit()
# os.system('omxplayer /home/pi/Downloads/music/omChant.mp4')
# proc = subprocess.Popen("omChant", shell=True)
# exit();
# print(os.getcwd())
#
#     if(files.endswith(".mp3")):
#         print(files)
#         files = files.replace(" ", "\ ")
#         proc = subprocess.Popen("omxplayer "+files, shell=True)
#         pid = proc.pid
#         time.sleep(10)
#         id = os.system("pgrep omxplayer")
#         os.system("killall omxplayer.bin ")
#         time.sleep(3)




# exit()


# pid = proc.pid
# time.sleep(50)
# proc.kill()
# print(pid)
# id = os.system("pgrep omxplayer")
# print('ID of omx = '+str(id))
# print(id)
# time.sleep(50)
# print(os.getpid("omx"))
#os.system("kill "+str(id))
#os.system("omxplayer Kuch\ kar\ gujarne\ ka.mp3 &")



#raw_input()

# proc = subprocess.Popen("omxplayer Kuch\ kar\ gujarne\ ka.mp3", shell=True)
# time.sleep(5)
# print(proc.pid)
# proc.kill()
# proc.terminate()
# id = os.system("pgrep omxplayer")
# os.system("kill "+str(id))


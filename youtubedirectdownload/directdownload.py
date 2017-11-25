import os
import pymysql


# myList=[1,2,3,4,5,6]
# print(myList)
#
# print(myList[3])
# for e in myList:
#     print(e)

def getMysqlconnection():
    # Open database connection
    db = pymysql.connect("localhost", "root", "", "susi",autocommit=True)

    # prepare a cursor object using cursor() method
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # cursor = db.cursor() # fetches as tuples
    return cursor

myDict = {"KalaChasma": "https://www.youtube.com/watch?v=k4yXQkG2s1E",
          "DhunKiLAge": "https://www.youtube.com/watch?v=etPRKWWji0Y"}
mydir = os.getcwd()

for key in myDict:
    value = myDict[key]
    #executingSting ='youtube-dl -o '+key+'.webm "'+value+'" --extract-audio --prefer-avconv --audio-format  mp3'
    #print(executingSting)
    #os.system(executingSting)

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

os.system("cd /home/pi/gitProjects/youtubedirectdownload/")
os.system("git pull")


with open(mydir+'/youtubevideos.txt','r') as f:
    lines = f.readlines()

# os.system("cd /home/pi/gitProjects/rasberryPiAlarm/music/")

for n in lines:
    spl =  n.split('@@@@')
    key1 = spl[1]
    value1 = spl[0]
    key1 = key1.replace("\n", "")
    # key1 = key1.replace(" ", "\ ")
    executingSting ='youtube-dl -o "/home/pi/gitProjects/rasberryPiAlarm/music/'+key1+'.webm " "'+value1+'" --extract-audio --prefer-avconv --audio-format  mp3'
    newcursor = getMysqlconnection()
    query = "SELECT COUNT(1) as cnt FROM songlist WHERE song = '"+value1+"'"
    newcursor.execute(query)
    data = newcursor.fetchone()
    CNT = data['cnt']
    newcursor.close()
    # print(executingSting)
    if CNT == 0:
        os.system(executingSting)
        query2 = "INSERT INTO songlist ( song ) values ('"+value1+"')"
        newcursor2 = getMysqlconnection()
        newcursor2.execute(query2)

#raw_input()


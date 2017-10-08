import os
myList=[1,2,3,4,5,6]
print(myList)

print(myList[3])
for e in myList:
    print(e)

myDict = {"KalaChasma": "https://www.youtube.com/watch?v=k4yXQkG2s1E",
          "DhunKiLAge": "https://www.youtube.com/watch?v=etPRKWWji0Y"}
mydir = os.getcwd()
print(mydir)
for key in myDict:
    value = myDict[key]
    #executingSting ='youtube-dl -o '+key+'.webm "'+value+'" --extract-audio --prefer-avconv --audio-format  mp3'
    #print(executingSting)
    #os.system(executingSting)

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in '%s': %s" % (cwd, files))

#text_file = open("youtubevideos.txt", "r")
#lines = text_file.readlines()
#print(lines)

with open(mydir+'/youtubevideos.txt','r') as f:
    lines = f.readlines()

for n in lines:
    spl =  n.split('@@@@')
    key1 = spl[1]
    value1 = spl[0]
    key1 = key1.replace("\n", "")
    key1 = key1.replace(" ", "\ ")
    executingSting ='youtube-dl -o '+key1+'.webm "'+value1+'" --extract-audio --prefer-avconv --audio-format  mp3'
    print(executingSting)
    os.system(executingSting)


#raw_input()


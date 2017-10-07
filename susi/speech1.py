#!/usr/bin/python
import os
import connectionMysql
import json
import start
from datetime import datetime
from time import mktime
# import pyttsx
from gtts import gTTS

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Sir please select from choices");
engine.setProperty('rate',50)
engine.runAndWait();

# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()

tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
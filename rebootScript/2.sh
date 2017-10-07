#!/bin/bash



echo "Now date " $(date)  >> /home/pi/gitprojects/rebootScript/shellOutput.txt


sudo lxterminal terminal --working-directory=/home/pi/gitprojects/rebootScript/ 

echo "Now date again" $(date)  >> /home/pi/gitprojects/rebootScript/shellOutput.txt

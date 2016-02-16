#!/bin/bash

echo "stopping xbmc" > /home/xbian/test
sudo service xbmc stop
echo "starting emulationstation" >> /home/xbian/test
emulationstation
echo "starting xbmc" >> /home/xbian/test
sudo service xbmc start
echo "end" >> /home/xbian/test



#!/bin/bash

sudo service xbmc stop
script -c "emulationstation" /dev/null
sudo service xbmc start



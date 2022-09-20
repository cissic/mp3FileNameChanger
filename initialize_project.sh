#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip3 install mp3-tagger # no sudo! otherwise package will be installed in / 

python3 -m venv venv

# sudo pip3 install spyder-kernels # if you want to develop in Spyder

python3 script.py

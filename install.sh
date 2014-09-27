#/bin/bash

sudo apt-get install xclip xsel python-pip
chmod 777 gistit.py
sudo mv gistit.py /usr/bin/gistit
echo "/usr/bin/gistit" >> ~/.xbindkeysrc
echo "  control + Mod1 + c" >> ~/.xbindkeysrc
xbindkeys

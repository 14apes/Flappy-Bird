#!/bin/bash
sudo apt-get install --yes python3 python3-pip
# use python3 and pip3
pip3 install virtualenv
if [ -d .fbVE ];then
    echo "virtualenv folder already created";
else
    virtualenv -p /usr/bin/python3 .fbVE/
fi
source .fbVE/bin/activate
pip install -r requirements.txt
echo "Installation Done"
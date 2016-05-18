#!/bin/bash

MYSQL_ROOT_PASSWORD=password

sudo apt-get -y update

sudo apt-get -y install python python-pip python-dev
sudo apt-get -y install sqlite3 tmux

sudo pip install -r requirements.txt

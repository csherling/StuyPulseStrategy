#!/bin/bash

MYSQL_ROOT_PASSWORD=password

sudo apt-get -y update

sudo apt-get -y install python python-pip python-dev
sudo apt-get -y install libmysqlclient-dev mysql-server

sudo pip install -r requirements.txt

sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD"

mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "CREATE DATABASE strategy;"

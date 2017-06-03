#/bin/bash
#install python, pip and virtualenv
sudo apt install python-minimal    
sudo apt install python-pip
sudo pip install virtualenv

#install sqlite
sudo apt install sqlite

#create virtual environment
virtualenv venv
source venv/bin/activate

#get flask and other components
pip install flask
#pip install sqlalchemy

#prepare database
sqlite3 service.db 'create table counter (domain string primary key, cnt int);'

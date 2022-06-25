#!/bin/sh

#kill all existing tmux sessions
tmux kill-server

#cd into project folder 
cd project-22-SUM-24-CAROLINE

#make sure ou have latest upates of git repository
#git fetch && git reset origin/main --hard

#enter python virtual environemnt & install dependencies 
source python3-virtualenv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=“development”

#start new detatched tmux session that goes to the project directory, 
#enters the python virtual environment 
#starts the Flask server.

#dnf install tmux #dont know if i need this 
#tmux new #dont know if i need this 
source python3-virtualenv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=“development”
tmux new-session -d -s portfolio_session 'flask run --host=0.0.0.0'
flask run
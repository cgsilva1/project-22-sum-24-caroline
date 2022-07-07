#!/bin/sh

#cd into project folder 
cd project-22-sum-24-caroline

#make sure ou have latest upates of git repository
git fetch && git reset origin/main --hard

#enter python virtual environemnt & install dependencies 
    #source python3-virtualenv/bin/activate
    #pip install -r requirements.txt
    #export FLASK_ENV=“development”

#spin containers down to prevent out of memory issues on our VPS instances when building in the next step
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

#Restart myportfolio service 
#systemctl daemon-reload
#systemctl restart myportfolio 


flask run --host=0.0.0.0

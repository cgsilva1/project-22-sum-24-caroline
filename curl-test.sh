#!/bin/sh

#POST endpoint request
curl --request POST http://localhost:5000/api/timeline_post -d 'name=Caroline&email=cgsilva@usc.edu&content=Just Added Database to my portfolio site!'
curl -X POST http://localhost:5000/api/timeline_post -d 'name=Caroline&email=cgsilva@usc.edu&content=Testing my endpoints with postman and curl.'

#see timeline posts 
curl http://localhost:5000/api/timeline_post

#create random timeline post using POST endpoint
#check GET endpoint to make sure it was added 

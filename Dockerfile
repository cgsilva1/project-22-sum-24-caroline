#choosing a python image as the base image 
FROM python:3.9-slim-buster
#FROM quay.io/centos/centos:stream8

#installing python
#RUN dnf install -y python3.9

#spcifying the directory
WORKDIR /myportfolio

#copy requirements.txt into the container image which improves caching 
COPY requirements.txt .
#COPY . .

#instal dependencies
RUN pip3 install -r requirements.txt

#copy all project files into the container image
COPY . .

#runs when a container is created from this image
CMD ["flask", "run", "--host=0.0.0.0"]

#spcify the port
EXPOSE 5000
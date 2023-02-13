FROM python:3.7-alpine
RUN sudo apt-get update
RUN sudo apt-get install git-all
RUN sudo apt install unixodbc-dev
RUN sudo apt install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

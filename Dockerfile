FROM python:3.7

# App setup
ADD . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8080

# Requirements installation
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# pull official base image
FROM python:3.9.6-slim-buster
# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# install system dependencies
RUN apt-get update \
&& apt-get -y install netcat gcc sqlite\
&& apt-get clean
# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY . .
# run entrypoint.sh
CMD ["python","app.py"]
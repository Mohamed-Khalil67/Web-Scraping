# pull official base image
FROM python:3.9.6-slim-buster
# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY . /usr/src/app/
# add entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# Embedding Sqlite into docker container
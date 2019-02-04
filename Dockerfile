# Use an official Python runtime as an image
FROM python:3.5

## make a local directory
RUN mkdir /flask_app

# set "flask_app" as the working directory from which CMD, RUN, ADD references
WORKDIR /flask_app

# now copy all the files in this directory to /flask_app
ADD . /flask_app

# install mysql-client
RUN apt-get update && apt-get install --no-install-recommends -y mysql-client

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
ENTRYPOINT /flask_app/entrypoint.sh




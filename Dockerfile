# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM ubuntu:18.04
WORKDIR /rest-server
ARG DEBIAN_FRONTEND=noninteractive

ADD rest-server.py .
ADD config.py .
ADD StorageClient.py .
ADD DatabaseClient.py .
ADD energyusageapplication-5cee0fdad987.json .


# Install any necessary dependencies
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y postgresql
RUN apt-get install -y python-psycopg2
RUN apt-get install -y libpq-dev

RUN pip3 install flask
RUN pip3 install gcloud
RUN pip3 install psycopg2
RUN pip3 install requests
RUN pip3 install jsonpickle

# Open port 5000 for serving the webpage
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "rest-server.py"]
FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

ADD worker-startup.sh .
ADD StorageClient.py .
ADD DatabaseClient.py .
ADD energyusageapplication-5cee0fdad987.json .

# Install any necessary dependencies
RUN apt-get update

RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y postgresql

RUN pip3 install pika
RUN pip3 install flask
RUN pip3 install gcloud
RUN pip3 install psycopg2
RUN pip3 install requests
RUN pip3 install jsonpickle

ADD worker.py .
ADD config.py .
ADD worker-startup.sh .

# Run worker startup script when the container launches
CMD ["python3", "worker.py"]
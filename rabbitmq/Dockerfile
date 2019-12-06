FROM rabbitmq

# Define environment variables.
ENV RABBITMQ_USER jon
ENV RABBITMQ_PASSWORD lab7

ADD init.sh /init.sh
EXPOSE 5672

# Define default command
RUN chmod 777 /init.sh
CMD ./init.sh
#!/bin/sh

# Create Rabbitmq user
sleep 2
bash -c "echo loopback_users=none > /etc/rabbitmq/rabbitmq.conf"
rabbitmqctl add_user jon lab7
rabbitmqctl set_user_tags jon administrator
rabbitmqctl set_permissions -p / jon  ".*" ".*" ".*"

echo "*** User 'jon' with password 'lab7' completed. ***" ; \
echo "*** Log in the WebUI at port 15672 (example: http:/localhost:15672) ***"

# $@ is used to pass arguments to the rabbitmq-server command.
# For example if you use it like this: docker run -d rabbitmq arg1 arg2,
# it will be as you run in the container rabbitmq-server arg1 arg2
rabbitmq-server $@
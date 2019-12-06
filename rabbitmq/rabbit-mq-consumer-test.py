import pika

credentials = pika.PlainCredentials(username="guest", password="guest")
connection = pika.BlockingConnection(pika.ConnectionParameters('35.247.62.142', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='toWorker')


def callback(ch, method, properties, body):
	print("Message Received: {}".format(body.decode('utf-8')))


channel.basic_consume(queue='toWorker', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
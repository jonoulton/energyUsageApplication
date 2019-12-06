import pika
import subprocess

credentials = pika.PlainCredentials(username="guest", password="guest")
connection = pika.BlockingConnection(pika.ConnectionParameters("35.247.62.142", port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='toWorker')

routing_key = "#.testPublish.info"

whoami = subprocess.run("whoami", stdout=subprocess.PIPE)
whoami = whoami.stdout.decode("utf-8").strip()

channel.basic_publish(exchange='', routing_key='toWorker', body='Producer Test')
print(" [x] Sent 'Producer Test!'")
connection.close()

from Database.DatabaseClient import DatabaseClient
from Storage.StorageClient import StorageClient
import jsonpickle
import config
import random
import pika

databaseClient = DatabaseClient()
storageClient = StorageClient()


def establish_rabbitmq_toWorker_connection():
	credentials = pika.PlainCredentials(username="guest", password="guest")
	connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBITMQ_ADDRESS, port=5672, credentials=credentials))
	channel = connection.channel()
	channel.queue_declare(queue='toWorker')
	return channel


def send_data_to_storage(jsonDataDict):
	try:
		print("Using StorageClient object to upload file")
		storageClient.upload_from_dict(jsonDataDict)
		print("Storage upload was successful")

	except Exception as e:
		print("Data was not successfully uploaded to storage")
		print("Exception: {}".format(e))
		return -1
	return 0


def send_data_to_database(jsonDataDict):
	try:
		# Store the data in a GCP database
		print("Using DatabaseClient object to upload data to database")
		databaseClient.add_data_from_dict(jsonDataDict)
		print("Database upload was successful")

	except Exception as e:
		print("Data was not successfully uploaded to database")
		print("Exception: {}".format(e))
		return -1
	return 0


def spin():
	sorted([random.randint(0,1000000) for _ in range(10000)])


def actions_POST(dataDict):
	send_data_to_storage(dataDict)
	send_data_to_database(dataDict)
	spin()


def actions_GET():
	raise NotImplementedError("The GET function has not been implemented yet")


def callback(ch, method, properties, body):
	# Decode the message
	body = jsonpickle.decode(body)

	# POST Request
	if body['method'] == "POST":
		actions_POST(body['jsonDataDict'])

	# GET Request
	if body['method'] == "GET":
		actions_GET()

	ch.basic_ack(delivery_tag=method.delivery_tag)


def consume():
	workerChannel.basic_consume(queue='toWorker', on_message_callback=callback)
	print(' [*] Waiting for messages. To exit press CTRL+C')
	workerChannel.start_consuming()


workerChannel = establish_rabbitmq_toWorker_connection()
logsChannel = None

consume()

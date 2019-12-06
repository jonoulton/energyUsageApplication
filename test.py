from Database.DatabaseClient import DatabaseClient

res = DatabaseClient().get_all_data_from_database()

for item in res:
	try:
		print("{}: {}".format(item, res[item][0]))
	except:
		print("{}: []".format(item))
for item in res:
	print(len(res[item]))

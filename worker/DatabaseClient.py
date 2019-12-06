import config
import psycopg2


class DatabaseClient:
	def __init__(self, host=config.DB_ADDRESS):
		self.dbname = config.DB_NAME
		self.user = config.DB_USER
		self.password = config.DB_PASSWORD
		self.host = host
		self.connection = psycopg2.connect(dbname=self.dbname,
										   user=self.user,
										   password=self.password,
										   host=self.host)
		self.cursor = self.connection.cursor()
		self.tables = ["gas", "electric", "solar", "wind"]

	def get_list_of_tables(self):
		"""
		Get the list of tables
		:return: List of Strings
		"""
		self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
		return [table[0] for table in self.cursor.fetchall()]

	def print_tables_names(self):
		"""
		Print the list of tables that are currently in the database
		:return: None
		"""
		print("Relation Names: {}".format(self.get_list_of_tables()))

	def drop_all_tables(self):
		"""
		Destroys all tables and all the data within them
		:return: None
		"""
		drop_table_command = """
		DROP TABLE IF EXISTS {} CASCADE;
		"""
		for table in self.get_list_of_tables():
			self.cursor.execute(drop_table_command.format(table))
		self.connection.commit()

	def create_database_tables(self):
		"""
		Delete the existing tables and recreate them
		:return: None
		"""
		make_tables_command = """
		DROP TABLE IF EXISTS electric CASCADE;
		CREATE TABLE electric (
			electric_id SERIAL UNIQUE NOT NULL,
			usage INT NOT NULL,
			dt TIMESTAMP NOT NULL,
			PRIMARY KEY(electric_id)
		);

		DROP TABLE IF EXISTS gas CASCADE;
		CREATE TABLE gas (
			gas_id SERIAL UNIQUE NOT NULL,
			usage INT NOT NULL,
			dt TIMESTAMP NOT NULL,
			PRIMARY KEY(gas_id)
		);

		DROP TABLE IF EXISTS wind CASCADE;
		CREATE TABLE wind (
			wind_id SERIAL UNIQUE NOT NULL,
			usage INT NOT NULL,
			dt TIMESTAMP NOT NULL,
			PRIMARY KEY(wind_id)
		);

		DROP TABLE IF EXISTS solar CASCADE;
		CREATE TABLE solar (
			solar_id SERIAL UNIQUE NOT NULL,
			usage INT NOT NULL,
			dt TIMESTAMP NOT NULL,
			PRIMARY KEY(solar_id)
		);
		"""
		self.cursor.execute(make_tables_command)
		self.connection.commit()

	def reset_database(self):
		self.drop_all_tables()
		self.create_database_tables()

	def add_data_from_dict(self, dataDict):
		"""
		Adds data to the database from a dictionary
		:param dataDict: dictionary of data to be added to the database
		:return: Int. 1 on success, -1 on failure
		"""
		fields = ["type", "usage", "dt"]
		for field in fields:
			if field not in dataDict:
				print("{} not in dataDict and is a required field".format(field))
				return -1

		postgres_insert_query = "INSERT INTO {} (usage, dt) VALUES (%s, TO_TIMESTAMP(%s, 'HH24:MI MM/DD/YYYY'))".format(dataDict['type'])
		record_to_insert = (dataDict['usage'], dataDict['dt'])
		self.cursor.execute(postgres_insert_query, record_to_insert)
		self.connection.commit()
		return 1

	def get_data_from_table(self, table, col="*"):
		"""
		Print the data from a relation in the database
		:param table: The name of the table
		:param col (optional): The name of the column to print data from
		:return: None
		"""
		postgres_select_query = "SELECT {} FROM {}".format(col, table)
		self.cursor.execute(postgres_select_query)
		resultList = []
		try:
			for row in self.cursor.fetchall():
				resultList.append([row[1], row[2]])
			return resultList
		except Exception as e:
			print("Exception encountered while parsing results of {}".format(table))
			return []

	def get_all_data_from_database(self):
		resultDict = {}
		for table in self.tables:
			resultDict[table] = self.get_data_from_table(table)
		return resultDict

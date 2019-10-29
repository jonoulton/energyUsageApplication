#! /Users/jon/anaconda3/bin/python3

"""
This file tests the functionality of the DatabaseClient class
It performs the following actions

"""

import random
from Database.DatabaseClient import DatabaseClient

dbClient = DatabaseClient()

print("Resetting the database")
dbClient.reset_database()

print("Adding some data")
dataDict = dict()
types = ["electric", "gas", "wind", "solar"]
datetime = "12:00 10/21/19",
usages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dataDict['type'] = 'electric'

for i in range(100):
    dataDict[i] = dict()
    dataDict[i]['type'] = random.choice(types)
    dataDict[i]['dt'] = datetime
    dataDict[i]['usage'] = random.choice(usages)
    dbClient.add_data_from_dict(dataDict[i])
print("Data has been added")
print()
for type in types:
    print("Data from {}:".format(type))
    dbClient.get_data_from_table(type)
    print()
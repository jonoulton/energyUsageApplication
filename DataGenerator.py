import scipy.stats as stats
import numpy as np

"""
Example Data:

"data0": {
"type": "electric",
"dt": "23:00 10/21/19",
"usage": 25
}

types: electric, gas, wind, solar
dt: hh:mm MM/DD/YY

~~~~~~~

Class DataGenerator Functionality:
	Should be able to generate a json data package

Datetime Range: 1 day?
1 submission per second
1440 minutes in a day

Returns a list of dictionaries that can be sent to the server

Current Ranges:
Electric: 350 - 600
Gas: 0 - 400
Solar: 0 - 400
Wind: 0 - 400
"""


class DataGenerator:
	def __init__(self):
		self.whatever = None
		self.datetimeRange = []
		self.generate_datetimes()
		self.numDataPoints = 1440
		self.dictFormat = {
			"type": None,
			"dt": None,
			"usage": None
		}
		self.returnList = []

	def generate_datetimes(self):
		for hour in range(24):
			for minute in range(60):
				self.datetimeRange.append("{:02d}:{:02d} 12/1/19".format(hour, minute))

	def generate_return_dict(self, dataType, dt, num):
		dataDict = {}
		for item in self.dictFormat:
			dataDict[item] = None
		dataDict["type"] = dataType
		dataDict["dt"] = dt
		dataDict['usage'] = int(num)
		return dataDict

	def append_data_to_return_list(self, vals, dataType):
		for item in range(self.numDataPoints):
			dataDict = self.generate_return_dict(dataType, self.datetimeRange[item], vals[item])
			self.returnList.append(dataDict)

	def generate_solar(self):
		# Uses a normal distribution
		vals = stats.norm.pdf(sorted(stats.norm.rvs(size=self.numDataPoints)))*1000
		self.append_data_to_return_list(vals, "solar")

	def generate_gas(self):
		# Uses an inverse normal distribution
		vals = list(map(lambda x: -(x-1)*1000-600, stats.norm.pdf(sorted(stats.norm.rvs(size=self.numDataPoints)))))
		self.append_data_to_return_list(vals, "gas")

	def generate_electric(self):
		# Uses a normal distribution
		vals = stats.norm.pdf(sorted(stats.semicircular.rvs(size=self.numDataPoints)))*1500
		self.append_data_to_return_list(vals, "gas")

	def generate_wind(self):
		# Uses a normal distribution
		vals = stats.norm.pdf(sorted(stats.alpha.rvs(a=.01, size=self.numDataPoints))) * 1000
		vals = [vals[(i + 500) % len(vals)] for i, x in enumerate(vals)]
		self.append_data_to_return_list(vals, "gas")

	def generate_all_data(self):
		self.generate_electric()
		self.generate_solar()
		self.generate_wind()
		self.generate_gas()
		return self.returnList
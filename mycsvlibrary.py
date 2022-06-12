def popuCSV(precipitation,temp_max,temp_min,wind,weather):
	import csv
	from datetime import date

	# list of column names
	field_names = ['date','precipitation','temp_max','temp_min','wind','weather']

	# Dictionary
	today = date.today()
	memo={'date':today,'precipitation':precipitation,'temp_max':temp_max,'temp_min':temp_min,'wind':wind,'weather':weather}
	
	f_object = csv.writer(open('seattle-weather.csv','a'))
	f_object.writerow([memo['date'],memo['precipitation'],memo['temp_max'],memo['temp_min'],memo['wind'],memo['weather']])

	# Open your CSV file in append mode
	# Create a file object for this file
	'''
	with open('E:\weather_project\seattle-weather.csv', 'a') as f_object:
		
		# Pass the file object and a list
		# of column names to DictWriter()
		# You will get a object of DictWriter
		dictwriter_object = DictWriter(f_object, fieldnames=field_names)

		#Pass the dictionary as an argument to the Writerow()
		dictwriter_object.writerow(dict)

		#Close the file object
		f_object.close()
	'''


def start_learning():
	import random_forest
	return random_forest.accuracy()

popuCSV(12.5,1.7,-2.8,5,4)

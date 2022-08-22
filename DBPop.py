import time
from mycsvlibrary import popuCSV,start_learning

# WEB-FRAMEWORK FOR INSERTION
from bottle import *

@route('/')
def index():
	return template('edit_task')

#'date','precipitation','temp_max','temp_min','wind','weather'

@route('/login')
def login():
	return template('input_box')

@route('/login', method='POST')
def do_login():
	precipitation = request.forms.get('precipitation')
	temp_max = request.forms.get('temp_max')
	temp_min = request.forms.get('temp_min')
	wind = request.forms.get('wind')
	weather = request.forms.get('weather')
	# FETCHING THE POST REQUEST BEAN
	try:
		popuCSV(precipitation,temp_max,temp_min,wind,weather)		
		#return template('success')
	except:
		return "<p>File Write Error</p>"
	finally:
		output_of_model = str(start_learning(precipitation,temp_max,temp_min,wind,weather))
		formhtml = "<h1>weather is ",output_of_model,"</h1>"
		
		if output_of_model=="sunny":
			return template('sunny.html')
			
		elif output_of_model=="rainy/cloudy":
			return template('cloudy.html')
			
		elif output_of_model=="drizzle":
			return template('drizzle.html')
			
		elif output_of_model=="snowy":
			return template('snowy.html')
			
		elif output_of_model=="foggy'":
			return template('foggy.html')
									
		else:
			return formhtml

os.system('START http://localhost:45000')
run(host='0.0.0.0', port=45000, debug = True)









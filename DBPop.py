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
	return '''
		<h2> Rupak Weather Portal </h2>
		<form action="/login" method="post">
		<fieldset>
		<legend> Update Timings: </legend><br>
						
			Precipitation: <input name="precipitation" type="text" placeholder="numeric values" /><br>
			Max Temperature: <input name="temp_max" type="text" /><br>
			Min Temperature: <input name="temp_min" type="text" /><br>
			Wind: <input name="wind" type="text" /><br>
			Weather: <input name="weather" type="text" /><br>

			<input value="Update" type="submit" />
		</fieldset>
		</form>

		
	'''

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
		output_of_model = str(start_learning())
		formhtml = "<h1>weather is ",output_of_model,"</h1>"
		return formhtml

os.system('START http://localhost:45000')
run(host='0.0.0.0', port=45000, debug = True)









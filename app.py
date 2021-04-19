# import Flask Dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)
# __name__ variable : magic methods in Python
	# denotes the name of the current function
	# use __name__ to determine if code is being run from command line or imported into another piece of code 

# Create Flask Routes
# Define the starting point (root):
@app.route('/')
	# NOTE: forward slash denotes that we want to put our data at the root of our routes
		# Foward slash commonly known as the highest level of hierachy in any computer system

# Create a function called hello_world() - Put code for specific route below @app.route every time Flask route is made
@app.route('/')
def hello_world():
	return 'Hello word'

# Run a Flask App
# 1. Need to use the Anaconda Powershell cmd line to navigate to folder where code is saved
	# NOTE: Environment variables are dynamic; used to modify the way a certain aspect of the computer operates
	# NOTE: `FLASK_APP` env.var : Want to modify the path that will run our `app.py` file -> to run our file
		# set FLASK_APP=app.py`
		# flask run
# IMPORTANT: local Host address and port number: 
	# NOTE: Running on http://127.0.0.1:5000/
# 2. Copy and paste localhost address into web browser
	# localhost:5000



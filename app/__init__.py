from flask import Flask, jsonify
import os

# instantiate app
app = Flask(__name__)

# pull in environment vars
app_settings = os.getenv('APP_SETTINGS')
# set config from config file (config.py)
app.config.from_object('app.config.DevelopmentConfig')

@app.route('/ping', methods=['GET'])
def ping_test():
	return jsonify({
		'status': 'success',
		'message': 'hello world'	
	})

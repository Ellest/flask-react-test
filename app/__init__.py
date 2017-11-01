from flask import Flask, jsonify

# instantiate app
app = Flask(__name__)

# set config from config file (config.py)
app.config.from_object('app.config.DevelopmentConfig')

@app.route('/ping', methods=['GET'])
def ping_test():
	return jsonify({
		'status': 'success',
		'message': 'hello world'	
	})
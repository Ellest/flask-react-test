from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from models import db, User

# instantiate app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db.init_app(app)
db.creat_all(app=app)

# routes

@app.route('/ping', methods=['GET'])
def ping_test():
	return jsonify({
		'status': 'success',
		'message': 'hello world'	
	})

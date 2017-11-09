from flask import Flask
from flask_script import Manager
from project import app, db

manager = Manager(app)

# Registers a new command so that we can run it from the command line
# Option to be used if we start considering Docker for deployment

@manager.command
def recreate_db():
	# Recreates a DB. 
	db.drop_all()
	db.create_all()
	db.session.commit()

if __name__ == '__main__':
	manager.run()
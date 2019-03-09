# app/__init__.py

# Third-party imports
from flask import Flask
from celery import Celery

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


import os

# local imports
from _config import app_config

# DB variable initialization
db = SQLAlchemy()
# Login Manager Initialization 
login_manager = LoginManager()


def make_celery(app):
	global celery

	celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
					broker=app.config['CELERY_BROKER_URL'], event_queue_expires=10)
	celery.conf.update(app.config)

	TaskBase = celery.Task
	class ContextTask(TaskBase):
		abstract = True
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return TaskBase.__call__(self, *args, **kwargs)
	celery.Task = ContextTask

	return celery



def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True, static_folder = './static')
	app.config.from_object(app_config[config_name.upper()])
	app.config.from_pyfile('_config.py')
	db.init_app(app)
	app.celery = make_celery(app)
	app.app_context().push()
	migrate = Migrate(app, db)

	from app import models
	#Admin Blueprint with URL Prefix
	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')
	#Home Blueprint 
	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)
	#Generate Login Manager
	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page."
	login_manager.login_view = "auth.login"

	#Configure Application Folders
	#Ensure Creation of Application Uploads Folder
	if not os.path.exists(app.config['UPLOAD_FOLDER']):
		os.makedirs(app.config['UPLOAD_FOLDER'])
	#Ensure Creation of Application Downloads Folder
	if not os.path.exists(app.config['DOWNLOAD_FOLDER']):
		os.makedirs(app.config['DOWNLOAD_FOLDER'])

	c = 0
	while c <=100:
		for item in app.config:
			print item

		c = c + 1

	# temporary route
	#@app.route('/')
	#def hello_world():
	#	return 'Hello, World!'

	return app
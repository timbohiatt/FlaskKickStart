# app/home/views.py
from flask import current_app as app
from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required
from sqlalchemy import and_

from os.path import join, dirname, realpath,basename
from . import home
from .. import db
from ..models import SampleTableObject

import os
import json, uuid



'''
#----------------------------------------------------------------------------------#
#
#	ROUTE: Home Page
#
#
#----------------------------------------------------------------------------------#
'''
@home.route('/')
def homepage():
	"""
	Render the homepage template on the / route
	"""
	return render_template('home/index.html', title="Welcome")


'''
#----------------------------------------------------------------------------------#
#
#	ROUTE: API CALL
#	CELERY BACKGROUND TASK
#
#----------------------------------------------------------------------------------#
'''
@app.celery.task(bind=True, name='runEngine')
def celery_sampleProcess(self):
	self.update_state(state='STARTED',meta={'current': 1, 'total': 100,'status': "Running"})
	return {'current': 100, 'total': 100, 'status': "Completed", 'custom':{"key":"Value", "key1":"value1"}}



'''
#----------------------------------------------------------------------------------#
#
#	ROUTE: API CALL
#
#
#----------------------------------------------------------------------------------#
'''
@app.route('/status/<task_id>')
def taskstatus(task_id):

	task = celery_sampleProcess.AsyncResult(task_id)
	if task.state == 'PENDING':
		# job did not start yet
		response = {
			'state': task.state,
			'current': 0,
			'total': 1,
			'status': 'Working...'
		}
	elif task.state == 'SUCCESS':
		response = {
			'state': task.state,
			'current': task.info.get('current', 0),
			'total': task.info.get('total', 1),
			'status': task.info.get('status', ''),
		}
	elif task.state != 'FAILURE':
		response = {
			'state': task.state,
			'current': task.info.get('current', 0),
			'total': task.info.get('total', 1),
			'status': task.info.get('status', '')
		}
		if 'result' in task.info:
			response['result'] = task.info['result']
	else:
		# something went wrong in the background job
		response = {
			'state': task.state,
			'current': 1,
			'total': 1,
			'status': str(task.info),  # this is the exception raised
		}
	return jsonify(response)




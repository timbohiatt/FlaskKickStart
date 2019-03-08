# app/models.py
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from app import db, login_manager



'''
	== SAMPLE TABLE OBJECT ==
	This object is only built as a sample object that will be built when the Flaksk Container is Deployed.
	You can remove this class object if you wish. Its Serves No Purpose other than to show you a sample.
'''

class SampleTableObject(UserMixin, db.Model):
	__tablename__ = 'sampleTableObjects'
	ID = db.Column(db.Integer, primary_key=True)
	sample_Integer = db.Column(db.Integer,nullable=False)
	sample_String = db.Column(db.String(100), nullable=False)
	sample_Float = db.Column(db.DECIMAL)
	sample_Boolean = db.Column(db.Boolean, default=True)
	#System Table Details.
	sys_active = db.Column(db.Boolean, default=False)
	sys_created = db.Column(db.DateTime, default=datetime.utcnow)
	sys_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



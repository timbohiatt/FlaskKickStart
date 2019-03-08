import os
from celery import Celery
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG')).celery



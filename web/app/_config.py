#config.py
import os

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments

    #CELERY Broker Configuration
    CELERY_BROKER_URL='pyamqp://guest@rabbitmq//',
    CELERY_RESULT_BACKEND='rpc://'

    #MYSQL Configuration
    mysql_user = os.environ['MYSQL_USER']
    mysql_pass = os.environ['MYSQL_USER_PASS']
    #mysql_host = str(os.environ['APP_NAME']+ "_MYSQL")
    mysql_host = "127.0.0.1"
    mysql_port = os.environ['MYSQL_PORT']
    mysql_db = os.environ['MYSQL_DB']


    #FLASK Configuration
    SECRET_KEY = os.environ['FLASK_SECRET']
    SQLALCHEMY_DATABASE_URI = str("mysql+pymysql://" + mysql_user + ":" + mysql_pass + "@" + mysql_host + ":" + mysql_port + "/" + mysql_db)

    count = 0
    while count <= 100:
        print SQLALCHEMY_DATABASE_URI 
        print mysql_user
        print mysql_pass
        print mysql_host
        print mysql_port
        print mysql_db
        count = count + 1

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    UPLOAD_FOLDER  = os.path.join(SITE_ROOT, 'static', 'uploads')
    DOWNLOAD_FOLDER  = os.path.join(SITE_ROOT, 'static', 'downloads')


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestConfig(Config):
    """
    Test and Integration Branch configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False



app_config = {
    'DEVELOPMENT': DevelopmentConfig,
    'TEST':TestConfig,
    'INTEGRATION':TestConfig,
    'PRODUCTION': ProductionConfig
}
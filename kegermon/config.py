import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'development_key')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME', 'admin')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', 'sandwiches')
    DEBUG = os.getenv('DEBUG', False)

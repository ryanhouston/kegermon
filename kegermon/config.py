import os

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'development_key')
    REDIS_URL  = "redis://redis:6379/0"

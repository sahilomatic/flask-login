import os

#Edited by sahil soni
#secret key is created and fetched from environement of server
SECRET_KEY = os.getenv('SECRET_KEY')
REDIS_HOST = "0.0.0.0"
REDIS_PORT = 6379
BROKER_URL = os.environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
    host=REDIS_HOST, port=str(REDIS_PORT)))
CELERY_RESULT_BACKEND = BROKER_URL
#done



DEBUG = True
LOG_ROOT = os.environ.get("LOG_ROOT")
LOG_FILENAME = "{}.log".format(os.environ.get("APPLICATION_NAME"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'encoding': 'utf-8',
            'filename': os.path.join(LOG_ROOT, LOG_FILENAME)
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': True,
        }
    }
}


MONGO_SETTINGS = {
    'DB_NAME': os.environ.get('DB_NAME'),
    'DB_HOST': os.environ.get('DB_HOST'),
    'DB_PORT': int(os.environ.get('DB_PORT', 27017)),
    'DB_USERNAME': os.environ.get('DB_USERNAME'),
    'DB_PASSWORD': os.environ.get('DB_PASSWORD'),
}

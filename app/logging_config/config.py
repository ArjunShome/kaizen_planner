import os


DEV = 'dev'
ENV_NAME = os.environ.get('ENV_NAME') or DEV

DEV_HANDLER = {
    'class': 'logging.handlers.TimedRotatingFileHandler',
    'filename': 'logs/{}.log'.format(ENV_NAME),
    'formatter': 'default',
    'backupCount': 10,
    'when': 'midnight',
    'interval': 1,
}

PROD_HANDLER = {
    'class': 'logging.StreamHandler',
    'formatter': 'default',
    'stream': 'ext://sys.stdout'
}


DEV_REQ_HANDLER = {
    'class': 'logging.handlers.TimedRotatingFileHandler',
    'filename': 'logs/{}.log'.format(ENV_NAME),
    'formatter': 'request_formatter',
    'backupCount': 10,
    'when': 'midnight',
    'interval': 1,
}

PROD_REQ_HANDLER = {
    'class': 'logging.StreamHandler',
    'formatter': 'request_formatter',
    'stream': 'ext://sys.stdout'
}

LOGGING_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s | %(module)s | %(lineno)d | %(levelname)s | %(message)s'
        },
        'request_formatter': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        }
    },
    'handlers': {
        'log_handler': PROD_HANDLER,
        'request_log_handler': PROD_REQ_HANDLER
    },
    'loggers': {
        '': {
            'handlers': ['log_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'RequestLogger': {
            'handlers': ['request_log_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

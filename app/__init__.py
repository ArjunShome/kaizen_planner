import logging
import logging.config
import logging.handlers
import time

from fastapi import FastAPI

from app.api import API_ROUTERS
from app.cache import app_cache
from app.logging_config.config import LOGGING_CONF


def create_app(config):
    """
    Initialize the core application.
    """

    # Creating the app
    logging.config.dictConfig(LOGGING_CONF)
    logging.Formatter.converter = time.gmtime

    app_cache.init_app(config.REDIS_CACHE_URL)

    fast_app = FastAPI()
    for router in API_ROUTERS:
        fast_app.include_router(router)

    return fast_app

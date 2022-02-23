import logging
from functools import wraps
from datetime import datetime
from flask import request


def log_this(f):
    """
    IMPORTANT: If you use this decorator with Flask, be sure to put it
    it after @route (Flask demands this to be the top decorarator)
    https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/
    """

    @wraps(f)
    def fw(*args, **kwargs):
        logging.info("#" * 80)
        logging.info("Function: {} | Start: {}".format(f.__name__, datetime.now()))
        logging.info("-" * 80)
        logging.info("args: {}".format(args))
        logging.info("-" * 80)
        logging.info("kwargs: {}".format(kwargs))
        logging.info("-" * 80)
        logging.info("json data: {}".format(request.get_json()))
        logging.info("=" * 80)
        retFunc = f(*args, **kwargs)
        logging.info("=" * 80)
        logging.info("Function: {} | End: {}".format(f.__name__, datetime.now()))
        logging.info("#" * 80)
        return retFunc

    return fw

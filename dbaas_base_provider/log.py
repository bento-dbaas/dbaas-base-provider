import logging
from functools import wraps
from datetime import datetime
import uuid
from flask import request


def log_this(f):
    """
    IMPORTANT: If you use this decorator with Flask, be sure to put it
    it after @route (Flask demands this to be the top decorarator)
    https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/
    """

    @wraps(f)
    def fw(*args, **kwargs):
        id = uuid.uuid4()
        logging.info("#" * 80)
        logging.info("{} | Start: {} - {}".format(f.__name__, datetime.now(), id))
        logging.info("args: {} - {}".format(args, id))
        logging.info("kwargs: {} - {}".format(kwargs, id))
        logging.info("json data: {} - {}".format(request.get_json(), id))
        retFunc = f(*args, **kwargs)
        logging.info("{} | End: {} - {}".format(f.__name__, datetime.now(), id))
        logging.info("#" * 80)
        return retFunc

    return fw

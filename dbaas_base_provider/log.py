import logging
from functools import wraps
from datetime import datetime


def log_this(f):
    @wraps(f)
    def fw(*args, **kwargs):
        logging.info("#" * 80)
        logging.info("#" * 80)
        logging.info(f"Function: {f.__name__}")
        logging.info(f'Start: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')
        logging.info("-" * 80)
        logging.info(f"args: {args}")
        logging.info("-" * 80)
        logging.info(f"kwargs: {kwargs}")
        logging.info("=" * 80)
        retFunc = f(*args, **kwargs)
        logging.info("=" * 80)
        logging.info(f"Function: {f.__name__}")
        logging.info(f'End: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')
        logging.info("#" * 80)
        logging.info("#" * 80)
        return retFunc

    return fw

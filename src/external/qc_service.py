''' Module to hold the functions that make calls to the qc-note-controller
    and the qc-category-controller '''

import requests, os

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)
EXTERNAL_API = os.getenv('EXTERNAL_API')
_caliber = EXTERNAL_API + '/qa'
''' Module to pull information from the 
    Caliber category-controller'''

import requests

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

_caliber = EXTERNAL_API + "/category"


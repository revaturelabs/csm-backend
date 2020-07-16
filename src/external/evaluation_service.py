'''this module is to pull from Caliber assessment-controller
    grade-controller and note-controller'''

import requests

from src.testing_logging.logger import get_logger

_log = get_logger(__name__)
_caliber = EXTERNAL_API + "/evalutaion"
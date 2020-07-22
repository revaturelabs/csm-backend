''' Module to pull information from the Caliber category-controller'''

import os
import requests

from src.logging.logger import get_logger

_log = get_logger(__name__)

EXTERNAL_API = os.getenv('EXTERNAL_API')
_caliber = EXTERNAL_API + '/category'

def get_category_data():
    '''this method hits the Caliber category-controller
       /category with a get request to get all category information'''
    return requests.get(_caliber).json()

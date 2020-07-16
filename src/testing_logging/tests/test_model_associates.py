'''This is the unittest file for the Associate class'''
import unittest

from src.models.associates import Associate
from src.testing_logging.logger import get_logger
_log = get_logger(__name__)

class AssociateTestSuite(unittest.TestCase):
    '''Test suite for the Associate class'''

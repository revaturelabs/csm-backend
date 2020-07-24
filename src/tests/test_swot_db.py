''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.swot_db import create_swot

class TestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    def test_create_swot(self):
        ''' This method will test the create_swot function '''
        
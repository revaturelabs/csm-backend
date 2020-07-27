''' This module will contain the test suite for the SWOT model '''
import unittest

from src.models.associates import Associate

class AssociateTests(unittest.TestCase):
    '''This is the test suite'''
    def test_constructor(self):
        ''' This will ensure that the object constructs'''
        new_associate = Associate()
        self.assertEqual(new_associate.__class__, Associate)

''' This module will contain the test suite for the SWOT model '''
import unittest

from src.models.swot import SWOT


class SwotTests(unittest.TestCase):
    '''This is the test suite'''
    def test_constructor(self):
        ''' This will ensure that the object constructs'''
        new_swot = SWOT()
        self.assertEqual(new_swot.__class__, SWOT)

     def test_from_dict(self):
        ''' This will test the from_dict classmethod. '''
        new_swot_dict = {
            'Strengths': ['strengths'],
            'Weaknesses': ['weaknesses'],
            'Opportunities': ['opportunities'],
            'Threats': ['threats'],
            'Notes': 'notes',
            'author': 'trainer',
            'date_created': 'the past'
        }
        new_swot = SWOT.from_dict(new_swot_dict)
        self.assertEqual(new_swot.__class__, SWOT)
        self.assertEqual(new_swot.__dict__, new_swot_dict)

''' This module will contain the test suite for the SWOT model '''
import unittest

from src.models.swot import SWOT


class SwotTests(unittest.TestCase):
    '''This is the test suite'''
    def test_constructor(self):
        ''' This will ensure that the object constructs'''
        new_swot = SWOT()
        self.assertEqual(new_swot.__class__, SWOT)

    def test_add_swot_item(self):
        ''' This will test the add_swot_item member function of a SWOT object '''
        new_swot = SWOT()
        new_swot.add_swot_item('strengths', 'Test strength')
        self.assertEqual(len(new_swot.strengths), 1) # The strengths array should have 1 item in it
        new_swot_two = new_swot
        new_swot_two.add_swot_item('nothing', 'Doesnt matter')
        self.assertEqual(new_swot, new_swot_two) # These should be equal because the function should 
                                                 # return the target swot unmodified if the field 
                                                 # doesn't exist

    def test_from_dict(self):
        ''' This will test the from_dict classmethod. '''
        new_swot_dict = {
            'strengths': ['strengths'],
            'weaknesses': ['weaknesses'],
            'opportunities': ['opportunities'],
            'threats': ['threats'],
            'notes': 'notes'
        }
        new_swot = SWOT.from_dict(new_swot_dict)
        self.assertEqual(new_swot.__class__, SWOT)
        self.assertEqual(new_swot.__dict__, new_swot_dict)

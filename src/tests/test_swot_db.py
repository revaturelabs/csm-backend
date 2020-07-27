''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.swot_db import create_swot

class TestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    @mock.patch('src.data.associates_db._associates.update_associate_swot')
    def test_create_swot(self, mock_update):
        ''' This method will test the create_swot function '''

        create_swot('email', 'query_val', {'new_swot': 'new_swot'})

        self.assertFalse(mock_update.called)

        create_swot('query_key', 'query_val', {'strengths': 'new_strengths',
                                               'weaknesses': 'new_weaknesses',
                                               'opportunities': 'new_opportunities',
                                               'threats': 'new_threats',
                                               'notes': 'new_notes'})

        self.assertFalse(mock_update.called)

        create_swot('email', 'query_val', {'strengths': 'new_strengths',
                                           'weaknesses': 'new_weaknesses',
                                           'opportunities': 'new_opportunities',
                                           'threats': 'new_threats',
                                           'notes': 'new_notes'})

        self.assertFalse(mock_update.called)
        
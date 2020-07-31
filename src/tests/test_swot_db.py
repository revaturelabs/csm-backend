''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
import datetime
from src.data.swot_db import create_swot

class TestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    @mock.patch('src.data.associates_db.update_associate_swot')
    def test_create_swot(self, mock_update):
        ''' This method will test the create_swot function '''

        create_swot('email', 'query_val', {'new_swot': 'new_swot'})

        self.assertFalse(mock_update.called)

        create_swot('query_key', 'query_val', {'Strengths': 'new_strengths',
                                               'Weaknesses': 'new_weaknesses',
                                               'Opportunities': 'new_opportunities',
                                               'Threats': 'new_threats',
                                               'Notes': 'new_notes',
                                               'date_created': 'the past',
                                               'author': 'staging manager'})

        self.assertFalse(mock_update.called)

        create_swot('email', 'query_val', {'author': 'staging manager',
                                           'Strengths': ['new_strengths'],
                                           'Weaknesses': ['new_weaknesses'],
                                           'Opportunities': ['new_opportunities'],
                                           'Threats': ['new_threats'],
                                           'Notes': 'new_notes',
                                           'date_created': datetime.datetime.now().replace(microsecond=0)})

        self.assertTrue(mock_update.called)
        
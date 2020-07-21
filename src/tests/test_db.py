''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.associates_db import create_associate, read_all_associates, \
                          read_all_associates_by_query, update_associate_swot
from src.models.associates import Associate

class TestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    @mock.patch('src.data.associates_db._associates.insert_one')
    def test_create_associate(self, mock_insert):
        ''' This method will test the create_associate function '''

        create_associate(Associate())

        self.assertTrue(mock_insert.called)

    @mock.patch('src.data.associates_db._associates.find')
    def test_read_all_associates(self, mock_find):
        ''' This method will test the read all associates function '''
        mock_find.return_value = ['all associates']

        all_associates = read_all_associates()

        self.assertTrue(mock_find.called)
        self.assertEqual(all_associates, ['all associates'])

    @mock.patch('src.data.associates_db._associates.find')
    def test_read_all_associates_by_query(self, mock_find):
        ''' This method will test the read all associates by query function '''
        mock_find.return_value = ['queried associates']

        associates = read_all_associates_by_query({'query': 'query'})

        self.assertTrue(mock_find.called)
        self.assertEqual(associates, ['queried associates'])

    @mock.patch('src.data.associates_db._associates.update_one')
    def test_update_associate_swot(self, mock_update):
        ''' This method will test the update associate swot function '''
        mock_update.return_value = True

        test = update_associate_swot('query', 'swot')

        self.assertTrue(test)
        self.assertTrue(mock_update.called)

''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.data import create_associate, create_swot, read_all_associates, \
                          read_all_associates_by_query, update_associate_swot
from src.models.associates import Associate

class TestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    @mock.patch('src.data.data.associates.insert_one')
    def test_create_associate(self, mock_insert):
        ''' This method will test the create_associate function '''

        create_associate(Associate())

        self.assertTrue(mock_insert.called)

    @mock.patch('src.data.data.associates.find_one_and_update')
    def test_create_swot(self, mock_foau):
        ''' This method will test the create_swot function '''
        mock_foau.return_value = 'Success'

        valid_swot = {
            'strengths': ['strengths'],
            'weaknesses': ['weaknesses'],
            'opportunities': ['opportunities'],
            'threats': ['threats'],
            'notes': 'notes'
        }
        test1 = create_swot('invalid', 'sf_id', {'swot': 'swot'})
        test2 = create_swot('email', 'email@email.com', {'invalid_swot': 'swot bad'})
        test3 = create_swot('email', 'email@email.com', valid_swot)

        self.assertEqual(test1, 'Incorrect query parameters')
        self.assertEqual(test2, 'Invalid SWOT')
        self.assertEqual(test3, 'Success')

    @mock.patch('src.data.data.associates.find')
    def test_read_all_associates(self, mock_find):
        ''' This method will test the read all associates function '''
        mock_find.return_value = ['all associates']

        all_associates = read_all_associates()

        self.assertTrue(mock_find.called)
        self.assertEqual(all_associates, ['all associates'])

    @mock.patch('src.data.data.associates.find')
    def test_read_all_associates_by_query(self, mock_find):
        ''' This method will test the read all associates by query function '''
        mock_find.return_value = ['queried associates']

        associates = read_all_associates_by_query({'query': 'query'})

        self.assertTrue(mock_find.called)
        self.assertEqual(associates, ['queried associates'])

    @mock.patch('src.data.data.associates.update_one')
    def test_update_associate_swot(self, mock_update):
        ''' This method will test the update associate swot function '''
        mock_update.return_value = True

        test = update_associate_swot('query', 'swot')

        self.assertTrue(test)
        self.assertTrue(mock_update.called)

''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.associates_db import create_associate, read_all_associates, \
                          read_all_associates_by_query, update_associate_swot, \
                          get_associate_batch_id, get_associate_sf_id, \
                          create_associates_from_scheduler
from src.models.associates import Associate

class AssociateTestDatabase(unittest.TestCase):
    ''' This is the database test suite '''

    @mock.patch('src.data.associates_db._associates.insert_one')
    def test_create_associate(self, mock_insert):
        ''' This method will test the create_associate function '''

        create_associate(Associate())

        self.assertTrue(mock_insert.called)

    # @mock.patch('src.data.associates_db.create_associate')
    # @mock.patch('src.external.caliber_processing.get_new_graduates')
    # @mock.patch('src.external.training_service.batch_current')
    # def test_create_associates_from_scheduler(self, mock_batches, mock_assoc_list, mock_create):
    #     ''' This method will test the create_associate function '''
    #     mock_batches.return_value = ['all batches currently training']
    #     mock_assoc_list.return_value = [{'name': 'assoc 1'}, {'name': 'assoc 2'},
    #                                     {'name': 'assoc 3'}]

    #     create_associates_from_scheduler()

    #     self.assertTrue(mock_create.called)
    #     self.assertEqual(3, mock_create.call_count)

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
    def test_update_associate_swot(self, mock_find):
        ''' This method will test the update associate swot function '''

        test = update_associate_swot({'salesforce_id': 'SF-1111'}, 'swot')

        self.assertTrue(mock_find.called)
        self.assertTrue(test)

    @mock.patch('src.data.associates_db._associates.find_one')
    def test_get_associate_batch_id(self, mock_find):
        ''' This method will test the get_associate_batch_id function '''
        mock_find.return_value = {'salesforce_id': 'SF-1111', 'email': 'mock12@revature.com',
                                  'batch_id': 'TR-9999', 'manager_id': 'Julie',
                                  'end_date': 'null', 'swot': 'null', 'status': 'Active'}

        batch = get_associate_batch_id({'email': 'mock12@revature.com'})

        self.assertTrue(mock_find.called)
        self.assertEqual(batch, 'TR-9999')

    @mock.patch('src.data.associates_db._associates.find_one')
    def test_get_associate_sf_id(self, mock_find):
        ''' This method will test the get_associate_sf_id function '''
        mock_find.return_value = {'salesforce_id': 'SF-1111', 'email': 'mock12@revature.com',
                                  'batch_id': 'TR-9999', 'manager_id': 'Julie',
                                  'end_date': 'null', 'swot': 'null', 'status': 'Active'}

        salesforce = get_associate_sf_id({'email': 'mock12@revature.com'})

        self.assertTrue(mock_find.called)
        self.assertEqual(salesforce, 'SF-1111')

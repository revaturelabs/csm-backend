''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.managers_db import manager_login, get_all_info, get_managers_by_batch, update_batches

class ManagerTestDatabase(unittest.TestCase):
    ''' This is the database test suite '''
    @mock.patch('src.data.managers_db._managers.find_one')
    def test_manager_login(self, mock_find):
        ''' This method will test the manager_login function '''
        mock_find.return_value = {'_id': 'julie@revature.com', 'username': 'Julie'}

        manager = manager_login('julie@revature.com')

        self.assertTrue(mock_find.called)
        self.assertEqual(manager, {'_id': 'julie@revature.com', 'username': 'Julie'})

    @mock.patch('src.data.managers_db._managers.find')
    def test_get_all_info(self, mock_find):
        ''' This method will test the get_all_info function '''
        mock_find.return_value = [{'_id': 'julie@revature.com', 'username': 'Julie'}]

        info = get_all_info()

        self.assertTrue(mock_find.called)
        self.assertEqual(info, [{'_id': 'julie@revature.com', 'username': 'Julie'}])

    @mock.patch('src.data.managers_db._managers.find_one')
    def test_get_managers_by_batch(self, mock_find):
        ''' This method will test the get_managers_by_batch function '''
        mock_find.return_value = {'_id': 'julie@revature.com', 'username': 'Julie'}

        managers = get_managers_by_batch('mock batch')

        self.assertTrue(mock_find.called)
        self.assertEqual(managers, {'_id': 'julie@revature.com', 'username': 'Julie'})

    @mock.patch('src.data.managers_db._managers.update_one')
    def test_update_batches(self, mock_update):
        ''' This method will test the update_batches function '''
        update_batches('mock manager', {'mock': 'mock'})

        self.assertTrue(mock_update.called)
        
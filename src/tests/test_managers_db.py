''' This module will contain the test suite for the database '''
import unittest
import unittest.mock as mock
from src.data.managers_db import manager_login

class ManagerTestDatabase(unittest.TestCase):
    ''' This is the database test suite '''
    @mock.patch('src.data.managers_db._managers.find_one')
    def test_manager_login(self, mock_find):
        ''' This method will test the manager_login function '''
        mock_find.return_value = {'_id': 'julie@revature.com', 'username': 'Julie'}

        manager = manager_login('julie@revature.com')

        self.assertTrue(mock_find.called)
        self.assertEqual(manager, {'_id': 'julie@revature.com', 'username': 'Julie'})
        
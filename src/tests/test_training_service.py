'''this module is to test the training_service module in src.external'''
import unittest
from unittest.mock import patch

from src.external.training_service import batch_current, get_batch_by_id

class TrainingServiceTest(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('requests.get')
    def test_batch_current(self, mock_get):
        '''this method is to test the batch_current function in caliber_processing'''

        batch_current()

        self.assertTrue(mock_get.called)

    @patch('requests.get')
    def test_get_batch_by_id(self, mock_get):
        '''this method is to test the get_batch_by_id function in caliber_processing'''

        get_batch_by_id('mock id')

        self.assertTrue(mock_get.called)

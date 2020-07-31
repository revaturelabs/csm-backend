'''this module is to test the evaluation_service module in src.external'''
import unittest
from unittest.mock import patch

from src.external.evaluation_service import get_associate_spider_data, get_batch_spider_data

class EvaluationServiceTest(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('requests.get')
    def test_get_associate_spider_data(self, mock_get):
        '''this method is to test the get_associate_spider_data function in caliber_processing'''

        get_associate_spider_data('mock batch', 'mock email')

        self.assertTrue(mock_get.called)

    @patch('requests.get')
    def test_get_batch_spider_data(self, mock_get):
        '''this method is to test the get_batch_spider_data function in caliber_processing'''

        get_batch_spider_data('mock batch')

        self.assertTrue(mock_get.called)

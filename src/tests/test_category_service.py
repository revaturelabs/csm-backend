'''this module is to test the category_service module in src.external'''
import unittest
from unittest.mock import patch

from src.external.category_service import get_category_data

class EvaluationServiceTest(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('requests.get')
    def test_get_category_data(self, mock_get):
        '''this method is to test the get_category_data function in caliber_processing'''

        get_category_data()

        self.assertTrue(mock_get.called)

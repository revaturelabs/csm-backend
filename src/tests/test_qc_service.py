'''this module is to test the qc_service module in src.external'''
import unittest
from unittest.mock import patch

from src.external.qc_service import get_note_headers, get_qc_category

class QCServiceTest(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('requests.get')
    def test_get_note_headers(self, mock_get):
        '''this method is to test the get_note_headers function in caliber_processing'''
        get_note_headers('mock assoc')

        self.assertTrue(mock_get.called)

    @patch('requests.get')
    def test_get_qc_category(self, mock_get):
        '''this method is to test the get_qc_category function in caliber_processing'''

        get_qc_category('mock batch', '4')

        self.assertTrue(mock_get.called)

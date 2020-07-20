'''this module is to test the caliber_processing module in src.external'''
import unittest
from unittest.mock import patch

from src.external.caliber_processing import get_qc_data
from src.external.qc_service import get_note_headers, get_qc_category

class Caliber_processing_test(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('src.external.qc_service.get_qc_category')
    @patch('src.external.qc_service.get_note_headers')
    def test_get_qc_data(self, mock_A, mock_B):
        '''this method is to test the get_qc_data function in caliber_processing'''
        mock_A.return_value = [{'noteId': 2, 'content': 'This is a Qc note on week 1', 'week': 1, 'batchId': 'TR-1345', 'associateId': 'SF-4942', 'employeeId': 'QC-User', 'type': 'QC_TRAINEE', 'technicalStatus': 'Average', 'createdOn': None, 'lastUpdated': None}]
        mock_B.return_value = 'Java'
        result = get_qc_data('SF-1')
        print(result)
        self.assertEqual(result[0], {'skill': 'Java', 'score': 'Average', 'content': 'This is a Qc note on week 1'})
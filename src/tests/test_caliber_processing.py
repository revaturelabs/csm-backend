'''this module is to test the caliber_processing module in src.external'''
import unittest
from unittest.mock import patch

from src.external.caliber_processing import get_qc_data, get_batch_and_associate_spider_data
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
        self.assertEqual(result[0], {'skill': 'Java', 'score': 'Average', 'content': 'This is a Qc note on week 1'})

    @patch('src.data.associates_db.get_associate_batch_id')
    @patch('src.external.evaluation_service.get_batch_spider_data')
    @patch('src.external.evaluation_service.get_associate_spider_data')
    def test_get_batch_and_associate_spider_data(self, mock_assoc_spider, mock_batch_spider,
                                                 mock_assoc_batch_id):
        '''this method is to test the batch_and_associate_spider_data function in caliber_processing'''
        mock_assoc_batch_id.return_value = 'TR-1077'
        mock_batch_spider.return_value = '''[{
                                                "traineeId": "TR-1077",
                                                "assessmentType": "Helm",
                                                "score": 47.7024629637599,
                                                "week": 1,
                                                "weight": 100
                                            },
                                            {
                                                "traineeId": "TR-1077",
                                                "assessmentType": "HTML",
                                                "score": 61.05993378162384,
                                                "week": 1,
                                                "weight": 100
                                            },
                                            {
                                                "traineeId": "TR-1077",
                                                "assessmentType": "CSS",
                                                "score": 45.23073920607567,
                                                "week": 1,
                                                "weight": 100
                                            }]'''
        mock_assoc_spider.return_value = '''[{
                                                "traineeId": "TR-1077",
                                                "assessmentType": "Helm",
                                                "score": 47.7024629637599,
                                                "week": 1,
                                                "weight": 100
                                            },
                                            {
                                                "traineeId": "TR-1077",
                                                "assessmentType": "HTML",
                                                "score": 61.05993378162384,
                                                "week": 1,
                                                "weight": 100
                                            },
                                            {
                                                "traineeId": "TR-1077",
                                                "assessmentType": "CSS",
                                                "score": 45.23073920607567,
                                                "week": 1,
                                                "weight": 100
                                            }]'''
        batch_spider, assoc_spider = get_batch_and_associate_spider_data('mock@revature.com')
        self.assertEqual(batch_spider, [{
                                            "assessmentType": "Helm",
                                            "score": 47.7024629637599,
                                            "week": 1
                                         },
                                         {
                                            "assessmentType": "HTML",
                                            "score": 61.05993378162384,
                                            "week": 1
                                         },
                                         {
                                            "assessmentType": "CSS",
                                            "score": 45.23073920607567,
                                            "week": 1
                                         }])
        self.assertEqual(assoc_spider, [{
                                            "assessmentType": "Helm",
                                            "score": 47.7024629637599,
                                            "week": 1
                                         },
                                         {
                                            "assessmentType": "HTML",
                                            "score": 61.05993378162384,
                                            "week": 1
                                         },
                                         {
                                            "assessmentType": "CSS",
                                            "score": 45.23073920607567,
                                            "week": 1
                                         }])

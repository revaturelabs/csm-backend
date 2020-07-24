'''this module is to test the caliber_processing module in src.external'''
import unittest
from unittest.mock import patch

from src.external.caliber_processing import get_qc_data, get_batch_and_associate_spider_data, get_batch_info
from src.external.qc_service import get_note_headers, get_qc_category

class Caliber_processing_test(unittest.TestCase):
    '''this class is to test the caliber processing module'''

    @patch('src.external.qc_service.get_qc_category')
    @patch('src.external.qc_service.get_note_headers')
    def test_get_qc_data(self, mock_A, mock_B):
        '''this method is to test the get_qc_data function in caliber_processing'''
        mock_A.return_value = [{'noteId': 2, 'content': 'This is a Qc note on week 1',
                                'week': 1, 'batchId': 'TR-1345', 'associateId': 'SF-4942',
                                'employeeId': 'QC-User', 'type': 'QC_TRAINEE',
                                'technicalStatus': 'Average', 'createdOn': None,
                                'lastUpdated': None}]
        mock_B.return_value = 'Java'
        result = get_qc_data('SF-1')
        self.assertEqual(result[0], {'skill': 'Java', 'score': 'Average', 'content': 'This is a Qc note on week 1'})

    @patch('src.external.evaluation_service.get_batch_spider_data')
    @patch('src.external.evaluation_service.get_associate_spider_data')
    def test_get_batch_and_associate_spider_data(self, mock_assoc_spider, mock_batch_spider):
        '''this method is to test the batch_and_associate_spider_data function in caliber_processing'''
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
        batch_spider, assoc_spider = get_batch_and_associate_spider_data('mock@revature.com', 'mock_batch')
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

    @patch('src.external.training_service.get_batch_by_id')
    def test_get_batch_info(self, mock_a):
        ''' this method is to test the get_batch_info module in caliber_processing'''
        mock_a.return_value = {'id': 223, 'batchId': 'TR-1345', 'name': 'Mock Batch 223',
                               'startDate': '2018-05-07', 'endDate': '2018-07-16', 'skill': 'PEGA',
                               'location': 'New York', 'type': 'Revature', 'goodGrade': 70, 'passingGrade': 80,
                               'employeeAssignments': [{'role': 'ROLE_LEAD_TRAINER',
                               'employee':
                                    {'email': 'mock1223.employee906bb611-b2a8-4dce-b70f-94f5fd97da44@mock.com', 
                                     'firstName': 'Mock 1223', 'lastName': 'Associate 1223'}, 'deletedAt': None}], 
                                'associateAssignments':[
                                    {'trainingStatus': 'Training','associate': 
                                        {'email': 'mock5.associateaea29a7d-5e25-4efc-a773-9d45a9bac92a@mock.com', 
                                        'salesforceId': 'SF-4934', 'firstName': 'Mock 5', 'lastName': 'Associate 5', 'flag': None}, 
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock12.associate709b5c28-660b-4bd3-be46-7fe1856269a9@mock.com',
                                        'salesforceId': 'SF-4941', 'firstName': 'Mock 12', 'lastName': 'Associate 12', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock7.associatebf0ac099-ae25-4330-83cc-bd3968528471@mock.com',
                                        'salesforceId': 'SF-4936', 'firstName': 'Mock 7', 'lastName': 'Associate 7', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock3.associate80b10a09-f2eb-499b-a29b-86b2b7abe9e3@mock.com',
                                        'salesforceId': 'SF-4932', 'firstName': 'Mock 3', 'lastName': 'Associate 3', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock4.associate2c462444-afd6-416a-b81e-9211ba20451d@mock.com',
                                        'salesforceId': 'SF-4933', 'firstName': 'Mock 4', 'lastName': 'Associate 4', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock11.associate4ce6aa14-91e0-42fa-bf05-19cd3b8d3f8c@mock.com',
                                        'salesforceId': 'SF-4940', 'firstName': 'Mock 11', 'lastName': 'Associate 11', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True},
                                    {'trainingStatus': 'Training', 'associate':
                                        {'email': 'mock0.associateb8d5b410-852e-4226-b6c1-8902c51f7b11@mock.com',
                                        'salesforceId': 'SF-4929', 'firstName': 'Mock 0', 'lastName': 'Associate 0', 'flag': None},
                                        'startDate': '2018-07-16', 'endDate': '2018-05-07', 'active': True}]}
        result = get_batch_info('TR-1345')
        self.assertEqual(result['trainer'][0]['employee']['firstName'], 'Mock 1223')
        self.assertEqual(result['associates'][1]['userID'], 'mock12.associate709b5c28-660b-4bd3-be46-7fe1856269a9@mock.com')
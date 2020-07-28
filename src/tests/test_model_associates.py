'''This is the unittest file for the Associate class'''
import unittest

from src.models.associates import Associate
from src.models.swot import SWOT
from src.logging.logger import get_logger
_log = get_logger(__name__)

class AssociateTestSuite(unittest.TestCase):
    '''Test suite for the Associate class'''
    associate = None
    def setUp(self):
        self.associate = Associate(0, 'mock assoc', 'test@email.com', 1, 2, 'mock trainer', 'end date')
    def tearDown(self):
        self.associate = None
    @classmethod
    def setUpClass(cls):
        cls.associate = Associate()
    @classmethod
    def tearDownClass(cls):
        cls.associate = None


    def test_get_salesforce_id(self):
        ''' Tests the get_salesforce_id method '''
        self.setUp()
        self.assertEqual(0, self.associate.get_salesforce_id())
        self.tearDown()

    def test_get_name(self):
        ''' Tests the get_salesforce_id method '''
        self.setUp()
        self.assertEqual('mock assoc', self.associate.get_name())
        self.tearDown()

    def test_get_email(self):
        ''' Tests the get_email method '''
        self.setUp()
        self.assertEqual('test@email.com', self.associate.get_email())
        self.tearDown()

    def test_get_batch_id(self):
        ''' Tests the get_salesforce_id method '''
        self.setUp()
        self.assertEqual(1, self.associate.get_batch_id())
        self.tearDown()

    def test_get_manager_id(self):
        ''' Tests the get_manager_id method '''
        self.setUp()
        self.assertEqual(2, self.associate.get_manager_id())
        self.tearDown()

    def test_get_end_date(self):
        ''' Tests the get_end_date method '''
        self.setUp()
        self.assertEqual('end date', self.associate.get_end_date())
        self.tearDown()

    def test_get_swot(self):
        ''' Tests the get_swot method '''
        self.setUp()
        self.assertEqual(SWOT().to_dict(), self.associate.get_swot()[0])
        self.tearDown()

    def test_get_trainers(self):
        ''' Tests the get_salesforce_id method '''
        self.setUp()
        self.assertEqual('mock trainer', self.associate.get_trainers())
        self.tearDown()

    def test_get_status(self):
        ''' Tests the get_status method '''
        self.setUp()
        self.assertEqual('Active', self.associate.get_status())
        self.tearDown()


    def test_set_id(self):
        ''' Tests the set_id method '''
        self.setUp()
        self.associate.set_salesforce_id(100)
        self.assertEqual(100, self.associate.salesforce_id)
        self.tearDown()

    def test_set_email(self):
        ''' Tests the set_email method '''
        self.setUp()
        self.associate.set_email(100)
        self.assertEqual(100, self.associate.email)
        self.tearDown()

    def test_set_manager_id(self):
        ''' Tests the set_manager_id method '''
        self.setUp()
        self.associate.set_manager_id(100)
        self.assertEqual(100, self.associate.manager_id)
        self.tearDown()

    def test_set_batch_id(self):
        ''' Tests the set_batch_id method '''
        self.setUp()
        self.associate.set_batch_id(100)
        self.assertEqual(100, self.associate.batch_id)
        self.tearDown()

    def test_set_end_date(self):
        ''' Tests the set_end_date method '''
        self.setUp()
        self.associate.set_end_date(100)
        self.assertEqual(100, self.associate.end_date)
        self.tearDown()

    def test_set_swot(self):
        ''' Tests the set_swot method '''
        self.setUp()
        self.associate.set_swot(100)
        self.assertEqual(100, self.associate.swot)
        self.tearDown()

    def test_set_status(self):
        ''' Tests the set_status method '''
        self.setUp()
        self.associate.set_status(100)
        self.assertEqual(100, self.associate.status)
        self.tearDown()

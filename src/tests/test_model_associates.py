'''This is the unittest file for the Associate class'''
import unittest

from src.models.associates import Associate
from src.logging import get_logger
_log = get_logger(__name__)

class AssociateTestSuite(unittest.TestCase):
    '''Test suite for the Associate class'''
    associate = None
    def setUp(self):
        self.associate = Associate(0, 'test@email.com', 1, 2, 'end date')
    def tearDown(self):
        self.associate = None
    @classmethod
    def setUpClass(cls):
        cls.associate = Associate()
    @classmethod
    def tearDownClass(cls):
        cls.associate = None

    '''getters'''
    def test_get_salesforce_id(self):
        self.setUp()
        self.assertEqual(0, self.associate.get_salesforce_id())
        self.tearDown()
    
    def test_get_email(self):
        self.setUp()
        self.assertEqual('test@email.com', self.associate.get_email())
        self.tearDown()

    def test_get_manager_id(self):
        self.setUp()
        self.assertEqual(1, self.associate.get_manager_id())
        self.tearDown()

    def test_get_manager_id(self):
        self.setUp()
        self.assertEqual(2, self.associate.get_batch_id())
        self.tearDown()
    
    def test_get_end_date(self):
        self.setUp()
        self.assertEqual('end date', self.associate.get_end_date())
        self.tearDown()

    def test_get_swot(self):
        self.setUp()
        self.assertEqual(None, self.associate.get_swot())
        self.tearDown()
    
    def test_get_status(self):
        self.setUp()
        self.assertEqual('Active', self.associate.get_status())
        self.tearDown()

    '''setters'''
    def test_set_id(self):
        self.setUp()
        self.associate.set_salesforce_id(100)
        self.assertEqual(100, self.associate.salesforce_id)
        self.tearDown()
    
    def test_set_email(self):
        self.setUp()
        self.associate.set_email(100)
        self.assertEqual(100, self.associate.email)
        self.tearDown()

    def test_set_manager_id(self):
        self.setUp()
        self.associate.set_manager_id(100)
        self.assertEqual(100, self.associate.manager_id)
        self.tearDown()

    def test_set_batch_id(self):
        self.setUp()
        self.associate.set_batch_id(100)
        self.assertEqual(100, self.associate.batch_id)
        self.tearDown()
    
    def test_set_end_date(self):
        self.setUp()
        self.associate.set_end_date(100)
        self.assertEqual(100, self.associate.end_date)
        self.tearDown()

    def test_set_swot(self):
        self.setUp()
        self.associate.set_swot(100)
        self.assertEqual(100, self.associate.swot)
        self.tearDown()
    
    def test_set_status(self):
        self.setUp()
        self.associate.set_status(100)
        self.assertEqual(100, self.associate.status)
        self.tearDown()
    
'''This is the unittest file for the Associate class'''
import unittest

from src.models.associates import Associate
from src.testing_logging.logger import get_logger
_log = get_logger(__name__)

class AssociateTestSuite(unittest.TestCase):
    '''Test suite for the Associate class'''
    associate = None
    def setUp(self):
        self.associate = Associate(0, 'test@email.com', 1, 'end date')
    def tearDown(self):
        self.associate = None
    @classmethod
    def setUpClass(cls):
        cls.associate = Associate()
    @classmethod
    def tearDownClass(cls):
        cls.associate = None

    '''getters'''
    def test_get_id(self):
        self.setUp()
        self.assertEqual(0, self.associate.get_id())
        self.tearDown()
    
    def test_get_email(self):
        self.setUp()
        self.assertEqual('test@email.com', self.associate.get_email())
        self.tearDown()

    def test_get_manager_id(self):
        self.setUp()
        self.assertEqual(1, self.associate.get_manager_id())
        self.tearDown()
    
    def test_get_end_date(self):
        self.setUp()
        self.assertEqual('end date', self.associate.get_end_date())
        self.tearDown()

    def test_get_SWOT(self):
        self.setUp()
        self.assertEqual(None, self.associate.get_SWOT())
        self.tearDown()
    
    def test_get_status(self):
        self.setUp()
        self.assertEqual('Active', self.associate.get_status())
        self.tearDown()
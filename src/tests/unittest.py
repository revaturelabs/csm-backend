'''This modual is the driver for unit tests in python
    Each file should have its own file for testing
    the file after a test is written it should be imported below'''
import unittest
from src.tests.test_swot import SwotTests
from src.tests.test_caliber_processing import CaliberProcessingTest
from src.tests.test_associates_db import AssociateTestDatabase
from src.tests.test_managers_db import ManagerTestDatabase
from src.tests.test_model_associates import AssociateTestSuite


if __name__ == '__main__':
    unittest.main()

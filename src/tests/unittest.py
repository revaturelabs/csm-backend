'''This modual is the driver for unit tests in python
    Each file should have its own file for testing
    the file after a test is written it should be imported below'''
import unittest
from src.tests.test_swot import SwotTests
from src.tests.test_associate_db import TestDatabase
from src.tests.test_caliber_processing import Caliber_processing_test
# test imports
'''when you import a test file be sure to import each test class in the file'''



if __name__ == '__main__':
    unittest.main()

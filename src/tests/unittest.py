'''This modual is the driver for unit tests in python
    Each file should have its own file for testing
    the file after a test is written it should be imported below'''
import unittest
from src.tests.test_swot import SwotTests
from src.tests.test_caliber_processing import Caliber_processing_test

if __name__ == '__main__':
    unittest.main()

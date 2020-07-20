'''This modual is the driver for unit tests in python
    Each file should have its own file for testing
    the file after a test is written it should be imported below'''
import unittest
from src.tests.test_swot import SwotTests
from src.tests.test_db import TestDatabase
# test imports
'''when you import a test file be sure to import each test class in the file'''



if __name__ == '__main__':
    unittest.main()

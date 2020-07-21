'''This modual is the driver for unit tests in python
    Each file should have its own file for testing
    the file after a test is written it should be imported below'''
import unittest
from src.tests.test_swot import SwotTests
from src.tests.test_db import TestDatabase
# test imports
'''when you import a test file be sure to import each test class in the file'''
<<<<<<< HEAD:src/testing_logging/unittest.py
from src.testing_logging.tests.sample_test import SampleTest
from src.testing_logging.tests.test_model_associates import AssociateTestSuite
from src.testing_logging.tests.test_swot import SwotTests
from src.testing_logging.tests.test_db import TestDatabase
=======

>>>>>>> b4e9fdab3c6b4db6e84d0778b8ce1ccc57cf1885:src/tests/unittest.py



if __name__ == '__main__':
    unittest.main()

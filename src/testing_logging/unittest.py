'''This modual is the driver for unit tests in python
    Each file should have its own file for testing 
    the file after a test is written it should be imported below'''
import unittest
# test imports
'''when you import a test file be sure to import each test class in the file'''
from src.testing_logging.tests.sample_test import SampleTest
<<<<<<< HEAD
from src.testing_logging.tests.test_model_associates import AssociateTestSuite
=======
from src.testing_logging.tests.test_swot import SwotTests
from src.testing_logging.tests.test_db import TestDatabase

>>>>>>> 9417c9945bec7cf56c19e6873ec3b11ecd882c84


if __name__ == '__main__':
    unittest.main()
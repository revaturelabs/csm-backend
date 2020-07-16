'''This modual is the driver for unit tests in python
    Each file should have its own file for testing 
    the file after a test is written it should be imported below'''
import unittest
# test imports
'''when you import a test file be sure to import each test class in the file'''
from src.testing_logging.tests.sample_test import SampleTest
from src.testing_logging.tests.test_model_associates import AssociateTestSuite


if __name__ == '__main__':
    unittest.main()
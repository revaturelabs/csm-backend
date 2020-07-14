'''This modual is the driver for unit tests in python
    Each file should have its own file for testing 
    the file after a test is written it should be imported below'''
import unittest
# test imports
'''when you import a test file be sure to import each test class in the file'''
from src.unittest.sample_test import SampleTest



if __name__ == '__main__':
    unittest.main()
'''This is a sample unittest'''
import unittest


class SampleTest(unittest.TestCase):
    '''this class is the sample unittest'''
    def test_sample(self):
        '''this is the sample test method'''
        self.assertAlmostEqual(1, 1)
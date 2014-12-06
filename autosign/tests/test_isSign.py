import unittest
import os
from autosign.main import isSign

class TestisSign(unittest.TestCase):
    """
    tests the isSign function in main module
    """
    def test_signed_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/signed')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(isSign(fName), True)

    def test_unsigned_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/unsigned')
        for filename in os.listdir(path):
            fName = os.path.join(path, filename)
            self.assertEqual(isSign(fName), False)
import unittest
import os
from signature.main import getIndex

class TestgetIndex(unittest.TestCase):
    """
    tests the getIndex function in main module
    """
    def test_signed_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/signed')
        for filename in os.listdir(path):
            print os.path.join(path, filename)
            start, end = getIndex(path, filename)
            self.assertNotEqual(start, None)
            self.assertNotEqual(end, None)
            length = end - start
            self.assertNotEqual(length, 0)

    def test_unsigned_files(self):
        dire = os.path.dirname(__file__)
        path = os.path.join(dire, 'testData/unsigned')
        for filename in os.listdir(path):
            print os.path.join(path, filename)
            start, end = getIndex(path, filename)
            self.assertEqual(start, None)
            self.assertEqual(end, None)


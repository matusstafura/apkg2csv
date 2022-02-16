import unittest
import sys,os

sys.path.append("src")
from script import *


class TestFile(unittest.TestCase):
    def test_header(self):
        x = header(connect('tests/tempfile'))
        self.assertEqual(['English', 'French', 'Word Type', 'Example', 'Example in English'],x)

if __name__ == '__main__':
    unittest.main()
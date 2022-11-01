from string import capwords
import unittest
import sys

sys.path.append("src")
from script import header, connect, values

class TestFile(unittest.TestCase):
    def test_header(self):
        x = header(connect('tests/tempfile'))
        self.assertEqual(['English', 'French', 'Word Type', 'Example', 'Example in English'],x)
    
    def test_values(self):
        cards = values(connect('tests/tempfile'))
        self.assertEqual([
            ['cat', 'le chat', 'noun', 'je vois le chat', 'I see the cat'],
            ['chien', 'le chien', 'noun', 'le chien me voit', 'the dog sees me']], 
        cards)
    
    def test_file(self):
        notAFile = connect('tests/temp.apkg')
        self.assertRaises(Exception,notAFile)


if __name__ == '__main__':
    unittest.main()
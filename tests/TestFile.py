import unittest
import sys
from string import capwords
sys.path.append("src")
from dbconnect import DBConnect

class TestFile(unittest.TestCase):
    def setUp(self):
        self.conn = DBConnect.connect('tests/tempfile')

    def test_header(self):
        header = DBConnect.header(self.conn)
        self.assertEqual(['English', 'French', 'Word Type', 'Example', 'Example in English'],header)
    
    def test_values(self):
        cards = DBConnect.values(self.conn)
        self.assertEqual([
            ['cat', 'le chat', 'noun', 'je vois le chat', 'I see the cat'],
            ['chien', 'le chien', 'noun', 'le chien me voit', 'the dog sees me'],
            ['king', 'roi', 'noun, masculine', "Le Prince Charles deviendra un jour Roi d'Angleterre.", 'Prince Charles will be King of England one day.&nbsp;']], 
        cards)
    
    def test_file(self):
        notAFile = DBConnect.connect('tests/temp.apkg')
        self.assertRaises(Exception,notAFile)

if __name__ == '__main__':
    unittest.main()

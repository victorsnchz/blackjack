import unittest
import sys

sys.path.append('src/game')
from rules import Rules

class TestRulesTypeCheck(unittest.TestCase):

    def test_number_of_decks(self):

        with self.assertRaises(TypeError):
            Rules(number_of_decks = 1.5) 

    def test_reshuffle_frequency(self):
        with self.assertRaises(TypeError):
            Rules(reshuffle_frequency = 'frequent')
        
    def test_surrender(self):    
        with self.assertRaises(TypeError):
            Rules(surrender = 'True')

class TestRulesValueCheck(unittest.TestCase):

    def test_number_of_decks(self):

        with self.assertRaises(ValueError):
            Rules(number_of_decks = 0)

if __name__ == '__main__':
    unittest.main()
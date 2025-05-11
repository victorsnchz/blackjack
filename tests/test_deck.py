import unittest
import sys
import copy

sys.path.append('src/game')
from deck import Deck
from cards import Card

class TestDeckInit(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_cards_full_deck(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_cards_unicity(self):
        self.assertEqual(len(self.deck.cards), len(set(self.deck.cards)))

class TestModifiersFunctions(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_draw(self):
        self.assertEqual(type(self.deck.draw()), Card)

    def test_remaining_cards(self):
        self.assertEqual(self.deck.remaining_cards(), 52)

    def test_remaining_cards_after_draw(self):
        self.assertEqual(type(self.deck.draw()), Card)
        self.assertEqual(self.deck.remaining_cards(), 51)

    def test_draw_until_deck_empty(self):
        
        cards_count = self.deck.remaining_cards()
        
        while not self.deck.is_empty():
            self.assertEqual(type(self.deck.draw()), Card)
            cards_count -= 1
            self.assertEqual(self.deck.remaining_cards(), cards_count)

        self.assertEqual(self.deck.is_empty(), True)

    def test_shuffle_deck(self):

        first_shuffle = copy.copy(self.deck.cards)
        self.deck.shuffle()
        second_shuffle = copy.copy(self.deck.cards)
        
        self.assertNotEqual(first_shuffle, second_shuffle)

class TestBooleanFunctions(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_is_empty(self):
        self.assertEqual(self.deck.is_empty(), False)

if __name__ == '__main__':
    unittest.main()
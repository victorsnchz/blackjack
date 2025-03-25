import unittest
from collections import defaultdict

import sys
sys.path.append('src/game')
from rules import Rules
from player import Player, HumanPlayer
from cards import Value, broadways, Card, Suit

class TestPlayerCards(unittest.TestCase):

    def setUp(self):
        self.player = HumanPlayer(Rules())
        self.target = defaultdict(int)

    def test_no_cards(self):
        self.assertEqual(self.player.player_cards, self.target)

    def test_add_one_card(self):
        card = Card(Suit.SPADES, Value.TWO)
        self.target[card.card_value] = 1

        # must trigger default dict for ACE to match player dict
        self.target[Value.ACE] = 0
        self.player.add_new_card(card)
        self.assertDictEqual(self.player.player_cards, self.target)

    def test_reset_player_cards(self):
        card = Card(Suit.SPADES, Value.TWO)
        self.player.add_new_card(card)
        self.player.reset_player_cards()
        self.assertEqual(self.player.player_cards, self.target)

class TestPlayerScore(unittest.TestCase):

    def setUp(self):
        self.player = HumanPlayer(Rules())

    def test_no_score(self):
        self.assertEqual(self.player.live_score, 0)
    
    def test_score_one_numeric_cards(self):

        card = Card(Suit.CLUBS, Value.TWO)
        self.player.add_new_card(card)

        self.assertEqual(self.player.score, card.card_value.value)

    def test_score_one_broadway(self):
        card = Card(Suit.HEARTS, Value.QUEEN)
        self.player.add_new_card(card)

        self.assertEqual(self.player.score, 10)

    def test_score_one_ace(self):
        card = Card(Suit.SPADES, Value.ACE)
        self.player.add_new_card(card)

        self.assertEqual(self.player.score, 11)

    def test_score_one_ace_one_broadway(self):
        card = Card(Suit.SPADES, Value.ACE)
        self.player.add_new_card(card)
        card = Card(Suit.DIAMONDS, Value.JACK)
        self.player.add_new_card(card)

        self.assertEqual(self.player.score, 21)

    def test_score_three_numeric(self):

        cards = (Card(Suit.SPADES, Value.THREE), 
                 Card(Suit.SPADES, Value.FOUR),
                 Card(Suit.SPADES, Value.FIVE))

        target = 0
        for card in cards:
            self.player.add_new_card(card)
            target += card.card_value.value
            self.assertEqual(self.player.score, target)

    def test_multiple_aces(self):

        cards = (Card(Suit.SPADES, Value.ACE), 
                 Card(Suit.SPADES, Value.ACE),
                 Card(Suit.SPADES, Value.NINE),
                 Card(Suit.SPADES, Value.TWO))

        target_scores = (11, 12, 21, 13)

        for card, target in zip(cards, target_scores):

            self.player.add_new_card(card)
            self.assertEqual(self.player.score, target)

if __name__ == '__main__':
    unittest.main()
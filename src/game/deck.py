import dataclasses
import random

from cards import Card, Value, Suit

@dataclasses.dataclass
class Deck:

    cards = list(Card(suit, value) for suit in Suit for value in Value)

    def shuffle(self):
        random.shuffle(self.cards)

    def remaining_cards(self) -> int:
        return len(self.cards)

    def is_empty(self) -> bool:
        return not bool(self.cards)
    
    def is_card_in_deck(self, card: Card) -> bool:
        return card in self.cards

    def draw(self) -> Card:
        
        if self.is_empty():
            raise KeyError('Cannot draw from an empty deck.')
        
        return self.cards.pop()
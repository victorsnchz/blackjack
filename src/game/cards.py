import enum
import dataclasses

class Suit(enum.Enum):
    SPADES = 'S'
    HEARTS = 'H'
    CLUBS = 'C'
    DIAMONDS = 'D'

class Value(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    
    # introduce an extra method to handle the broadway cards
    JACK = 11
    QUEEN = 12
    KING = 13

broadways = (Value.JACK, Value.QUEEN, Value.KING)

@dataclasses.dataclass(frozen=True)
class Card:
    
    suit: Suit
    card_value: Value
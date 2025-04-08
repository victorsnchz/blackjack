from abc import ABC, abstractmethod
from collections import defaultdict

from bookkeeping import Moves
from cards import Card, Value, broadways
from rules import Rules

class Player(ABC):
    
    def __init__(self, rules: Rules):
        self.rules = rules
        self.player_cards = defaultdict(int)
        self.live_score: int = 0
    
    @abstractmethod
    def next_move(self) -> Moves:
        print('do nothing')

    def update_score(self):

        score = 0

        for card_value, count in self.player_cards.items():
            if card_value == Value.ACE:
                aces = count
            
            elif card_value in broadways:
                score += 10 * count
            
            else:
                score += card_value.value * count

        aces = self.player_cards[Value.ACE]
        if aces != 0:

            if score + aces > 11:
                score +=  aces

            else:
                score += 11 + aces - 1

        self.score = score

    def add_new_card(self, card: Card) -> None:
        self.player_cards[card.card_value] += 1
        self.update_score()

    def reset_player_cards(self) -> None:
        self.player_cards = defaultdict(int)

class Dealer(Player):

    def __init__(self, rules):
        super().__init__(rules)
    
    def reset_live_cards(self):
        return super().reset_live_cards()

    def update_live_cards(self, reshuffle=False) -> None:
        pass

    def next_move(self):
        print('dealer next move')
    
class HumanPlayer(Player):

    def __init__(self, rules):
        super().__init__(rules)

    def reset_live_cards(self):
        return super().reset_live_cards()

    def update_live_cards(self, reshuffle=False) -> None:

        """ Empty method for player, exists for polymorphism.
        
        Could in the future implement live-metrics for players to help in 
        decision making.
        """
        pass

    def next_move(self) -> Moves:
        print('human next move')

class Bot(Player):

    def __init__(self, rules):
        super().__init__(rules)

        self.cards_history = defaultdict(int)

    def update_live_cards(self, reshuffle=False):
        pass

    def next_move(self) -> Moves:
        print('bot next move')
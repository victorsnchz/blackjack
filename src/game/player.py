from abc import ABC, abstractmethod

from bookkeeping import Moves

class Player(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def update_live_cards(self, reshuffle = False) -> None:
        pass

    @abstractmethod
    def next_move(self) -> Moves:
        pass

class Dealer(Player):

    def __init__(self):
        super().__init__()
    
    def update_live_cards(self, reshuffle=False) -> None:
        pass

    def next_move(self) -> Moves:
        pass
    
class HumanPlayer(Player):
    
    def __init__(self):
        super().__init__()

    def update_live_cards(self, reshuffle=False) -> None:

        """ Empty method for player, exists for polymorphism.
        
        Could in the future implement live-metrics for players to help in 
        decision making.
        """
        pass

    def next_move(self) -> Moves:
        return super().next_move()

class Bot(Player):
    def __init__(self):
        super().__init__()

    def update_live_cards(self, reshuffle=False):
        pass

    def next_move(self) -> Moves:
        return super().next_move()
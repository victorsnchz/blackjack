from abc import ABC, abstractmethod

class Player(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def next_move(self):
        pass

class Dealer(Player):

    def __init__(self):
        super().__init__()
    
    
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

class Bot(Player):
    def __init__(self):
        super().__init__()
from rules import Rules
from player import Player, Dealer

class Game:
    
    def __init__(self):
        
        self.rules = Rules()

        self.dealer = Dealer(self.rules)
        
        self.players = dict()
        pass

    def play_round(self):
        
        # shuffle deck based on re-shuffle rules
        # 

        pass

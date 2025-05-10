from dataclasses import dataclass

@dataclass
class Bankroll:

    current: float

    def __post_init__(self):

        self.verify_values()

        self.history = list(tuple)

        
    def verify_values(self):
        
        if type(self.current) is not float:
            raise TypeError('Current bankroll value must be of type',
                            f'float not {type(self.current)}')

        if self.current < 0:
            raise ValueError('Current bankroll value must be non negative',
                            f'not {self.current}')
        
    
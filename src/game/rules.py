import dataclasses
from bookkeeping import ReshuffleFrequency

@dataclasses.dataclass(frozen=True)
class GameConfig:
    MIN_DEKCS: int = 1


@dataclasses.dataclass(frozen=True)
class Rules:

    number_of_decks: int = 1
    reshuffle_frequency: ReshuffleFrequency = ReshuffleFrequency.LOW
    surrender: bool = False

    def __post_init__(self):
        
        if type(self.number_of_decks) is not int:
            raise TypeError('Number of decks must be an integer not ',
                            f'{type(self.number_of_decks)}')
        
        if self.number_of_decks < GameConfig.MIN_DEKCS:
            raise ValueError('Number of decks must be AT LEAST '
                             f'{GameConfig.MIN_DEKCS}.')
        
        if type(self.reshuffle_frequency) is not ReshuffleFrequency:
            raise TypeError('Reshuffle frequency must be a ReshuffleFrequency object ',
                            f'{type(self.reshuffle_frequency)}')
        
        if type(self.surrender) is not bool:
            raise TypeError('Option to allow surrender must be a boolean not ',
                            f'{type(self.surrender)}')
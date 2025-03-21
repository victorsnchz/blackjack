import enum

class ReshuffleFrequency(enum.Enum):
    LOW = enum.auto()
    MODERATE = enum.auto()
    HIGH = enum.auto()

class Moves(enum.Enum):
    pass

class PlayerMoves(Moves):
    HIT = enum.auto()
    STAND = enum.auto()
    DOUBLE_DOWN = enum.auto()
    SPLIT = enum.auto()
    SURRENDER = enum.auto()

class DealerMoves(Moves):
    HIT = enum.auto()
    STAND = enum.auto()
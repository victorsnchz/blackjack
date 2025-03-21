import enum

class ReshuffleFrequency(enum.Enum):
    LOW = enum.auto()
    MODERATE = enum.auto()
    HIGH = enum.auto()

class PlayerMoves(enum.Enum):
    HIT = enum.auto()
    STAND = enum.auto()
    DOUBLE_DOWN = enum.auto()
    SPLIT = enum.auto()
    SURRENDER = enum.auto()

class DealerMoves(enum.Enum):
    HIT = enum.auto()
    STAND = enum.auto()
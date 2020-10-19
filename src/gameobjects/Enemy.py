from collections import namedtuple
from game.GameError import GameError
from gameobjects.GameObject import GameObject

def minmax(obj):
    MinMax = namedtuple('MinMax', ['min', 'max'])
    if type(obj) is dict:
        return MinMax(int(obj['min']), int(obj['max']))
    return MinMax(int(obj), int(obj))

class Enemy(GameObject):
    """
    Represents an Enemy within the game.

    @author Jacob Heard
    @editor Nausher Rao (SherRao#8509)
    """
    attributes = {
        'name': (True, lambda x: x),
        'health': (True, minmax),
        'defence': (True, minmax),
        'attack': (True, minmax),
        'xp': (True, minmax)
    }

    def __init__(self):
        super().__init__(self)

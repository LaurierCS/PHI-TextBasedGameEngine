from GameError import GameError
from random import randint
from Util import Util


class Enemy(object):
    def __init__(self, name : str, attack : int, health : int, defence : int, xp : int):
        self.name = name
        self.attack = attack
        self.health = health
        self.defence = defence
        self.xp = xp


class EnemyTemplate(object):
    
    def __init__(self, yml):
        try:
            self.name = yml['name']
            self.health = Util.parse_minmax_object(yml, 'health', int)
            self.attack = Util.parse_minmax_object(yml, 'attack', int)
            self.defence = Util.parse_minmax_object(yml, 'defence', int)
            self.xp = Util.parse_minmax_object(yml, 'xp', int)
        except (KeyError, ValueError) as err:
            name = '<no name provided>' if 'name' not in yml else yml['name']
            raise GameError("Error loading enemy '{}' : {}".format(name, err))

    def create_enemy(self) -> Enemy:
        """
        Factory/builder method to create an enemy object from
        this template
        """
        attack = randint(self.attack['min'], self.attack['max'])
        health = randint(self.health['min'], self.health['max'])
        xp = randint(self.xp['min'], self.xp['max'])
        defence = randint(self.defence['min'], self.defence['max'])
        return Enemy(self.name, attack, health, defence, xp)


from GameError import GameError
from random import randint
from Util import Util


class Enemy(object):
    """
    For a single instance of an enemy in game.
    """
    def __init__(self, name : str, attack : int, health : int, defence : int, xp : int):
        """
        @param name The name of the enemy (Example: "spider")
        @param attack Points of damage this enemy can do
        @param health Starting number of health points
        @param defence How much damage can be deflected per hit
        @param xp Number of experience points to award for beating this enemy
        """
        self.name = name
        self.attack = attack
        self.health = health
        self.defence = defence
        self.xp = xp


class EnemyTemplate(object):
    """
    A template for creating enemy instances, each template corresponds to 1 entry in the enemies.yaml file
    """
    
    def __init__(self, yml):
        """
        @param yml object parsed from yaml representing an enemy blueprint
        """
        self.name = yml['name']
        self.health = Util.parse_minmax_object(yml, 'health', int)
        self.attack = Util.parse_minmax_object(yml, 'attack', int)
        self.defence = Util.parse_minmax_object(yml, 'defence', int, 0)
        self.xp = Util.parse_minmax_object(yml, 'xp', int, 0)

    def create_enemy(self) -> Enemy:
        """
        Factory/builder method to create an enemy object from
        this template
        @return an enemy object created from this template
        """
        attack = randint(self.attack['min'], self.attack['max'])
        health = randint(self.health['min'], self.health['max'])
        xp = randint(self.xp['min'], self.xp['max'])
        defence = randint(self.defence['min'], self.defence['max'])
        return Enemy(self.name, attack, health, defence, xp)


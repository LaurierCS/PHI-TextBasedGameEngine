from random import randint
from game.GameError import GameError
from game.YamlUtil import YamlUtil
from gameobjects.Entity import Entity

class Enemy(Entity):
    """
    Represents an Enemy within the game.

    @editor Nausher Rao (SherRao#8509)
    """

    def __init__(self, name: str, health: int, defence: int, attack: int, xp: int):
        """
        @param attack Points of damage this enemy can do
        @param xp Number of experience points to award for beating this enemy
        """
        super().__init__(self, name, False, health, defence)
        self.attack = attack
        self.xp = xp

    def update(self):
        pass;


class EnemyTemplate(object):
    """
    A template for creating enemy instances, each template corresponds to 1 entry in the enemies.yaml file
    """
    
    def __init__(self, yml):
        """
        @param yml object parsed from yaml representing an enemy blueprint
        """
        self.name = yml['name']
        self.health = YamlUtil.parse_minmax_object(yml, 'health', int)
        self.attack = YamlUtil.parse_minmax_object(yml, 'attack', int)
        self.defence = YamlUtil.parse_minmax_object(yml, 'defence', int, 0)
        self.xp = YamlUtil.parse_minmax_object(yml, 'xp', int, 0)

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
        return Enemy(self.name, health, defence, attack, xp)


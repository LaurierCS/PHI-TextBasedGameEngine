from GameError import GameError
from random import randint

class EnemyTemplate(object):
    
    def __init__(self, yml):
        try:
            self.name = yml['name']
            self.min_health = yml['min_health']
            self.max_health = yml['max_health']
            self.min_defense = yml['min_defense']
            self.max_defense = yml['max_defense']
            self.min_xp = yml['min_xp']
            self.max_xp = yml['max_xp']
        except KeyError as err:
            name = '<no name provided>' if 'name' not in yml else yml['name']
            raise GameError("Error loading enemy '{}' : {}".format(name, err))

    def create_enemy(self):
        health = randint(self.min_hp, self.max_xp+1)
        xp = randint(self.min_xp, self.max_xp+1)
        defense = randint(self.min_defense, self.max_defense+1)
        return Enemy(self.name, health, defense, xp)


class Enemy(object):
    def __init__(self, name, health, defense, xp):
        self.name = name
        self.health = health
        self.defense = defense
        self.xp = xp

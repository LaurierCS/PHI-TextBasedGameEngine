from GameError import GameError
from random import randint

class EnemyTemplate(object):
    
    def __init__(self, yml):
        try:
            self.name = yml['name']
            if 'health' in yml:
                self.min_health = int(yml['health'])
                self.max_health = int(yml['health'])
            else:
                self.min_health = int(yml['min_health'])
                self.max_health = int(yml['max_health'])
            if 'attack' in yml:
                self.min_attack = int(yml['attack'])
                self.max_attack = int(yml['attack'])
            else:
                self.min_attack = int(yml['min_attack'])
                self.max_attack = int(yml['max_attack'])

            if 'defence' in yml:
                self.min_defence = int(yml['defence'])
                self.max_defence = int(yml['defence'])
            else:
                self.min_defence = int(yml['min_defence'])
                self.max_defence = int(yml['max_defence'])
            if 'xp' in yml:
                self.min_xp = int(yml['xp'])
                self.max_xp = int(yml['xp'])
            else:
                self.min_xp = int(yml['min_xp'])
                self.max_xp = int(yml['max_xp'])
        except (KeyError, ValueError) as err:
            name = '<no name provided>' if 'name' not in yml else yml['name']
            raise GameError("Error loading enemy '{}' : {}".format(name, err))

    def create_enemy(self):
        attack = randint(self.min_attack, self.max_attack+1)
        health = randint(self.min_health, self.max_health+1)
        xp = randint(self.min_xp, self.max_xp+1)
        defence = randint(self.min_defence, self.max_defence+1)
        return Enemy(self.name, attack, health, defence, xp)


class Enemy(object):
    def __init__(self, name, attack, health, defence, xp):
        self.name = name
        self.attack = attack
        self.health = health
        self.defence = defence
        self.xp = xp

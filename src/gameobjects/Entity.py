from game.Game import Game
from game.GameError import GameError
from game.YamlUtil import YamlUtil
from random import randint

class Entity(object):
    """
    Represents an Entity within the game, such as NPC's, animals, or enemies.

    @author Nausher Rao (SherRao#8509)
    """

    def __init__(self, game: Game, name: str, friendly: bool, health: int, defence: int ):
        """
        @param game The instance of the game controlling this entity
        @param name The name of the enemy (Example: "spider")
        @param friendly Whether the entity is friendly toward the player or not
        @param health Starting number of health points
        @param defence How much damage can be deflected per hit
        """
        self.game = game
        self.name = name
        self.friendly = friendly
        self.health = health
        self.defence = defence

    def update(self):
        """
        Called when this entity should update its logic
        """
        pass;



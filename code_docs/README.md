# Python Documentation

## Classes

**[Interaction](Interaction.md)**: Represents an in-game interaction. For example: a user entering a room and being provided with choice of what to do. 

**[Enemy](Enemy.md)**: Represents an Enemy within the game.   


**[EnemyTemplate](EnemyTemplate.md)**: A template for creating enemy instances, each template corresponds to 1 entry in the enemies.yaml file 

**[Item](Item.md)**: An item object enables developers to add usable/interactable that the player can pickup, drop, and use.   


**[Entity](Entity.md)**: Represents an Entity within the game, such as NPC's, animals, or enemies.   


**[GameError](GameError.md)**: A custom exception for providing more information to the user. The general use of this class is to catch an exception, add some additional information, then raise GameError 

**[Game](Game.md)**: A Game object is an instance of one entire game. It keeps track of all enemy templates, rooms, items, player info, and so on. 

**[YamlUtil](YamlUtil.md)**: a static utility class, all utility functions with no better place to live should go in here 


## Functions

# Python Documentation

## Classes

**[Util](Util.md)**: a static utility class, all utility functions with no better place to live should go in here 

**[Enemy](Enemy.md)**: For a single instance of an enemy in game. 

**[EnemyTemplate](EnemyTemplate.md)**: A template for creating enemy instances, each template corresponds to 1 entry in the enemies.yaml file 

**[Game](Game.md)**: A Game object is an instance of one entire game. It keeps track of all enemy templates, rooms, items, player info, and so on. 

**[GameError](GameError.md)**: A custom exception for providing more information to the user. The general use of this class is to catch an exception, add some additional information, then raise GameError 



## Functions


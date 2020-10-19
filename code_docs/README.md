# Python Documentation

## Classes

**[ValidGameObject](ValidGameObject.md)**: 

**[GameObject](GameObject.md)**: Base class to be used for all in-game instantiable objects 

**[Interaction](Interaction.md)**: Represents an in-game interaction. For example: a user entering a room and being provided with choice of what to do. 

**[Enemy](Enemy.md)**: Represents an Enemy within the game.   


**[Item](Item.md)**: An item object enables developers to add usable/interactable that the player can pickup, drop, and use.   


**[GameError](GameError.md)**: A custom exception for providing more information to the user. The general use of this class is to catch an exception, add some additional information, then raise GameError 

**[Game](Game.md)**: A Game object is an instance of one entire game. It keeps track of all enemy templates, rooms, items, player info, and so on. 

**[YamlUtil](YamlUtil.md)**: a static utility class, all utility functions with no better place to live should go in here 


## Functions

### test_parser_validate







### test_parser_binary







### test_parser_compile







### set_gameobject_id



#### Parameters
name | description | default
--- | --- | ---
id |  | 





### test_load_from_template







### test_instantiate_gameobject_subclass







### test_missing_required_attribute







### test_unexpected_attribute







### minmax



#### Parameters
name | description | default
--- | --- | ---
obj |  | 





### tokenize



#### Parameters
name | description | default
--- | --- | ---
effect |  | 
error |  | 





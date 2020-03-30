# Game


A Game object is an instance of one entire game. It keeps track of all enemy templates, rooms, items, player info, and so on. 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
enemies | List of EnemyTemplate objects | 
items | TODO: not yet implemented | 
rooms | TODO: not yet implemented | 
player | TODO: not yet implemented | 
self |  | 





### save_game_state


Saves the current state of the game into a file TODO: not yet implemented 

#### Parameters
name | description | default
--- | --- | ---
save_path | the path of the file to write game data into | 
self |  | 





### load_game_state


Loads a game state previously saved by save_game_state. TODO: not yet implemented 

#### Parameters
name | description | default
--- | --- | ---
load_path | the path of the save file to load | 
self |  | 





### load_game


Loads yaml files from input directory into a game object. 

#### Parameters
name | description | default
--- | --- | ---
directory | directory to load the game from | 





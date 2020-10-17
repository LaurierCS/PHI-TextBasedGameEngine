from Util import Util

class Game(object):
    """
    A Game object is an instance of one entire game. It keeps
    track of all enemy templates, rooms, items, player info, and 
    so on.
    """
    
    def __init__(self, enemies, items, rooms, player):
        """
        @param enemies List of EnemyTemplate objects
        @param items TODO: not yet implemented
        @param rooms TODO: not yet implemented
        @param player TODO: not yet implemented
        """
        # TODO: These might not all be arrays (player in particular)
        self.enemies = []
        self.items = []
        self.rooms = []
        self.player = []
    
    def save_game_state(self, save_path : str) -> None:
        """
        Saves the current state of the game into a file
        TODO: not yet implemented
        @param save_path the path of the file to write game data into
        """
        pass
    
    def load_game_state(self, load_path : str) -> None:
        """
        Loads a game state previously saved by save_game_state.
        TODO: not yet implemented
        @param load_path the path of the save file to load
        """
        pass
    
    @staticmethod
    def load_game(directory : str):
        """
        Loads yaml files from input directory into a game object.
        @param directory directory to load the game from
        @return a loaded Game object
        """
        enemies = Util.load_yaml_data( Util.get_yaml_filename("enemies") )
        rooms = Util.load_yaml_data( Util.get_yaml_filename("rooms") )
        items = Util.load_yaml_data( Util.get_yaml_filename("items") )
        player = Util.load_yaml_data( Util.get_yaml_filename("player") )
        return Game(enemies, items, rooms, player)

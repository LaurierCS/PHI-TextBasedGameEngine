class Game(object):

    def __init__(self, enemies, items, rooms, player):
        # TODO: These might not all be arrays (player in particular)
        self.enemies = []
        self.items = []
        self.rooms = []
        self.player = []
    
    def save_game_state(self, save_path : str) -> None:
        pass
    
    @staticmethod
    def load_game(directory : str) -> Game:
        """
        Loads yaml files from input directory into a game object
        """
        enemies = Util.load_yaml_data( Util.get_yaml_filename("enemies") )
        rooms = Util.load_yaml_data( Util.get_yaml_filename("rooms") )
        items = Util.load_yaml_data( Util.get_yaml_filename("items") )
        player = Util.load_yaml_data( Util.get_yaml_filename("player") )
        return Game(enemies, items, rooms, player)

class Game(object):

    def __init__(self):
        # TODO: These might not all be arrays (player in particular)
        self.enemies = []
        self.items = []
        self.rooms = []
        self.player = []
    
    def load_game(self, game_path : str) -> None:
        pass
    
    def save_game_state(self, save_path : str) -> None:
        pass

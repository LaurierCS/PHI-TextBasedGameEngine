import os, sys
import argparse
import pickle

from game.YamlUtil import YamlUtil
from game.Game import Game

# Create the command line argument parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('game', type=str,
        help='The directory or binary file containing the game to load')
parser.add_argument('--validate', action='store_false',
        help='Check that the yaml is correctly formatted; does not run the game')
parser.add_argument('--compile', type=str,
        help='Filename to write compiled game into')
parser.add_argument('--binary', action='store_false',
        help='Load a binary game file')

if __name__ == '__main__':
    args = parser.parse_args()

    if os.path.isdir(args.game):
        game = Game.load_game(args.game)
        if args.compile:
            with open(args.compile, 'wb') as file:
                pickle.dump(file, game)
            print(f'Successfully created {args.compile}')
    elif os.path.isfile(args.game):
        # TODO: pickle is insecure and prone to tampering, alternatives?
        # Note: Arbitrary code execution via injected pickled function
        # Is encryption + checksum viable somehow? Might require password.
        with open(args.game, 'rb') as file:
            game = pickle.load(file)
    else:
        print(f"{args.game}: game not found", file=sys.stderr)
        quit()

    print(game.enemies, game.rooms, game.player, game.items)

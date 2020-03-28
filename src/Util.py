"""
    This file contains the definition for the Util class, which is a Utility
    class that handles the interaction between the filesystem and the program's
    data.

    All methods of this class are static, and can therefore be called in the 
    following manner:
        Utils.<method_name>()
    
    This reduces the amount of code duplication when reading from files.

    Author: Nick Mills (Discord: Knifesurge#1723; Everywhere: Knifesurge)
    Editors: <IF YOU WORKED ON THIS FILE, PLEASE ADD YOUR NAME! :) >
    Date: 2020-03-26
"""
import yaml
import os.path as path
from Game import Game
from GameError import GameError


def load_data(filename : str) -> None:
    """
    Load yaml data from a file and applies custom rules (like include)
    """
    objects = []
    loaded = [] # List of files we have already loaded
    filestack = [filename] # Keep track of files we still need to load
    while len(filestack) > 0:
        # Get the next file to parse, skip if already done
        fname = filestack[-1]
        del filestack[-1]
        if fname in loaded:
            print("'{}' already loaded, skipping...".format(fname))
            continue
        
        # Get the object and add to our object list
        obj = get_yaml_object(fname)
        loaded.append( fname )
        # If we include other files, add them to the stack
        if 'include' in obj:
            filestack.extend( obj['include'] )
            del obj['include'] # Remove includes from our yaml object
        objects.append( obj )
    return objects

def get_yaml_object(filename : str) -> (bool, dict):
    """
    Wrapper method for yaml.safe_load(), loads an object from a yaml file
    """
    with open( filename, 'r' ) as stream:
        data = yaml.safe_load( stream )
        return data

def get_yaml_filename(directory : str, name_prefix : str):
    yml_extension = path.join(directory, name_prefix + ".yml")
    yaml_extension = path.join(directory, name_prefix + ".yaml")
    if path.isfile(yml_extension):
        return yml_extension
    if path.isfile(yaml_extension):
        return yaml_extension
    raise GameError("Could not find yaml file '{}'.yaml".format(name_prefix))


class Util():
    @staticmethod
    def load_game(directory : str) -> Game:
        enemies = load_data( get_yaml_filename("enemies") )
        rooms = load_data( get_yaml_filename("rooms") )
        items = load_data( get_yaml_filename("items") )
        player = load_data( get_yaml_filename("player") )
        return Game(enemies, items, rooms, player)

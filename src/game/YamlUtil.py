"""
Author: Nick Mills (Discord: Knifesurge#1723; Everywhere: Knifesurge)
<IF YOU WORKED ON THIS FILE, PLEASE ADD YOUR NAME! :) >
Editors: Jacob Heard 
Date: 2020-03-26
@author
"""
import yaml
import re
import os.path as path
from game.GameError import GameError

class YamlUtil():
    """
    a static utility class, all utility functions with no better place 
    to live should go in here
    """

    @staticmethod
    def load_yaml_data(filename : str):
        """
        Load yaml data from a file and applies custom rules (like include)
        @param filename the name of the yaml file to load
        @return a list of all yaml objects loaded from the file, & included files
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
            obj = YamlUtil.get_yaml_object(fname)
            loaded.append( fname )
            # If we include other files, add them to the stack
            if 'include' in obj:
                filestack.extend( obj['include'] )
                del obj['include'] # Remove includes from our yaml object
            objects.append( obj )
        return objects

    @staticmethod
    def get_yaml_object(filename : str):
        """
        Wrapper method for yaml.safe_load(), loads an object from a yaml file
        @param filename the name of the file to load from
        @return a python object representing the yaml file
        """
        with open( filename, 'r' ) as stream:
            data = yaml.safe_load( stream )
            print('loaded:', data)
            return data

    @staticmethod
    def get_yaml_filename(directory : str, name_prefix : str) -> str:
        """
        Helper function to get either a .yml or .yaml file given the name
        @param directory the directory to look in
        @param name_prefix the expected file name without extension
        @return the path to the file with the correct extension
        @throws GameError if neither file exists
        """
        yml_extension = path.join(directory, name_prefix + ".yml")
        yaml_extension = path.join(directory, name_prefix + ".yaml")
        if path.isfile(yml_extension):
            return yml_extension
        if path.isfile(yaml_extension):
            return yaml_extension
        raise GameError("Could not find yaml file '{}'.yaml".format(name_prefix))

    @staticmethod
    def parse_minmax_object(obj : dict, key : str, transform=lambda x: x, default=None):
        """
        Parses a value from a yaml object, returns a dictionary with
        two entries: min and max

        @param obj the dict to search in
        @param key the key to look for
        @param transform method to apply to the result (e.g. int to convert to integers)
        @param default default value to use if the key is not found
        
        @throws GameError if an expected key is missing, or the provided transform lambda fails
        @return a dict in the form {'min':min_val, 'max':max_val}
        """
        try:
            if ('min_' + key in obj) and ('max_' + key in obj):
                result = {
                    'min' : transform(obj['min_'+key]), 
                    'max' : transform(obj['max_'+key])
                }
            elif key in obj:
                result = { 
                    'min' : transform(obj[key]), 
                    'max' : transform(obj[key])
                }
            elif default is not None:
                result = {'min':default,'max':default}
            else:
                raise GameError("'{}' is a required field, but no value was provided".format(key))
        except Exception as ex:
            if ex is GameError:
                raise ex
            raise GameError("Error formatting property '{}': {}".format(key, ex))
        
        return result

    @staticmethod
    def get_names(yaml_objects):
        """
        Ensures all names are valid and unique, simplifies if necessary.

        @throws GameError is a name is invalid or duplicate
        @return a list of simplified, unique, valid names
        """
        names = set()
        for obj in yaml_objects:
            if 'name' in obj:
                name = YamlUtil.simplify_name(obj['name'])
                if not name:
                    raise GameError(f'The name "{obj["name"]}" is invalid')
                elif name in names:
                    simple = f' ({name})' if name != obj['name'] else ''
                    raise GameError(f'The name "{obj["name"]}"{simple} is used multiple times')
                names.add(name)
        return list(names)

    @staticmethod
    def simplify_name(name: str) -> str:
        """
        Simplifies a name based on naming standards. Returns the simplified name, or None if the name is invalid.

        @param name Name to simplify & validate
        @return simplified name, or '' if name is invalid
        """
        name = name.lower().strip()
        # replace multiple spaces with single space
        name = re.sub(' +', ' ', name)
        if not re.match('^[_a-z]+(( [_a-z]+)?[_a-z0-9]*)*$', name): 
            return ''
        return name

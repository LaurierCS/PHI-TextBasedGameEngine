"""
Author: Nick Mills (Discord: Knifesurge#1723; Everywhere: Knifesurge)
<IF YOU WORKED ON THIS FILE, PLEASE ADD YOUR NAME! :) >
Editors: Jacob Heard 
Date: 2020-03-26
@author
"""
import yaml
import os.path as path
from GameError import GameError

class Util():
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
            obj = Util.get_yaml_object(fname)
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

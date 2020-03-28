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

class Util():
    # No constructor needed as this class is purely static

    """
        This list holds all loaded data.
        It is modified by:
            Util.load_data()    -> Populates the list
            Util.clear_data()   -> Clears the list
    """
    _data = []

    
    @staticmethod
    def load_data(filename : str) -> None:
        """
        =====================================================================
        Attempts to read the yaml file and populate this class' data field.
        =====================================================================
        Parameters:
            | filename - The name of the file (str)
        =====================================================================
        Returns:
            None
        =====================================================================
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
        # TODO: Parse object list into *something*
        # For now, just toss all objects into our _data list
        Util._data.extend( objects )

    @staticmethod
    def get_yaml_object( filename : str ) -> (bool, dict):
        """
        Wrapper method for yaml.safe_load(), loads an object from a yaml file
        """
        with open( filename, 'r' ) as stream:
            data = yaml.safe_load( stream )
            return data

    
    @staticmethod
    def clear_data() -> None:
        """
        =====================================================================
        Clears the list of data this class holds
        =====================================================================
        Parameters:
            None
        =====================================================================
        Returns:
            None
        =====================================================================
        """
        Util.data.clear()
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
        pass

    
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
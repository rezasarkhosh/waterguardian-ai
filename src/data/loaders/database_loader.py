from .base_loader import BaseLoader
import pandas as pd


class DatabaseLoader(BaseLoader):
    """
    
    A loader class for loading data from a database.

    parameters: Database connection string
    returns: pandas DataFrame
    
    """
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def load(self):
        """

        Load data from the database.

        parameters: Database connection string
        returns: pandas DataFrame
        
        """

        raise NotImplementedError("Database loading is not implemented yet.")
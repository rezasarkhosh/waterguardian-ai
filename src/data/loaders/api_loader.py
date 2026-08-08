from .base_loader import BaseLoader
import pandas as pd

class APILoader(BaseLoader):
    """
    load Tabular data from REST API
    """

    def __init__(self, url: str):

        """
        Initialize the API loader.
        Parameters
        ----------
        url : str
            URL of the API endpoint.
        """
        # Store the API endpoint for later use.
        self.url = url



    def load(self) -> pd.DataFrame:

        """
        Load data from the API.
        Returns
        -------
        pd.DataFrame
            Data retrieved from the API.
        """
        # The API loading logic will be implemented
        # in a later sprint.
        raise NotImplementedError(
            "APILoader has not been implemented yet."
        )
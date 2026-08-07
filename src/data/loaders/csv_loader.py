from .base_loader import BaseLoader
import pandas as pd
import csv
from pathlib import Path


class CSVLoader(BaseLoader):
    """
    This loader is responsible for CSV Files

    """

    def __init__(self, path: str):
        self.path = Path(path)


    def load(self) -> pd.DataFrame:
        """
        Read a csv file and reutrns it as pandas Dataframe.
        
        """
        #File does not exit
        if not self.path.exists():
            raise FileNotFoundError(f"{self.path} does not exist")

        if not self.path.is_file():
            raise ValueError(
                f"{self.path} is not a valid file."
                )
        try:
            dataframe = pd.read_csv(self.path)
        # The file exists but contains no data.  
        except pd.errors.EmptyDataError:
            raise ValueError(
                f"The CSV file is empty: {self.path}"
            )
        # Pandas could not parse the CSV format.
        except pd.errors.ParserError:
            raise ValueError(
                f"Invalid CSV format: {self.path}"
            )


        return dataframe

        

        

    
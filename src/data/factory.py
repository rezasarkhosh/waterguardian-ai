from pathlib import Path

from .loaders.base_loader import BaseLoader
from .loaders.csv_loader import CSVLoader

class LoaderFactory:
    """
    Factory responsible for creating data loaders.
    
    """

    @staticmethod
    def create(path: str) -> BaseLoader:
        """
        Create an appropriate loader based on file type.

        Parameters:
        path: str -> Path to the input dataset.

        returns: baseloader -> A concrete loader instance.
        
        
        """
        #convert input file into a path object
        file_path = Path(path)

        if file_path.suffix.lower() == '.csv':
            return CSVLoader(path)

        raise ValueError(
            f"Unsupported file format: {file_path.suffix}"
        )
    
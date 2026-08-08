import yaml
from pathlib import Path


def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    Parameters: config_path (str): Path to the YAML configuration file.
    Returns: dict: Configuration as a dictionary.

    """

    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    #Open the YAML file for reading
    with open(path, 'r') as file:
        config = yaml.safe_load(file)

    return config

class Config:
    """
    Provide convenient access to project configuration.
    """
    def __init__(self, config_path: str):
        # Load the YAML configuration into a dictionary.
        self._config = load_config(config_path)

    @property
    def dataset_path(self) -> str:
        """
        Get the dataset path from the configuration.

        Returns: str: Dataset path.
        """
        return self._config["dataset"]["path"]



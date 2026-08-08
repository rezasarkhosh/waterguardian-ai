from src.config.config import Config
import pytest

def test_config_returns_dataset_path():
    """
    Test that Config correctly reads the dataset path.
    """

    # Create a Config object using the project configuration file.
    config = Config("config.yaml")

    # Verify that the dataset path is loaded correctly.
    assert config.dataset_path == "data/raw/example.csv"

def test_config_raises_error_for_missing_file():
    """
    Test that Config raises FileNotFoundError
    when the configuration file does not exist.
    """

    # Verify that a missing configuration file
    # raises the expected exception.
    with pytest.raises(FileNotFoundError):
        Config("config/not_existing.yaml")
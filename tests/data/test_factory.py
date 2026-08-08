import pytest

from src.data.factory import LoaderFactory
from src.data.loaders.csv_loader import CSVLoader

def test_factory_returns_csv_loader():
    """
    Test that LoaderFactory returns an instance of CSVLoader when given a CSV file path.
    """
    csv_file_path = "data/raw/example.csv"
    loader = LoaderFactory.create(csv_file_path)

    # Verify that the returned object is an instance of CSVLoader.
    assert isinstance(loader, CSVLoader)

    def test_factory_raises_value_error_for_unsupported_file_type():
        """
        Test that LoaderFactory raises a ValueError for unsupported file types.
        """
        unsupported_file_path = "data/raw/example.txt"
        with pytest.raises(ValueError):
            LoaderFactory.create(unsupported_file_path)                
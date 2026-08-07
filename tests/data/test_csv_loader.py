import pytest 
from pathlib import Path
import pandas as pd

from src.data.loaders.csv_loader import CSVLoader

def test_csv_loader_returns_dataframe(tmp_path: Path):
    """
    Test that CSVLoader returns a pandas DataFrame.
    """

    csv_file = tmp_path / "sample.csv"

    csv_file.write_text(
        "name,age\nAlice,24\nBob, 30"
    )

    loader = CSVLoader(str(csv_file))

    dataframe = loader.load()
    # Verify the returned object type.
    assert isinstance(dataframe, pd.DataFrame)
    # Verify the number of rows.
    assert len(dataframe) == 2
    # Verify the column names.
    assert list(dataframe.columns) == ["name", "age"]

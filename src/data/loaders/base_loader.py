from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path

class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> pd.DataFrame:
        """Load data from a source."""
        pass


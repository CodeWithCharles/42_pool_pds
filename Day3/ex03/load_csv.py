import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Loads a csv file with pandas and returns a dataframe

    Args:
        path (str): The file's path

    Raises:
        AssertionError: File not found
        AssertionError: Invalid file format

    Returns:
        pd.DataFrame: Dataframe resulting from the read of the file
    """
    try:
        if not os.path.exists(path):
            raise AssertionError(f"File not found: {path}")
        if not path.lower().endswith(".csv"):
            raise AssertionError("Invalid file format")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        return pd.DataFrame()

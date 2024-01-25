import pandas as pd
import numpy as np

from analysis_measured_data.exceptions import InputNotValidException


def make_time_to_index(df: pd.DataFrame) -> pd.DataFrame:
    """Takes the time column and sets it as the dataframe index

    Input:
        df  pd.DataFrame    input dataframe

    """

    if "time" not in df.columns:
        raise InputNotValidException("time column not found")
    return df.set_index("time")


def pandas_to_numpy(df: pd.DataFrame) -> np.ndarray:
    return df.to_numpy()


def read_file(path: str) -> pd.DataFrame:
    """
    Read a data file into a pandas dataframe

    Args:
        path: A string representing the path of the file to be read.

    Returns:
        A pandas DataFrame representing the contents of the file.

    Example:
        >>> read_file("data.csv")
              Column1  Column2
        0         1        5
        1         2        6
        2         3        7
        3         4        8

    """
    df = pd.read_csv(
        path,
        sep=r"\s+",
    )
    return df

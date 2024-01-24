#!/usr/bin/env python

import pandas as pd

from analysis_measured_data.exceptions import InputNotValidException


def make_time_to_index(df: pd.DataFrame) -> pd.DataFrame:
    """Takes the time column and sets it as the dataframe index

    Input:
        df  pd.DataFrame    input dataframe

    """

    if "time" not in df.columns:
        raise InputNotValidException("time column not found")
    return df.set_index("time")


def read_file(path: str) -> pd.DataFrame:
    """
    Read a file from the given path and return it as a pandas DataFrame.

    :param path: Path of the file to be read.
    :type path: str
    :return: The content of the file as a pandas DataFrame.
    :rtype: pd.DataFrame
    """
    df = pd.read_csv(
        path,
        sep=r"\s+",
    )
    return df

#!/usr/bin/env python

import pandas as pd
import exceptions


def make_time_to_index(df: pd.DataFrame) -> pd.DataFrame:
    """Takes the time column and sets it as the dataframe index

    Input:
        df  pd.DataFrame    input dataframe

    """

    if "time" not in df.columns:
        raise exceptions.InputNotValidException("time column not found")
    return df.set_index("time")


def read_file(path: str) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        sep=r"\s+",
    )
    return df

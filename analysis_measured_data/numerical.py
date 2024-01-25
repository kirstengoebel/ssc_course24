import pandas as pd
import numpy as np


def fourier_transform(df: pd.DataFrame, column: str) -> np.ndarray:
    """_summary_

    Args:
        df (pd.DataFrame): input dataframe
        column (str): relevant column for FFT

    Returns:
        np.ndarray: FFT
    """
    return np.fft.fft(df[column])


def fourier_transform_frequencies(
    df: pd.DataFrame, sampling_rate: int = 1
) -> np.ndarray:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        sampling_rate (int, optional): _description_. Defaults to 1.

    Returns:
        np.ndarray: _description_
    """
    return np.fft.fftfreq(len(df), d=sampling_rate)


def autocorr(x):
    result = np.correlate(x, x, mode="full")
    return result[result.size / 2 :]  # noqa: E203

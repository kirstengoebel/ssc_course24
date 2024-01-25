import pandas as pd
import numpy as np


def fourier_transform(df: pd.DataFrame, column: str) -> np.ndarray:
    """
    does a fourier transformation on a dataframe column
    Args:
        df: A pandas DataFrame containing the data.
        column: The name of the column in the DataFrame on which
        Fourier Transform is to be performed.

    Returns:
        An array containing the Fourier Transform of the specified column
        in the DataFrame.
    """
    return np.fft.fft(df[column])


def fourier_transform_frequencies(
    df: pd.DataFrame, sampling_rate: int = 1
) -> np.ndarray:
    """
    Args:
        df: A pandas DataFrame representing the data samples.
        sampling_rate: An integer representing the rate at
        which the data samples were collected.

    Returns:
        A 1-dimensional numpy array containing the frequencies
        corresponding to the Fourier transform of the given data samples.
    """
    return np.fft.fftfreq(len(df), d=sampling_rate)


def autocorr(x):
    result = np.correlate(x, x, mode="full")
    return result[result.size / 2 :]  # noqa: E203

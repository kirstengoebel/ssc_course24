import pandas as pd
import numpy as np

from analysis_measured_data.numerical import (
    fourier_transform,
    fourier_transform_frequencies,
)


def test_fourier_transform():
    # Create a sample DataFrame
    data = {"Time": [0, 1, 2, 3, 4], "Values": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)

    # Perform Fourier Transform
    result = fourier_transform(df, "Values")

    # Expected Fourier Transform values
    expected_result = np.fft.fft([1, 2, 3, 4, 5])

    # Assert the result is almost equal to the expected result
    # this is a change for the docs
    np.testing.assert_almost_equal(result, expected_result)


def test_fourier_transform_frequencies():
    data = {"Time": [0, 1, 2, 3, 4], "Values": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    result = fourier_transform_frequencies(df)

    # Expected Fourier Transform values
    expected_result = np.fft.fftfreq(len([1, 2, 3, 4, 5]))
    np.testing.assert_almost_equal(result, expected_result)

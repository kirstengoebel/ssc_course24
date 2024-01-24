import random

import pandas as pd
import pytest

from analysis_measured_data.exceptions import InputNotValidException
from analysis_measured_data.input_reading import read_file, make_time_to_index


def test_read_file_correct_input():
    file_name = "../data/efield.t"
    result = read_file(file_name)
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert result.ndim == 2
    assert result.shape == (101, 4)


def test_read_file_not_exists():
    file_name = "../data/nonexistent.t"
    with pytest.raises(FileNotFoundError):
        read_file(file_name)


# TODO there should be more tests like trying to read a file with a
#  different structure


def test_set_time_as_index_with_time_column():
    test_data = pd.DataFrame(
        {
            "time": range(100, 200),
            "value1": [random.randint(0, 100) for _ in range(100)],
            "value2": [random.randint(0, 100) for _ in range(100)],
        }
    )
    assert test_data.index[0] == 0
    assert list(test_data.columns) == ["time", "value1", "value2"]
    result = make_time_to_index(test_data)
    assert result is not None
    assert result.index[0] == 100
    assert list(result.columns) == ["value1", "value2"]


def test_set_time_as_index_without_time_column():
    test_data = pd.DataFrame(
        {
            "value1": [random.randint(0, 100) for _ in range(100)],
            "value2": [random.randint(0, 100) for _ in range(100)],
        }
    )
    assert test_data.index[0] == 0
    with pytest.raises(InputNotValidException):
        make_time_to_index(test_data)

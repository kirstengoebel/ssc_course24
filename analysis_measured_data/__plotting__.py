import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def plot_variables_over_time(dataframe, path_save):
    """
    Plot remaining variables over time.

    Parameters:
    - dataframe: pd.DataFrame, input containing time and other variables
    - path_save: str, path to directory for saving plots as .pdf

    Returns:
    - None
    """

    # Check if the time variable is present in the DataFrame
    if "time" not in dataframe.columns:
        raise ValueError("Time variable 'time' not found.")

    # Extract non-time variables for plotting
    variables_to_plot = dataframe.columns.difference(["time"])

    # Plot each variable over time
    for variable in variables_to_plot:
        plt.figure(figsize=(10, 6))
        plt.plot(dataframe["time"], dataframe[variable], label=variable)
        plt.title(f"{variable}")
        plt.xlabel("time")
        plt.ylabel(variable)
        plt.legend()
        plt.show()

        # Save the plot as a PDF file
        pdf_file_path = Path(f"{path_save}" + f"{variable}" + ".pdf")
        plt.savefig(pdf_file_path, format="pdf")


# Example usage:
# Test data
example_dataframe = pd.DataFrame(
    {
        "time": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "a": [1, 3, 5, 2, 7, 8, 4, 6, 9, 2],
        "b": [10, 8, 6, 9, 4, 3, 7, 5, 2, 9],
        "c": [5, 2, 7, 4, 8, 1, 9, 3, 6, 10],
    }
)

example_path = "..\test"

plot_variables_over_time(example_dataframe, example_path)

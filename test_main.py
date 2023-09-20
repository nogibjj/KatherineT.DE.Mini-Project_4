"""
Test Cases
"""
# import functions
from main import sum_stats, visualization
import pandas as pd


# define test function
def test_sum_stats():
    # read dataset
    cereal = pd.read_csv("cereal.csv", sep=";")
    visualization(cereal)
    summary = sum_stats(cereal)
    assert (
        cereal["calories"].mean() == summary.loc["mean", "calories"]
    ), "Mean test failed"
    assert (
        cereal["protein"].median() == summary.loc["50%", "protein"]
    ), "Median test failed"
    assert (
        cereal["rating"].min() == summary.loc["min", "rating"]
    ), "Standard deviation test failed"
    print("All Test passed!")


# test
if __name__ == "__main__":
    test_sum_stats()

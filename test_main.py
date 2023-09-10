"""
Test Cases
"""
#import functions
from main import sum_stats, visualization
import pandas as pd

#define test function
def test_sum_stats(data):
    summary = sum_stats(data)

    assert data['calories'].mean() == summary.loc['mean', 'calories']
    assert data['protein'].median() == summary.loc['50%', 'protein'], "Median test failed"
    assert data['rating'].min() == summary.loc['min', 'rating'], "Standard deviation test failed"
    print("All Test passed!")

#read dataset
cereal = pd.read_csv("cereal.csv",sep=";")

#test
if __name__ == "__main__":
    print(sum_stats(cereal))
    visualization(cereal)
    test_sum_stats(cereal)
    
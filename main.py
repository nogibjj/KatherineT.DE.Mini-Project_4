"""
Main function goes here
"""

#import pandas and pyplot
import pandas as pd
import matplotlib.pyplot as plt

#define summary statistics function
def sum_stats(data):
    return data.describe()


#define visualization function
def visualization(data):
    plt.hist(data["calories"], bins=10, color="purple")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.title("Cereal Calories Histogram")
    plt.show()
    return

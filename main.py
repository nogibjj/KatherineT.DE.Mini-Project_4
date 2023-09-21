"""
Main function goes here
"""

# import pandas and pyplot
import matplotlib.pyplot as plt
import pandas as pd
from ydata_profiling import ProfileReport


def read(csv,sep):
    data = pd.read_csv(csv,sep=sep)
    return data


# read the CSV file
cereal = read("cereal.csv",";")

# compute summary statistics
summary = cereal.describe()

# plot a histogram of the "Age" column
plt.hist(cereal["calories"], bins=10, color="purple")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.title("Cereal Calories Histogram")
plt.savefig("Cereal Calories.png")
plt.show()

# generate a analyse report
def generate_report():
    report = cereal.loc[:, ["calories"]]
    profile = ProfileReport(
        report, title="Cereal Calories", explorative=True
    )
    profile.to_file("data_profiling_report.html")
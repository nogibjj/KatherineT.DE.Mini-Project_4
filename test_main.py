"""
Test goes here

"""

from main import read, generate_report

# read dataset


def test_csv():
    cereal = read("cereal.csv", ";")
    assert cereal["calories"].max() == 160, "Mean test failed"
    assert cereal["protein"].median() == 3, "Median test failed"
    assert cereal["fat"].count() == 77, "Count test failed"
    print("All Test passed!")


if __name__ == "__main__":
    test_csv()
    generate_report()

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

# Your code here
dtype = reviews.points.dtype

q1.check()

point_strings = reviews.points.astype('str')

q2.check()

n_missing_prices = reviews.price.isnull().sum()

q3.check()

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

q4.check()

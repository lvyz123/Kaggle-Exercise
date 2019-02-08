import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

median_points = reviews.points.median()

q1.check()

countries = reviews.country.unique()

q2.check()

reviews_per_country = reviews.country.value_counts()

q3.check()

centered_price = reviews.price.map(lambda p: p-reviews.price.mean())

q4.check()

bargain_wine = reviews.loc[(reviews.points/reviews.price).idxmax(),'title']

q5.check()

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

q6.check()

import math
reviews.loc[reviews.country == 'Canada','points'] = 3
star_ratings = reviews.points.map(lambda p: math.ceil((p - 74)/10))

q7.check()

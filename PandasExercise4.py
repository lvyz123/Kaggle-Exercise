import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

q1.check()

best_rating_per_price = reviews.groupby('price').points.max().sort_index()

q2.check()

price_extremes = reviews.groupby('variety').price.agg([min,max])

q3.check()

sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min','max'],ascending=False)

q4.check()

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

q5.check()

reviewer_mean_ratings.describe()

country_variety_counts = reviews.groupby(['country','variety']).variety.count().sort_values(ascending=False)

q6.check()

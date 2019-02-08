import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")

reviews.head()

# Your code here
renamed = reviews.rename(columns={'region_1': 'region','region_2':'locale'})

q1.check()

reindexed = reviews.rename_axis('wines',axis='rows')

q2.check()

combined_products = pd.concat([gaming_products,movie_products])

q3.check()

powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

meets = powerlifting_meets.set_index('MeetID')
competitors = powerlifting_competitors.set_index('MeetID')
powerlifting_combined = meets.join(competitors)

q4.check()

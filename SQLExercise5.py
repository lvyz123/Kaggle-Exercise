# Set up feedack system
from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex5 import *

# import package with helper functions 
import bq_helper

# create a helper object for this dataset
chicago_taxi_helper = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                               dataset_name="chicago_taxi_trips"

# Your code here to find the table name
chicago_taxi_helper.list_tables()

# write the table name as a string below
table_name = 'taxi_trips'

q_1.check()

# your code here
chicago_taxi_helper.head(table_name)

rides_per_year_query = """
SELECT EXTRACT(year FROM trip_start_timestamp) AS year,COUNT(1) num_trips
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
GROUP BY year
ORDER BY year
"""

rides_per_year_result = chicago_taxi_helper.query_to_pandas_safe(rides_per_year_query)


print(rides_per_year_result)
q_3.check()

rides_per_month_query = """
SELECT EXTRACT(month FROM trip_start_timestamp) AS month,COUNT(1) num_trips
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE EXTRACT(year FROM trip_start_timestamp) = 2017
GROUP BY month
ORDER BY month
"""

rides_per_month_result = chicago_taxi_helper.query_to_pandas_safe(rides_per_month_query)

print(rides_per_month_result)
q_4.check()

speeds_query = """
WITH RelevantRides AS
(SELECT trip_start_timestamp, trip_seconds, trip_miles
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE EXTRACT(YEAR FROM trip_start_timestamp) = 2017
and EXTRACT(month FROM trip_start_timestamp) >= 1
and EXTRACT(month FROM trip_start_timestamp) < 7
and trip_seconds > 0 and trip_miles > 0
)

SELECT EXTRACT(hour FROM trip_start_timestamp) AS hour_of_day, COUNT(1) num_trips, 3600 * SUM(trip_miles) / SUM(trip_seconds) AS avg_mph
FROM RelevantRides
GROUP BY hour_of_day
ORDER BY hour_of_day
"""

# Set high max_gb_scanned because this query looks at more data
speeds_result = chicago_taxi_helper.query_to_pandas_safe(speeds_query, max_gb_scanned=20)

print(speeds_result)
q_5.check()

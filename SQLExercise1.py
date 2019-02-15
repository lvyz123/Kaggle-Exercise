# Set up feedack system
from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex1 import *


# create a helper object for our bigquery dataset
import bq_helper
chicago_crime = bq_helper.BigQueryHelper(active_project= "bigquery-public-data", 
                                         dataset_name = "chicago_crime")
print("Setup Complete")

table_list = chicago_crime.list_tables() # Write the code you need here to figure out the answer

num_tables = len(table_list)  # store the answer as num_tables and then run this cell

q_1.check()

crime_schema = chicago_crime.table_schema('crime') # Write the code to figure out the answer

num_timestamp_fields = sum(crime_schema.type=='TIMESTAMP') # put your answer here

q_2.check()

crime_table = chicago_crime.head('crime') # Write the code here to explore the data so you can find the answer

fields_for_plotting = ['latitude', 'longitude']

q_3.check()

# Set up feedack system
from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex4 import *

# import package with helper functions 
import bq_helper

# create a helper object for this dataset
education_data = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                          dataset_name="world_bank_intl_education")
                                          
education_data.head('international_education')

# Your Code Here

country_spend_pct_query = """
SELECT country_name,AVG(value) avg_ed_spending_pct
FROM `bigquery-public-data.world_bank_intl_education.international_education`
WHERE year >= 2010 and year <= 2017 and indicator_code = 'SE.XPD.TOTL.GD.ZS'
GROUP BY country_name
ORDER BY AVG(value) DESC
"""

country_spending_results = education_data.query_to_pandas_safe(country_spend_pct_query)

print(country_spending_results.head())
q_1.check()

# Your Code Here
code_count_query = """SELECT indicator_code,indicator_name,COUNT(1) num_rows
                        FROM `bigquery-public-data.world_bank_intl_education.international_education`
                        WHERE year = 2016
                        GROUP BY indicator_code,indicator_name
                        HAVING COUNT(1) >= 175
                        ORDER BY num_rows DESC"""

code_count_results = education_data.query_to_pandas_safe(code_count_query)

print(code_count_results.head())
q_2.check()

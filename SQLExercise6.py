# Set up feedack system
from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex6 import *

# import package with helper functions 
import bq_helper

# create a helper object for this dataset
stack_overflow = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                              dataset_name="stackoverflow")

# Your code here

list_of_tables = stack_overflow.list_tables()    # get a list of available tables

print(list_of_tables)
q_1.check()

stack_overflow.head('posts_answers')

stack_overflow.head('posts_questions')

# Your code here
questions_query = \
"""
SELECT id, title, owner_user_id
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE tags LIKE '%bigquery%'
"""

questions_results = stack_overflow.query_to_pandas_safe(questions_query, max_gb_scanned=25) # this query reads a lot of data
print(questions_results.head())
q_3.check()

from time import time


answers_query = \
"""
SELECT a.id, a.body, a.owner_user_id
FROM `bigquery-public-data.stackoverflow.posts_answers` as a
INNER JOIN `bigquery-public-data.stackoverflow.posts_questions` as q ON a.parent_id = q.id
WHERE q.tags LIKE '%bigquery%'
"""

answers_results = stack_overflow.query_to_pandas_safe(answers_query, max_gb_scanned=50) # query scans more than 1GB of data, but less than 2.
print(answers_results.head())
q_4.check()

# your code here
bigquery_experts_query = \
"""
SELECT a.owner_user_id AS user_id, COUNT(a.id) number_of_answers
FROM `bigquery-public-data.stackoverflow.posts_answers` as a
INNER JOIN `bigquery-public-data.stackoverflow.posts_questions` as q ON a.parent_id = q.id
WHERE q.tags LIKE '%bigquery%'
GROUP BY user_id
"""
bigquery_experts_results = stack_overflow.query_to_pandas_safe(bigquery_experts_query, max_gb_scanned=50)

print(bigquery_experts_results)
q_5.check()

Solution:

def expert_finder(topic, stack_overflow_helper):
    '''
    Returns a DataFrame with the user_id's who have written stackoverflow answers on topic.

    Inputs:
        topic: A string with the topic we are interested
        stack_overflow_helper: A bigquery_helper object that specifies the connection to the stack overflow DB

    Outputs:
        results: A DataFrame with columns for user_id and number_of_answers. Follows similar logic to bigquery_experts_results shown above.
    '''
    my_query = """SELECT a.owner_user_id AS user_id, COUNT(1) AS number_of_answers
                  FROM `bigquery-public-data.stackoverflow.posts_questions` q
                        INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` a
                        ON q.id = a.parent_Id
                  WHERE q.tags like '%' + tag + '%'
                  GROUP BY a.owner_user_id
                """
    # a real service would have good error handling for queries that scan too much data
    my_results = stack_overflow_helper.query_to_pandas_safe(my_query, max_gb_scanned=2)
    return 

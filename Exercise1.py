# Code you have previously used to load data
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex3 import *

print("Setup Complete")

# print the list of columns in the dataset to find the name of the prediction target
print("The prediction target is ")

#y = _
y=home_data.SalePrice
step_1.check()

# Create the list of features below
# feature_names = ___
feature_names=['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
# select data corresponding to features in feature_names
#X = _
X=home_data[feature_names]
step_2.check()

# Review data
# print description or statistics from X
#print(_)
X.describe()
# print the top few lines
#print(_)
X.head()

# from _ import _
from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)

step_3.check()

predictions = iowa_model.predict(X.head(1460))
print(predictions)
step_4.check()

#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( 'TOTAL', 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)




### your code below
# for key, value in data_dict.iteritems():
#     print key, value['salary'], value['bonus']

for k in data_dict:
    if (data_dict[k]['bonus'] > 10000000 and data_dict[k]['bonus'] != 'NaN') and \
       (data_dict[k]['salary'] > 2000000 and data_dict[k]['salary'] != 'NaN'):
        print k


for j in data_dict:
    if (data_dict[j]['bonus'] > 5000000 and data_dict[j]['bonus'] != 'NaN') and \
       (data_dict[j]['salary'] > 1000000 and data_dict[j]['salary'] != 'NaN'):
        print j


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
enron_data = pickle.load(open("./final_project/final_project_dataset.pkl", "rb"))
people_of_interest= open("./final_project/poi_names.txt", "r")
#number of individuals in list
print len(enron_data)

#number of deatures per individual
print len(enron_data[enron_data.keys()[0]])

#features per person
print enron_data[enron_data.keys()[0]]

#number of persons of interes
num_of_POI=0
for a in enron_data:
    if enron_data[a]['poi']:
        num_of_POI+=1

print num_of_POI


num_lines = sum(1 for line in open("./final_project/poi_names.txt", "r"))
print people_of_interest.read()
print num_lines

people_of_interest.close()

#number of stocks belonging to pretence james
print enron_data['PRENTICE JAMES']['total_stock_value']

# email messages from colwell wesley
print enron_data['COLWELL WESLEY']['from_this_person_to_poi'] 

#number of stock options from SKILLING K JEFFREY
# print enron_data.keys()    
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
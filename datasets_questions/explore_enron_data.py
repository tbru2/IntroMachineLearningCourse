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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
count = 0
salCount = 0
emailCount = 0
totalPaymentCount = 0
poiNaNCount = 0
for person, feature in enron_data.items():
    if feature["poi"]:
        if feature["total_payments"] == 'NaN':
            poiNanCount += 1
        count += 1
    if feature["salary"] != 'NaN':
        salCount += 1
    if feature["email_address"] != 'NaN':
        emailCount += 1
    if feature["total_payments"] != 'NaN':
        totalPaymentCount += 1
print count
print salCount
print emailCount
print enron_data["SKILLING JEFFREY K"]
print ("total Payment Count: ",  totalPaymentCount)
print ("poi count: ", poiNaNCount)

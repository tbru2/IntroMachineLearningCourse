#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state = 42, test_size=.30)

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
acc = accuracy_score(pred,labels_test)

true_positives = [(x,y) for x,y in zip(pred,labels_test) if x == y and x == 1]
print sum(pred)
print len(features_test)
print "true_positives:", len(true_positives)

print precision_score(pred,labels_test)
print recall_score(labels_test,pred)

predictions = [0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1]
true_labels = [0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0]
true_positives2 = [(a,b) for a,b in zip(pred,labels_test) if a==b and x==1]
print len(true_positives2)

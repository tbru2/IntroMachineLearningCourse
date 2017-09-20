#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
import collections

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###





t0 = time()

clf = SVC(kernel='rbf',C=10000.)
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0,3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Predicting Time:", round(time()-t1,3), "s"


counter = collections.Counter(pred)
print counter[1], counter[0] 


acc = accuracy_score(pred, labels_test)
print acc
#########################################################



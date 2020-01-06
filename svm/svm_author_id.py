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
from sklearn import svm
from sklearn.metrics import accuracy_score
import collections
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
clf=svm.SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1= time()
predict=clf.predict(features_test)
print predict[10], predict[26], predict[50]
print "prediction time: ", round(time()- t1, 3), "s"
collection_num=collections.Counter(predict)
print collection_num
accuracy= accuracy_score(labels_test, predict)

print accuracy
# print(features_test)

#########################################################
### your code goes here ###

#########################################################



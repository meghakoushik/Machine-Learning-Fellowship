#!/usr/bin/env python
# coding: utf-8

# In[15]:


#import libraries
import nltk 
import random
import pickle
from nltk.corpus import movie_reviews


# In[16]:


#load Pickle file
file = open("test.pickle","rb")
testing_set = pickle.load(file)


# In[17]:


classifier = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier)


# In[18]:


#find accuracy:

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)


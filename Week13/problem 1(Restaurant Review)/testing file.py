#!/usr/bin/env python
# coding: utf-8

# In[17]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
import pickle


# In[18]:


file = open('test.pickel', 'rb')
# dump information to that file
x_test = pickle.load(file)
y_test = pickle.load(file)


# In[19]:



classifier = open("GaussianNB.pickel","rb")
classifier = pickle.load(classifier)


# In[21]:


class NLP:
    def nlp_model(self,x_test,y_test):
        classifier = GaussianNB()
        classifier.fit(x_test,y_test)
        return classifier  
    def predict(self,x_test,classifier):
        y_pred= classifier.predict(x_test)
        return y_pred
    def accuracy(self,y_test,y_pred):
        accuracy= accuracy_score(y_test,y_pred)
        return accuracy   
    def confusion_matrix(self,y_test,y_pred):
        cm = confusion_matrix(y_test,y_pred)
        return cm
def main():
    obj= NLP()
    
    #fitting naive Bayes to the trainning set  model
    classifier = obj.nlp_model(x_test,y_test)
    print(classifier)
        
    #predicting the test set
    y_pred = obj.predict(x_test,classifier)
    print("\n pridiction value\n",y_pred)
   
    #calculating accuracy
    accuracy = accuracy_score(y_test,y_pred)*100
    print("accuracy",accuracy)
    
    #making the confusion matrix
    cm= obj.confusion_matrix(y_test,y_pred)
    print("confusion matrix value\n\n",cm)


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





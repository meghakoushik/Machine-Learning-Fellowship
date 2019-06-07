#!/usr/bin/env python
# coding: utf-8

# In[9]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report


# In[10]:


#load and read csv file
data_module = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t')
data_module.head()


# In[11]:


#data pre-Processing
corpus =[]
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',data_module['Review'][i])
    review = review.lower()
    review=review.split()
    ps =PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review =' '.join(review)
    corpus.append(review)


# In[12]:


#creating a bag of words
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(corpus).toarray()
y=data_module.iloc[:,1].values


# In[13]:


#split dataset into train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[14]:


print("x_train",x_train.shape)
print("x_test",x_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)


# In[15]:


#feature scalling
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


# In[19]:


class NLP:
    def naive_bayes(self,x_train,y_train):
        classifier = GaussianNB()
        classifier.fit(x_train,y_train)
        return classifier
    def predict(self,x_test,classifier):
        y_pred= classifier.predict(x_test)
        return y_pred
    def accuracy(self,y_test,y_pred):
        accuracy = accuracy_score(y_test,y_pred)
        return accuracy
    def confusion_matrix(self,y_test,y_pred):
        cm = confusion_matrix(y_test,y_pred)
        return cm
def main():
    obj= NLP()
    
    #fitting naive Bayes to the trainning set  model
    classifier = obj.naive_bayes(x_train,y_train)
    print(classifier)
    
    #predicting the test set
    y_pred = obj.predict(x_test,classifier)
    print("\n pridiction value\n",y_pred)
    
    #calculating accuracy
    accuracy = obj.accuracy(y_test,y_pred)*100
    print("accuracy :", accuracy)
    
    accuracy=classification_report(y_test, y_pred)
    print("\naccuracy\n",accuracy)

    #making the confusion matrix
    cm= obj.confusion_matrix(y_test,y_pred)
    print("confusion matrix value\n\n",cm)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





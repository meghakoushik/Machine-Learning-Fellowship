#!/usr/bin/env python
# coding: utf-8

# In[20]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
import pickle
import warnings
warnings.filterwarnings("ignore")


# In[21]:


data_module = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t')
data_module


# In[22]:


data_module.info()


# In[23]:


data_module.describe()


# In[24]:


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


# In[25]:


# from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(corpus).toarray()
y=data_module.iloc[:,1].values


# In[26]:


#split dataset into train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

x_train,x_cv,y_train,y_cv = train_test_split(x_train,y_train,test_size=0.30,random_state=0)


# In[27]:


x_test.shape,y_test.shape


# In[28]:


x_train.shape,x_cv.shape,y_train.shape,y_cv.shape 


# In[29]:


# open a file, where you ant to store the data
file = open('test.pickel', 'wb')
# dump information to that file
pickle.dump(x_test, file)
pickle.dump(y_test, file)
# close the file
file.close()


# In[30]:


# train.to_csv('train.csv',index=0)
# x_test.to_csv('test.csv',index=0)


# In[31]:


print("x_train",x_train.shape)
print("x_test",x_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)


# In[32]:


#feature scalling
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


# In[33]:


class NLP:
    def nlp_model(self,x_train,y_train):
        classifier = GaussianNB()
        classifier.fit(x_train,y_train)
        return classifier
    def predict(self,x_cv,classifier):
        y_pred= classifier.predict(x_cv)
        return y_pred
    def confusion_matrix(self,y_cv,y_pred):
        cm = confusion_matrix(y_cv,y_pred)
        return cm
def main():
    obj= NLP()
    
    #fitting naive Bayes to the trainning set  model
    classifier = obj.nlp_model(x_train,y_train)
    print(classifier)
        
    #predicting the test set
    y_pred = obj.predict(x_cv,classifier)
    print("\n pridiction value\n",y_pred)
   
    #calculating accuracy
    accuracy = accuracy_score(y_cv,y_pred)*100
    print("accuracy",accuracy)
    
    accuracy = average_precision_score(y_cv, y_pred)* 100
    print("Accuracy: average_precision_score :", accuracy)
    
    #calculating accuracy 
    classification_accuracy = classification_report(y_cv, y_pred)
    print("\n\naccuracy\n",classification_accuracy)

    #making the confusion matrix
    cm= obj.confusion_matrix(y_cv,y_pred)
    print("confusion matrix value\n\n",cm)
    
    # create pickle file
    file = open('GaussianNB.pickel','wb')
    # dump information to that file
    pickle.dump(classifier,file)
    #file the close
    file.close()
    



if __name__ == '__main__':
    main()


# In[34]:


#using Random Forest classifier
class Random_forest_Regression:
    def random_forest_model(self,x_train,y_train):
        classifier = RandomForestClassifier(criterion='entropy',random_state=0)
        classifier.fit(x_train,y_train)
        return classifier
        
    def predict(self,x_cv,classifier):
        y_pred= classifier.predict(x_cv)
        return y_pred
    
    def accuracy(self,y_cv,y_pred):
        accuracy = accuracy_score(y_cv,y_pred)*100
        return accuracy

    def confusion_matrix(self,y_cv,y_pred):
        cm = confusion_matrix(y_cv,y_pred)
        return cm
def main():
    obj= Random_forest_Regression()
    
    #fitting naive Bayes to the trainning set  model
    classifier = obj.random_forest_model(x_train,y_train)
    print(classifier)
        
    #predicting the test set
    y_pred = obj.predict(x_cv,classifier)
    print("\n pridiction value\n",y_pred)
   
    #calculating accuracy
    accuracy = obj.accuracy(y_cv,y_pred)
    print("accuracy",accuracy)
    
    accuracy = average_precision_score(y_cv, y_pred)* 100
    print("Accuracy: average_precision_score :", accuracy)
    
    #calculating accuracy 
    classification_accuracy = classification_report(y_cv, y_pred)
    print("\n\naccuracy\n",classification_accuracy)

    #making the confusion matrix
    cm= obj.confusion_matrix(y_cv,y_pred)
    print("confusion matrix value\n\n",cm)
    
    # create pickle file
    file = open('Random_forest.pickel','wb')
    # dump information to that file
    pickle.dump(classifier,file)
    #file the close
    file.close()
    



if __name__ == '__main__':
    main()


# In[35]:


#using Random Forest classifier
class Decision_Regression:
    def decision_model(self,x_train,y_train):
        classifier =DecisionTreeClassifier(random_state=0)
        classifier.fit(x_train,y_train)
#         print(x_train,y_train)
        return classifier
        
    def predict(self,x_cv,classifier):
        y_pred= classifier.predict(x_cv)
        return y_pred
    
    def accuracy(self,y_cv,y_pred):
        accuracy = accuracy_score(y_cv,y_pred)*100
        return accuracy

    def confusion_matrix(self,y_cv,y_pred):
        cm = confusion_matrix(y_cv,y_pred)
        return cm
def main():
    obj= Decision_Regression()
    
    #fitting naive Bayes to the trainning set  model
    classifier = obj.decision_model(x_train,y_train)
    print(classifier)
        
    #predicting the test set
    y_pred = obj.predict(x_cv,classifier)
    print(" pridiction value",y_pred)
   
    #calculating accuracy
    accuracy = obj.accuracy(y_cv,y_pred)
    print("accuracy",accuracy)
    
    accuracy = average_precision_score(y_cv, y_pred)* 100
    print("Accuracy: average_precision_score :", accuracy)
    
    #calculating accuracy 
    classification_accuracy = classification_report(y_cv, y_pred)
    print("accuracy",classification_accuracy)

    #making the confusion matrix
    cm= obj.confusion_matrix(y_cv,y_pred)
    print("confusion matrix value",cm)
    
    # create pickle file
    file = open('decision_tree.pickel','wb')
    # dump information to that file
    pickle.dump(classifier,file)
    #file the close
    file.close()
    



if __name__ == '__main__':
    main()


# In[ ]:





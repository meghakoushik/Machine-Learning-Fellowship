#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
import sklearn
import pickle
import importlib.util


# In[2]:


# importing utility file 
spec = importlib.util.spec_from_file_location("Util","/home/user/PycharmProjects/Machine-Learning-Fellowship/week12/utility_class.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
util_obj = foo.Util()


# In[3]:


#load and read csv file
data_module= pd.read_csv('Mall_Customers.csv')
data_module.head()


# In[4]:


data_module.info()


# In[5]:


data_module.describe()


# In[6]:


#check null value into the dataset
data_module.isnull().sum()


# In[7]:


#remove duplicate value
data_module.duplicated().sum()


# In[8]:


x_train=data_module.iloc[:,[3,4]].values
x_train.shape


# In[9]:


#using the elbow method 
#find the optimal no. of cluster
WCSS=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x_train)
    WCSS.append(kmeans.inertia_)
plt.plot(range(1,11),WCSS)
plt.title('The Elbow Method')
plt.xlabel('Number of cluster')
plt.ylabel('WCSS')
plt.show()


# In[10]:


class K_means:
    def k_means_model(self):
        kmeans=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
        return kmeans

def main():
    obj=K_means()
    
    kmeans =obj.k_means_model()
    print(kmeans)
    
    y_kmeans= util_obj.predict(x_train,kmeans)
    print("\npridict value",y_kmeans)
    
    print('\nvisualization of kmeans:')
    util_obj.visualizing(x_train,y_kmeans,kmeans)

if __name__ == '__main__':
    main()
 


# In[ ]:





# In[ ]:





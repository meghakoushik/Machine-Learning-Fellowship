#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
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


#read and load csv file
data_module= pd.read_csv("USCensus1990.data.txt",nrows=1000)
data_module.head()


# In[4]:


data_module.info()


# In[5]:


data_module.describe()


# In[6]:


#check null value
data_module.isnull().sum()


# In[7]:


#remove duplicate value
data_module.duplicated().sum()


# In[8]:


# x_train=data_module.iloc[:,[3,4]].values
x_train=data_module.iloc[:1000].values
x_train.shape


# In[9]:


#using dendrogram to find optimal no. of clusters.
dendrogram= sch.dendrogram(sch.linkage(x_train,method='ward'))
plt.title('Dendrogram')
plt.xlabel('customers')
plt.ylabel('Euclidean distance')
plt.show()  


# In[10]:


class Hierarchical_clustering:
    def hierarchical_model(self):
        hc =AgglomerativeClustering(n_clusters=4,affinity='euclidean',linkage='ward')
        return hc

def main():
    obj=Hierarchical_clustering()
    
    hc =obj.hierarchical_model()
    print(hc)
    
    y_hc= util_obj.predict(x_train,hc)
    print("\npridict value",y_hc)
    
    print("\nvisualization of hierarchical clustering:")
    util_obj.hierachical_visualization(x_train,y_hc,hc)

if __name__ == '__main__':
    main()
 


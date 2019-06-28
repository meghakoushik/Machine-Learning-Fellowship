#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from ipykernel.kernelapp import IPKernelApp


# In[2]:


#load and read csv file
data_module = pd.read_csv('bank.csv',delimiter = ';')
data_module.head()


# In[3]:


data_module.info()


# In[4]:


data_module.describe()


# In[5]:


data_module.drop_duplicates()
data_module.head()


# In[6]:


data_module.dtypes


# In[7]:


data_module.isnull().sum()


# In[8]:


data_module.replace(np.NaN,data_module.mean(),inplace= True)
data_module.head()


# In[9]:


data_module.replace(['yes','no'],[1,0],inplace=True)
data_module.head()


# In[10]:


data_module= pd.get_dummies(data_module)


# In[11]:


#feature scalling
data_module = data_module- data_module.min()/data_module.max()-data_module.min()


# In[12]:


#seprating the output
def separate(data_module):
    output = data_module.y
    data_module = data_module.drop('y', axis=1)
    return data_module, output 
data_module, output = separate(data_module)


# In[13]:


def split(data_module,output):
    train_data = int(0.70*len(data_module))
    test_data = len(data_module)-train_data
    print("train data",train_data)
    print("test_data",test_data)
    x_train = np.array(data_module[:train_data])   
    x_test = np.array(data_module[:test_data])

   
    train_per_y = int(0.70*len(output))
    test_per_y = len(output)-train_per_y
    
    y_train = np.array(output[:train_per_y])
    y_test = np.array(output[:test_per_y])
    
    y_train = y_train.reshape(-1,1)
    y_test = y_test.reshape(-1,1)
    
    return x_train,y_train,x_test,y_test
x_train,y_train,x_test,y_test = split(data_module,output)


# In[14]:


#print train and test data shapes
print("x_train data shape",x_train.shape)
print("y_train data shape",y_train.shape)
print("x_test data shape",x_test.shape)
print("y_test data shape",y_test.shape)


# In[18]:


class Single_neural_network:
    def __init__(self):
        self.learning_rate= 0.01
        self.epoch =2000
    def gradient_descent(self,x_train,y_train,weigth,bias):
        db=0
        for i in range (self.epoch):
            #input layer z =w.T+b
            z=np.dot(x_train,weigth)+bias
            #z = np.dot(weigth.T,x_train.T)
            #using sigmoid function
            sigmoid = 1/(1+np.exp(-z))
           
            dz = np.subtract(sigmoid,y_train)
            
            dw = np.dot(x_train.T,dz)/len(x_train)
          
            db = np.sum(dz)/len(x_train)
          
            #update weight and bias
            weigth = (weigth -np.dot(self.learning_rate,dw))
            bias = bias - np.dot(self.learning_rate,db)
        return weigth,bias



    def predict(self,x_test,weigth,bias):
        z=(np.dot(x_test,weigth)+bias)
        sigmoid= 1/((1+np.exp(-z))+bias)
        predict= np.zeros((x_test.shape[0],1),dtype=float)
        for i in range(0,len(x_test)):
            if round(sigmoid[i][0], 2) <= 0.5:
                predict[i][0]=0
            else:
                predict[i][0]=1
        return predict
    
    def accuracy(self,y_test, predict):
        count= 0
        for i in range(len(y_test)):
            if predict[i]==y_test[i]:
                count+=1
        count= (count/len(y_test))*100
        return count


def main(x_train,y_train,x_test,y_test):
    obj = Single_neural_network()

    x_train = np.column_stack((np.ones((x_train.shape[0], 1)), x_train))
    print("\nshape of x_train",x_train.shape)
    x_test = np.column_stack((np.ones((x_test.shape[0],1)), x_test))
    print("shape of x_test",x_test.shape)

    bias=1
    x_size =48
    weigth = np.full((x_size+1,1),0.08)
#     print("original weigth shape",weigth.shape)
    
    weigth,bias = obj.gradient_descent(x_train,y_train,weigth,bias)
    
    predict_test = obj.predict(x_test,weigth,bias) 
#     print(predict_test)
    predict_train = obj.predict(x_train,weigth,bias)
#     print(predict_train)
    
    accuracy_train= obj.accuracy(predict_train,y_train)
    print("accuracy of traindata",accuracy_train)
    accuracy_test= obj.accuracy(predict_test,y_test)
    print("accuracy of testdata", accuracy_test)
    
if __name__ == '__main__':
    main(x_train,y_train,x_test,y_test)
     


# In[ ]:





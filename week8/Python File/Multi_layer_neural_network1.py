#!/usr/bin/env python
# coding: utf-8

# In[130]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[131]:


#load and read csv file
data_module = pd.read_csv('bank.csv',delimiter = ';')
data_module.head()


# In[132]:


data_module.info()


# In[133]:


data_module.drop_duplicates()
data_module.head()


# In[134]:


#check datatypes
data_module.dtypes


# In[135]:


#Check null values
data_module.isnull().sum()


# In[136]:


#Replace Null value by mean
data_module.replace(np.NaN,data_module.mean(),inplace= True)
data_module.head()


# In[137]:


data_module.replace(['yes','no'],[1,0],inplace=True)
data_module.head()


# In[138]:


data_module= pd.get_dummies(data_module)


# In[139]:


#feature scalling
data_module = data_module- data_module.min()/data_module.max()-data_module.min()


# In[140]:


#seprating the output
def separate(data_module):
    output = data_module.y
    data_module = data_module.drop('y', axis=1)
    return data_module, output 
data_module, output = separate(data_module)


# In[141]:


#Splitting dataset into train and test
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


# In[142]:


#print train and test data shapes
print("x_train data shape",x_train.shape)
print("y_train data shape",y_train.shape)
print("x_test data shape",x_test.shape)
print("y_test data shape",y_test.shape)


# In[144]:


class Multi_layer_network:
    def __init__(self):
        self.learning_rate= 0.011
        self.epoch= 500
    
    def gradient_descent(self,x_train,y_train):
        layer = [x_train.shape[1],4,5,3,1]
        weigth =[]
        bias =[]
    
        a = [0] * len(layer)
        z = [0] * len(layer)
        A = [0] * len(layer)
        dg = [0] * len(layer)
        da = [0] * len(layer)
        dz = [0] * len(layer)
        db = [0] * len(layer)
        dw = [0] * len(layer)
        a[0] =x_train.T
        #Random Initalization
        for i in range(len(layer)):
            weigth.append(np.random.randn(layer[i],layer[i-1])*0.01)
            bias.append(np.zeros(((layer[i],1))))
        
        #forword propogation
        for k in range(self.epoch):
            for i in range(1,len(layer)):
                print("layer",i)
                print("weight ", i, "= ", weigth[i].shape)
                print("bias", i, "= ", bias[i].shape)
                z[i] = np.dot(weigth[i],a[i-1])+bias[i]    
                print("z",z[i].shape)
                a[i] = (1/(1-np.exp(-z[i])))
                print("a",a[i].shape)
            
            #backword Propogation  
            for i in reversed(range(1,len(layer))):
                print("layer",i)
                da[i]=(-(y_train.T/a[i])+((1-y_train.T)/(1-a[i])))
                print("da shape",da[i].shape)
                dg[i]= (1 / (1 + np.exp(-z[i])))*(1-(1/(1 + np.exp(-z[i]))))
                print("dg",da[i].shape)
                dz[i]=da[i]*dg[i]
                print("dz",da[i].shape)
                dw[i]= np.dot(dz[i],a[i-1].T)/len(x_train)
                print("dw",da[i].shape)
                db[i]= np.sum(dz[i],axis=1,keepdims=True)/len(x_train)
                print("db",da[i].shape)
                weigth[i]= weigth[i]-np.dot(self.learning_rate,dw[i])
                bias[i]= bias[i] - np.dot(self.learning_rate,db[i])
                np.seterr(divide='ignore', invalid='ignore')
        return weigth[i],bias[i]
    
    def predict(self,x_test,weigth,bias):
        layer=[x_test.shape[1],4,5,3,1]
        a = [0]*len(layer)
        z= [0]*len(layer)
        a[0]=x_test.T
        for i in range(1,len(layer)):
            z[i]=np.dot(weigth[i],a[i-1])+bias
            a[i]=(1/(1+np.exp(-z[i])))
            return a[-1]

    def accuracy(self,y_test,test_predict):  
        test_predict=np.nan_to_num(test_predict)
        accuracy = 100 -(np.mean(np.abs(test_predict - y_test))*100)
        return accuracy
    
def main():
    obj = Multi_layer_network()
  
    weigth,bias = obj.gradient_descent(x_train,y_train)
    print("weight:",weigth.shape)
    print("bias:",bias.shape)   
 
    y_predict_train= obj.predict(x_train,weigth,bias)
#     print("predict train",y_predict_train)
    y_predict_test = obj.predict(x_test,weigth,bias)
#     print("predict test",y_predict_test)
    
    accuracy_train = obj.accuracy(y_predict_train,y_train)
    print("\n train data accuracy",accuracy_train)
    
    accuracy_test = obj.accuracy(y_predict_test,y_test)
    print("\n test data accuracy",accuracy_test)

if __name__ == '__main__':
    main()
    


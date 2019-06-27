import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')
import sklearn
import pickle

class Util:
     
    def split(self,data_module,value):

        train, test = train_test_split(data_module,test_size = value)
        print("train : ", train.shape, " test : ", test.shape)
        return train,test
   
    def feature_scalling(self,x_train,y_train):
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        x_train = sc_x.feature_scalling(x_train)
        y_train =sc_y.feature_scalling(y_train)
        return x_train,y_train

    def predict(self,x_train,classifier):
        predict = classifier.predict(x_train)
        return predict
   
    def confusion_matrix(self,y_train,predict):
        cm= confusion_matrix(y_train,predict)
        return cm
    
    def accuracy(self,predict,y_train):
        accuracy = sklearn.metrics.accuracy_score(y_train,predict)*100
        return accuracy
    
    def create_pickle(self,classifier,file_name):
        file = open(file_name,'wb')
        pickle.dump(classifier,file)     
        file.close()
    
    def load_pickle(self,file_name):
        file = open(file_name,'rb')  
        file_load = pickle.load(file)
        print(file_load)
#         return file_load
    
    def visualization(self,x_train,y_train,predict,classifier):
        x1,x2=np.meshgrid(np.arange(start=x_train[:,0].min()-1,stop=x_train[:,0].max()+1,step=0.01),
                                np.arange(start=x_train[:,1].min()-1,stop=x_train[:,1].max()+1,step=0.01 ))
        plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,
                     cmap=ListedColormap(('red','green')))
        plt.xlim(x1.min(),x1.max())
        plt.ylim(x2.min(),x2.max())
        
        for i,j in enumerate(np.unique(y_train)):
            plt.scatter(x_train[y_train==j,0],x_train[y_train==j,1],c=ListedColormap(('red','green'))(i),label=j)
        
        plt.title('predict user will click the ad or not(train dataset)')
        plt.xlabel('Age')
        plt.ylabel('estimated salary')
        plt.show()
        
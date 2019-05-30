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

    def predict(self,x_train,kmeans):
        y_kmeans = kmeans.fit_predict(x_train)
        return y_kmeans

    #k-meanas visualization
    def visualizing(self,x_train,y_kmeans,kmeans):
        #visualizing
        plt.scatter(x_train[y_kmeans==0,0],x_train[y_kmeans==0,1],s= 100,c='red',label='cluster1')
        plt.scatter(x_train[y_kmeans==1,0],x_train[y_kmeans==1,1],s= 100,c='blue',label='cluster2')
        plt.scatter(x_train[y_kmeans==2,0],x_train[y_kmeans==2,1],s= 100,c='green',label='cluster3')
        plt.scatter(x_train[y_kmeans==3,0],x_train[y_kmeans==3,1],s= 100,c='pink',label='cluster4')
        plt.scatter(x_train[y_kmeans==4,0],x_train[y_kmeans==4,1],s= 100,c='cyan',label='cluster5')
        plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroid')
        plt.title('cluster of clients')
        plt.xlabel('AnnualIncome')
        plt.ylabel('spendingScore')
        plt.legend()
        plt.show()
        

    
    # hierachical cluster visualiation
    def hierachical_visualization(self,x_train, y_hc,hc):

        plt.scatter(x_train[y_hc == 0 , 0], x_train[y_hc == 0 ,1], s = 100, c = 'red', label = 'Careful')
        plt.scatter(x_train[y_hc == 1 , 0], x_train[y_hc == 1 ,1], s = 100, c = 'blue', label = 'Standard')
        plt.scatter(x_train[y_hc == 2 , 0], x_train[y_hc == 2 ,1], s = 100, c = 'cyan', label = 'Target')
        plt.scatter(x_train[y_hc == 3 , 0], x_train[y_hc == 3 ,1], s = 100, c = 'green', label = 'Careless')
        plt.scatter(x_train[y_hc == 4 , 0], x_train[y_hc == 4 ,1], s = 100, c = 'magenta', label = 'Sensible')
        
        plt.title('cluster of client')
        plt.xlabel('Annual income')
        plt.ylabel('Spending score')
        plt.legend()
        plt.show()
    
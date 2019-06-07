#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import nltk
import random
from nltk.corpus import movie_reviews
import pickle
import collections


# In[2]:


#Create list of movie review document
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]


random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

counter=collections.Counter(all_words)
print(counter.most_common())
          
 


# In[3]:


#converting words to features
word_features = list(all_words.keys())[:3000]
print(word_features)


# In[4]:


#we write a function that will be used to create feature set. The feature set is used to train the classifier.
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# In[5]:


# print one feature set.
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))


# In[6]:


featuresets = [(find_features(rev), category) for (rev, category) in documents]


# In[7]:


# split the data with:
#creating train and test dataset

training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]


# In[8]:


#create pickle file:

file = open('test.pickle', 'wb')

# dump information to that file
pickle.dump(testing_set, file)

# close the file
file.close()


# In[9]:


#train our classifier , using naive Bayes classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
print(classifier)


# In[10]:


print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)


# In[11]:


#show 15 most informative features.
features= classifier.show_most_informative_features(15)
features


# In[12]:


save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


# In[ ]:





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:37:55 2019

@author: aureliemutschler
"""

# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# import dataset
print("Loading dataset...")
dataset = pd.read_csv("Social_Network_Ads.csv")
print("...Done.")
print(dataset.describe(include="all"))

# Separate target variable Y from features X
print("Separating labels from features...")
features_list = ['Gender', 'Age', 'EstimatedSalary']
X = dataset.loc[:,features_list]
Y = dataset.loc[:,"Purchased"]
print("...Done.")
print()

# Divide dataset Train set & Test set 
print("Dividing into train and test sets...")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, 
                                                    random_state=0, 
                                                    stratify=Y) # Stratified splitting !!!
print("...Done.")
print()

# Convert pandas DataFrames to numpy arrays before using scikit-learn
X_train = X_train.values
X_test = X_test.values
Y_train = Y_train.tolist()
Y_test = Y_test.tolist()

### Training pipeline ###
print("--- Training pipeline ---")
print()  

# Encoding categorical features and standardizing numeric features
print("Encoding categorical features and standardizing numerical features...")
print(X_train)
print()

numeric_features = [1, 2]
numeric_transformer = StandardScaler()

categorical_features = [0]
categorical_transformer = OneHotEncoder()

featureencoder = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),    
        ('num', numeric_transformer, numeric_features)
        ]
    )

X_train = featureencoder.fit_transform(X_train)
print("...Done.")
print(X_train)
print()

# Training model
print("Training model...")
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)
print("...Done.")

# Predictions on training set
print("Predictions on train set...")
Y_train_pred = classifier.predict(X_train)
print("...Done.")
print()

### Test pipeline ###
print("--- Test pipeline ---") 

# Encoding categorical features and standardizing numeric features
print("Encoding categorical features and standardizing numerical features...")
print()

X_test = featureencoder.transform(X_test)
print("...Done.")
print(X_test)
print()

# Predictions on training set
print("Predictions on test set...")
Y_test_pred = classifier.predict(X_test)
print("...Done.")
print()

### Assessment of performances ###
print("--- Assessment of performances ---")

print("F1-score on train set : ", f1_score(Y_train, Y_train_pred))
print("F1-score on test set : ", f1_score(Y_test, Y_test_pred))
print()

print("Confusion matrix on train set : ")
print(confusion_matrix(Y_train, Y_train_pred))
print("Confusion matrix on test set : ")
print(confusion_matrix(Y_test, Y_test_pred))
print()


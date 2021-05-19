# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pMIWDpiyTe4NwC5yXwRzYmT1kUlXedXk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

features=pd.read_csv('training_data.csv')
features_test=pd.read_csv('test_data.csv')

print(features)

features=features.drop(['unit','patient_id','created_at','reference_high', 'reference_low','gender'],axis=1)

features_test=features_test.drop(['unit','patient_id','created_at','reference_high', 'reference_low','Unnamed: 0'],axis=1)

features.head(15)

features=features[features.standard_lab_parameter_name.str.contains('Chloride',case=False)]
features_test=features_test[features_test.standard_lab_parameter_name.str.contains('Chloride',case=False)]

features_test.head(15)

features.head(15)

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(features.age_group, features.parameter_value, color ='maroon',
        width = 0.4)
 
plt.xlabel("age_group")
plt.ylabel("parameter_value")
plt.title("chloride comparision of train_data")
plt.show()

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(features_test.age_group, features_test.parameter_value, color ='maroon',
        width = 0.4)
 
plt.xlabel("age_group")
plt.ylabel("parameter_value")
plt.title("chloride comparision of test_data")
plt.show()
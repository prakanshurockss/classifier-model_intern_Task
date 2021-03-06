# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pMIWDpiyTe4NwC5yXwRzYmT1kUlXedXk
"""

!pip install pandas-profiling==2.7.1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_profiling
from pandas_profiling import ProfileReport

features=pd.read_csv('training_data.csv')
features_test=pd.read_csv('test_data.csv')

#print(features)

features=features.drop(['created_at','reference_high', 'reference_low','gender'],axis=1)

features_test=features_test.drop(['unit','created_at','reference_high', 'reference_low','Unnamed: 0'],axis=1)

features=features[features.standard_lab_parameter_name.str.contains('Chloride',case=False)]
features_test=features_test[features_test.standard_lab_parameter_name.str.contains('Chloride',case=False)]

features_test.head(15)

#features_test.head(15)

#features.head(10000)

features.parameter_value[features.parameter_value == 0.67] =103
features_test.parameter_value[features_test.parameter_value == 0.67] =103

#generate profile report
profile= ProfileReport(features_test)
profile.to_file(output_file="chloride1.html")

features.describe()

pd.value_counts(features['age_group'])

age_list_new=features['age_group'].unique().tolist()
print(age_list_new)

list_mean=[]
for list in age_list_new:
  ans=features[features['age_group']==list]
  mean11=np.mean(ans['parameter_value'])
  list_mean.append(mean11)
  print(ans)
  print("==========================")
  print(ans.parameter_value.describe())
  ans.describe()
  fig = plt.figure(figsize=(50,10))
 
  # creating the bar plot
  plt.bar(ans.patient_id, ans.parameter_value, color ='maroon',width=10)
  plt.xlabel("age_group")
  plt.ylabel("parameter_value")
  plt.title("chloride comparision of"+ list)
  plt.show()
  print("-----------------------------------------------------")

print(list_mean)
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(age_list_new, list_mean, color ='maroon',
        width = 0.4)
 
plt.xlabel("age_group")
plt.ylabel("parameter_value")
plt.title("chloride comparision of train_data")
plt.show()

list_mean_test=[]
for list in age_list_new:
  ans=features_test[features_test['age_group']==list]
  mean12=np.mean(ans['parameter_value'])
  list_mean_test.append(mean12)
  print(ans)
  print("==========================")
  print(ans.parameter_value.describe())
  ans.describe()
  fig = plt.figure(figsize=(50,10))
 
  # creating the bar plot
  plt.bar(ans.patient_id, ans.parameter_value, color ='maroon',width=10)
  plt.xlabel("age_group")
  plt.ylabel("parameter_value")
  plt.title("chloride comparision of"+ list)
  plt.show()
  print("-----------------------------------------------------")

fig = plt.figure(figsize = (10, 5))
print(list_mean_test)
 
# creating the bar plot
plt.bar(age_list_new, list_mean_test, color ='maroon',
        width = 0.4)
 
plt.xlabel("age_group")
plt.ylabel("parameter_value")
plt.title("chloride comparision of test_data")
plt.show()
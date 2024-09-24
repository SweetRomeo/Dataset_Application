# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:02:23 2024

@author: BERKE
"""

import pandas as pd

data_frame = pd.DataFrame()
print(data_frame)

list_first = ['Python', 'Tutorial', 'for', 'Computer']
data_frame1 = pd.DataFrame(list_first)
print(data_frame1)

nested_list = [['Berke',  25], ['Kaya', 20]]
data_frame2 = pd.DataFrame(nested_list)
print(data_frame2)

data = {'Name' : ['Mustafa', 'Mehmet', 'Aslı'], 'Age' : [23, 27, 31]}
data_frame3 = pd.DataFrame(data);
print(data_frame3)

data1 = [{"Address" : "Pune",  "Contact" : 99999999}, 
         {"Name" : "Sevinç", "Address" : "Turkey", "Contact" : 99999999 }]
data_frame4 = pd.DataFrame(data1, index = ["one", "two"])
print(data_frame4)

l1 = ["A", "B",  "C"]
l2 = [10, 20, 30]
list_of_rows = list(zip(l1, l2))
data_frame5 = pd.DataFrame(list_of_rows)
print(data_frame5)

data_series = {"one" : pd.Series(l1, index = l2), 
               "two" : pd.Series([50,60,70], index = l2)}
data_frame6 = pd.DataFrame(data_series)
print(data_frame6)

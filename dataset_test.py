# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:09:03 2024

@author: BERKE
"""

import pandas as pd

dataset = pd.read_csv("balanced_data.csv")

col1 = dataset["sensor_id"]

print(col1)

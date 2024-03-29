# -*- coding: utf-8 -*-
"""Preprocessing_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mSFL5Nthx08dXtaNn9khvXkpfM6TQy3a
"""

import pandas as pd

# Reading the CSV file
frailty_data = pd.read_csv("/content/raw_frailty_data1.csv")

# Getting the info of the complete CSV
print(frailty_data.info())

# Renaming the columns
frailty_data.columns = ['Height', 'Weight', 'Age', 'Grip_Strength', 'Frailty']

frailty_data['Grip_Strength'] = round(frailty_data['Grip_Strength'] * 2.20462, 1)

# Understanding the data and dimensions
print(frailty_data.columns)
print(frailty_data.shape)

# Getting the top rows
print(frailty_data.head())

# Getting the data structure
print(frailty_data.dtypes)

# Converting 'Frailty' column to categorical type
frailty_data['Frailty'] = frailty_data['Frailty'].astype('category')

# Checking for missing values
print(frailty_data.isna().any())

# Writing the cleaned data to a new CSV file
frailty_data.to_csv("clean_frailty_data.csv", index=False)
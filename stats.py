""" Unit 2, lesson 1 Statistics"""

"""Data copied from a British government survey of 
average weekly household spending (in British 
pounds) on alcohol and tobacco products in each 
of the 11 regions of Great Britain"""

import pandas as pd
from scipy import stats 

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

"""splitting the string on newlines"""
data = data.splitlines()

"""list comprehension"""
data = [i.split(',') for i in data]

"""creating pandas dataframe"""
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

"""mean, median and mode of Alcohol and Tobacco"""
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print( "Alcohol mean is {0}".format(df['Alcohol'].mean()))

print("alcohol median is {0}".format(df['Alcohol'].median()))

print("alcohol mode result: {0}".format(stats.mode(df['Alcohol'])))

print("tobacco mean {0}".format(df['Tobacco'].mean()))

print("tobacco median {0}".format(df['Tobacco'].median()))

print("tobacco mode {0}".format(stats.mode(df['Tobacco'])))

"""Measures of central tendency, variability of data"""
"""Range, variance and std of alcohol and tobacco"""

print("The range in alcohol data: {0}".format(max(df['Alcohol']) - min(df['Alcohol'])))

print("The variance in alcohol data: {0}".format(df['Alcohol'].var()))



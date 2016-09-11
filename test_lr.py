import numpy as np 
import pandas as pd 
import statsmodels.api as sm 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

intrt = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

'''Reshaping data using transpose'''
y = np.matrix(intrt).transpose()

x1 = np.matrix(fico).transpose()

x2 = np.matrix(loanamt).transpose()

'''Input matrix'''
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()











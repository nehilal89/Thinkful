import pandas as pd 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loanamt = loansData['Amount.Requested']

intrt = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

loanl = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))


"""Convert FICO scores into a numerical value, 
and save it in a new column called FICO.Score"""

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: x.split('-'))

loansData['FICO.Score'] = loansData['FICO.Score'].map(lambda x: [float(n) for n in x])

fico = loansData['FICO.Score']

"""Histogram for FICO_Score"""

'''import matplotlib.pyplot as plt 

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()'''

"""Scatter plot of loansData"""

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

"""There is an approximate but unmistakable linear 
trend between FICO Score and Interest Rate, while 
there is no apparent trend between Monthly 
Income and Interest Rate."""

"""Linear Regression Analysis
a linear model with two independent variables: 
FICO Score and Loan Amount. This will help us 
determine the dependent variable, Interest Rate."""

'''Linear model
InterestRate = b + a1(FICOScore) + a2(LoanAmount)'''

import numpy as np 
import pandas as pd 
import statsmodels.api as sm 

intrt = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

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











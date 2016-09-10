"""Data Cleaning"""

import pandas as pd 
import statsmodels.api as sm 

loansData_clean = pd.read_csv('/Users/nilu057/thinkful/loansData_clean.csv')

loansData_clean['FICO.Score'] = loansData_clean['FICO.Range'].map(lambda x: x.split('-'))

loansData_clean['FICO.Score'] = loansData_clean['FICO.Score'].map(lambda x: int(min(x)))

fico = loansData_clean['FICO.Score']

intrt = loansData_clean['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 2))

loanl = loansData_clean['Loan.Length'].map(lambda x: int(x.rstrip('months')))

loansData_clean['lower_rate'] = loansData_clean[intrt].map(lambda x: 1 if x < 0.12 else 0)

print(loansData_clean['lower_rate'])

loansData_clean['intercept'] = 1.0

ind_vars = loansData_clean[loanl, fico]

'''print(loansData_clean[loansData_clean['Interest.Rate'] == 0.10].head())
print(loansData_clean[loansData_clean['Interest.Rate'] == 0.13].head())'''

"""Logistic Regression Model"""

logit = sm.Logit(loansData_clean['lower_rate'], loansData_clean[ind_vars])

"""fitting the model"""

result = logit.fit()

"""fitted coefficients"""
coeff = result.params
print(coeff)

"""linear prediction"""
''''interest_rate = -60.125 + 0.087423(FicoScore) - 0.000174(LoanAmount)'''

"""logistic function"""











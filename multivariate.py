#Use income (annual_inc) to model interest rates (int_rate).
#Add home ownership (home_ownership) to the model.
#Does that affect the significance of the coefficients in the original model?
#Try to add the interaction of home ownership and incomes as a term.
# How does this impact the new model?

#multiple linear regression

import pandas as pd

import numpy as np 


lending_data = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/blob/master/loans/loansData.csv')

intrt = lending_data['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

loanl = lending_data['Loan.Length'].map(lambda x: int(x.rstrip('months')))

lending_data['FICO.Score'] = lending_data['FICO.Range'].map(lambda x: x.split('-'))

lending_data['FICO.Score'] = lending_data['FICO.Score'].map(lambda x: int(min(x)))

fico = lending_data['FICO.Score']

Inc = lending_data['Monthly.Income']

print(inc)

"""Multiple Regression Analysis"""
y = np.matrix(intrt).transpose()

x1 = np.matrix(fico).transpose()

x2 = np.matrix(loanl).transpose()

x3 = np.matrix(Inc).transpose()

x4 = np.matrix(home_ownership).transpose()

x = np.column_stack([x1,x2,x3,x4])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()






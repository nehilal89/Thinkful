"""Lending Club Data"""

import matplotlib.pyplot as plt 
import pandas as pd 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

"""Boxplot"""

loansData.boxplot(column='Amount.Funded.By.Investors')

plt.show()

"""Histogram"""
loansData.hist(column='Amount.Funded.By.Investors')

plt.show()

"""QQ plot"""

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()




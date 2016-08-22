"""Lending Club Data"""

import matplotlib.pyplot as plt 

import pandas as pd 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

"""Boxplot"""

loansData.boxplot(column= "Amount.Requested")

plt.show()


"""Histogram"""
loansData.hist(column= "Amount.Requested")

plt.show()

"""QQ plot"""

import scipy.stats as stats

plt.figure()

graph = stats.probplot(loansData["Amount.Requested"], dist="norm", plot=plt)

plt.show()

"""Amounts between 5000 and 10000 seem to be both highly requested
and highly funded as values displayed on histogram. Amounts greater than
20000 were not requested as much"""




"""Testing Loan Data"""
"""Chi-square test"""

from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd 
import collections

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())

"""Resulting figure of data: there are around 25 unique number of open credit lines,
7 - 8 seems to be the most frequent open credit lines. The resulting
data is not evenly distributed"""

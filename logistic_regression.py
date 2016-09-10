"""Data Cleaning"""

import pandas as pd 
import statsmodels.api as sm 

def clean_loan_data(dataframe):
	dataframe['FICO.Score'] = dataframe['FICO.Range'].map(lambda x: x.split('-'))
	dataframe['FICO.Score'] = dataframe['FICO.Score'].map(lambda x: int(min(x)))
	fico = dataframe['FICO.Score']
	intrt = dataframe['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 2))
	loanl = dataframe['Loan.Length'].map(lambda x: int(x.rstrip('months')))
	dataframe['lower_rate'] = dataframe[intrt].map(lambda x: 1 if x < 0.12 else 0)
	return dataframe

def logistic_regression(cleaned_dataframe):
	cleaned_dataframe['intercept'] = 1.0
	ind_vars = cleaned_dataframe[loanl, fico]

	"""Logistic Regression Model"""
	logit = sm.Logit(cleaned_dataframe['lower_rate'], cleaned_dataframe[ind_vars])

	"""fitting the model"""
	result = logit.fit()

	"""linear prediction"""
	''''interest_rate = -60.125 + 0.087423(FicoScore) - 0.000174(LoanAmount)'''
	return result


def main():
	rawDataframe = pd.read_csv('/Users/nilu057/thinkful/dataframe.csv')
	cleanedDataframe = clean_loan_data(rawDataframe)
	print("Cleaned datas lower_rate %s " % dataframe['lower_rate'])
	result = logistic_regression(cleanedDataframe)
	# fitted coefficients	
	print("Logistic Regression coefficent: %s" % result.params)

if __name__ == '__main__':
	main()


'''print(dataframe[dataframe['Interest.Rate'] == 0.10].head())
print(dataframe[dataframe['Interest.Rate'] == 0.13].head())'''






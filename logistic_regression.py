import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

rateclean = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')), 4))
loansData['Interest.Rate'] = rateclean


lengthclean = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = lengthclean

loansData['FICO.Score'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

s = pd.Series(loansData['Interest.Rate'])
test = s <= 12

intercept = 1.0

loansData['Intercept'] = float(intercept)

loansData['Interest.LT12'] = test

ind_vars = ['Amount.Requested','FICO.Score','Intercept']

df = pd.DataFrame


logit = sm.Logit(loansData['Interest.LT12'], loansData[ind_vars])

result = logit.fit()

coeff = result.params
print coeff

a2 = coeff.values[0]*-1
a1 = coeff.values[1]
b = coeff.values[2]

userscore = input('Enter a FICO Score:' )
useramt = input('Enter a loan amount:' )

def linear_function(userscore, useramt, b, a1, a2):
		intrtcalc = (b + (a1 * userscore) - (a2 * useramt))
		return intrtcalc

test2 = linear_function(userscore, useramt, b, a1, a2)
	
print test2 

def logistic_function(userscore, useramt, b, a1, a2):
	lfcalc = 1 / (1+ math.e**(intercept + (a1 * userscore) - (a2 * useramt)))
	print lfcalc
	return lfcalc

test1 = logistic_function(userscore, useramt, b, a1, a2)

print test1

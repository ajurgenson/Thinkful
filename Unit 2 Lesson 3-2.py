import pandas as pd
import matplotlib.pyplot as plt
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

rateclean = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
rateclean[0:5]

lengthclean = loansData['Loan.Length'][0:5].map(lambda x: int(x.rstrip(' months')))
lengthclean[0:5]

loansData['FICO.Score'] = loansData['FICO.Range'].astype(str)
print loansData['FICO.Score'][0:5]

loans_list = loansData['FICO.Score'].tolist()

FICO = []
for array in range(len(loans_list)):
    loan = loans_list[array].split("-")  # Split each sub-array on '-'
    FICO.append(int(loan[0]))

loansData['FICO.Score'] = FICO

# Plot histogram
plt.figure()
p = loansData['FICO.Score'][0:5].hist()
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
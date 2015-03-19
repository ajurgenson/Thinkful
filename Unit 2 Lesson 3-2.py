import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

rateclean = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
rateclean[0:5]

lengthclean = loansData['Loan.Length'][0:5].map(lambda x: int(x.rstrip(' months')))
lengthclean[0:5]

ficoclean = loansData['FICO.Range'][0:5].map(lambda x: x.split('-'))
ficoclean[0:5]

ficoclean = ficoclean.map(lambda x: [int(n) for n in x])
ficoclean[0:5]



# ficoclean.compress([:,1, out])

# things = ficoclean.keys()

# serieal = pd.series(ficoclean[name][:,1] for name in things)


# x=0
# while x < 5:
# 	ficotest.append(ficoclean.values[x][0])
# 	x = x+1

# print(ficotest)

# ficoclean.values[4][0]

# plt.figure()
# p = ficoclean[0:5].hist()
# plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
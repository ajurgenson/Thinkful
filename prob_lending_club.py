import collections
import scipy.stats as stats
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

print("Loading QQ graph - amount requested")
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

print("Loading QQ graph - amount funded by investors")
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()


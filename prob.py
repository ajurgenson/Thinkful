import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

#List of data from the first part of U2 L2-1
testlist = [1, 4, 5, 6, 9, 9, 9]

#counts figures in testlist
c = collections.Counter(testlist)

#sums values for figure
count_sum = sum(c.values())

#outputs frequencies as percent of 100
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#Box Plot
plt.boxplot(testlist)
plt.show()

# Histogram
plt.hist(testlist, histtype='bar')
plt.show()

#QQ Plot
plt.figure()  
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show() #this will generate the first graph
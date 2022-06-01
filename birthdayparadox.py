import matplotlib.pyplot as plt
import numpy as np  
import statistics 
import math
import time

from scipy.stats import norm
start_time = time.time()
N2=1000
maxnumberforxaxis=65
mu=np.zeros(maxnumberforxaxis-2)
sigma=np.zeros(maxnumberforxaxis-2)
for k in range(2,maxnumberforxaxis):
	probability=[]
	for j in range(100):
		
		count=0
		for i in range(N2):
			
			result=False
			A=np.random.randint(1,366,size=k)
			if len(A) != len(set(A)):
				result=True
			count+=int(result)
		probability.append(count/N2)
	(mu[k-2], sigma[k-2]) = norm.fit(probability)
	if k==23:
		plot=plt.figure(1)		
		n, bins, patches = plt.hist(probability, 30, density=True, facecolor='green', alpha=0.75)
		z=norm.pdf(bins,mu[k-2],sigma[k-2])
		l = plt.plot(bins, z, 'r--', linewidth=2)
		plt.xlabel('Probability ')
		plt.ylabel('Ocurrences')
		plt.title(r'$\mathrm{Histogram\ of\ Probabilities:}\ N=%d,\ \mu=%.3f,\ \sigma=%.3f$' %(k,mu[k-2], sigma[k-2]))
		plt.grid(True)

	
N=range(2,maxnumberforxaxis)
plot=plt.figure(2)
plt.errorbar(N, mu, sigma,fmt='ob',capsize=2,markersize=2)
y=[]
x=[]
for i in range(len(N)):
	y.append(1-math.perm(365,N[i])/365**N[i])
	x.append(0.5)
	
plt.plot(N,y,'r')
plt.plot(N,x,'r')
plt.xlabel('Number of people in the group')
plt.ylabel('Probability of finding two people with same birthday')
plt.title(r'Graph of the Birthday Paradox')
plt.grid(True)
print("--- %.2f seconds ---" % (time.time() - start_time))
plt.show()
	


import matplotlib.pyplot as plt
import numpy as np   
import math
stoptime=[]
maxnumber=25+1
for n in range(1,maxnumber):
	x=[]
	x.append(n)
	while n!= 1:
		if n%2==0:
			n=n//2
			x.append(n)
		else:
			n=3*n+1
			x.append(n)
	
		
	stoptime.append(len(x)-1)
plt.scatter(range(1,maxnumber),stoptime)
plt.xticks(np.arange(min(range(1,maxnumber)), max(range(1,maxnumber))+1, 1.0))
plt.yticks(np.arange(min(stoptime), max(stoptime)+1, 1.0))
plt.xlabel('Starting Number')
plt.ylabel('Number of Steps or Stopping time')
plt.title(r'A "simple" problem')
plt.grid(True)
plt.show()
	


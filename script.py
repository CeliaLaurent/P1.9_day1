from __future__ import print_function    # (at top of module)
import numpy as np
import matplotlib.pyplot as plt

# creating xval using numpy to set range given that the standard range function is for integers only
# using np.around to have exact evenly spaced numbers between -5.0 and 5.0 (inclusive, 0.1 apart) 
# converting it to a list to match instructions of the exerrcises.
xval=list(np.around(np.arange(-5.,5.,0.1),decimals=1))

# create empty yval list to test plotting 
yval=list(np.zeros((len(xval)),dtype=float))

plt.plot(xval,yval)
plt.xlabel('x')
plt.ylabel('y')
plt.title('basics')
plt.show()


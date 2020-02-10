from __future__ import print_function    # (at top of module)
import numpy as np
import matplotlib.pyplot as plt
import sys

def function1(x):
    return x

# adding usage instructions
def usage():
    print("Usage: this scripts takes one <int> argument")
    print(" - 'python script.py 1' plots y=x")
    sys.exit() 

if(len(sys.argv)!=2):
    usage()

# creating xval using numpy to set range given that the standard range function is for integers only
# using np.around to have exact evenly spaced numbers between -5.0 and 5.0 (inclusive, 0.1 apart) 
# converting it to a list to match instructions of the exerrcises.
xval=list(np.around(np.arange(-5.,5.,0.1),decimals=1))

if(sys.argv[1]=="1"):
    # if user entered argument 1 : 
    yval=function1(xval)
else:
    # create null yval list as default case 
    yval=list(np.zeros((len(xval)),dtype=float))

# plots -----------------------------------------------
plt.plot(xval,yval)
plt.xlabel('x')
plt.ylabel('y')
plt.title('basics arg='+sys.argv[1])
plt.show()


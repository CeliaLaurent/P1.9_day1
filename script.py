from __future__ import print_function    # (at top of module)
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

def function1(x):
    return x

def function2(x):
    y=list(np.zeros((len(xval)),dtype=float))
    for pos,val in enumerate(x):
      y[pos]=math.sin(val)
    return y

def function3(x):
    y=list(np.zeros((len(xval)),dtype=float))
    for pos,val in enumerate(x):
      y[pos]=math.cos(val)
    return y

def function4(x):
    y=list(np.zeros((len(xval)),dtype=float))
    for pos,val in enumerate(x):
      y[pos]=math.tan(val)
    return y

# adding usage instructions
def usage():
    print("Usage: this scripts takes one <int> argument")
    print(" - 'python script.py 1' plots y=x")
    print(" - 'python script.py 2' plots y=sin(x)")
    print(" - 'python script.py 3' plots y=cos(x)")
    print(" - 'python script.py 4' plots y=tan(x)")
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
elif(sys.argv[1]=="2"):
    # if user entered argument 2 : 
    yval=function2(xval)
elif(sys.argv[1]=="3"):
    # if user entered argument 3 : 
    yval=function3(xval)
elif(sys.argv[1]=="4"):
    # if user entered argument 4 : 
    yval=function4(xval)
else:
    # create null yval list as default case 
    yval=list(np.zeros((len(xval)),dtype=float))

# plots -----------------------------------------------
plt.plot(xval,yval)
plt.xlabel('x')
plt.ylabel('y')
plt.title('calling function '+sys.argv[1])
plt.show()


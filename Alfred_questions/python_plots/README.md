# Plotting data files using python and alfred

```
import sys
import numpy as np 
import matplotlib.pyplot as plt

ifile = sys.argv[1]

x,y = np.genfromtxt(ifile,delimiter='',usecols=(0,1),\
                  comments='#',unpack=True,dtype=None).astype(np.float64)

plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(min(x)*0.9, max(x)*1.1)
plt.ylim(min(y)*0.9, max(y)*1.1)
plt.show()
```

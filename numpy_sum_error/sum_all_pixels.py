import numpy as np
from astropy.io import fits

# data
infile = 'psf0.fits.zip'
# infile = 'a.fits'
data = fits.getdata(infile)

# method 1
total1 = np.sum(data)

    
# method 2
total2 = 0.0
for i in range(data.shape[0]):
    total2 += np.sum(data[i])
    
# difference
diff = total1 - total2
print('{:.2f}'.format(total1))
print('{:.2f}'.format(total2))
print('{:.2f}'.format(total1-total2))

#!python
# -*- coding: utf-8 -*-#
"""
Create fitsfile.

@author: Bhishan Poudel

@date:  Feb 20, 2018

"""
# Imports

import numpy as np
from astropy.io import fits

def create_fitsfile(outfile):
    data = np.arange(1,21).reshape(4,5)
    print(data)
    
    fits.writeto(outfile,data,clobber=True)

def main():
    """Run main function."""
    outfile = 'a.fits'
    create_fitsfile(outfile)

if __name__ == "__main__":
    main()

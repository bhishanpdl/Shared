#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-19-2016 Wed
# Last update : Oct 25, 2016 Tue
#
# Command: galfit sim.feedme
# Command: galfit -o3 galfit.01
# Command: ds9 -multiframe imgblock.fits &
#
#
# Estimated time : 1 min for 1 input galaxy
#
# Imports
from __future__ import division, unicode_literals, print_function
import subprocess
import os
import time
from string import ascii_uppercase
import astropy.io
from astropy.io import fits
from astropy.io.fits import getdata
from astropy.io.fits import getheader
from astropy.io.fits import getval

_sim_feedme = r'sim.feedme'


def replace_galfit_param(name, value, object_num=1, fit=True):
    """
    Replaces a parameter value in the galfit configuration file.

    param name: parameter name, without the following parenthesis
    param value: new value for the parameter. Best provided as a string
    param object_num: For object parameters, which object to change. Galfit
                   numbering, whichs starts with 1. Non-object params (e.g. B)
                   should use default object=1
    param fit: Whether to fit the parameter (True) or hold fixed (False)
    """
    name, value = str(name), str(value)
    with open(_sim_feedme) as f:
        gf_file = f.readlines()

    # Location of param.
    loc = [i for i in range(len(gf_file)) if
           gf_file[i].strip().startswith(name + ')')][object_num - 1]
    param_str = gf_file[loc]
    comment = param_str.find('#')
    if name in ascii_uppercase:
        fmt = '{}) {} {}'
        param_str = fmt.format(name, value, param_str[comment:])
    else:
        fmt = '{}) {} {} {}'
        param_str = fmt.format(name, value, '0' if fit else '1',
                               param_str[comment:])
    gf_file[loc] = param_str
    with open(_sim_feedme, 'w') as f:
        f.writelines(gf_file)


def run_galfit(galaxy, outdir, count):
    """ Runs galfit on the given input galaxies and creates model
        and residue images in the output directory

        galaxy : base name of input galaxy, e.g f606w  for f814w
        outdir : output directory, e.g. galfit_outputs
        count  : count number of galaxy, e.g. 0 for f606w_gal0.fits
    """
    print('{} {} {}'.format('Running loop: ', count, ''))
    # galaxy = f606w or f814w
    path = '/Users/poudel/jedisim/simdatabase/colors'
    ingal = path + '/' + galaxy + '_gal' + str(count) + '.fits'
    psf = galaxy + '_psf.fits'  # psf in the same directory

    #  get the value of magnitude and radius of input galaxy
    mag = getval(ingal, 'MAG')
    rad = getval(ingal, 'RADIUS')

    # create feedme according to galaxy
    # For A-Z object_num is 1
    # Fit=True means it is fixed and not changed
    replace_galfit_param('A', ingal, object_num=1, fit=True)
    replace_galfit_param('D', psf, object_num=1, fit=True)

    # For objects, object_num starts from 1
    # 1 = devauc, 2 = expdisk
    for obj_num in [1, 2]:
        replace_galfit_param('3', mag, object_num=obj_num, fit=True)
        replace_galfit_param('4', rad, object_num=obj_num, fit=True)

    #  delete previous output before running
    #  but do not delete fit.log
    outfiles = [r'imgblock.fits', r'subcomps.fits', 'galfit.01']
    for outfile in outfiles:
        if os.path.exists(outfile):
            print('{} {} {}'.format('Deleting: ', outfile, ''))
            os.remove(outfile)

    # run galfit
    cmd = 'galfit sim.feedme && galfit -o3 galfit.01 && rm -r galfit.01 '
    subprocess.call(cmd, shell=True)

    # get residual map from imgblock.fits
    residual = outdir + '/' + galaxy + '_res' + str(count) + '.fits'

    # get devauc and expdisk models from subcomps.fits
    devauc = outdir + '/' + galaxy + '_devauc' + str(count) + '.fits'
    expdisk = outdir + '/' + galaxy + '_exp' + str(count) + '.fits'
    expdisk_res = outdir + '/' + galaxy + '_exp_res' + str(count) + '.fits'

    # for imgblock.fits 0 is empty, 1 is input, 2 is residual
    data1, header1 = fits.getdata(r'imgblock.fits', ext=2, header=True)

    # for subcomps.fits 0 is subcomps.fits, 1 is devauc, 2 is expdisk
    data2, header2 = fits.getdata(r'subcomps.fits', ext=1, header=True)
    data3, header3 = fits.getdata(r'subcomps.fits', ext=2, header=True)

    fits.writeto(residual, data1, header1, clobber=False)
    fits.writeto(devauc, data2, header2, clobber=False)
    fits.writeto(expdisk, data3, header3, clobber=False)
    fits.writeto(expdisk_res, data3 + data1, header3, clobber=False)
    print('{} {} {}'.format('Output file: ', residual, ''))
    print('{} {} {}'.format('Output file: ', devauc, ''))
    print('{} {} {}'.format('Output file: ', expdisk, ''))
    print('{} {} {}'.format('Output file: ', expdisk_res, ''))


if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    galfit_outdir = 'galfit_outputs'

    # for i in list(range(0,101)):
    for count in list(range(101)):
        run_galfit('f606w', galfit_outdir, count)
        run_galfit('f814w', galfit_outdir, count)

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime, '\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

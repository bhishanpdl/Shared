# parameter file for galfit
# Header values for f606w_gal14.fits
# NAXIS1  = 601
# NAXIS2  = 601
# MAG     = 22.4002
# RADIUS  = 13.683
# PIXSCALE=  0.03
# MAG0    = 30
#
# #   Main commands : ic '1 0 %1 0 == ?'  INPUT_GALAXY  > mask.fits
#                 rm -r imgblock.fits subcomps.fit ; galfit expdisk_devauc.sh
#                 galfit -o3 galfit.01 && rm -r galfit.01
#                 ds9 -cmap a -scale log -multiframe imgblock.fits subcomps.fits &
#
# ic '1 0 %1 0 == ?'  f606w_gal14.fits  > mask.fits
# ds9 mask.fits f606w_gal14.fits &
#
# IMAGE and GALFIT CONTROL PARAMETERS
A) f606w_gal14.fits
B) imgblock.fits       # Output data image block
C) none                # Sigma image name (made from data if blank or "none")
D) f606w_psf.fits # Input PSF image and (optional) diffusion kernel
E) 2                   # PSF fine sampling factor relative to data
F) mask.fits           # Bad pixel mask (FITS image or ASCII coord list)
G) none                # File with parameter constraints (ASCII file)
H) 1 601 1 601         # Image region to fit (xmin xmax ymin ymax)
I) 200  200            # Size of the convolution box (x y)
J) 30.0 # Magnitude photometric zeropoint
K) 0.03  0.03          # Plate scale (dx dy)    [arcsec per pixel]
O) regular             # Display type (regular, curses, both)
P) 0                   # Choose: 0=optimize, 1=model, 2=imgblock, 3=subcomps

# IMAGE and GALFIT OBJECT PARAMETERS
# Component number: 1
# Exponential function (concentration index n = 1)
# This gives disk profile.
0) expdisk            # Object type
1) 301.  301.  1 1    # position x, y        [pixel]
3) 22.4002 1         # total magnitude
4) 13.683 1         #     Rs               [Pixels]
9) 0.5        1       # axis ratio (b/a)
10) 100.0      1      # position angle (PA)  [Degrees: Up=0, Left=90]
Z) 0                  #  Skip this model in output image?  (yes=1, no=0)


# Component number: 2
# deVaucouleur function (concentration index n = 4)
# This gives the bulge profile.
0) devauc             # Object type
1) 300.0 300.0 1 1    # position x, y        [pixel]
3) 22.4002 1         # total magnitude
4) 13.683 1         #     R_e              [Pixels]
9) 0.5        1       # axis ratio (b/a)
10) 100.0       1     # position angle (PA)  [Degrees: Up=0, Left=90]
Z) 0                  #  Skip this model in output image?  (yes=1, no=0)

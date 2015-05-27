# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import astropy.io.fits as fits
from scipy.ndimage import gaussian_filter
import numpy as np
import random


def generate_star(intensity, count, outfile):
    #generates 100 synthetic stars to be added into a today image for the Monte Carlo simulation
    
# Create empty image
    nx, ny = 4096, 4096 #number of x pixels, number of y pixels
    image = np.zeros((ny, nx)) #generates an array of zeros

# Set number of stars
    n=100
    counter = 0 #counter ensures that we have n number of stars
    while counter < count:
    # find x,y coordinates of candidate star
        r = np.random.random(1) * nx

# Generate random positions
    
        theta = np.random.uniform(0., 2. * np.pi,1)

# Generate random fluxes
    #f = np.random.random(n) ** 2

# Compute position
        x = nx / 2 + r * np.cos(theta)
        y = ny / 2 + r * np.sin(theta)
        x=round(x,0)
        y=round(y,0)
        #print x
        #print y

# Add stars to image
# ==> First for loop and if statement <==
    
        
        if x >= 0 and x < nx and y >= 0 and y < ny: #if the randomly generated positions for the stars are within the image, then the counter is increased. this ensures that we have n number of stars in the end.
            image[y, x]= intensity
            counter=counter +1
            #print counter

# Convolve with a gaussian
    image = gaussian_filter(image, 1) #to take into account the gaussian nature of the stars


# Write out to FITS image
#Resulting FITS image will have 100 synthetic stars
    fits.writeto(outfile, image, clobber=True)




# searching_for_supernovae
Undergraduate thesis : "Searching for Supernovae". 
A pipeline was developed with the goal of searching for Type Ia Supernovae using the University of British Columbia’s 
Southern Observatory’s 0.35 m robotic telescope located on Cerro Tololo, Chile. 

----------------------------------------------------------------------------------------------------------

The Align program (anchor_star:
The align program aligns each observation image with respect to a chosen reference image. 
The align program matches 10 bright stars in the observation image to the corresponding bright stars in the 
reference image.

Example:

----------------------------------------------------------------------------------------------------------
Find Supernovae program:
Either due to imperfections in aligning the today image with respect to the master image or due to different seeing,
the residual image will contain the residual of the bright stars present in the today image.
The Find Supernovae program compares the coordinates of the objects in the residual image with the 
coordinates of bright stars in the master image and generates a list of potential supernovae candidates.

//Example: 
$ipython find_supernovae(list_that_is_being_checked,reference list) 
The first that is being checked contains the coordinates of the residuals. 

----------------------------------------------------------------------------------------------------------

The Varying Radius program: (more info needed)
The varying radius program optimizes the dead zone radius by taking into the account the size of the stars 
in an image via the number of pixels of the semi major axis



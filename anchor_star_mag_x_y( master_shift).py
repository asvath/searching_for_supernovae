# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def extract_xyab(filename): 
#extracts the x and y coordinates and the semi major and semi minor axes
    masterFile = open(filename, 'r')

    i = 0
    alert = False
    x=[]
    y=[]
    a=[]
    b=[]
    for line in masterFile:
    
        if '#' in line:
            alert = True

        if '#' not in line and alert
        
            splittedline=line.split()
            x.append(float(splittedline[1])) #adds x value of new line to x the  list
            y.append(float(splittedline[2])) #adds y value of new line to y the list
            a.append(float(splittedline[6]))
            b.append(float(splittedline[7]))
            
        
    masterFile.close()
    return x,y,a ,b  

# <codecell>

x,y,a,b=extract_xyab('master2.txt')
#gets the x and y coordinates of objects in reference image
x_today,y_today,a_today,b_today=extract_xyab('A1185-20140321-001-flat.txt')
#gets x and y coordinates of objects in the image that is to be shifted#
# <codecell>

import numpy as np
def get_brightest_stars(num_stars,x,y,a,b):
    #gets the coordinates of the brightest stars in the image.
    #x and y coordinates of those stars, the semi major and minor axis.
    real_x_values = [x_val for (a_val,x_val) in sorted(zip(a,x), reverse=True, key=lambda pair: pair[0])]
    real_y_values = [y_val for (a_val,y_val) in sorted(zip(a,y), reverse=True, key=lambda pair: pair[0])]
    real_b_values = [b_val for (a_val,b_val) in sorted(zip(a,b), reverse=True, key=lambda pair: pair[0])]
    real_a_values = sorted(a, reverse=True)
    frame_x=[] #to avoid the edge of the image
    frame_y=[]
    frame_a=[]
    frame_b=[]
    for k in range(0, len(real_x_values)):
        if real_x_values[k]>500 and real_x_values[k]<3500 and real_y_values[k]>500 and real_y_values[k]<3500 and real_a_values[k]-real_b_values[k]<3:
            #to avoid the edge of the image and to get a-b <3 (semi major-semi minor axis is to approximately get the bright stars by assuming that bright stars are circular in an image.
                       frame_x.append(real_x_values[k])
                       frame_y.append(real_y_values[k])
                       frame_a.append(real_a_values[k])
                       frame_b.append(real_b_values[k])
                       if len(frame_x)>num_stars:
                            break
                       
                   
    return frame_x, frame_y, frame_a, frame_b

# <codecell>

master_x, master_y, master_a, master_b =get_brightest_stars(90,x,y,a,b) #gets the brightest stars of the master image
today_x, today_y, today_a, today_b= get_brightest_stars(10,x_today,y_today,a_today, b_today)#gets brightest stars of the image to be shifted

# <codecell>

print sorted(zip(today_x, today_y, today_a, today_b))
print '---'

# <codecell>

#with these two lists write a function that calculates the cost (distances) between stars in reference & to be shifted list: shift

# <codecell>

def single_cost(master_x,master_y,master_a,master_b,x,y,a,b):
    #calculates the minimum distance between one coordinate in the image to be shifted vs coordinates in reference image. 
    #cost is calculated as we don't know if the brightest stars in the image to be shifted is the same as those in the master image
    distance_list=[]
    
    for i in range(0,len(master_x)):
        if np.abs(master_a[i]-a)<1.5 and np.abs(master_b[i]-b)<1.5: #to check if the object in the image to be shifted is similar to the object in the reference image by checking if their semi major and minor axis are close in pixel value
            dist=np.sqrt((x-master_x[i])**2 + (y-master_y[i])**2) #calculates the difference in distance between the object that is being checked and all similar objects in the reference image
            distance_list.append(dist)
    try:
        return min(distance_list)    #takes the least cost, therefore the minimum distance obtained in the step before this
    except:
        print x,y,a
        return 0

def grand_cost(master_x,master_y,master_a,today_x,today_y,today_a,delta_x,delta_y):
    #checks the total minimum distance that the entire image needs to be shifted by
    list_single_cost_sq=[]
    for j in range(0, len(today_x)):
        min_distance=single_cost(master_x,master_y,master_a,master_b,today_x[j]+delta_x,today_y[j]+delta_y,today_a[j],today_b[j])
        list_single_cost_sq.append(min_distance)
    return np.mean(list_single_cost_sq)

# <codecell>
import scipy
from scipy.optimize import minimize
optimize_cost=lambda (delta_x,delta_y) : grand_cost(master_x,master_y,master_a,today_x,today_y,today_a,delta_x,delta_y) #optimize the least cost

myfit = scipy.optimize.minimize(optimize_cost,np.asarray([0,0]))
                        #method="L-BFGS-B", options={'maxiter':500})

# <codecell>

print int(myfit.x[0]), int(myfit.x[1])





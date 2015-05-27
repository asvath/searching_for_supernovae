
# <nbformat>3.0</nbformat>
# <codecell>

def extract_xyab(filename):
    #gets the x and y coordinates of the file
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

        if '#' not in line and alert:
            
       # print line
        # entire program is here
        #f(a) = a is the argument of function, f. X[n]=nth entry of a vector,X, list etc.
        
            splittedline=line.split()
            x.append(float(splittedline[1])) #adds x value of new line to x the  list
            y.append(float(splittedline[2])) #adds y value of new line to y the list
            a.append(float(splittedline[6]))
            b.append(float(splittedline[7]))
        
    masterFile.close()
    return x,y,a,b 

import numpy as np



# <codecell>

def is_candidate_a_supernova(x_test, y_test, x_master, y_master,a_master,b_master):
    #to test if candidate is a supernova
    
    Supernova = True
     
    for x_star,y_star,a_star,b_star in zip(x_master, y_master,a_master,b_master):
        r=max(a_star,b_star) #sorts the coordinates, the semi major and minior axes
        
        if (x_test-x_star)**2 + (y_test-y_star)**2 <((1)*r)**2: #the optimal dead zone radius for this case is the number in the brackets (( )*r)**2. 
            #The program compares if the objects in the today image has a match in the master image via the dead zone radius. 
            #The dead zone radius is the radius set up around the coordinate on the bright stars list from the master image.
            Supernova = False
            break
        
    return Supernova

# <codecell>

def list_supernovae(x_diff,y_diff,x_master,y_master,a_master,b_master):
    #returns list of the x coordinates and of the y coordinates of the the objects that were left unmatched in the process above
    list_supernova_x=[]
    list_supernova_y=[]
    for j in range(0, len(x_diff)):
        c=x_diff[j]
        d=y_diff[j]
        Supernova=is_candidate_a_supernova(c,d,x_master,y_master,a_master,b_master) #calls the previous function to check if candidate is a supernova
        if Supernova==True:
            list_supernova_x.append(c) #appends to list
            list_supernova_y.append(d)
    return list_supernova_x, list_supernova_y

# <codecell>

def find_supernovae(res_fake_star_on_galaxy,master_comprehensive):
    #generates a list that has both the x and the y coordinates of the supernovae candidates
    x_master, y_master, a_master,b_master =extract_xyab(master_comprehensive)

    x_diff,y_diff,a_diff,b_diff=extract_xyab(res_fake_star_on_galaxy)

    list_supernova_x, list_supernova_y=list_supernovae(x_diff,y_diff,x_master,y_master,a_master,b_master)

# <codecell>

    outputFile = open('list_of_supernovae.txt', 'w') # a txt file is generated containing the list of supernovae candidates

    outputFile.write('List of Supernovae!\n')

    for i in range(0, len(list_supernova_x)):
                   x_value = list_supernova_x[i]
                   y_value = list_supernova_y[i]
                   outputFile.write(str(x_value) + ' '+ str(y_value) + '\n')
               
    outputFile.close()
    return len(list_supernova_x)

# <codecell>



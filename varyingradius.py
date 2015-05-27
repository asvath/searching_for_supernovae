
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

# <codecell>

x_master, y_master, a_master,b_master =extract_xyab('master_comprehensive.txt')
#gets the x and y coordinates of objects in the the master image
# <codecell>

x_diff,y_diff,a_diff,b_diff=extract_xyab('test_res.txt')
#gets the x and y coordinates of the file test_res which is the file that contains the x and y coordinates of the residuals in the residual image

# <codecell>

def is_candidate_a_supernova(x_test, y_test, x_master, y_master,a_master,b_master, alpha):
    #checks if the coordinates in the residual image matches the coordinates in the master image. alpha is the proportionality constant that relates the major axis of a star to the dead zone radius. i.e alpha=dead zone radius/semi major axis
    #we want to determine the optimal dead zone radius.i.e alpha the proportionality constant
    Supernova = True
     
    for x_star,y_star,a_star,b_star in zip(x_master, y_master,a_master,b_master):
        r=max(a_star,b_star)
        
        if (x_test-x_star)**2 + (y_test-y_star)**2 <(alpha*r)**2:
            Supernova = False
            break
        
    return Supernova

# <codecell>

def list_supernovae(x_diff,y_diff,x_master,y_master,a_master,b_master,alpha):#generates the list of the x and y coordinates of potential supernovae candidates
    list_supernova_x=[]
    list_supernova_y=[]
    for j in range(0, len(x_diff)):
        c=x_diff[j]
        d=y_diff[j]
        Supernova=is_candidate_a_supernova(c,d,x_master,y_master,a_master,b_master, alpha)
        if Supernova==True:
            list_supernova_x.append(c)
            list_supernova_y.append(d)
    return list_supernova_x, list_supernova_y


# <codecell>

results_list=[]

def frange(start, end=None, inc=None): #changes the alpha value and checks the number of objects that show up as potential SNe candidates. 
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L
alpha_list = [round(x,2) for x in frange(0.1,5,0.1)]
for j in range(0, len(alpha_list)):
    
    alpha=alpha_list[j]
    
    
    list_supernova_x, list_supernova_y=list_supernovae(x_diff,y_diff,x_master,y_master,a_master,b_master, alpha)
    results_list.append(len(list_supernova_x))

# <codecell>

len(list_supernova_x)

# <codecell>

outputFile = open('list_of_supernovae.txt', 'w')

outputFile.write('List of Supernovae!\n')

for i in range(0, len(list_supernova_x)):
               x_value = list_supernova_x[i]
               y_value = list_supernova_y[i]
               outputFile.write(str(x_value) + ' '+ str(y_value) + '\n')
               
outputFile.close()

# <codecell>

print results_list

# <codecell>

import matplotlib.pyplot as plt
%pylab inline
plt.plot(alpha_list,results_list)
plt.ylabel('number of stars detected')
plt.xlabel('alpha = rejection radius/semi-major axis')
#plt.title(str([alpha for alpha, result in zip(alpha_list,results_list) if not result>0][0]))
figure=plt.gcf()
#figure.set_size_inches(8,6)
figure.set_size_inches(8,6)
plt.savefig('plot_alpha_without_fake_star.jpg',dpi=600)

# <codecell>

[alpha for alpha, result in zip(alpha_list,results_list) if not result>0][0] #reports the alpha value when the SNe candidate list no longer has a false alarm (not a supernova but still shows up on the list)

# <codecell>

print alpha

# <codecell>



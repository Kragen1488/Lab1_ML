import numpy as np
import random
import matplotlib.pyplot as plt

def Checkcirc(listofpoints,a,b,cp):
    scirc = 0
    for i in range(cp):
        sum = 0
        for j in range(b):
            sum = sum + (listofpoints[i][j])**2
        if sum <= (a/2)**2:
            scirc +=1
    return scirc/cp
        

if __name__ == '__main__':
    listofpoints = []
    a = 100 
    cp = 10000 

    bmin = 1 
    bmax = 20 
    xlist = np.linspace(bmin, bmax, bmax-bmin+1)
    ylist = []

    
    for b in range(bmin,bmax+1):
        listofpoints = []
        for i in range(cp):
            temp = []
            for j in range(b):
                temp.append( random.randint(-a/2, a/2) )
            listofpoints.append( temp )
        ylist.append(Checkcirc(listofpoints,a,b,cp))
    
    plt.plot(xlist, ylist)
    plt.show()
 
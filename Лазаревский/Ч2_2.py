import numpy as np
import matplotlib.pyplot as plt

def Calculatorf(a):
    return a - (a**3)/6 + (a**5)/120 - (a**7)/5040

def Calculatorg(a):
    return np.sin(a)

if __name__ == '__main__':
    amin = -5.0
    amax = 5.0
    alist = np.linspace(amin, amax, 1000)
    blist_f = [Calculatorf(a) for a in alist]
    blist_g = [Calculatorg(a) for a in alist]
    plt.plot(alist, blist_f)
    plt.plot(alist, blist_g)
    plt.show()

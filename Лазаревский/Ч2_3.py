import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    r = 10
    disk = plt.Circle((0, 0), r, color='r')
    ax=plt.gca()
    ax.add_patch(disk)
    plt.axis('scaled')
    plt.show()

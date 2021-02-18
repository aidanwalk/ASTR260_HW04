import matplotlib.pyplot as plt
import numpy as np

#load data from file
potential = np.loadtxt('calculated_potential.txt', delimiter=',')
#filter out data extremes 
potential[potential > 10e11] = None
#plot and show
plt.contourf(potential)
plt.show()
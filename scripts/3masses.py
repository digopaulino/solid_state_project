# First, lets make a system with 3 masses
import numpy as np
from scipy import linalg as la

m=1 #Mass
k=1 #Elastic Constant

n=3 #Number of masses


D = np.zeros(shape=(3,3))

for i in range(0,2):
    D[i][i]=2*k/m
D[0][1]=-k/m
D[1][0]=-k/m
D[1][2]=-k/m
D[2][1]=-k/m


eigvalues = la.eig(D)[0]
eigvectors = la.eig(D)[1]

print('Frequencies: ', eigvalues)
print('Displacements: ', eigvectors)
print('Displacement of the first mass: ', eigvectors[0])

import numpy as np
from scipy import linalg as la

m=1 #Mass
k=1 #Elastic Constant
n = int(input('Insira o número de massas: ')) #Number of masses

D = np.zeros(shape=(n,n))

D[0][0]=k/m #Define a diagonal nas bordas
D[n-1][n-1]=k/m

for i in range(1,(n-1)):
    D[i][i]=2*k/m #Define a diagonal no centro
    D[i][i+1]=-k/m #Define os vizinhos da diagonal no centro
    D[i][i-1]=-k/m

D[0][1]=-k/m #Define os vizinhos da diagonal nas bordas
D[n-1][n-2]=-k/m

a, v = la.eig(D) #Autovalores para a, autovetores para v

ind = np.argsort(a) #Retornam os índices que ordenariam os autovalores
eigvalues = np.around(a[ind],10) #Vetor de autovalores ordenados
eigvectors = np.around(v[:,ind],10) #Matriz de autovetores ordenados

import matplotlib.pyplot as plt
from masses import *
import numpy as np

size= 0.4 #4/size deve ser um número inteiro
m = int(4/size)

w2 = np.arange(0, 4, size)
counts = np.zeros(shape=(m))
x_axis = np.zeros(shape=(m))

for i in range(0,m):
    for j in range(0,len(eigvalues)):
        if eigvalues[j] < w2[i]+size and eigvalues[j] >= w2[i]:
            counts[i]+=1

for i in range(0,len(w2)):
    x_axis[i] = w2[i]+size/2


print(counts)
plt.title('Densidade de estados')
plt.bar(x_axis, counts, width=size, color='w', edgecolor='r')
plt.xticks(np.arange(0, 4.1, 0.4))
plt.yticks(np.arange(0,400,1))
plt.xlabel(r'$\omega^2$')
plt.axis([-0.05, 4, 0, 30]) #ALTERAR ÚLTIMO VALOR PARA MUDAR VALOR MÁXIMO DE Y
#plt.xticks(x_axis)
plt.ylabel('Count')

plt.show()

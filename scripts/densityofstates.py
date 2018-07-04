import matplotlib.pyplot as plt
from masses import *
import numpy as np

size=0.1
m = 40

x_axis = np.arange(0, 4, size)
counts = np.zeros(shape=(m))

for i in range(0,40):
    for j in range(0,len(eigvalues)):
        if eigvalues[j] < x_axis[i]+0.1 and eigvalues[j] >= x_axis[i]:
            counts[i]+=1

print(counts)
plt.title('Densidade de estados')
plt.bar(x_axis, counts, width=0.1, color='w', edgecolor='r')
plt.xticks(np.arange(0, 4.1, 0.4))
plt.yticks(np.arange(0,16,1))
plt.xlabel(r'$\omega^2$')
plt.axis([-0.05, 4, 0, 12])
#plt.xticks(x_axis)
plt.ylabel('Count')

plt.show()

import matplotlib.pyplot as plt
from masses import *
from random import randint

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

m = 0 #randint(0,n-1)
txt = chr(969)+'² = '+str(round(eigvalues[m].real, 6))

title = 'Deslocamento das massas com a frequencia ', m
plt.title(title)

plt.text(60,0.14,txt,fontsize=12)
plt.plot(x_axis, eigvectors[:,m], linestyle='--', marker='o', color='b')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')

plt.show()

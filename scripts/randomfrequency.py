import matplotlib.pyplot as plt
from masses import *
from random import randint

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)
m = randint(0,n-1)
txt = 'w² = ', eigvalues[m].real

title = 'Gráfico do deslocamento das massas com a frequencia ', m
plt.title(title)

plt.text(1,0.1,txt,fontsize=9)
plt.plot(x_axis, eigvectors[m], linestyle='--', marker='o', color='b')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')

plt.show()

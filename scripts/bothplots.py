import matplotlib.pyplot as plt
from masses import *

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

txt = 'Azul é ', eigvalues[0].real, '.\n O vermelho é ', eigvalues[n-1].real

plt.title('Deslocamento das massas com a primeira e última frequência')
plt.text(1,0.1,txt,fontsize=9)
plt.plot(x_axis, eigvectors[0], linestyle='--', marker='o', color='b')
plt.plot(x_axis, eigvectors[n-1], linestyle='--', marker='x', color='r')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.show()

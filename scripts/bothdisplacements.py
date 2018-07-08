import matplotlib.pyplot as plt
from masses import *

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

txt = 'Azul: '+chr(969)+'² = '+str(round(eigvalues[0].real, 6))+'. \nVermelho: '+chr(969)+'² = '+str(round(eigvalues[n-1].real, 6))
plt.text(1,0.04,txt,fontsize=9)

plt.title('Deslocamento das 1000 massas com a primeira e última frequência')
plt.plot(x_axis, eigvectors[:,0], linestyle='--', marker='x', color='b')
plt.plot(x_axis, eigvectors[:,n-1], linestyle='--', marker='.', color='r')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')

plt.savefig('both-1000.jpg')
plt.show()

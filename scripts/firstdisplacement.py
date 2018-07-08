import matplotlib.pyplot as plt
from masses import * #Usa masses.py

x_axis=[] #Faz o eixo x, com número dos corpos
for i in range(0,n):
    x_axis.append(i+1)


#faz texto
txt = chr(969)+'² = '+str(round(eigvalues[0].real, 6))
plt.text(60,0.102,txt,fontsize=12)

#Faz o gráfico
plt.title('Deslocamento das 100 massas com a primeira frequência')
plt.plot(x_axis, eigvectors[:,0], linestyle='--', marker='o')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.savefig('First-100.jpg')
plt.show()

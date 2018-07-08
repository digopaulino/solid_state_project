import matplotlib.pyplot as plt
from masses import * #Usa o masses.py

x_axis=[]       #Faz o eixo x com os corpos
for i in range(0,n):
    x_axis.append(i+1)

#Faz o texto w²=0.00000 na posićão específica
txt = chr(969)+'² = '+str(round(eigvalues[n-1].real, 6))
plt.text(70,0.13,txt,fontsize=12)

plt.title('Deslocamento das 100 massas com a última frequência') #Define título
plt.plot(x_axis, eigvectors[:,n-1], linestyle='--', marker='.', color='b') #Faz o gráfico
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.savefig('Last-100.jpg')
plt.show()

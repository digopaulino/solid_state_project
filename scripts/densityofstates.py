import matplotlib.pyplot as plt
from masses import *
import numpy as np

size= 0.4 #4/size deve ser um número inteiro. Tamanho do intervalo de omega²
m = int(4/size) #Número de intervalos de omega²

w2 = np.arange(0, 4, size) #Cria os intervalos de omega²
counts = np.zeros(shape=(m)) #Vetor vazio p/ o contador
x_axis = np.zeros(shape=(m)) #Matriz vazia p/ o eixo x

#Contador do número de autovalores em cada intervalo
for i in range(0,m):
    for j in range(0,len(eigvalues)):
        if eigvalues[j] < w2[i]+size and eigvalues[j] >= w2[i]:
            counts[i]+=1

for i in range(0,len(w2)): #Define o eixo x, deslocando omega²
    x_axis[i] = w2[i]+size/2


print(counts)

#Faz gráfico de barras
plt.title('Densidade de estados para 1000 massas')
plt.bar(x_axis, counts, width=size, color='w', edgecolor='r') #Gráfico de barras

#Faz os ticks dos eixos
plt.xticks(np.arange(0, 4.1, 0.4))
plt.yticks(np.arange(0,400,20))
plt.xlabel(r'$\omega^2$')
plt.ylabel('Count')

#Intervalo dos eixos do gráfico
plt.axis([-0.05, 4, 0, 220]) #ALTERAR ÚLTIMO VALOR PARA MUDAR VALOR MÁXIMO DE Y (22 p 100, 220 p 1000)
#plt.xticks(x_axis)

plt.savefig('density-1000.jpg')
plt.show()

import matplotlib.pyplot as plt
from masses import *

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

txt = 'w² = ', eigvalues[n-1].real

plt.title('Gráfico do deslocamento das massas com a última frequência')
plt.text(1,0.1,txt,fontsize=9)
plt.plot(x_axis, eigvectors[n-1], linestyle='--', marker='o', color='b')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.show()

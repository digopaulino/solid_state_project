import matplotlib.pyplot as plt
from masses import *

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

txt = chr(969)+'² = '+str(round(eigvalues[n-1].real, 6))
plt.text(60,0.140,txt,fontsize=12)

plt.title('Deslocamento das massas com a última frequência')
plt.plot(x_axis, eigvectors[:,n-1], linestyle='--', marker='o', color='b')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.show()

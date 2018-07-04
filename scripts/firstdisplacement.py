import matplotlib.pyplot as plt
from masses import *

x_axis=[]
for i in range(0,n):
    x_axis.append(i+1)

txt = chr(969)+'² = '+str(round(eigvalues[0].real, 6))
plt.text(60,0.1,txt,fontsize=12)

plt.title('Deslocamento das massas com a primeira frequência')
plt.plot(x_axis, eigvectors[:,0], linestyle='--', marker='o')
plt.xlabel('Corpo')
#plt.xticks(x_axis)
plt.ylabel('Deslocamento')


plt.show()

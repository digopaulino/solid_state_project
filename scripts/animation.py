import matplotlib.pyplot as plt
import matplotlib.animation as animation
from masses import *
import numpy as np

#Configurar a figura, antes de colocar os dados
fig = plt.figure()
ax = plt.axes(xlim=(450, 550), ylim=(-0.08, 0.08))
line, = ax.plot([], [], 'o-', lw=2)
text = ax.text(500,0.055, '')

#Funcao de inicializacão: plota o background de cada frame
def init():
    line.set_data([], [])
    text.set_text('')
    return line, text

#Funcao de animaca0: chamada sequencialmente, e plota os dados
def animate(i):
    x = []
    for j in range(0,n):
        x.append(j+1)
    y = eigvectors[:,i]
    line.set_data(x, y)
    text.set_text(str(i))
    return line, text

#Chama o animador (faz o filme). Blit=true é para fazer um novo frame só quando
#muda algum dado
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=30, blit=True)


anim.save('1000masses(450-550).mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

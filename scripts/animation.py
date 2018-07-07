import matplotlib.pyplot as plt
import matplotlib.animation as animation
from masses import *
import numpy as np

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, n), ylim=(-0.08, 0.08))
line, = ax.plot([], [], 'o-', lw=2)
text = ax.text(10,0.055, '')
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    text.set_text('')
    return line, text

# animation function.  This is called sequentially
def animate(i):
    x = []
    for j in range(0,n):
        x.append(j+1)
    y = eigvectors[:,i]
    line.set_data(x, y)
    text.set_text(str(i))
    return line, text

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n, interval=30, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('1000masses.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

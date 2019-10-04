import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
##x= [1,2,3,4,5]
##y= [10,20,30,500,40]
##
##
##plt.bar(x,y)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate():
    xs=[]
    ys=[]
    for i in range(1,20):
        xs.append(i)
        ys.append(i*10)
        ax1.clear()
        ax1.bar(xs,ys)
        fig.canvas.draw()

##ani = animation.FuncAnimation(fig,animate)
animate()



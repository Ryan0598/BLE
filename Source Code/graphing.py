import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.style.use('fivethirtyeight')

def animate(i):
    pullData = open("data.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
	
    ax1.clear()
    ax1.plot(xar,yar, color='red')
ani = animation.FuncAnimation(fig, animate, interval=5000)


plt.title('BLE Scan')
plt.xlabel('Scan Time (Seconds)')
plt.ylabel('Devices Found')
plt.tight_layout()
plt.show()

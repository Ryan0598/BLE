import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from matplotlib.ticker import MaxNLocator




fig, (ax1, ax2) = plt.subplots(2)


#fig = plt.figure()




fig.suptitle('Bluetooth Low Energy Scan', fontsize=20, fontweight='bold')


plt.style.use('fivethirtyeight')

'''

ax1.set_title('BLE Scan', fontsize=18, fontweight='bold')
ax1.set_xlabel('Scan Time (Seconds)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Devices Found', fontsize=16, fontweight='bold')

ax2.set_title('BLE Scan2', fontsize=18, fontweight='bold')
ax2.set_xlabel('Scan Time (Seconds)2', fontsize=16, fontweight='bold')
ax2.set_ylabel('Devices Found2', fontsize=16, fontweight='bold')

'''



plt.title('BLE Scan2', fontsize=18, fontweight='bold')
plt.xlabel('Scan Time (Seconds)2', fontsize=16, fontweight='bold')
plt.ylabel('Devices Found2', fontsize=16, fontweight='bold')

ax1.yaxis.set_major_locator(MaxNLocator(integer=True))



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
    ax1.plot(xar,yar, color='green')

ani = animation.FuncAnimation(fig, animate, interval=5000)



plt.tight_layout()  

plt.show()

#
#	DEVICE IDENTIFICATION USING WIRELESS TECHNOLOGIES
#	AUTHOR : RYAN PARKINS
#

# https://github.com/karulis/pybluez - pybluez library
# sudo apt-get install libbluetooth-dev
# sudo apt-get install pkg-config
# sudo apt-get install libboost-python-dev
# sudo apt-get install libboost-thread-dev
# sudo apt-get install libbluetooth-dev
# sudo apt-get install libglib2.0-dev
# sudo apt-get install python-dev
# sudo pip install gattlib
# sudo pip install matplotlib
# sudo apt install python-tk
# sudo pip install pybluez

import datetime
import bluetooth
from bluetooth.ble import DiscoveryService
from gattlib import DiscoveryService
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from matplotlib.ticker import MaxNLocator

#########################################################################
######################  declare variables  ##############################
#########################################################################


devices_count = [] #list of devices found inside a scan

time_passed = []
addresses = []

scanCount = 0
time = 0
scanCount = time * scanCount
scanTime = 5


#########################################################################
########################  create graphs  ################################
#########################################################################

#fig, (ax1, ax2) = plt.subplots(2)
fig, (ax1) = plt.subplots(1)
fig.suptitle('Bluetooth Low Energy Scan', fontsize=20, fontweight='bold')
plt.style.use('fivethirtyeight')
plt.title('BLE Scan', fontsize=18, fontweight='bold')
plt.xlabel('Scan Time (Seconds)', fontsize=16, fontweight='bold')
plt.ylabel('Devices Found', fontsize=16, fontweight='bold')
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))



#########################################################################
###########################  LE Scan  ###################################
#########################################################################

def lescan():
	
	#define global variables 
	global time
	global scanTime
	global timePassed
	global scanCount
	
	
	print("\n####################Scanning######################")
	service = DiscoveryService("hci1")
	devices = service.discover(5)
	count = 0
	
	
	
	for address, name in devices.items():
		count = count + 1
		print("\n" + str(count) + "  {} --- {}".format(address, name))
		addresses.append(format(address))
		
		
		
		
	time = time + scanTime
	time_passed.append(time)	
	print ("-------------- Seconds Passed : " + str(time) + "----------------")
	devices_count.append(count)
	
	return (time_passed , devices_count)
		
		

#########################################################################
#########################  animate graph function  ######################
#########################################################################




def animate(i):
	
	
	global time_passed
	global devices_count

    # Create a loop
    	#for i in xrange(1):

    	lescan()
    # Clear the graph
    	ax1.clear()
    # Plot the graph
    	ax1.plot(time_passed, devices_count)
    	
# Run the animation function and show the graph
ani = animation.FuncAnimation(fig, animate, interval=5000)

plt.show()

		


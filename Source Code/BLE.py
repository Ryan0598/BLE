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


#relevant imports
import datetime
import bluetooth
import random
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
scatter_devs = []
scatter_time = []
scatter_colour = []
devicesDictionary = {}
colourDictionary = {}

scanCount = 0
time = 0
scanCount = time * scanCount
scanTime = 5


#########################################################################
########################  create graphs  ################################
#########################################################################

#fig, (ax1, ax2) = plt.subplots(2)
fig, (ax1,ax2) = plt.subplots(2, sharey=True)
plt.rcParams.update({'font.size': 22})

fig.suptitle('Bluetooth Low Energy Scan', fontsize=20, fontweight='bold')


plt.style.use('fivethirtyeight')
plt.title('BLE Scan', fontsize=18, fontweight='bold')
#plt.xlabel('Scan Time (Seconds)', fontsize=16, fontweight='bold')
#plt.ylabel('Devices Found', fontsize=16, fontweight='bold')


ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set(title = 'Bluetooth Low Energy - Device Identification', ylabel = 'Device Count')


ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.set(xlabel = 'Time (Seconds)', ylabel = 'Device ID')



#########################################################################
###########################  LE Scan  ###################################
#########################################################################

def lescan():
	
	#define global variables 
	global time
	global scanTime
	global timePassed
	global scanCount
	global scatter_devs
	global scatter_colour
	global scatter_time
	global devicesDictionary
	
	
	print("\n####################Scanning######################")
	service = DiscoveryService("hci1")
	ScanDevices = service.discover(5)
	count = 0

	time = time + scanTime
	time_passed.append(time)	
	
	
	
#########################################################################
##	plot relevant data to graph data sets - 
	
	
	for address, name in ScanDevices.items():
		count = count + 1
		print("\n" + str(count) + "  {} --- {}".format(address, name))
		addresses.append(format(address))
		

		scatter_time.append(time)
		if str(address) in devicesDictionary:
			id = devicesDictionary.get(str(address))
			scatter_devs.append(id)
			#colour = colourDictionary.get(id)
			#scatter_colour.append (colour)
	
		else:
			id = (len(devicesDictionary) + 1)
			devicesDictionary.update( { str(address) : id } )
			colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))
			colourDictionary.update ( { id : colour })
			scatter_devs.append(id)
			

		
	
	
	print ("-------------- Seconds Passed : " + str(time) + "----------------")
	
	print devicesDictionary.items()
	print colourDictionary.items()
	devices_count.append(count)
	
	return (time_passed , devices_count , scatter_time, scatter_devs, scatter_colour)
		
		

#########################################################################
#########################  animate graph function  ######################
#########################################################################




def animate(i):
	
	
	global time_passed
	global devices_count
	global scatter_time
	global scatter_devs
	global scatter_colour

    	lescan()
    # Clear the graph
    	ax1.clear()
    # Plot line graph
    	ax1.plot(time_passed , devices_count)
	 # plot scatter graph
    	ax2.scatter(scatter_time, scatter_devs)
    	
# Run the animation function and show the graph
ani = animation.FuncAnimation(fig, animate, interval=5000)

plt.show()

		


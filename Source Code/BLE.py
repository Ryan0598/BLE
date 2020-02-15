#
#	DEVICE IDENTIFICATION USING WIRELESS TECHNOLOGIES
#	AUTHOR : RYAN PARKINS
#



# sudo pip install gattlib
# sudo pip install matplotlib
# sudo apt install python-tk
# sudo pip install pybluez
# sudo pip install ptable
# sudo pip install art
# sudo pip install pandas
#
#
#
# sudo apt-get install libbluetooth-dev
# sudo apt-get install pkg-config
# sudo apt-get install libboost-python-dev
# sudo apt-get install libboost-thread-dev
# sudo apt-get install libbluetooth-dev
# sudo apt-get install libglib2.0-dev
# sudo apt-get install python-dev



# relevant imports
import datetime
import random
import os
import tkMessageBox
from datetime import datetime
from gattlib import DiscoveryService
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import csv
import pandas
import json
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
from prettytable import PrettyTable
from art import *


#########################################################################
######################  declare variables  ##############################
#########################################################################


devices_count = [] #list of devices found inside a scan
time_passed = []
addresses = []
scatter_devs = []
scatter_time = []
scatter_colour = []
patches = []
devicesDictionary = {}
colourDictionary = {}
totaldevCount = []
newdevCount = []
knowndevCount = []
time_list = []
x = PrettyTable()
art=text2art("BLE   Scanner")
scanCount = 0
time = 0
scanCount = time * scanCount
scanTime = 5
scanRef = ''
os.system('cls||clear')#clear screen


print(art)#print ble scanner logo

#print welcome message
print('\n Welcome to BLE Scanner, Enter a scan reference below in order to start the scan. \n Data will be diplayed here in a graphical format, simply press the "save" button on the graph in order to save a copy (Image). \n Mac Data will be saved in the form of a text file and will be named with relation to the scan reference. \n\n in order to identify specific devices, simply create or edit a text file in the code directory, \n Simply write into the file, (Each Line) MAC_Address Reference')
scanRef = raw_input("\n Scan Reference : ")

#create a dictionary from the blacklist text file, gathering addresses and descriptions of devices being searched for
blackListDict = {}
with open ("BLACKLIST.txt") as f:
	for line in f:
		(key, val) = line.split()
		blackListDict [str(key)] = val
		


#create a file to store the scan data to, write the reference and time into the file
s = open(str(scanRef) + "_ScanData.txt" , "w+")
s.write ("Bluetooth Low Energy Scan, Reference : " + str(scanRef) + " - Date And Time of Scan Start : " + str(datetime.now())) 


#########################################################################
########################  create graphs  ################################
#########################################################################


#set a matplotlib figure with 2 subplots
fig, (ax1,ax2) = plt.subplots(2, sharey=True)

#set some parameters for the chart, font and titles
plt.rcParams.update({'font.size': 22})
fig.suptitle('Bluetooth Low Energy Scan', fontsize=20, fontweight='bold')
plt.style.use('fivethirtyeight')
plt.title('BLE Scan', fontsize=18, fontweight='bold')
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
	global scanCount
	global scatter_devs
	global scatter_colour
	global scatter_time
	global devicesDictionary
	global totaldevCount
	global newdevCount
	global knowndevCount
	global time_list


# set the service to a discoveryservice from the bluetooth adapter, HCI0 for internal adapter, HCI1 for external
	service = DiscoveryService("hci0")
	#carry out a LE scan for the time specified
	ScanDevices = service.discover(scanTime)
	#set variables to 0 to clear from previous scan
	count = 0
	knownCount = 0
	unknownCount = 0
	#increase time by the scan time, in order to increase the time_passed
	time = time + scanTime
	time_passed.append(time)	
	
	
	
#########################################################################
##	plot relevant data to graph data sets - 
	
	s.write("\n -------------------------------------------")
	s.write("\n\n Scan Time : " + str(time))
	
	
	#for each device found in the scan, add 1 to the amount of devices found, and add these to the graph lists
	for address, name in ScanDevices.items():
		count = count + 1
		addresses.append(format(address))
		scatter_time.append(time)
		
		#if the device is in blacklist, then alert the user
		for key in blackListDict:
			if key == str(address):
				tkMessageBox.showinfo(title="Device In Range!", message="Device found, \n\n" + str (blackListDict[str(address)]) + "\n\n " + str (address))
				

		#if the address is in devices dictionary, gat its ID and plot it
		if str(address) in devicesDictionary:
			id = devicesDictionary.get(str(address))
			scatter_devs.append(id)
			knownCount = knownCount + 1
			s.write ("\n " + str(id) + " : " + str(address))
			

		# if the device is new, 
		else:
			id = (len(devicesDictionary) + 1)
			devicesDictionary.update( { str(address) : id } )
			colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))
			colourDictionary.update ( { id : colour })
			scatter_devs.append(id)
			unknownCount = unknownCount + 1
			s.write ("\n " + str(id) + " : " + str(address))
			
			
	totalDevs = unknownCount + knownCount
	totaldevCount.append (totalDevs)
	newdevCount.append(unknownCount)
	knowndevCount.append(knownCount)
	devices_count.append(count)
	
	
	

	
	
	return (time_passed , devices_count , scatter_time, scatter_devs, scatter_colour, totaldevCount, newdevCount, knowndevCount)
		
		

#########################################################################
#########################  animate graph function  ######################
#########################################################################






def animate(i):
	
	
	global time_passed
	global devices_count
	global scatter_time
	global scatter_devs
	global scatter_colour
	global scanRef
	

	 # Run a LE scan
    	lescan()
    # Clear the screen
    	os.system('cls||clear')
    # clear graph data
    	x.clear()
    # print ble art logo
    	print(art)
    # print how many devices have been seen in total
    	print "\n \n Total Devices Seen : " + str((len(devicesDictionary)))
    # Clear the graph
    	ax1.clear()
    # Plot line graph
    	ax1.plot(time_passed , devices_count)
	 # plot scatter graph
    	ax2.scatter(scatter_time, scatter_devs)
    	

    # add columns with relevant data to the table
    	x.add_column('Scan Time', time_passed)
    	x.add_column('Devices in Range', devices_count)
    	x.add_column('New Devices', newdevCount)
    	x.add_column('Known Devices', knowndevCount)
    	# print the table
    	print (x)
    	
    	

    	
    		

    	
# Run the animation function and show the graph
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()

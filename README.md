# BLE
Bluetooth Low Energy - Device Identification Using Wireless Technologies
###########################################################

This project is able to scan for nearby bluetooth low-energy (BLE) devices within close proximity, 
these devices will be mapped live in two forms

  1 - Devices in current range (Number)
  
  2 - Uniquely identified devices in range (Devices shown independantly - Eg; Device 2 identifiable from others)
  
###########################################################

Uses for this software include -

  - BLE presence detection
  - Device presence, locating unique devices
  - Missing persons / pets / property
  
  
###########################################################

The software requires a number of prerequisites before it can be run, these include,

  - Bluetoth 4.0+ hardware (built in or bluetooth 4.0+ dongle)
  - Python, linux terminal
  - A number of software libraries (See Below)

###########################################################

Python dependancies -
	
	# sudo pip install gattlib
	# sudo pip install matplotlib
	# sudo apt install python-tk
	# sudo pip install pybluez
	# sudo pip install ptable
	# sudo pip install art
	# sudo pip install pandas
	# sudo apt-get install libbluetooth-dev
	# sudo apt-get install pkg-config
	# sudo apt-get install libboost-python-dev
	# sudo apt-get install libboost-thread-dev
	# sudo apt-get install libbluetooth-dev
	# sudo apt-get install libglib2.0-dev
	# sudo apt-get install python-dev
	
	
Installation Instructions
############################################################

1 - Install all dependancies above onto the system

2 - Navigate to the code directory

3 - run the program using "sudo python BLE.py"

4 - The program should run, ensure you alter the device configuration in the code, use HCI0 for internal bluetooth and HCI1 for an external dongle

5 - The program will prompt for a reference, enter a reference, this will be used to name files

6 - If you want to enable notifications when particular devices are in range, simply add / edit "BLACKLIST.txt" in the code directory, simply on each line, add the following 

	MAC_ADDRESS DESCRIPTION
	
just simply add as many devices as requires seperated by new lines. 

7 - Once running, the terminal window will diaplay a sumary of the scan so far, including information about how many devices have been seen so far, this screen will update every time a scan period has completed, The screen will also display a live-updating graph, showing how many devices are in range, and a device specific is in-range Chart, this can be used alongside the text file saved after the scan to reference the graph to MAC addresses.

8 - To save a copy of the graph in its current form, simply press the save button 

9 - To finish the scan, Close the graph window

10 - Open the code directory and a text file will contain all the scan information such as mac addresses seen at what time.


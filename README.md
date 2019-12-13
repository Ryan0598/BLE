# BLE
Bluetooth Low Energy - Device Identification
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

  - Bluetoth 4.0+ hardware
  - Python
  - A number of software libraries (See Below)

###########################################################

Python dependancies -

	- sudo apt-get install libbluetooth-dev pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev

	- sudo pip install gattlib matplotlib python-tk pybluez

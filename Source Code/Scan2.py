####https://ianharvey.github.io/bluepy-doc/scanner.html
####https://ianharvey.github.io/bluepy-doc/scanentry.html?highlight=scanentry




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
# sudo pip install tableprint
# sudo pip install PrettyTable



# import the necessary parts of the bluepy library
from bluepy.btle import Scanner, DefaultDelegate
import datetime
import tableprint as tp
import numpy as np
from prettytable import PrettyTable



from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style



###################################################################################################
###################################################################################################


scanTime = 5
mac_addresses = []
mac_addresses_known = []

f= open("data.txt","w")
f.write(" ")
f.close()







###################################################################################################
###################################################################################################



###################################################################################################
###################################################################################################


# create a delegate class to receive the BLE broadcast packets
class ScanDelegate(DefaultDelegate):

	
	
    def __init__(self):
        DefaultDelegate.__init__(self)


###################################################################################################
###################################################################################################



    # when this python script discovers a BLE broadcast packet, print a message with the device's MAC address
    def handleDiscovery(self, dev, isNewDev, isNewData):
    	

        if isNewDev:
            mac_addresses.append(dev.addr)
            mac_addresses_known.append(dev.addr)
            print (len(mac_addresses)), (datetime.datetime.now().time()),  "----" , dev.addr, dev.rssi,   " NEW"

            
        elif isNewData:
            print "------Received new data from", dev.addr, dev.rssi, " At " , (datetime.datetime.now().time()), "Update - " , dev.updateCount






###################################################################################################
###################################################################################################


# create a scanner object that sends BLE broadcast packets to the ScanDelegate
scanner = Scanner().withDelegate(ScanDelegate())



###################################################################################################
###################################################################################################

def main():
	
	global scanTime
	
	
	while True:
# start the scanner and keep the process running for 5 seconds per scan
		
		f= open("data.txt","a+")
		print "Starting..."
		scanner.start()
		scanner.process(5)
		print "Stopped.."
		scanner.clear()
		f.write(str(scanTime) + "," + (str(len(mac_addresses))) + "\n")
		del mac_addresses[:]
		scanTime = scanTime + 5
		f.close() 
		
		



		
    
###################################################################################################
###################################################################################################


main()

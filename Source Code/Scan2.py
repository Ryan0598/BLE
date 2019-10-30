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

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


###################################################################################################
###################################################################################################


# style.use('')

fig = plt.figure()
# creating a subplot
ax1 = fig.add_subplot(1, 1, 1)

mac_addresses = []

###################################################################################################
###################################################################################################

class tableprint():
	data = np.random.randn(5, 5)
	headers = ['ID', 'MAC', 'First Seen', 'Last Seen','RSSI']
	tp.table(data, headers)
	#print(tableprint.header(['ID', 'MAC', 'First Seen', 'Last Seen','RSSI']))
	
#class table():
	#t = PrettyTable(['ID', 'MAC', 'First Seen', 'Last Seen','RSSI'])
   #t.add_row(['1', dev.addr , datetime.datetime.now().time()), datetime.datetime.now().time()), dev.rssi)
   #print(t)



###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################


# create a delegate class to receive the BLE broadcast packets
class ScanDelegate(DefaultDelegate):
	
	
	#count = 1
	#addresses = []
	
	
    def __init__(self):
        DefaultDelegate.__init__(self)


###################################################################################################
###################################################################################################



    # when this python script discovers a BLE broadcast packet, print a message with the device's MAC address
    def handleDiscovery(self, dev, isNewDev, isNewData):
    	

        if isNewDev:
            print (len(mac_addresses)+1), (datetime.datetime.now().time()),  "----" , dev.addr, dev.rssi,   " NEW"
            mac_addresses.append(dev.addr)
            
        elif isNewData:
            print "------Received new data from", dev.addr, dev.rssi, " At " , (datetime.datetime.now().time()), "Update - " , dev.updateCount






###################################################################################################
###################################################################################################






# create a scanner object that sends BLE broadcast packets to the ScanDelegate
scanner = Scanner().withDelegate(ScanDelegate())



###################################################################################################
###################################################################################################




# start the scanner and keep the process running
scanner.start()
scanner.process(5)
    
###################################################################################################
###################################################################################################

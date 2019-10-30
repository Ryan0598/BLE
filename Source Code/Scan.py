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
# from bluetooth.ble import DiscoveryService
from gattlib import DiscoveryService
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



####################################################################################
####################################################################################

# style.use('')

fig = plt.figure()
# creating a subplot
ax1 = fig.add_subplot(1, 1, 1)


####################################################################################
####################################################################################
#####################BLUETOOTH LOW ENERGY SCAN #####################################
####################################################################################
####################################################################################


def lescan():
    BLEblackList = open('BLEblacklist.txt', 'a')


ScanFile = open('Scan.txt', 'a')

print("\nScanning...\n\n")
service = DiscoveryService("hci1")
devices = service.discover(5)
count = 1
known = "False"
now = datetime.datetime.now()

print ("\n------  MAC Address ------------- Device Name   --------  Date  /  Time  ---------------- Known?-----\n")

for address, name in devices.items():
    with open('BLEblacklist.txt') as f:
        if format(address) in f.read():
            known = "True"
            print("\n" + str(count) + "    {}   ---   {}".format(address, name) + "  -------  " + str(
                now) + "  -----   " + str(known))
            count = count + 1
            known = "False"
        else:
            print("\n" + str(count) + "    {}   ---   {}".format(address, name) + "  -------  " + str(
                now) + "  -----   " + str(known))
            BLEblackList.write("\n    {}   ---   {}".format(address, name) + "  ---   " + str(now))
            count = count + 1

    ScanFile.write(str(count) + "," + str(count) + "\n")


####################################################################################
####################################################################################
################################ GRAPHING DATA #####################################
####################################################################################
####################################################################################

def animate(i):
    graph_data = open('Scan.txt', 'r').read()
    lines = graph_data.split('\n')
    print("Plotting...")

    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()


def main():
    lescan()
    # animate(i)
    print("Finished...")


main()

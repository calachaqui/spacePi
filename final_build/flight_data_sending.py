#!/usr/bin/python3

##--------------import libraries------------------##
import time,datetime
##altimeter
from MPL3115A2 import MPL3115A2
mpl3115a2 = MPL3115A2()

##GPS
import gps
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

##LoRa
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x
##-------------setup altimeter-------------------##
while True :
        mpl3115a2.control_alt_config()
        mpl3115a2.data_config()
        time.sleep(1)
        alt = mpl3115a2.read_alt_temp()
        alt_ft = alt['a'] * 3.281
        print( "Altitude : %.2f ft"%(alt_ft))
        print( "Temperature in Celsius : %.2f C"%(alt['c']))
        print( "Temperature in Fahrenheit : %.2f F"%(alt['f']))
        mpl3115a2.control_pres_config()
        time.sleep(1)
        pres = mpl3115a2.read_pres()
        print( "Pressure : %.2f kPa"%(pres['p']))
        print( " ************************************* ")

##-------------setup GPS-------------------------##

##-------------setup LoRa------------------------##


##-------------get data--------------------------##

##altitude
##GPS
##temperature


##-------------prepare data package--------------##


##-------------send data-------------------------##



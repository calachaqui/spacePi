#!/usr/bin/python3

#sending data with LoRa and python
#File Name: transmission.py
#help guide: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/sending-data-using-a-lora-radio
#Author: Jacob Wood

# Import Python System Libraries
import time,datetime
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x


# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

#Sending a packet
message = input('type message here: ')
print('preparing first packet')
#preparing data
tmstp = datetime.datetime.now()
first_data = bytes('Hello Radio World, %s %s' % (message,tmstp),'utf-8')
print('sending first packet...')
rfm9x.send(first_data)
print('first packet sent')

#!/usr/bin/python3
"""
receiving data with LoRa and python
File Name: reception.py
help guide: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/sending-data-using-a-lora-radio
Author: Jacob Wood
"""
# Import Python System Libraries
import time
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

#Receiving a packet
print('Begining to look for packets')
while True:
  packet = None
  # check for packet rx
  packet = rfm9x.receive()
  if packet is None:
    time.sleep(3)
  else:
    #print recieved packet
    print('Receiving Packet...')
    time.sleep(.5)
    packet_text = str(packet, "utf-8")
    print('Received packet: ',packet_text)
    with open('file_name.txt','w') as log:
      log.write(packet_text)

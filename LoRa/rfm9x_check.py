#!/usr/bin/python3
"""
Learn Guide: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/rfm9x-raspberry-pi-setup
Author: Jacob Wood
"""
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x

#setup pins
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)

print('looking for radio...')

time.sleep(1)

try:
  rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
  print("I found the RFM9x radio")
except RuntimeError as error:
  print("Error finding radio: ", error)

time.sleep(1)

print('ending test')

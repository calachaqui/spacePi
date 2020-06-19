#!/usr/bin/python3
#import from python system libraries
import sqlite3
import datetime
import time
from sqlite3 import Error as e
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

#execution loop for receiving and sending
While True:
#listen for incoming messages
  packet = None
  packet = rfm9x.receive()
#store message if any received
  if packet != None:
    packet_text = str(packet, "utf-8")
    packet_list = packet_text.split(",")
  #read msg_type
    msg_type = packet_list[0]
  #read sender_id
    sender = packet_list[1]
    conn = sqlite3.connect('rocket_data.db')
    c = conn.cursor()
    sql_cmd = """INSERT INTO incoming_message VALUES(datetime('localtime'),?,?,?,'received',NULL);"""
    c.execute(sql_cmd,(msg_type,sender,packet_text))
    conn.commit()
    conn.close()
  #send next messagge in database queue table
  conn = slqite3.connect('rocket_data.db')
  c = conn.cursor()
  #select next data from outgoing_message table
  sql_cmd = """SELECT q_timestamp,message FROM outgoing_message ORDER BY q_timestamp DESC limit 1;"""
  next_queue = c.fetchone()
  for next in next_queue:
    msg_id = next[0]
    message = next[1]
  #send message
  rfm9x.send(message)
  #update outgoing_message table for sent_status
  sql_cmd = """UPDATE outgoing_message
SET send_status='sent',
send_timestamp=datetime('localtime') where q_timestamp = ?;"""
  c.execute(sql_cmd,(msg_id))
  conn.commit()
  conn.close()
#sleep short time
  time.sleep(0.1)

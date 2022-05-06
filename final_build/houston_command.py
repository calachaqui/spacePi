#!/usr/bin/python3

#imports
import sqlite3
from sqlite3 import Error
from subprocess import Popen
import sys,os


##setup command DB
dbase = "/home/slice/spacePi/final_build/houston.db"

if not os.path.exists(dbase):
  conn = sqlite3.connection(dbase)
  c = conn.cursor()
  sql_cmd = """CREATE TABLE IF NOT EXISTS send_commands (
cmd_time DATETIME,
command VARCHAR(16),
send_status VARCHAR(16);"""
  try:
    c.execute(sql_cmd)
  except Error as e:
    print("table not created: %s" %e)
    conn.close()
    sys.exit(e)
  conn.commit()
  conn.close()

##start LoRa as subprocess
hmess = "/home/slice/spacePi/final_build/houston_messaging.py"

hmpr = Popen(hmess)

##enter command loop
while True:
  input_v = ['START','STOP','END']
  command = input("ENTER Command 'START', 'STOP', 'END'\ntype here:")
  if command in input_v:
    ##add command to dbase
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    sql_cmd = """ INSERT INTO send_commands VALUES(datetime('now','localtime'),?,'pending');"""
    c.execute(sql_cmd,(command))
    conn.commit()
  else:
    print("%s is not a valid choice" % command)


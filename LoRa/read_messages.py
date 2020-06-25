import sqlite3
from subprocess import Popen

#first look for data messages
conn = sqlite3.connect('rocket_data.db')
c = conn.cursor()
sql_cmd = """SELECT msg_timestamp,message FROM incoming_message
 WHERE exec_status='pending' AND msg_type = 'DATA';"""
c.execute(sql_cmd)
for msg in c:
#insert data into the telemetry table
  msg_data = msg[0].split(',')
  alti = msg_data[2]
  tempr = msg_data[3]
  gps_c = msg_data[4]
  rcd_tm = msg_data[5]
  sql_cmd = """INSERT INTO telemetry_data VALUES(?,?,?,?);"""
  c.execute(sql_cmd,(rcd_tm,alti,tempr,gps_c))
  conn.commit()
  sql_cmd =  """UPDATE incoming_message SET exec_status = 'written'
 exec_timestamp = datetime('localtime') WHERE msg_timestamp = ?;"""
  c.execute(sql_cmd,msg[1])
  conn.commit()

#second look for command messages
sql_cmd = """SELECT msg_timestamp,message FROM incoming_message
 WHERE exec_status = 'pending' AND msg_type = 'COMMAND';"""
c.execute.(sql_cmd)
for msg in c:
#find out what command is given
  msg_data = msg[0].split(',')
  in_command = msg_data[1]
#execute command in order of reception
  if in_command == 'START ROCKET DATA':
    ##start rocket sampling program
    data_sampler = Popen('python3 data_sampler.py')

  if incommand == 'STOP ROCKET DATA':
    ##stop rocket sampling program
    data_sampler.terminate()

  sql_cmd = """UPDATE incoming_message SET exec_status = 'executed'
 exec_timestamp = datetime('localtime') WHERE msg_timestamp = ?;"""
  c.execute(sql_cmd,msg[1])
  conn.commit()
conn.close()

import sqlite3
from sqlite3 import Error as e

# connect to datebase
conn = sqlite3.connect('rocket_data.db')
c = conn.cursor()

sql_cmd = """CREATE TABLE outgoing_message (
q_timestamp datetime,
msg_type CHAR(12),
sender_id VARCHAR(24),
message CHAR(255),
send_status CHAR(12),
send_timestamp datetime,
PRIMARY KEY (q_timestamp)
)"""

c.execute(sql_cmd)

sql_cmd = """CREATE TABLE incoming_message (
msg_timestamp datetime,
msg_type CHAR(12),
sender_id VARCHAR(24),
message CHAR(255),
exec_status CHAR(12),
exec_timestamp datetime,
PRIMARY KEY (msg_timestamp)
)"""

c.execute(sql_cmd)

sql_cmd = """CREATE TABLE rocket_data (
rcd_timestamp datetime,
altitude FLOAT,
temp FLOAT,
gps_coord CHAR(50),
PRIMARY KEY (rcd_timestamp)
)"""

#c.execute(sql_cmd)

conn.commit()
print("database and tables are created")

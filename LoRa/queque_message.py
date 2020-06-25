import sqlite3,getpass

#get user variables
sender = getpass.getuser()

#get data for outgoing_message table
msg_type = "command"
send_status = "queued"
message = "things and stuff and data"

conn = sqlite3.connect("rocket_data.db")
c = conn.cursor()
sql_cmd = """INSERT INTO outgoing_message
 VALUES(datetime('localtime'),?,?,?,?,NULL);"""
c.execute(sql_cmd,(msg_type,sender,message,send_status))
conn.commit()
conn.close()

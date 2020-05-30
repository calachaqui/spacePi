#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import time

c = open('gps_points.csv','w') 
c.write('longitude,latitude\n')

with open('GPS_output.txt','r') as g:
  line = g.readline()
  if line:
    print('next line')
  while line:
    line_set = line.split(',')
    NS = line_set[1]
    EW = line_set[3]
    tm = line_set[5]
    valid = line_set[6]
    if valid == 'A':
      lat = round(float(NS) / 100,7)
      lon = round(float(EW) / -100,7)
      tme = '%s:%s'%(tm[0:2],tm[2:4])
    else:
      lat = lon = tme = valid
    line = g.readline()
    if valid == 'A':
      c.write('%s,%s\n'%(lon,lat))
    #print('%s %s : %s'%(lat,lon,tme))
c.close()

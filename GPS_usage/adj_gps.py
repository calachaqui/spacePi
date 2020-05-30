#!/usr/bin/python3

pnts = open('gps_points.csv','w')

with open('GPS_output.txt','r') as gps:
  lines = gps.readlines()
  for lin in lines:
    things = lin.split(',')
    try:
      n = float(things[1]) / 100
      w = float(things[3]) / 100
    except:
      print('no gps data')
      pass
    na = round( n + 0.153241,6)
    wa = w + 0.3146625
    wa = round(wa*-1,6)
    pnts.write('%s,%s\n'%(na,wa))
    print(na,wa)

pnts.close()

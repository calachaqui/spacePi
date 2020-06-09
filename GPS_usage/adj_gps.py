#!/usr/bin/python3
with open('GPS_output.txt','r') as gps:
  things = gps.read().split(',')
  n = float(things[1]) / 100
  w = float(things[3]) / 100
  na = round( n + 0.153241,6)
  wa = w + 0.3146625
  wa = round(wa*-1,6)

print(na,wa)

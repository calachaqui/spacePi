#!/usr/bin/python3

import gps

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
##        print(report)
        s_time = ""
        s_lat = ""
        s_lon = ""
        s_alt = ""
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                s_time = report.time
            if hasattr(report, 'lat'):
                s_lat = report.lat
            if hasattr(report, 'lon'):
                s_lon = report.lon
            if hasattr(report, 'alt'):
                s_alt = report.alt * 3.281
        print("time:%s\ncoordinates:%s,%s\naltitude:%s\n" %(s_time,s_lat,s_lon,s_alt))
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")

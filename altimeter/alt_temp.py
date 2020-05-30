from MPL3115A2 import MPL3115A2
mpl3115a2 = MPL3115A2()
 
while True :
	mpl3115a2.control_alt_config()
	mpl3115a2.data_config()
	time.sleep(1)
	alt = mpl3115a2.read_alt_temp()
	print "Altitude : %.2f m"%(alt['a'])
	print "Temperature in Celsius : %.2f C"%(alt['c'])
	print "Temperature in Fahrenheit : %.2f F"%(alt['f'])
	mpl3115a2.control_pres_config()
	time.sleep(1)
	pres = mpl3115a2.read_pres()
	print "Pressure : %.2f kPa"%(pres['p'])
	print " ************************************* "

import time

while 1:
	tempfile = open("/sys/devices/w1_bus_master1/10-000800c4dc4a/w1_slave")
	thetext = tempfile.read()
	tempfile.close()

	tempdata = thetext.split("\n") [1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000

	print temperature
	time.sleep(1)


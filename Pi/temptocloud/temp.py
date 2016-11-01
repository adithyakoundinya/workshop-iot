import time
import httplib, urllib

def doit(temp):
    params = urllib.urlencode({'field1': temp, 'key':'RASXPSLQP8ASV570'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")

    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()
 
while 1:
	tempfile = open("/sys/devices/w1_bus_master1/10-000800c4dc4a/w1_slave")
	thetext = tempfile.read()
	tempfile.close()

	tempdata = thetext.split("\n") [1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000

	print temperature
	doit(temperature)
	time.sleep(16)



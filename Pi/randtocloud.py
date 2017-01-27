import time
import random

import httplib, urllib

def doit(temp):

    params = urllib.urlencode({'field1': temp, 'key':'XLOE5V8J8HEYQ2JS'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")

    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()
 
while 1:
	value = random.normalvariate(1,10)
	print value
	doit(value)
	time.sleep(16)



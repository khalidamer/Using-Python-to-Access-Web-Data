'''
Calling a JSON API
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points
To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
http://python-data.dr-chuck.net/geojson
This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py
'''
import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
    address = input(' Enter your address: ')
    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})
    print(url)
    connect = urllib.request.urlopen(url, context=ctx)
    data = connect.read().decode()
    try: js = json.loads(data)
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print(data)
        continue
    print(js)
    placeid = js["results"][0]['place_id']
    print ("Place id",placeid)

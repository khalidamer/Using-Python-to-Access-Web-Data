'''
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353540.json (Sum ends with 71)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://python-data.dr-chuck.net/comments_42.json'
connect = urllib.request.urlopen(url, context=ctx)
data = connect.read().decode()
data = json.loads(data)
sum=0
for comment in data['comments']:
    sum += int(comment['count'])
print(sum)

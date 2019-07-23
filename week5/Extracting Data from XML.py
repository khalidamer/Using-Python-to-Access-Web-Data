# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://python-data.dr-chuck.net/comments_42.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
sum=0
for comment in comments:
    sum += int(comment.find('count').text)
print(sum)

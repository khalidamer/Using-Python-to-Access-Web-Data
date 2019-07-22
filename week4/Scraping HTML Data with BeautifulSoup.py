# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum = 0
for tag in soup('span'):
    sum += int(tag.text)
print(sum)

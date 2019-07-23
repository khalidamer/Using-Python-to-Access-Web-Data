import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
num_repeat = int(input('Enter num of repeat: '))
position = int(input("Enter position: "))
name=[]
for i in range(num_repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a')
    for ind,tag in enumerate(tags):
        if ind != position-1:continue
        url = tag.get('href')
        name.append(tag.text)
print(' '.join(name))

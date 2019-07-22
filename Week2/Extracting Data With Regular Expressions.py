import re
fileName = '13chil.txt'# your file name
with open(fileName,'r') as f:
    data = f.read()
digits = (re.findall('[0-9]+',data))
print(sum(list(map(int,digits))))

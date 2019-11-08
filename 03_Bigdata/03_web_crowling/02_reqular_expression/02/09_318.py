import re
p= re.compile('(blue|white|red)')
print(p.sub('colour','blue_socks and red shoes'))
print(p.sub('colour','blue_socks and red shoes',count=1))
print(p.sub('colour','blue_socks and red shoes',count=2))

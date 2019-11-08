import re

p=re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))

m = p.search('ABCABCAB OK?')
print(m)

p = re.compile('(홍정우)')
m = p.search('홍정우홍정우 OK?')
print(m)

m = p.search('홍정우홍정우 귀염둥이 홍정우!')
print(m)
print(m.group(0))
print(m.group(1))
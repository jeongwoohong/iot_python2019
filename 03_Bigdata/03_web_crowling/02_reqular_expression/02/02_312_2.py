import re

p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m=p.search("Park 010-2334-2949")
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))



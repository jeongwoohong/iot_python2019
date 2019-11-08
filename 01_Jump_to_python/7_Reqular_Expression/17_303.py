import re

p=re.compile('a.b', re.DOTALL)
original_text=("a\nb")

m = p.match(original_text)

print(m)
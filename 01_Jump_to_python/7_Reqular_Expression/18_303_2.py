import re
p=re.compile('[a-z]', re.IGNORECASE)
p.match('python')
print(m)
p.match('Python')
print(m)
p.match('PYTHON')
print(m)

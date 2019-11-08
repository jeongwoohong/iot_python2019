import re
original_text='life is too short'
p=re.compile('[a-z]+')

result = p.finditer(original_text)

for r in result:
    print(r)
    print(r.group())

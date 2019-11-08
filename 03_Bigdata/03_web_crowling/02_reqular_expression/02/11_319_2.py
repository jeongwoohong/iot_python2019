import re
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile('\d+')
print(p.sub(hexrepl.'Call 65490 for printing. 49152 for user code.')

result = ''
for c in input():
    if c == c.lower():
        result += c.upper()
    elif c == c.upper():
        result += c.lower()
print(result)

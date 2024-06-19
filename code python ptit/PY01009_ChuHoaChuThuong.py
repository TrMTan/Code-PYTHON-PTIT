s, c = input(), 0
for i in range(len(s)):
    if s[i].islower():
        c += 1  
if c >= len(s) - c:
    print(s.lower())
else:
    print(s.upper())

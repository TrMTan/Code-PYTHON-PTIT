import re

l = []
for _ in range(int(input())):
    a = re.findall(r'[0-9]+', input())
    for i in a:
        l.append(int(i))
l.sort()
for i in l:
    print(i)

# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa
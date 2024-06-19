import re

s = ""
for _ in range(int(input())):
    s += input().lower() + " "
l = re.findall(r'\w+', s)
a = {}
for i in l:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
b = sorted(a.items(), key=lambda x: (-x[1], x[0]))
for i in b:
    print(i[0], i[1])
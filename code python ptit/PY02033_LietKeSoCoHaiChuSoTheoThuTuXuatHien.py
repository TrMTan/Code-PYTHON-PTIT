s, res = input(), []
for i in range(0, len(s) - 1, 2):
    res.append(s[i] + s[i + 1])
a = {}
for i in res:
    if i not in a:
        a.update({i: 1})
    else:
        a[i] += 1
print(*a.keys())

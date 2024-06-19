s, res = input(), []
k = int(input())
for i in range(0, len(s) - 1, 2):
    res.append(s[i] + s[i + 1])
res.sort()
a = {}
for i in res:
    if i not in a:
        a.update({i: 1})
    else:
        a[i] += 1
check = False
for i in a:
    if a[i] >= k:
        print(i, a[i])
        check = True
if check == False:
    print("NOT FOUND")
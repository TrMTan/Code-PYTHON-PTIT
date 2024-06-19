a = {}
f = open('VANBAN.in', 'r')
s = 0 # s: do dai tu thuan nghich dai nhat
for i in f.read().split():
    if i == i[::-1]:
        if len(i) > s:
            s = len(i) # cap nhat do dai tu thuan nghich dai nhat
            a.clear()
            a[i] = 1 
        elif len(i) == s:
            if i not in a: a[i] = 1
            else: a[i] += 1
for i in a:
    print(i, a[i])
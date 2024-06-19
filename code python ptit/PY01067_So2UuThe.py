a = []
b = [0, 1, 2]

def check(n):
    d = 0
    for i in n:
        if i =='2': d += 1
    if d > len(n) / 2: return True
    return False

def gen(s):
    if check(s): a.append(s)
    if len(s) < 10:
        for i in b:
            gen(s + str(i))
    
gen('1')
gen('2')
a = sorted([int(i) for i in a])
for t in range(int(input())):
    n = int(input())
    for i in range(n):
        print(a[i], end=' ')
    print()
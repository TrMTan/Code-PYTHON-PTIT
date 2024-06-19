n = int(input())
a = []
while len(a) < n:
    a.extend([int(x) for x in input().split()])
    
chan = sorted([int(x) for x in a if x % 2 == 0])
le = sorted([int(x) for x in a if x % 2 == 1], reverse=True)

i1, i2 = 0, 0
for i in a:
    if i % 2 == 0:
        print(chan[i1], end=' ')
        i1 += 1
    else:
        print(le[i2], end=' ')
        i2 += 1    
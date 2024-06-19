n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
c, l = [], []
for i in a:
    if i % 2 == 0:
        c.append(i)
    else:
        l.append(i)
c.sort(reverse=True)
l.sort()
for i in a:
    print(l.pop() if i % 2 else c.pop(), end=' ')
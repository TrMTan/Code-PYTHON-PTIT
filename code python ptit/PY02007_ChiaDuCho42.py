dd = [0] * 42
cnt, kq = 10, 0
while cnt > 0:
    a = [int(i) for i in input().split()]
    cnt -= len(a)
    for i in a:
        if dd[i % 42] == 0:
            dd[i % 42] = 1
            kq += 1
print(kq)            
a, k, n = map(int, input().split())
ok = 0
i = 1
while True:
    if k * i > n: break
    if k * i - a > 0:
        print(k * i - a, end = " ")
        ok = 1
    i += 1
if ok == 0: print(-1)
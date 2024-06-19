def Try(i, l):
    global n, k
    if len(l) == k:
        print(*l)
        return
    for j in range(i, n):
        Try(j + 1, l + [a[j]])

n, k = [int(i) for i in input().split()]
a = sorted(list(set([int(i) for i in input().split()])))
n = len(a)  

Try(0, [])

a = [0] * 10001
b = []
for i in range(2, 10001):
    if a[i] == 0:
        for j in range(i*i, 10001, i):
            a[j] = 1
        b.append(i)

n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in a:
    s = 10**9
    for j in b:
        s = min(s, abs(i-j))
    ans = max(ans, s)
print(ans)


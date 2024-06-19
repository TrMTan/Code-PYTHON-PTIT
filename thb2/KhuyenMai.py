n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [[] for _ in range(n)]
for i in range(n):
    c[i] = [a[i], b[i]]

c.sort(key=lambda x: x[0] - x[1])
i, res = 0, 0
while i < n:
    if k > 0:
        res += c[i][0]
        k -= 1
    else:
        if c[i][0] < c[i][1]:
            res += c[i][0]
        else:
            res += c[i][1]
    i += 1
print(res)
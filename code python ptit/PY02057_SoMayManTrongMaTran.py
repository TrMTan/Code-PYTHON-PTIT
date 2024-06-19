import math

n, m = map(int, input().split())
a = [[0] * m] * n
minv = 10000
maxv = 0
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    for j in a[i]:
        if j < minv:
            minv = j
        if j > maxv:
            maxv = j
res = maxv - minv
check = False
b = []
for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            b.append(f"Vi tri [{i}][{j}]")
            check = True
if not check:
    print("NOT FOUND")
else: 
    print(res)
    for i in b:
        print(i)
# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77
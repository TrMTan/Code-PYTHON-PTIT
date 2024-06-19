import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [[0] * m] * n
res = -1
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    for j in a[i]:
        if snt(j) and j > res:
            res = max(res, j)

if res == -1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f"Vi tri [{i}][{j}]")

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
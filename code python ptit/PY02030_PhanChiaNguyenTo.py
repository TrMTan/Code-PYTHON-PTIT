from math import sqrt

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 2

def kt(n, a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    for i in range(n):
        if snt(sum(b[: i + 1])) and snt(sum(b[i + 1 :])): return i
    return "NOT FOUND"

n = int(input())
a = list(map(int, input().split()))
print(kt(n, a))

# 10
# 3 6 7 3 4 7 3 6 4 4